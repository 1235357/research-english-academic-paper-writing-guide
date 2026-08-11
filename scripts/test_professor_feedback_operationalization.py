#!/usr/bin/env python3
"""Regression checks for operationalizing detailed advisor feedback."""

from __future__ import annotations

from pathlib import Path

from playbook_contract import (
    keyword_bag,
    relocate_once,
    replace_once,
    require_mutation_rejected,
    require_no_forbidden_contradictions,
    require_paragraph,
    require_sentence,
    require_unique_section,
)


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "research-english-academic-paper-writing-guide"
PLAYBOOK = SKILL / "references" / "playbooks" / "13-review-feedback-evidence-contract.md"


def validate_operationalization(text: str) -> None:
    triage = require_unique_section(text, "Mandatory triage", 2)
    require_paragraph(
        triage,
        "native annotation objects",
        "author",
        "creation time",
        "page or paragraph anchor",
        "object ID",
        "exact text",
    )
    require_sentence(
        triage, "conditional or ambiguous feedback", "optional", "pending confirmation"
    )
    require_sentence(triage, "permission is not evidence")
    require_paragraph(
        triage,
        "configurations",
        "logs",
        "checkpoints",
        "result artifacts",
        "experimental facts",
        "venue documents",
        "submission policy",
    )

    tables = require_unique_section(text, "Table and citation rules", 2)
    require_sentence(tables, "one row per dataset or method", "distinct provenance")
    require_sentence(tables, "never write", "and related sources", "claim-bearing table")
    comparison = require_unique_section(text, "Comparison eligibility", 3)
    require_sentence(
        comparison,
        "comparison-eligible",
        "task output",
        "observable inputs",
        "split",
        "horizon",
        "features",
        "supervision",
        "oracle information",
        "metric definition",
        "aggregation statistic",
    )

    artifact = require_unique_section(text, "Artifact and provenance gate", 2)
    require_sentence(artifact, "generated artifact is stale", "declared inputs", "changed")
    require_paragraph(
        artifact,
        "backbone claim",
        "encoder",
        "configuration",
        "checkpoint",
        "result artifact",
        "one chain",
    )

    language = require_unique_section(text, "Language and finding discipline", 2)
    require_sentence(language, "one sentence", "one core meaning")
    require_paragraph(
        language,
        "borrow, adapt, or imitate",
        "task",
        "output",
        "supervision",
        "mechanism",
        "evaluation axes",
    )
    title = require_unique_section(text, "Title-level mechanism gate", 3)
    require_sentence(title, "method-name claim", "technical claim", "not branding")
    require_sentence(
        title,
        "matched",
        "distinguishing experiment",
        "compatible inputs",
        "supervision",
        "compute budget",
        "selection rule",
        "evaluation contract",
    )

    figures = require_unique_section(text, "Figure evidence cards", 2)
    require_paragraph(
        figures,
        "figure evidence card",
        "reader question",
        "one core claim",
        "source artifact",
        "comparison contract",
        "body-text anchor",
        "status",
    )
    release = require_unique_section(text, "Submission and release safety", 2)
    require_sentence(release, "do not use a credential", "reviewer material")
    require_sentence(release, "revoke", "rotate", "safe to distribute")
    require_no_forbidden_contradictions(text)


def verify_mutation_guards(text: str) -> None:
    terms = [
        "Mandatory triage",
        "native annotation objects author creation time page or paragraph anchor object ID exact text",
        "conditional or ambiguous feedback optional pending confirmation",
        "permission is not evidence",
        "one row per dataset or method distinct provenance",
        "and related sources claim-bearing table",
        "comparison-eligible task output observable inputs split horizon features supervision oracle information metric definition aggregation statistic",
        "generated artifact is stale declared inputs changed",
        "encoder configuration checkpoint result artifact one chain",
        "one sentence one core meaning",
        "borrow adapt or imitate task output supervision mechanism evaluation axes",
        "method-name claim technical claim not branding",
        "matched distinguishing experiment compatible inputs supervision compute budget selection rule evaluation contract",
        "figure evidence card reader question one core claim source artifact comparison contract body-text anchor status",
        "credential reviewer material revoke rotate safe to distribute",
    ]
    require_mutation_rejected("keyword bag", validate_operationalization, keyword_bag(terms))
    require_mutation_rejected(
        "section relocation",
        validate_operationalization,
        relocate_once(text, "Permission is not evidence."),
    )
    require_mutation_rejected(
        "negation reversal",
        validate_operationalization,
        replace_once(text, "Permission is not evidence.", "Permission is evidence."),
    )


def main() -> int:
    text = PLAYBOOK.read_text(encoding="utf-8")
    validate_operationalization(text)
    verify_mutation_guards(text)

    print("professor-feedback operationalization passed (3 mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
