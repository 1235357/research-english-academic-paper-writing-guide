# Experiments, Conclusion, and References

> Task playbook distilled from 第五讲：英文学术论文之写作思路——实验、结论和参考文献 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-05-experiments-conclusion-references.md`


## Operating principle

Apply this skill to keep every research-writing decision centered on the paper's core problem. Always check whether the paper's problem, method, experiment, conclusion, and references form one aligned story:

```text
problem -> method designed for the problem -> experiments proving the method -> conclusion after verification -> references supporting the research context
```

For detailed course-derived explanations and source context, consult `references/lectures/lecture-05-experiments-conclusion-references.md`. For provenance, use `references/provenance.md`.

## Default workflow for paper-writing tasks

1. Identify the central research problem and the specific claim the section must support.
2. Map each method component to the problem it solves.
3. Require experiments to prove those method components and the original motivation one by one.
4. Write analysis in this order: conclusion first, factual support second, mechanism explanation third, exception or limitation fourth.
5. Close with verified conclusions, explicit limitations, future work, complete acknowledgements, and checked references.

## Experiment section standards

Use five requirements as a review checklist:

- Consistency: experiments must support the theory, method, and introduction motivation.
- Core results: foreground important evidence; do not give all experiments equal weight.
- Honesty: do not cherry-pick the best run, the best case, or the prettiest visualization. Mention error bars, fluctuations, parameter settings, and representative cases when relevant.
- Analysis: explain why results happen, including comparable or worse results.
- Limitations: state the method's capability boundary.

Flag these failure modes immediately:

- The paper only reports SOTA but lacks analysis.
- The method is written as `step1 -> step2 -> step3` without explaining why each step solves the problem.
- The problem, method, and experiments each tell a different story.
- The experiment section repeats table values instead of deriving conclusions.
- The paper hides weak results, omits limitations, or overclaims beyond the evidence.

## Result comparison pattern

When writing or revising comparison with existing methods, structure the paragraph as:

```text
Conclusion: state the main finding from the table or figure.
Evidence: cite the relevant datasets, metrics, and method groups.
Mechanism: explain which design difference causes the result.
Exception: analyze weaker or abnormal results, including dataset properties, fairness, extra data, extra knowledge, or task mismatch.
```

Before analyzing results, group baseline methods by technical route so later comparisons can discuss method-level differences instead of reintroducing every baseline.

## Ablation study pattern

Do not list ablations as an undifferentiated set of variants. Group them by design dimension, such as:

- representation or modality components;
- reasoning or inference steps;
- encoding choices;
- objective functions, losses, or training strategies;
- data, knowledge, retrieval, or prompt components.

For each dimension, answer:

- what design choice is being verified;
- what role the component plays;
- whether it works alone or synergistically with other components;
- which metrics or examples show the effect;
- whether the evidence supports the claim made in the method section.

A weak ablation statement says: "removing each module decreases performance." A strong ablation analysis explains what each module contributes and why that contribution matters.

## Visualization and interpretation pattern

Never merely redescribe a figure or its caption. For qualitative, visualization, attention, explanation, or case-study analysis, write:

```text
Observation 1: what capability the visualization demonstrates.
Evidence 1: which case, node, relation, attention, retrieved fact, generated answer, or error supports it.
Observation 2: how the visualization distinguishes the method from baselines.
Boundary: what the visualization reveals about failures or multiple plausible answers.
```

Use representative examples rather than only the best cases. Add statistics when possible.

## Conclusion section standards

Distinguish the conclusion from the abstract:

- The abstract introduces motivation, method idea, and headline result before the reader sees the paper.
- The conclusion states findings after all experiments and analysis have verified them.

A good conclusion should:

1. summarize the work and the specific problem solved;
2. state the verified main findings;
3. describe the effect or performance level without exaggeration;
4. mention limitations or capability boundaries;
5. indicate future work.

Avoid repeating the introduction or restating all numerical results.

### Limitation honesty, placement, and conclusion closure

Never delete, soften, or hide a true limitation. A limitation is part of the
paper's evidence boundary, not a confession of failure. The conclusion should
briefly mention limitations or capability boundaries and identify future work,
as Lecture 5 requires.

Avoid mechanical repetition. Give essential protocol boundaries where readers
need them to interpret a method or result. Then use the conclusion to synthesize
the most consequential boundary and the corresponding next direction rather
than copying the same sentence or every number again. If a venue permits
supplementary material, detailed mechanisms, secondary diagnostics, and full
numeric breakdowns may move there, but the main paper must remain interpretable
on its own.

Write the boundary neutrally: state the documented design choice, what it
supports, what it does not establish, and what evidence would extend it. Do not
open the conclusion with a list of caveats; first summarize the verified
contribution, then close with a concise boundary and future direction.

## Acknowledgement standards

For camera-ready or final manuscripts, include only appropriate non-author acknowledgements:

- people who helped but are not co-authors;
- institutions, datasets, platforms, or resource providers;
- grants and project funding;
- reviewers or researchers who provided suggestions, when appropriate.

Do not use acknowledgements to obscure authorship contributions.

## Reference standards

Check references for completeness and format before submission:

- no missing important related work;
- conference or journal format compliance;
- correct title capitalization;
- correct full names or abbreviations of venues;
- correct author spelling;
- no missing year, venue, volume, issue, pages, DOI, or arXiv identifiers when required.

Treat reference quality as part of the paper's professionalism.

## Revision timeline guidance

Encourage writing and revision throughout the research process:

```text
project start        -> project slides: motivation and planned method
reliable results     -> paper framework: contributions, method framework, experiments, introduction
one month before     -> paper draft: complete content, covered experiments, figures/tables
one week before      -> paper revision: experiments, logic, language, figures/tables, 10+ revisions
submission deadline  -> complete study and submit the best reachable version
```

For deadline planning, recommend maintaining project slides from the beginning and evolving them into the paper framework.

## Output checklists to use in responses

When reviewing a draft, provide a compact diagnosis under these headings when useful:

```text
Problem-method-experiment alignment
Core experimental evidence
Missing analyses or abnormal results
Ablation and module-level proof
Interpretation or qualitative evidence
Limitations and future work
Conclusion vs abstract
Acknowledgements and references
Revision priority
```

When writing a section for the user, explicitly preserve the problem-centered logic and avoid unsupported claims. Ask for the paper's task, method, claims, tables, and target venue if the user has not provided enough context to write or review responsibly.

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-05-experiments-conclusion-references.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
