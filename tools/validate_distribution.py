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

def check(root: Path) -> dict:
    import jsonschema
    import yaml
    errors, preserved, appended = [], [], []
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
        match = re.match(r"---\r?\n(.*?)\r?\n---(?:\r?\n|$)", p.read_text(), re.S)
        require(bool(match), f"Missing Skill YAML: {p}")
        if not match:
            continue
        data = yaml.safe_load(match[1])
        name, description = data.get("name", ""), data.get("description", "")
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
        if size == old["size"] and original_prefix:
            preserved.append(old["path"])
        elif size > old["size"] and original_prefix and append_allowed:
            appended.append(old["path"])
        else:
            errors.append(f"Original bytes changed rather than additively extended: {old['path']}")
    return {"schema": "distribution-validation/1", "repository": package["name"], "version": package["version"], "official_plugin_schema": "Agent Plugins 1.0.0", "official_schema_passed": not any(e.startswith("Official plugin schema") for e in errors), "skill_names": skills, "original_files": len(baseline["files"]), "original_files_exact": len(preserved), "original_files_with_exact_preserved_prefix": appended, "claude_online_validation": {"status": "blocked", "reason": "automatic approval review rejected a previous CLI validation process that attempted to send private data to api.anthropic.com; no retry or bypass"}, "hosted_upload_or_directory_approval_tested": False, "errors": errors, "passed": not errors}

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
