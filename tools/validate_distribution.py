#!/usr/bin/env python3
"""Offline official-schema, original-byte, marketplace, and Skill validation."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

# Offline prior-snapshot identity, independently derived from Git blobs at
# this reviewed commit. Package validation must not need Git or the network.
# These constants are review-controlled provenance, not a signature or proof
# of external authorization. Keep the original-byte baseline unchanged.
SEMANTIC_BEFORE_COMMIT = '981d865eafc5c92b939a77cbd3352bc6bb4c7871'
SEMANTIC_BEFORE_SHA256 = {
    ".github/workflows/validate.yml": "1a350ad83ead4f567da40ebbde28922b5e426d9967df532fe6aafb6323825a69",
    "NOTICE": "3079b22f6d2b667aae575ff232a51e8a16cde9c344ad10b800bce889d60f604f",
    "README.md": "3bd7e462f205b62d1e4085699c17072688cc87c6b0627f55bc435f52a72dff99",
    "skills/research-english-academic-paper-writing-guide/SKILL.md": "8bcf4175204c4058a1817fa79d8afa8167338c8f179100acf9c2db63dae7164d",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/01-overview.md": "e50e63465372b1dff3a7414e6aaf76cd783757f153c16fc33c0d7bd67898cb9a",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/02-conception-and-title.md": "a80aaf524e63ddaa993c2bd119d230fd6a13fbadcdd97fb834d5b342a9b34e2e",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/03-abstract-and-introduction.md": "1500261f70b0bc5bd47aaf7117c9ae8d3fd4548d7fca4f18541b94db352079a5",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/04-related-work-and-method.md": "fc52072e5b0d3d01543c780bb6e53c8686447e7d6de7cf012dacff10c4922979",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/05-experiments-conclusion-references.md": "7c4890c0c5df7963a2fc0a308710ba5a58fe812effdec480be98b9072ac03cec",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/06-motivation-figure.md": "f1e462c5552959cd0fe0e15fb623865632f53fcf5f76c4cbcf68dfecc44eb3e3",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/08-framework-figure-extension.md": "cc6af0f75fcbbdb3169d4b8fb40aa79e9f0417d68f899f0a3ca7960ea6ed6d97",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/09-concise-and-rigorous.md": "24ce243939e506511b2366f083b03e603a224025b2e7e7f88825ada40dba2020",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/10-terminology-symbols-figures-references.md": "5370360f083e98037f0624bc8eb35cdb520c501e5b096b816a8197b841431493",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/11-innovation-angles.md": "3f42a5f55c0c8c9d8fda05df2cdf98d4d80e2ae0e537fad685f73f97dff86c64",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/11-pre-prerequisites.md": "6231d973d96c1a91a223b992e4aea12b36ca1ae5887689931f5bdda93b68fa7c",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/12-find-papers-literature-review.md": "7ddc01e4ed5e15f132699069d082935db9cd92c37ceb7f0b0cfccef1067c77ab",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/13-review-feedback-evidence-contract.md": "0529b241067b70bae7aaa6320aeb1d51d98ec302806d6a5675d1e8a00962f71e",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/14-figure-schema-and-rendering-gate.md": "44976cfeea6645635a7d541225bc096c75880a259ed5d9f080f93f137854f4f0",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/16-fast-reader-and-skim-path.md": "46f5e9791f2da6990481e265dd26571421a87ca316d8668ae8abb82ea307fddb",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/17-native-register-and-ai-detection.md": "30af12c81c1f6617b34b6f67f1fc1e07835a9d0cd20f3e2fb436387d4a336414",
    "skills/research-english-academic-paper-writing-guide/references/playbooks/18-submission-sprint-discipline.md": "25f08fa88ac20f1e0ad8926af7a655ddf60798a64bd12d65b0db7c847b3601f4",
    "skills/research-english-academic-paper-writing-guide/references/provenance.md": "e7d31716466becb5e4d2d8b53e0c9ddb9544b1b5f193fb3d916534f279f760b5",
    "skills/research-english-academic-paper-writing-guide/references/quick-reference.md": "8cc53df91eb6586f222483a02c08b943e76f59dd8619e31e28c5a7c85bfb6673",
    "skills/research-english-academic-paper-writing-guide/scripts/measure_prose_rhythm.py": "2738f660b83936624fd002ac0ffbf2a4ad15e88144d3b051a3c0962be6dcff42"
}
SEMANTIC_AMENDMENT_PATHS = set(SEMANTIC_BEFORE_SHA256)
SEMANTIC_ADDED_PATHS = {
    "skills/research-english-academic-paper-writing-guide/references/course-review-notes.md",
}

def course_original(path: str) -> bool:
    return path == "docs/course-full-reconstruction.md" or path.endswith(
        "/references/course-full-reconstruction.md"
    ) or "/references/lectures/" in path


def check(root: Path) -> dict:
    import jsonschema
    import yaml
    errors, preserved, appended, amended, added = [], [], [], [], []
    def require(condition, message):
        if not condition:
            errors.append(message)
    schema = json.loads((root / "docs/ecosystem/agent-plugin.schema.json").read_text())
    plugin = json.loads((root / "plugin.json").read_text())
    for error in jsonschema.Draft202012Validator(schema).iter_errors(plugin):
        errors.append(f"Official plugin schema: {error.message}")
    interface = plugin.get("extensions", {}).get("com.openai", {}).get("interface", {})
    for field in ("displayName", "shortDescription"):
        require(isinstance(interface.get(field), str) and 0 < len(interface[field]) <= 30, f"OpenAI directory {field} must be 1-30 characters")
    package = json.loads((root / "package.json").read_text())
    claude = json.loads((root / ".claude-plugin/plugin.json").read_text())
    require(plugin["name"] == claude["name"], "Portable/Claude plugin identities differ")
    require(plugin["version"] == package["version"] == claude["version"], "Plugin/npm versions differ")
    require(bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", plugin["version"])), "Invalid release SemVer")
    require(claude.get("description") == plugin.get("description") and bool(claude.get("description")), "Claude description is missing or inconsistent")
    require(not any(k in package.get("scripts", {}) for k in ["preinstall", "install", "postinstall", "prepare", "prepublish"]), "Package must not execute lifecycle code")
    require(not package.get("dependencies"), "Offline installer must have no runtime dependencies")
    for executable, target in package.get("bin", {}).items():
        require(target == "bin/install.mjs" and (root / target).is_file(), f"Missing offline bin: {executable}")
    am = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    cm = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    require(am["name"] == cm["name"], "Marketplace identities differ")
    require(len(am["plugins"]) == len(cm["plugins"]) == 1, "Expected one root plugin in each marketplace")
    entry, overlay = am["plugins"][0], cm["plugins"][0]
    require(entry["name"] == overlay["name"] == plugin["name"], "Marketplace plugin identity differs")
    require(entry["source"] == {"source": "local", "path": "./"} and overlay["source"] == "./", "Marketplace root path must resolve to ./")
    require(entry.get("policy") == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Marketplace install/auth policies missing")
    require(entry.get("category") == "Productivity", "Marketplace category missing")
    skills = []
    for p in sorted((root / "skills").glob("*/SKILL.md")):
        skill_text = p.read_text()
        match = re.match(r"---\r?\n(.*?)\r?\n---(?:\r?\n|$)", skill_text, re.S)
        require(bool(match), f"Missing Skill YAML: {p}")
        if not match:
            continue
        data = yaml.safe_load(match[1])
        name, description = data.get("name", ""), data.get("description", "")
        # Historical body versions are deliberately retained. A package identity
        # must be visible before them, including in clients that show only a prefix.
        body = skill_text[match.end():].lstrip()
        release_prefix = ("## Current package release (authoritative)\n\n"
                          f"Current package version: `{package['version']}`.\n")
        require(body.startswith(release_prefix), f"Skill current-release notice must lead body and match package version: {p}")
        require(len(re.findall(r"(?m)^Current package version:", body)) == 1,
                f"Skill needs exactly one current-package version declaration: {p}")
        require(isinstance(name, str) and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)) and len(name) <= 64 and name == p.parent.name, f"Invalid Skill folder/name: {p}")
        require(isinstance(description, str) and 0 < len(description) <= 1024 and not re.search(r"<[^>]*>", description), f"Invalid Skill description: {p}")
        require((p.parent / "references/installation.md").is_file(), f"Skill cannot access installation instructions: {p}")
        require((p.parent / "references/installation.md").read_bytes() == (root / "docs/INSTALLATION.md").read_bytes(), f"Skill and repository install instructions differ: {p}")
        # OpenAI submission validation applies to the namespaced identity, not
        # only the standalone Agent Skills name limit. npm identity is separate.
        require(len(f"{plugin['name']}:{name}") <= 64, f"skill_identity_too_long: {plugin['name']}:{name} exceeds 64 characters")
        skills.append(name)
    require(bool(skills), "No root skills discovered")
    baseline = json.loads((root / "docs/distribution-baseline.json").read_text())
    # The baseline remains untouched. Exceptions name the exact old baseline
    # identity and exact replacement bytes, with an auditable rationale.
    amendment_path = root / "docs/semantic-amendments.json"
    amendment_rows = {}
    try:
        manifest = json.loads(amendment_path.read_text())
        require(manifest.get("schema") == "derived-semantic-amendments/1", "Invalid amendment schema")
        require(manifest.get("baseline_commit") == baseline["base_commit"], "Amendment baseline commit differs")
        require(manifest.get("before_commit") == SEMANTIC_BEFORE_COMMIT, "Amendment before commit differs from pinned snapshot")
        rows = manifest.get("files", [])
        require(isinstance(rows, list), "Amendment files must be an array")
        if not isinstance(rows, list):
            rows = []
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("path"), str):
                errors.append("Malformed amendment row")
                continue
            relative = row["path"]
            require(relative not in amendment_rows, f"Duplicate amendment: {relative}")
            require(relative in SEMANTIC_AMENDMENT_PATHS and not course_original(relative), f"Unapproved amendment path: {relative}")
            require(isinstance(row.get("reason"), str) and bool(row["reason"].strip()), f"Missing amendment reason: {relative}")
            for field in ("baseline_sha256", "before_sha256", "after_sha256"):
                require(isinstance(row.get(field), str) and bool(re.fullmatch(r"[a-f0-9]{64}", row[field])), f"Invalid amendment {field}: {relative}")
            require(relative in SEMANTIC_BEFORE_SHA256 and row.get("before_sha256") == SEMANTIC_BEFORE_SHA256.get(relative), f"Amendment before hash differs from pinned snapshot: {relative}")
            require(isinstance(row.get("after_size"), int) and row["after_size"] > 0, f"Invalid amendment size: {relative}")
            amendment_rows[relative] = row
        require(set(amendment_rows) == SEMANTIC_AMENDMENT_PATHS, "Amendment paths differ from the reviewed derived-file set")
        added_rows = manifest.get("added_files", [])
        require(isinstance(added_rows, list), "Added files must be an array")
        seen_added = set()
        for row in added_rows if isinstance(added_rows, list) else []:
            if not isinstance(row, dict) or not isinstance(row.get("path"), str):
                errors.append("Malformed added-file row")
                continue
            relative = row["path"]
            require(relative not in seen_added, f"Duplicate added file: {relative}")
            seen_added.add(relative)
            require(relative in SEMANTIC_ADDED_PATHS and not course_original(relative), f"Unapproved added-file path: {relative}")
            require(isinstance(row.get("reason"), str) and bool(row["reason"].strip()), f"Missing added-file reason: {relative}")
            require(isinstance(row.get("after_sha256"), str) and bool(re.fullmatch(r"[a-f0-9]{64}", row["after_sha256"])), f"Invalid added-file hash: {relative}")
            require(isinstance(row.get("after_size"), int) and row["after_size"] > 0, f"Invalid added-file size: {relative}")
            # Reject unknown paths before opening them, including absolute/parent paths.
            if relative not in SEMANTIC_ADDED_PATHS:
                continue
            p = root / relative
            if not p.is_file() or p.is_symlink():
                errors.append(f"Added file missing or symlinked: {relative}")
            elif p.stat().st_size != row.get("after_size") or hashlib.sha256(p.read_bytes()).hexdigest() != row.get("after_sha256"):
                errors.append(f"Added bytes differ from exact reviewed replacement: {relative}")
            else:
                added.append(relative)
        require(seen_added == SEMANTIC_ADDED_PATHS, "Added-file paths differ from the reviewed set")
    except (OSError, ValueError, TypeError) as exc:
        errors.append(f"Cannot read semantic amendments: {exc}")
    for old in baseline["files"]:
        p = root / old["path"]
        if not p.is_file() or p.is_symlink():
            errors.append(f"Original missing: {old['path']}")
            continue
        size = p.stat().st_size
        h = hashlib.sha256()
        with p.open("rb") as stream:
            remaining = old["size"]
            while remaining:
                block = stream.read(min(1024 * 1024, remaining))
                if not block:
                    break
                h.update(block); remaining -= len(block)
        original_prefix = remaining == 0 and h.hexdigest() == old["sha256"]
        append_allowed = p.suffix == ".md" and "/assets/" not in "/" + old["path"]
        amendment = amendment_rows.get(old["path"])
        if amendment is not None:
            require(amendment.get("baseline_sha256") == old["sha256"], f"Amendment old baseline hash differs: {old['path']}")
            current_sha = hashlib.sha256(p.read_bytes()).hexdigest()
            if size == amendment.get("after_size") and current_sha == amendment.get("after_sha256"):
                amended.append(old["path"])
            else:
                errors.append(f"Amended bytes differ from exact reviewed replacement: {old['path']}")
        elif course_original(old["path"]) and (size != old["size"] or not original_prefix):
            errors.append(f"Course original must remain byte-identical: {old['path']}")
        elif size == old["size"] and original_prefix:
            preserved.append(old["path"])
        elif size > old["size"] and original_prefix and append_allowed:
            appended.append(old["path"])
        else:
            errors.append(f"Original bytes changed rather than additively extended: {old['path']}")
    return {"schema": "distribution-validation/1", "repository": package["name"], "version": package["version"], "official_plugin_schema": "Agent Plugins 1.0.0", "official_schema_passed": not any(e.startswith("Official plugin schema") for e in errors), "skill_names": skills, "original_files": len(baseline["files"]), "original_files_exact": len(preserved), "original_files_with_exact_preserved_prefix": appended, "derived_files_with_explicit_amendments": amended, "added_files_with_explicit_review": added, "claude_online_validation": {"status": "blocked", "reason": "automatic approval review rejected a previous CLI validation process that attempted to send private data to api.anthropic.com; no retry or bypass"}, "hosted_upload_or_directory_approval_tested": False, "errors": errors, "passed": not errors}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = check(args.root.resolve())
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["passed"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
