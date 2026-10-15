#!/usr/bin/env python3
"""Build single-root Skill/plugin ZIPs and verify every entry against source bytes."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
STAMP = (1980, 1, 1, 0, 0, 0)

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def tracked(root: Path) -> list[str]:
    data = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    names = sorted({x.decode("utf-8") for x in data.split(b"\0") if x})
    for name in names:
        p = root / name
        if p.is_symlink() or not p.is_file():
            raise ValueError(f"Tracked source is not a regular file: {name}")
        if ".git" in PurePosixPath(name).parts:
            raise ValueError("Git internals cannot enter a release")
    return names

def zip_info(name: str, mode: int = 0o644, stored: bool = False) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=STAMP)
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | mode) << 16
    info.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
    return info

def write_archive(output: Path, top: str, entries: list[dict], metadata: dict) -> dict:
    """Entries have path, source Path or data bytes, plus optional source-relative provenance."""
    rows = []
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise ValueError(f"Refusing to overwrite an existing release asset: {output}")
    for e in entries:
        rel = e["path"]
        parts = PurePosixPath(rel).parts
        if not parts or rel.startswith("/") or ".." in parts or "\\" in rel:
            raise ValueError(f"Unsafe archive path: {rel}")
        if "source" in e:
            source = Path(e["source"])
            if source.is_symlink() or not source.is_file():
                raise ValueError(f"Not a regular source: {source}")
            size, sha = source.stat().st_size, digest(source)
            mode = source.stat().st_mode & 0o777
        else:
            size, sha, mode = len(e["data"]), hashlib.sha256(e["data"]).hexdigest(), e.get("mode", 0o644)
        row = {"path": rel, "size": size, "sha256": sha, "mode": mode}
        if "source_relative" in e:
            row["source_relative"] = e["source_relative"]
        if "encoding" in e:
            row["encoding"] = e["encoding"]
            row["decoded_size"] = e["decoded_size"]
            row["decoded_sha256"] = e["decoded_sha256"]
        rows.append(row)
    if len({x["path"] for x in rows}) != len(rows):
        raise ValueError("Duplicate archive entry")
    manifest = {"schema": "single-root-skill-release/1", "root": top, **metadata, "files": rows}
    manifest_data = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    uncompressed = sum(r["size"] for r in rows) + len(manifest_data)
    if metadata.get("max_uncompressed_bytes") and uncompressed >= metadata["max_uncompressed_bytes"]:
        raise ValueError(f"Cloud package exceeds its strict byte budget: {top}: {uncompressed}")
    temporary = output.with_name(output.name + ".partial")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
            for e, row in zip(entries, rows):
                info = zip_info(f"{top}/{row['path']}", row["mode"], row["size"] >= 2 * 1024 * 1024 or row["path"].endswith((".png", ".jpg", ".gz", ".zip", ".pdf")))
                if "source" in e:
                    with Path(e["source"]).open("rb") as source, z.open(info, "w", force_zip64=True) as target:
                        shutil.copyfileobj(source, target, length=1024 * 1024)
                else:
                    z.writestr(info, e["data"])
            z.writestr(zip_info(f"{top}/release-manifest.json"), manifest_data)
        report = verify_archive(temporary, source_entries=entries)
        if temporary.stat().st_size >= 2 * 1024 ** 3:
            raise ValueError("GitHub Release assets must be below 2 GiB each")
        temporary.rename(output)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    return {"file": output.name, "size": output.stat().st_size, "sha256": digest(output), "uncompressed_bytes": uncompressed, **report}

def verify_web_plugin(z: zipfile.ZipFile, top: str, manifest: dict) -> None:
    """Validate the dedicated portable web artifact, not account/UI acceptance."""
    import yaml
    names = z.namelist()
    normalized = set()
    for info in z.infolist():
        name = info.filename
        parts = name.split("/")
        key = unicodedata.normalize("NFC", name).casefold()
        if (any(not part or part in (".", "..") or part != part.strip() or ":" in part for part in parts)
                or "\\" in name or len(parts) > 20 or key in normalized
                or not stat.S_ISREG(info.external_attr >> 16) or info.flag_bits & 1):
            raise ValueError(f"Unsafe web ZIP path/type: {name}")
        normalized.add(key)
        if info.file_size > 100 * 1024 ** 2:
            raise ValueError("Web ZIP entry exceeds 100 MiB")
    if len(names) > 5000 or sum(i.file_size for i in z.infolist()) > 512 * 1024 ** 2:
        raise ValueError("Web ZIP exceeds conservative submission limits")
    data = json.loads(z.read(f"{top}/plugin.json"))
    if data.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("Web plugin requires the portable manifest schema")
    name = data.get("name")
    if (not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:[.-][a-z0-9]+)*", name)
            or len(name) > 64 or name != top or data.get("version") != manifest.get("version")):
        raise ValueError("Web plugin identity/version mismatch")
    allowed = {"plugin.json", "LICENSE", "NOTICE"}
    skill_paths = []
    for row in manifest["files"]:
        rel = row["path"]
        if rel not in allowed and not rel.startswith("skills/"):
            raise ValueError(f"Repository-only file in web plugin: {rel}")
        if any(field in row for field in ("encoding", "decoded_size", "decoded_sha256")):
            raise ValueError("Web plugin files must be original unencoded source bytes")
        if row.get("source_relative") != rel:
            raise ValueError("Web plugin source path must be preserved")
        if re.fullmatch(r"skills/[^/]+/SKILL.md", rel):
            skill_paths.append(rel)
    if not allowed.issubset({r["path"] for r in manifest["files"]}) or not skill_paths:
        raise ValueError("Web plugin requires its manifest, legal files and skills")
    identities = set()
    for rel in skill_paths:
        payload = z.read(f"{top}/{rel}")
        if len(payload) > 1024 ** 2:
            raise ValueError("Web skill entrypoint exceeds 1 MiB")
        match = re.match(r"---\r?\n(.*?)\r?\n---(?:\r?\n|$)", payload.decode("utf-8"), re.S)
        metadata = yaml.safe_load(match[1]) if match else None
        if (not isinstance(metadata, dict) or metadata.get("name") != rel.split("/")[1]
                or not isinstance(metadata.get("description"), str) or not metadata["description"].strip()):
            raise ValueError("Web skill frontmatter/name mismatch")
        identity = f"{name}:{metadata['name']}"
        if len(identity) > 64 or identity in identities:
            raise ValueError("Web skill identity exceeds 64 characters or is duplicated")
        identities.add(identity)


def verify_archive(archive: Path, root: Path | None = None, source_entries: list[dict] | None = None) -> dict:
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        if len(set(names)) != len(names):
            raise ValueError("Duplicate ZIP names")
        for item in z.infolist():
            p = PurePosixPath(item.filename)
            if item.filename.startswith("/") or ".." in p.parts or "\\" in item.filename or ((item.external_attr >> 16) & 0o170000) == stat.S_IFLNK:
                raise ValueError(f"Unsafe ZIP entry: {item.filename}")
        roots = {PurePosixPath(n).parts[0] for n in names if PurePosixPath(n).parts}
        if len(roots) != 1:
            raise ValueError("ZIP must contain exactly one root folder")
        top = next(iter(roots))
        manifest = json.loads(z.read(f"{top}/release-manifest.json"))
        if manifest.get("schema") != "single-root-skill-release/1" or manifest.get("root") != top:
            raise ValueError("Invalid release manifest")
        if manifest.get("kind") not in {"skill", "cloud-skill", "plugin", "web-plugin"}:
            raise ValueError("Unsupported archive kind")
        expected = {f"{top}/{row['path']}" for row in manifest["files"]} | {f"{top}/release-manifest.json"}
        if set(names) != expected:
            raise ValueError("Archive and complete file manifest disagree")
        if manifest["kind"] in ("skill", "cloud-skill"):
            skill_text = z.read(f"{top}/SKILL.md").decode("utf-8")
            import re
            if not re.search(rf"(?m)^name:\s*{re.escape(top)}\s*$", skill_text):
                raise ValueError("Single-root folder and Skill name disagree")
        elif manifest["kind"] == "plugin":
            if f"{top}/plugin.json" not in expected or f"{top}/.claude-plugin/plugin.json" not in expected:
                raise ValueError("Plugin overlay/root manifest missing")
        elif manifest["kind"] == "web-plugin":
            verify_web_plugin(z, top, manifest)
            if archive.stat().st_size > 100_000_000:
                raise ValueError("Web ZIP exceeds 100 MB")
            if root is not None:
                actual_skills = {r["path"] for r in manifest["files"] if r["path"].startswith("skills/")}
                expected_skills = {n for n in tracked(root) if n.startswith("skills/")}
                if actual_skills != expected_skills:
                    raise ValueError("Web plugin must preserve every tracked skill file")
        sources = {e["path"]: e for e in source_entries or []}
        for row in manifest["files"]:
            info = z.getinfo(f"{top}/{row['path']}")
            h = hashlib.sha256()
            with z.open(info) as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    h.update(block)
            if info.file_size != row["size"] or h.hexdigest() != row["sha256"]:
                raise ValueError(f"ZIP byte mismatch: {row['path']}")
            source = sources.get(row["path"])
            if source and "source" in source:
                if digest(Path(source["source"])) != row["sha256"]:
                    raise ValueError(f"Source changed during packaging: {row['path']}")
            if root is not None and row.get("source_relative") and not row.get("encoding"):
                p = (root / row["source_relative"]).resolve()
                if root.resolve() not in p.parents or digest(p) != row["sha256"]:
                    raise ValueError(f"Source mismatch: {row['source_relative']}")
        total = sum(i.file_size for i in z.infolist())
        budget = manifest.get("max_uncompressed_bytes")
        if budget and total >= budget:
            raise ValueError("ZIP exceeds cloud uncompressed budget")
    return {"root": top, "kind": manifest["kind"], "files_verified": len(manifest["files"]), "all_entries_sha256_verified": True, "zip_crc_verified_by_full_read": True}

def build(root: Path, output: Path, kind: str, skill_name: str | None = None) -> list[dict]:
    package = json.loads((root / "package.json").read_text())
    names = tracked(root)
    skill_names = [p.parent.name for p in (root / "skills").glob("*/SKILL.md")]
    if skill_name:
        if skill_name not in skill_names:
            raise ValueError("Unknown Skill name")
        skill_names = [skill_name]
    result = []
    if kind in ("skill", "all"):
        for name in sorted(skill_names):
            prefix = f"skills/{name}/"
            selected = [n for n in names if n.startswith(prefix)]
            if prefix + "SKILL.md" not in selected or prefix + "references/installation.md" not in selected:
                raise ValueError("Skill entry/installation file is untracked; stage all release files before building")
            entries = [{"path": n[len(prefix):], "source": root / n, "source_relative": n} for n in selected]
            result.append(write_archive(output / f"{name}-v{package['version']}-skill-full.zip", name, entries, {"kind": "skill", "version": package["version"], "source_repository": package["repository"]["url"], "source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()}))
    if kind in ("plugin", "all"):
        required = {"plugin.json", ".claude-plugin/plugin.json", ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json", "package.json", "bin/install.mjs"}
        if not required.issubset(names):
            raise ValueError(f"Required distribution files are untracked: {sorted(required - set(names))}")
        entries = [{"path": n, "source": root / n, "source_relative": n} for n in names]
        result.append(write_archive(output / f"{package['name']}-v{package['version']}-plugin.zip", package["name"], entries, {"kind": "plugin", "version": package["version"], "source_repository": package["repository"]["url"], "source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()}))
    if kind in ("web-plugin", "all"):
        plugin = json.loads((root / "plugin.json").read_text())
        if plugin.get("version") != package["version"]:
            raise ValueError("Web plugin and package versions differ")
        required = {"plugin.json", "LICENSE", "NOTICE"}
        if not required.issubset(names):
            raise ValueError("Web plugin manifest/legal files must be tracked")
        selected = [n for n in names if n in required or n.startswith("skills/")]
        entries = [{"path": n, "source": root / n, "source_relative": n} for n in selected]
        result.append(write_archive(output / f"{plugin['name']}-v{package['version']}-web-plugin.zip", plugin["name"], entries,
                                    {"kind": "web-plugin", "version": package["version"],
                                     "source_repository": package["repository"]["url"],
                                     "source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()}))
    output.mkdir(parents=True, exist_ok=True)
    (output / "release-assets.json").write_text(json.dumps({"schema": "release-assets/1", "assets": result}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "SHA256SUMS.txt").write_text("".join(f"{r['sha256']}  {r['file']}\n" for r in result), encoding="utf-8")
    return result

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--kind", choices=["skill", "plugin", "web-plugin", "all"], default="all")
    parser.add_argument("--skill")
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.verify:
        print(json.dumps(verify_archive(args.verify, root=root), ensure_ascii=False))
        return
    if not args.output:
        parser.error("--output outside the repository is required")
    output = args.output.resolve()
    if output == root or root in output.parents:
        raise ValueError("Release output must remain outside the source repository")
    print(json.dumps(build(root, output, args.kind, args.skill), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
