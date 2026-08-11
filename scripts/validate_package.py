#!/usr/bin/env python3
"""Validate the publishable skill repository without network access."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "research-english-academic-paper-writing-guide"
RAW_EXTENSIONS = {".pdf", ".zip", ".tar", ".gz", ".7z", ".png", ".jpg", ".jpeg", ".webp", ".txt"}
SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile("Github" + "-MCP", re.IGNORECASE),
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "NOTICE",
        ROOT / "CHANGELOG.md",
        ROOT / "scripts" / "playbook_contract.py",
        ROOT / "scripts" / "test_review_feedback_evidence_playbook.py",
        ROOT / "scripts" / "test_professor_feedback_operationalization.py",
        ROOT / "scripts" / "test_dataset_census_experiment_evidence.py",
        ROOT / "docs" / "course-full-reconstruction.md",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "course-full-reconstruction.md",
        SKILL / "references" / "lecture-index.md",
        SKILL / "references" / "provenance.md",
        SKILL / "references" / "quick-reference.md",
        SKILL / "references" / "playbooks" / "13-review-feedback-evidence-contract.md",
        SKILL / "references" / "playbooks" / "15-table-taxonomy-and-layout.md",
        SKILL / "references" / "playbooks" / "16-fast-reader-and-skim-path.md",
    ]
    for path in required:
        if not path.is_file():
            fail(errors, f"missing required file: {path.relative_to(ROOT)}")


def check_skill_frontmatter(errors: list[str]) -> None:
    text = read(SKILL / "SKILL.md")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(errors, "SKILL.md missing YAML frontmatter")
        return
    keys = [line.split(":", 1)[0] for line in match.group(1).splitlines() if line and not line.startswith(" ")]
    if keys != ["name", "description"]:
        fail(errors, f"SKILL.md frontmatter keys should be name,description only; got {keys}")
    desc_match = re.search(r'^description:\s*"(.+)"$', match.group(1), re.M)
    if not desc_match:
        fail(errors, "SKILL.md description must be a quoted single-line string")
    elif not (desc_match.group(1).startswith("Use when ") or desc_match.group(1).startswith("Always-on")):
        fail(errors, "SKILL.md description should start with 'Use when ' (conditional trigger) or 'Always-on' (unconditional trigger, by explicit design)")
    elif len(desc_match.group(1)) > 1024:
        fail(errors, "SKILL.md description exceeds 1024 characters")


def check_counts(errors: list[str]) -> None:
    lectures = sorted((SKILL / "references" / "lectures").glob("*.md"))
    playbooks = sorted((SKILL / "references" / "playbooks").glob("*.md"))
    if len(lectures) != 13:
        fail(errors, f"expected 13 lecture files, got {len(lectures)}")
    # NOTE: update this count deliberately whenever a playbook is added or
    # removed -- it is intentionally a hard assertion, not inferred, so a
    # forgotten update fails loudly instead of silently under-checking the
    # package. (This count drifted after 4.6.0 added playbooks 17 and 18
    # without updating it; the package shipped failing its own validator
    # until the 4.6.1 correction pass caught it.)
    EXPECTED_PLAYBOOK_COUNT = 19
    if len(playbooks) != EXPECTED_PLAYBOOK_COUNT:
        fail(errors, f"expected {EXPECTED_PLAYBOOK_COUNT} playbook files, got {len(playbooks)}")
    feedback_playbook = SKILL / "references" / "playbooks" / "13-review-feedback-evidence-contract.md"
    if not feedback_playbook.is_file():
        fail(errors, "missing reviewer-feedback evidence-contract playbook")
    for lecture in lectures:
        headings = [line for line in read(lecture).splitlines() if line.startswith("# ")]
        # Each lecture file now holds two independently-authored full
        # reconstructions of the same lecture, spliced back to back (v4.0.0
        # merge): Version 1's own top-level heading, a "# Version 2 — ..."
        # divider heading, then Version 2's own original top-level heading
        # (preserved as its author wrote it) — three top-level headings,
        # not one, is correct post-merge.
        if len(headings) != 3:
            fail(errors, f"{lecture.relative_to(ROOT)} should have exactly three top-level headings (Version 1 + Version 2 divider + Version 2's own title); got {len(headings)}")
        if not any(h.startswith("# Version 2") for h in headings):
            fail(errors, f"{lecture.relative_to(ROOT)} is missing its 'Version 2' companion-reconstruction section")

    integrated = ROOT / "docs" / "course-full-reconstruction.md"
    skill_integrated = SKILL / "references" / "course-full-reconstruction.md"
    top = [line for line in read(integrated).splitlines() if line.startswith("# ")]
    # 1 preamble + 13 lectures * 3 headings each (Version 1 + Version 2
    # divider + Version 2's own title) + 1 closing appendix = 41.
    if len(top) != 41:
        fail(errors, f"integrated reconstruction should have 41 top-level headings (post v4.0.0 merge); got {len(top)}")
    if skill_integrated.exists():
        if read(skill_integrated) != read(integrated):
            fail(errors, "skill course-full-reconstruction.md must match docs/course-full-reconstruction.md")
        if "## Agent 阅读协议" not in read(skill_integrated):
            fail(errors, "skill course-full-reconstruction.md missing Agent reading protocol")


def check_openai_yaml(errors: list[str]) -> None:
    text = read(SKILL / "agents" / "openai.yaml")
    required_snippets = [
        "interface:",
        'display_name: "Research and English Academic Paper Writing Guide"',
        'short_description: "Research planning and academic paper writing"',
        'default_prompt: "Use $research-english-academic-paper-writing-guide to first consult the full course reconstruction',
    ]
    for snippet in required_snippets:
        if snippet not in text:
            fail(errors, f"openai.yaml missing expected snippet: {snippet}")
    if "icon:" in text:
        fail(errors, "openai.yaml should not use unsupported icon field")


def tracked_files() -> list[Path]:
    """Return the exact publishable Git surface, excluding local audit inputs."""

    import subprocess

    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def check_no_raw_or_secret_files(errors: list[str]) -> None:
    for path in tracked_files():
        if not path.is_file():
            continue
        if path.suffix.lower() in RAW_EXTENSIONS:
            fail(errors, f"raw/non-source asset should not be published: {path.relative_to(ROOT)}")
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(errors, f"possible credential in {path.relative_to(ROOT)}")


def check_python_syntax(errors: list[str]) -> None:
    for path in ROOT.rglob("*.py"):
        if ".git" in path.parts:
            continue
        try:
            ast.parse(read(path), filename=str(path))
        except SyntaxError as exc:
            fail(errors, f"python syntax error in {path.relative_to(ROOT)}: {exc}")


def check_markdown_local_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for match in link_pattern.finditer(read(path)):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                fail(errors, f"local link escapes repo in {path.relative_to(ROOT)}: {match.group(1)}")
                continue
            if not target_path.exists():
                fail(errors, f"missing local link in {path.relative_to(ROOT)}: {match.group(1)}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    if (SKILL / "SKILL.md").exists():
        check_skill_frontmatter(errors)
    check_counts(errors)
    if (SKILL / "agents" / "openai.yaml").exists():
        check_openai_yaml(errors)
    check_no_raw_or_secret_files(errors)
    check_python_syntax(errors)
    check_markdown_local_links(errors)

    if errors:
        print("validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
