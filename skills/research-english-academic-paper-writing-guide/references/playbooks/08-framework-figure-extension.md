# English Academic Paper Writing: Writing Ideas - Model Framework Diagram Drawing Extension

> Task playbook distilled from 第八讲：英文学术论文之写作思路——模型框架图绘制延伸 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-08-framework-figure-extension.md`


Apply this skill as standing guidance. When the task is unrelated to academic figures, still preserve the meta-principles: identify the communicative purpose, separate contribution from background, remove irrelevant detail, name concepts consistently, and make the final answer traceable to the user's materials.

## Core doctrine

A model framework figure is not a visual dump of everything the author did. It is a reader-facing argument. It must answer the few questions a reviewer must understand before they can believe the contribution.

Use this priority order:

1. Clarify the expected reader's confusion.
2. Identify the actual contribution type.
3. Allocate the most visual and textual space to the contribution, not to the longest implementation step.
4. Make inputs, outputs, and key processes explicit.
5. Use module boundaries to show which intermediate problem each module solves.
6. Name every process, variable, and symbol with terms consistent with the manuscript and field convention.
7. Keep identical semantics visually and textually consistent across the figure and paper.

## Contribution-type routing

Choose the actual contribution and reader need. These course examples are not an
exhaustive taxonomy; frameworks without pretraining/fine-tuning should show their
actual interfaces and processes. Data, evaluation, systems and delivery figures
may emphasize access boundaries, contracts, latency, reliability or recovery.
Do not invent a training stage or scientific novelty to fit the example.

### Transferred pretraining framework (the ET-BERT case)

Examples: ET-BERT for encrypted traffic classification with pre-training transformers.

Show:
- how raw domain data becomes model-consumable input;
- what new pre-training or representation task is designed;
- how downstream fine-tuning works;
- which parts are domain-specific adaptations rather than generic borrowed framework pieces.

Do not overdraw:
- generic preprocessing;
- traditional baseline comparisons;
- familiar transformer internals unless they are modified.

### Complex multi-module model

Examples: DualVD visual dialogue framework.

Show:
- complete input and output objects;
- separate information-flow paths with clear module boundaries;
- concrete, minimal examples for text, image regions, graph nodes, or relation paths;
- enough process detail that a reader can follow each arrow.

Do not include every raw datum. A framework figure is a selective schematic.

### Local mechanism contribution such as loss, objective, training strategy, or debiasing

Examples: CogTree loss for unbiased scene graph generation.

Show:
- the mechanism in detail;
- the real or representative data that exposes the core problem;
- a measured before/after effect with source/settings, or an explicitly labeled schematic/expected distribution or bias change;
- training and prediction paths separately if they differ.

Compress inherited backbone detail only where its identity, input/label flow, assumptions and interfaces remain clear or precisely referenced. Preserve reproducibility-critical boundaries even when they are not novel, then emphasize the actual contribution.

## Figure planning workflow

Before drafting or reviewing a diagram, answer these questions explicitly:

1. What are the input, output, and key process?
2. What is the paper's real contribution: framework, module, data representation, task, pre-training objective, loss, training procedure, or analysis mechanism?
3. What must a skeptical reviewer understand first?
4. Which components are only background or existing methods?
5. What terms, symbols, and variables must match the manuscript exactly?
6. Which examples are minimal, intuitive, and closest to the core problem?
7. Does the figure explain mechanism and effect, or only repeat a process list?

## Review checklist

Reject or revise a figure when any of these are true:

- The figure looks polished but the innovation is not visible.
- Routine background crowds out the contribution or necessary interfaces; retain preprocessing, baselines and inherited components when central to the claim or its validity.
- The most saturated colors or boldest boxes are not the contribution.
- Modules are shown but their purpose is not legible.
- Training, fine-tuning, inference, or prediction paths are mixed without distinction.
- A loss or objective is reduced to a tiny block even though it is the main contribution.
- Figure terminology differs from the methodology text.
- Symbols, colors, line styles, or names are reused inconsistently.
- The diagram includes raw examples that do not help explain the core problem.
- The diagram cannot be described in one contribution-centered sentence.

## Response behavior

When helping with a manuscript, figure, method section, or lecture reconstruction:

1. State the contribution type first.
2. Identify what the figure or text must make the reader believe.
3. Recommend what to emphasize, what to suppress, and how to name modules.
4. Provide a concrete figure structure in text before suggesting visual polish.
5. Preserve source fidelity. If using the bundled lecture, cite the relevant page or transcript section in prose.
6. When the user requests markdown-only reconstruction, do not embed images. Describe slide visuals precisely in text, tables, or code-block schematics.

---

## Appendix: course templates and checklists for this lecture

## Framework Diagram Playbook Derived from Lecture 8

### One-sentence rule

Do not draw what you happened to implement; draw what the reviewer must understand to believe the contribution.

### Five non-negotiable principles

1. Make input, output, and key process explicit.
2. Highlight innovation and avoid listing non-contribution content.
3. Divide modules by the problem each module solves.
4. Name every process, variable, and symbol precisely.
5. Keep identical meanings consistent between figure and manuscript.

### ET-BERT lesson: new framework in an old domain

When adapting a known framework such as pre-training transformers to a domain where readers do not expect it, draw the domain-specific bridge:

- raw traffic -> datagram/token representation;
- pre-training tasks -> why they are meaningful despite invisible content;
- fine-tuning tasks -> why they match domain needs.

Avoid using the figure for traditional method comparison. Put that in motivation or related work.

### DualVD lesson: complex can still be clear

A complicated diagram is acceptable when:

- inputs and outputs are explicit;
- information paths are separated;
- module names are specific;
- arrows imply actual data flow;
- examples are selected, not exhaustive.

### CogTree lesson: draw the mechanism, not the inherited framework

When the contribution is a loss or objective:

- sketch the existing model only enough to locate where the loss applies;
- draw the loss construction and effect in detail;
- use a real example aligned with the core problem;
- distinguish observed distribution/representation changes from schematic expectations; neither alone proves a causal mechanism;
- separate training and prediction if they differ.

### Pre-drawing prompt template

Use this prompt internally before producing a figure plan:

```text
The paper's contribution is: [type].
The figure must convince the reader that: [claim].
The likely reviewer confusion is: [questions].
The figure's largest visual region should be: [innovation].
The figure should suppress or omit: [background details].
The exact module names that must match the text are: [names].
The minimal running example is: [example].
```

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-08-framework-figure-extension.md`
- Once this figure's content is designed, authoring the schema document and
  placeholder (and the human-only rendering gate) follow
  `14-figure-schema-and-rendering-gate.md`.
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
