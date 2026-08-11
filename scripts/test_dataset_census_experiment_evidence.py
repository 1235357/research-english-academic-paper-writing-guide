#!/usr/bin/env python3
"""Regression checks for dataset census, experiment expansion, and release evidence."""

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
    require_table_schema,
    require_unique_section,
)


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "research-english-academic-paper-writing-guide"
PLAYBOOK = SKILL / "references" / "playbooks" / "13-review-feedback-evidence-contract.md"


DATASET_CENSUS_SCHEMA = [
    "Canonical dataset",
    "Citation",
    "Task role",
    "Construction lineage",
    "Train validation and test counts",
    "Result status",
    "Exclusion reason",
]

EXPERIMENT_QUEUE_SCHEMA = [
    "Manuscript claim",
    "Closest control",
    "Evaluation contract",
    "Dataset and split",
    "Seeds",
    "Metric and decision rule",
    "Result or log destination",
    "Resource budget",
    "Stop condition",
]

RELEASE_INVENTORY_SCHEMA = [
    "Path",
    "Role",
    "License or redistribution status",
    "Checksum",
]


def validate_dataset_experiment_release(text: str) -> None:
    census = require_unique_section(text, "Dataset census and imported-number provenance", 3)
    require_sentence(census, "dataset census", "repository", "rather than from the draft")
    require_table_schema(census, DATASET_CENSUS_SCHEMA)
    require_sentence(
        census,
        "source table or page",
        "task",
        "split",
        "horizon",
        "features",
        "supervision",
        "metric",
        "aggregation",
    )

    experiments = require_unique_section(text, "Claim-driven experiment expansion", 2)
    require_paragraph(
        experiments,
        "claim-driven experiment queue",
        "manuscript claim",
        "closest control",
        "evaluation contract",
        "dataset and split",
        "seeds",
        "metric",
        "result/log destination",
        "resource budget",
        "stop condition",
    )
    require_table_schema(experiments, EXPERIMENT_QUEUE_SCHEMA)
    require_sentence(experiments, "resource availability is a scheduling signal", "not evidence")
    require_sentence(
        experiments,
        "promote a result only after",
        "all planned seeds finish",
        "control is valid",
        "log is parseable",
        "claim ledger",
        "exact artifact",
    )
    require_paragraph(
        experiments,
        "update budget",
        "corpus coverage",
        "ordered subset selection",
        "tasks",
        "labels",
        "full corpus",
        "task and action coverage",
        "invalid control",
    )

    checkpoint = require_unique_section(text, "Checkpoint-coherent result rows", 3)
    require_sentence(
        checkpoint,
        "checkpoint-selection rule",
        "every metric",
        "same selected epoch",
        "artifact",
    )
    require_sentence(checkpoint, "per-metric maxima", "never assemble")
    require_paragraph(
        checkpoint,
        "paired seeds",
        "zero-score tie",
        "deterministic tie rule",
        "disclose",
    )
    require_paragraph(
        checkpoint,
        "rounded console log",
        "full-precision JSONL",
        "exact mean or standard deviation",
    )
    require_sentence(checkpoint, "metric name must match the scored event")

    identity = require_unique_section(text, "Review-artifact identity ledger", 3)
    require_paragraph(
        identity,
        "reviewed artifact hash",
        "native annotation ID",
        "source revision",
        "rebuilt PDF hash",
        "resolution status",
    )
    exemplar = require_unique_section(text, "Exemplar-format transfer gate", 3)
    require_paragraph(
        exemplar,
        "structure-only ledger",
        "table hierarchy",
        "row granularity",
        "header grouping",
        "symbol semantics",
        "caption contract",
    )
    require_sentence(exemplar, "minimum font", "legible")

    figures = require_unique_section(text, "Figure evidence cards", 2)
    require_paragraph(
        figures,
        "all figure evidence cards",
        "number",
        "example",
        "arrow",
        "module label",
        "source/result contract",
        "placeholder status",
    )
    release = require_unique_section(text, "Submission and release safety", 2)
    require_table_schema(release, RELEASE_INVENTORY_SCHEMA)
    require_paragraph(
        release,
        "package inventory",
        "every included file",
        "role",
        "license or redistribution status",
        "checksum",
    )
    require_paragraph(
        release,
        "secret scan",
        "archive members",
        "metadata",
        "generated logs",
        "version-control history",
        "clean directory",
        "smoke test",
    )
    require_no_forbidden_contradictions(text)


def verify_mutation_guards(text: str) -> None:
    terms = DATASET_CENSUS_SCHEMA + EXPERIMENT_QUEUE_SCHEMA + RELEASE_INVENTORY_SCHEMA + [
        "Dataset census and imported-number provenance",
        "dataset census repository rather than from the draft",
        "source table or page task split horizon features supervision metric aggregation",
        "claim-driven experiment queue manuscript claim closest control evaluation contract dataset and split seeds metric result/log destination resource budget stop condition",
        "resource availability is a scheduling signal not evidence",
        "all planned seeds finish control is valid log is parseable claim ledger exact artifact",
        "update budget corpus coverage ordered subset selection tasks labels full corpus task and label coverage invalid control",
        "checkpoint-selection rule every metric same selected epoch artifact per-metric maxima",
        "paired seeds zero-score tie deterministic tie rule disclose",
        "rounded console log full-precision JSONL exact mean or standard deviation",
        "metric name must match the scored event",
        "review-artifact identity ledger native annotation ID rebuilt PDF hash",
        "structure-only ledger minimum font legible",
        "all figure evidence cards number example arrow module label source/result contract placeholder status",
        "package inventory every included file role license or redistribution status checksum secret scan archive members metadata generated logs version-control history clean directory smoke test",
    ]
    require_mutation_rejected(
        "keyword bag", validate_dataset_experiment_release, keyword_bag(terms)
    )
    require_mutation_rejected(
        "section relocation",
        validate_dataset_experiment_release,
        relocate_once(
            text,
            "Separate the update budget from corpus coverage. Limiting updates per epoch is not equivalent to permanently limiting the dataset. Audit the loader before running: ordered subset selection can preserve the requested update count while silently removing tasks or labels. For a budget-matched study, sample from the full corpus with a predeclared seeded or stratified rule unless reduced-corpus exposure is the intended intervention. Record full-corpus and selected-subset sample, task and label coverage. If a subset is biased, quarantine the run as an invalid control and rerun; do not explain the resulting collapse as a method limitation.",
        ),
    )
    require_mutation_rejected(
        "negation reversal",
        validate_dataset_experiment_release,
        replace_once(
            text,
            "Resource availability is a scheduling signal, not evidence of contribution or a reason to launch redundant runs.",
            "Resource availability is research evidence and a reason to launch redundant runs.",
        ),
    )


def main() -> int:
    text = PLAYBOOK.read_text(encoding="utf-8")
    validate_dataset_experiment_release(text)
    verify_mutation_guards(text)

    print("dataset/experiment/release semantic contract passed (3 mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
