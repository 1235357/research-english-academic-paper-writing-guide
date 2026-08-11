#!/usr/bin/env python3
"""Structural regression test for the reviewer-feedback evidence playbook."""

from __future__ import annotations

from pathlib import Path

from playbook_contract import (
    keyword_bag,
    relocate_once,
    replace_once,
    require_heading_order,
    require_mutation_rejected,
    require_no_forbidden_contradictions,
    require_ordered_workflow,
    require_sentence,
    require_table_schema,
    require_unique_section,
)


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "research-english-academic-paper-writing-guide"
PLAYBOOK = SKILL / "references" / "playbooks" / "13-review-feedback-evidence-contract.md"


LEVEL_TWO_WORKFLOW = [
    "Operating principle",
    "Mandatory triage",
    "Contract discipline",
    "Table and citation rules",
    "Claim-driven experiment expansion",
    "Artifact and provenance gate",
    "Language and finding discipline",
    "Figure evidence cards",
    "Submission and release safety",
    "Output pattern",
    "Revision order",
    "Common failure modes",
    "Deep dive",
]

CLAIM_LEDGER_SCHEMA = [
    "Claim or table cell",
    "Metric or event",
    "Split",
    "Seed and checkpoint selection",
    "Evaluation contract",
    "Code entrypoint",
    "Result artifact",
    "Required revision and status",
]


def validate_playbook(playbook: str) -> None:
    title = require_unique_section(
        playbook, "Reviewer Feedback, Evidence Contracts, and Submission-Safe Revision", 1
    )
    if title.start_line != 1:
        raise AssertionError("playbook title must be the first line")
    require_heading_order(playbook, LEVEL_TWO_WORKFLOW)

    triage = require_unique_section(playbook, "Mandatory triage", 2)
    require_ordered_workflow(
        triage,
        [
            ["exact source location", "author interpretation"],
            ["claim", "venue-policy"],
            ["claim ledger", "metric", "evaluation contract", "result/log path"],
            ["P0 conflicts", "style work"],
        ],
    )
    require_table_schema(triage, CLAIM_LEDGER_SCHEMA)

    contract = require_unique_section(playbook, "Contract discipline", 2)
    require_sentence(
        contract,
        "do not mix incompatible evaluation contracts",
        "headline",
        "average",
        "ablation",
        "conclusion",
    )
    tables = require_unique_section(playbook, "Table and citation rules", 2)
    require_sentence(tables, "dataset", "method", "metric source", "table", "citation")

    revision = require_unique_section(playbook, "Revision order", 2)
    require_ordered_workflow(
        revision,
        [
            ["freeze", "review sources", "transcribe requirements"],
            ["source/TeX/PDF/result drift"],
            ["claim ledger", "comparison-contract map"],
            ["run", "exclude", "experiments"],
            ["tables", "figure evidence cards", "verified artifacts"],
            ["one sentence", "one core meaning"],
            ["rebuild", "citations/references/layout", "hashes"],
        ],
    )
    failures = require_unique_section(playbook, "Common failure modes", 2)
    require_table_schema(failures, ["Failure", "Required correction"])
    require_no_forbidden_contradictions(playbook)


def verify_mutation_guards(playbook: str) -> None:
    bag_terms = LEVEL_TWO_WORKFLOW + CLAIM_LEDGER_SCHEMA + [
        "claim ledger",
        "Do not mix incompatible evaluation contracts",
        "headline average ablation conclusion",
        "Every dataset method and metric source named in a table needs a citation",
        "compiled PDF",
        "Official submission policy",
        "credential",
        "Failure",
        "Required correction",
    ]
    require_mutation_rejected("keyword bag", validate_playbook, keyword_bag(bag_terms))
    require_mutation_rejected(
        "section relocation",
        validate_playbook,
        relocate_once(
            playbook,
            "Do not mix incompatible evaluation contracts in a headline, average, ablation, or conclusion.",
        ),
    )
    require_mutation_rejected(
        "negation reversal",
        validate_playbook,
        replace_once(
            playbook,
            "Do not mix incompatible evaluation contracts",
            "Mix incompatible evaluation contracts",
        ),
    )


def main() -> int:
    if not PLAYBOOK.is_file():
        raise AssertionError("missing reviewer-feedback evidence-contract playbook")
    playbook = PLAYBOOK.read_text(encoding="utf-8")
    skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    validate_playbook(playbook)
    verify_mutation_guards(playbook)
    if "13-review-feedback-evidence-contract.md" not in skill:
        raise AssertionError("SKILL.md does not route reviewer-feedback audits to the playbook")
    print("review-feedback structural/semantic contract passed (3 mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
