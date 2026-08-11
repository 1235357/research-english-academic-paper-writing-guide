#!/usr/bin/env python3
"""Regression test: the reusable skill must stay faithful and domain-general."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "research-english-academic-paper-writing-guide"
SKILL_MD = SKILL / "SKILL.md"
PLAYBOOK_05 = SKILL / "references" / "playbooks" / "05-experiments-conclusion-references.md"
PLAYBOOK_13 = SKILL / "references" / "playbooks" / "13-review-feedback-evidence-contract.md"
PLAYBOOK_17 = SKILL / "references" / "playbooks" / "17-native-register-and-ai-detection.md"
PLAYBOOK_18 = SKILL / "references" / "playbooks" / "18-submission-sprint-discipline.md"
COURSE_DOC = ROOT / "docs" / "course-full-reconstruction.md"
COURSE_SKILL = SKILL / "references" / "course-full-reconstruction.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require_course_fidelity() -> None:
    if read(COURSE_DOC) != read(COURSE_SKILL):
        raise AssertionError("bundled course reconstruction drifted from the canonical copy")

    skill = read(SKILL_MD)
    if "12 numbered lectures plus one pre-lecture bonus" not in skill:
        raise AssertionError("SKILL.md must describe the source as 12 lectures plus one bonus")
    if "Original_Transcript+PDF" not in skill:
        raise AssertionError("SKILL.md must route fidelity disputes to available original material")


def require_course_consistent_conclusion_rule() -> None:
    playbook = read(PLAYBOOK_05)
    forbidden = (
        "state each true limitation exactly once in the main text",
        "not repeated in the Conclusion",
    )
    for phrase in forbidden:
        if phrase.casefold() in playbook.casefold():
            raise AssertionError(f"playbook 05 contradicts Lecture 5: {phrase!r}")

    required = (
        "conclusion",
        "limitations or capability boundaries",
        "future work",
        "avoid mechanical repetition",
    )
    normalized = " ".join(playbook.casefold().split())
    for phrase in required:
        if phrase.casefold() not in normalized:
            raise AssertionError(f"playbook 05 missing course-consistent conclusion guidance: {phrase}")


def require_general_feedback_playbook() -> None:
    playbook = read(PLAYBOOK_13)
    project_only_terms = (
        "FULL-SR",
        "selected-evidence",
        "global-fusion",
        "BERT",
        "DeBERTa",
        "GPU",
        "shard",
        "legal query",
        "26-entry ceiling",
        # "Counter too large" is intentionally NOT in this list: it is the
        # literal LaTeX engine error string for \appendix's \Alph{section}
        # overflow, reusable by any paper regardless of domain. Keeping the
        # exact string is what makes the playbook entry findable by search;
        # it is a universal LaTeX fact, not project jargon.
    )
    hits = [term for term in project_only_terms if term.casefold() in playbook.casefold()]
    if hits:
        raise AssertionError(f"project-specific incidents leaked into the general playbook: {hits}")

    if "should not be smaller than a Benchmark/Setup section" in playbook:
        raise AssertionError("section-size heuristic is written as a universal hard rule")

    skill = read(SKILL_MD)
    forced = re.search(
        r"advisor or reviewer feedback[\s\S]{0,180}?first apply[\s\S]{0,100}?13-review-feedback",
        skill,
        re.IGNORECASE,
    )
    if forced:
        raise AssertionError("specialized evidence playbook is forced ahead of the course")
    required_route = (
        "after the relevant course lecture",
        "optional evidence and submission audit",
    )
    normalized = " ".join(skill.casefold().split())
    for phrase in required_route:
        if phrase not in normalized:
            raise AssertionError(f"SKILL.md missing subordinate routing phrase: {phrase}")


def require_general_sprint_and_register_playbooks() -> None:
    """Playbooks 17 and 18 (added in 4.6.0) must meet the same generalization
    bar playbook 13 was already held to in require_general_feedback_playbook.
    They were not covered by any test until this function was added in the
    4.6.1 correction pass -- that gap is exactly how the 4.6.0 draft shipped
    with one project's incident numbers standing in for general rules."""
    playbook_17 = read(PLAYBOOK_17)
    playbook_18 = read(PLAYBOOK_18)

    # Terms/strings that are artifacts of one specific prior sprint, not
    # transferable facts. Their presence means an "Illustrative case" was
    # not actually generalized, or a stray incident detail leaked back in.
    project_only_terms_18 = (
        "292",              # the mis-rounded headline ratio's specific value
        "274",              # its corrected counterpart
        "0.1489",
        "151×",
        "141.9",            # the specific column-gap measurement
        "31.5133",          # the specific fused-digit-string collision
        "CONQUER",
        "main_7_29",        # a project's specific frozen-snapshot filename
        "What are you even doing",   # verbatim personal quote
        "colleague's layout work",   # verbatim personal quote
    )
    hits_18 = [t for t in project_only_terms_18 if t.casefold() in playbook_18.casefold()]
    if hits_18:
        raise AssertionError(f"project-specific sprint incident leaked into playbook 18: {hits_18}")

    if "Illustrative case" not in playbook_18:
        raise AssertionError(
            "playbook 18 must clearly label any concrete instance as an "
            "'Illustrative case', not present it as the rule itself"
        )

    # Playbook 17's own measured case is its evidence base, not forbidden --
    # unlike playbook 18's incident log, the CV/percentage figures here are
    # what the playbook teaches. What IS forbidden is presenting them without
    # the n=1/self-reported caveat, or dropping the dated, multi-source
    # framing of the bias evidence back down to one undated statistic.
    required_17 = (
        "n = 1",
        "2025",
        "generalization discipline",
        "measured case",
    )
    normalized_17 = " ".join(playbook_17.casefold().split())
    for phrase in required_17:
        if phrase.casefold() not in normalized_17:
            raise AssertionError(f"playbook 17 missing required honesty/generalization marker: {phrase!r}")

    for playbook_name, text in (("17", playbook_17), ("18", playbook_18)):
        if "Generalization discipline" not in text:
            raise AssertionError(
                f"playbook {playbook_name} is missing the 'Generalization discipline' "
                "header every extension playbook (13-18) must carry"
            )

    skill = read(SKILL_MD)
    normalized_skill = " ".join(skill.casefold().split())
    if "read as a report of what happened once on one project" not in normalized_skill:
        raise AssertionError(
            "SKILL.md Forbidden Moves must state the generalization-discipline "
            "guardrail skill-wide, not only inside individual playbook headers"
        )


def require_version_coherence() -> None:
    skill_match = re.search(r"^Version:\s*`([^`]+)`", read(SKILL_MD), re.MULTILINE)
    changelog_match = re.search(r"^##\s+([0-9]+\.[0-9]+\.[0-9]+)\s+-", read(ROOT / "CHANGELOG.md"), re.MULTILINE)
    if not skill_match or not changelog_match:
        raise AssertionError("could not parse SKILL.md or CHANGELOG version")
    if skill_match.group(1) != changelog_match.group(1):
        raise AssertionError(
            f"version drift: SKILL.md={skill_match.group(1)}, CHANGELOG={changelog_match.group(1)}"
        )


def require_local_source_assets_do_not_enter_publishable_package() -> None:
    tracked = subprocess.run(
        ["git", "ls-files", "Original_Transcript+PDF"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    if tracked:
        raise AssertionError("raw original transcripts/PDFs must remain local verification sources")
    validation = subprocess.run(
        ["python3", "scripts/validate_package.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if validation.returncode != 0:
        raise AssertionError(
            "package validation must inspect the tracked release surface, not reject local untracked sources:\n"
            + validation.stdout
            + validation.stderr
        )


def main() -> int:
    require_course_fidelity()
    require_course_consistent_conclusion_rule()
    require_general_feedback_playbook()
    require_general_sprint_and_register_playbooks()
    require_version_coherence()
    require_local_source_assets_do_not_enter_publishable_package()
    print("course fidelity and generality contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
