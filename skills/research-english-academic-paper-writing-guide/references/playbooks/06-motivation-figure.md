# Research Motivation Figure Drawing

> Task playbook distilled from 第六讲：英文学术论文之写作思路——研究动机图绘制 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-06-motivation-figure.md`


## Purpose

Apply Yu Jing's lecture method for turning an academic paper's research motivation into a reviewer-facing visual argument. Treat the research motivation figure as the backbone of the paper introduction: it must make the solved problem, prior-work limitation, proposed innovation, representative examples, and narrative logic visible before the reader studies the full paper.

Use this skill as a default thinking layer. When the user asks for any research-writing, paper-revision, figure-design, motivation, introduction, contribution, related-work, or academic communication task, run the relevant checks below before answering.

## Core Doctrine

A motivation figure is not decoration and not an author-only memo. It is a compact argument for reviewers who have not worked on the project. It must answer:

1. What scientific or technical problem is being solved?
2. Why is this problem important?
3. Why do existing methods or representations fail?
4. What is the paper's new idea, framework, or implementation detail?
5. Which examples prove the contrast sharply and without ambiguity?
6. How does the figure map onto the introduction's background -> status quo -> problem -> method logic?

## Default Workflow

For any relevant task, proceed in this order:

1. **Classify the contribution type.** Decide whether the work is mainly a new idea/small model, a new framework/large model, or a technical implementation refinement. If unclear, state the ambiguity and infer a working type.
2. **Separate demand, scientific problem, and solution.** Do not let the proposed method masquerade as the problem. Write the actual need, the research problem behind it, and the method separately.
3. **Extract the contrast.** Identify what existing methods can do, what they cannot do, and the exact dimension where the proposed method differs.
4. **Choose representative examples.** Prefer examples that are vivid, unambiguous, reviewer-credible, and collectively cover the paper's central claim.
5. **Standardize the comparison.** Compare existing and proposed approaches at the same level of abstraction. For framework papers, modularize every method into the same pipeline stages and highlight differences at the same stage.
6. **Use precise terminology.** Replace vague labels with task-accurate terms. Define arrows, symbols, abbreviations, inputs, outputs, entities, relations, and modules.
7. **Align with the introduction.** Map each major figure element to the exact introduction paragraph or sentence it supports.
8. **Review from the non-author viewpoint.** Ask whether a reviewer can infer the problem, limitation, innovation, and contribution from the figure alone. If not, revise.

## Revision Heuristics from the Lecture

Use the MuKEA iteration pattern when the contribution is a new idea or representation:

- V1 failure: intuitive motivation only; arrows unclear; core problem missing; no professional symbols.
- V2 failure: examples chosen but labels vague, triples listed too textually, examples may be ambiguous, layout unprofessional.
- V3 improvement: unified graph-like representation and better examples, but paper contribution may still be unclear.
- Final target: highlight entities and relations, mark prior-method failure vs proposed-method success, and make the figure correspond to introduction text.

Use the ET-BERT iteration pattern when the contribution is a new framework:

- V1 failure: technical history, data, methods, and outputs mixed together; framework differences inaccurate.
- V2 failure: more categories but capability boundaries remain fuzzy; innovation hidden behind existing model names.
- Final target: one modular pipeline shared by all compared frameworks, with differences shown at the same processing stage.

## Common Anti-Patterns

Flag and fix these immediately:

- The figure is understandable only to the authors.
- The figure lacks the core problem or why it matters.
- Arrows, icons, or colors have no defined meaning.
- Examples are biased, ambiguous, or too narrow to support the claim.
- The comparison mixes levels such as data source, model family, feature type, and learning paradigm in one row.
- Terms are broad or inaccurate, such as calling a specific knowledge graph merely "textual knowledge".
- Long lists of triples or modules force the reviewer to search manually for the point.
- The proposed method is labeled only with generic existing names, hiding the actual innovation.
- Figure elements do not appear in the introduction's narrative logic.

## Output Patterns

When asked to design or revise a motivation figure, return one of these structures unless the user requests a different format:

- **motivation figure brief**: problem, limitation, innovation, examples, layout, symbol semantics, introduction mapping.
- **figure review report**: verdict, missing problem, terminology issues, weak examples, unclear visual logic, figure-text mismatch, prioritized fixes.
- **iteration plan**: current version diagnosis, next-version edits, final-version acceptance criteria.
- **introduction alignment map**: paragraph-by-paragraph mapping from background/status quo/problem/method to figure elements.

## Quality Gate

Before finalizing any answer influenced by this skill, verify:

- The solved problem is explicit.
- The proposed innovation is explicit.
- At least one contrastive, representative example is identified or requested.
- Terminology and symbol semantics are precise.
- Existing and proposed methods are compared at the same abstraction level.
- The figure can be narrated directly inside the paper introduction.

---

## Appendix: course templates and checklists for this lecture

## Motivation Figure Workflow

### 1. Start from the introduction problem

A research motivation figure should be designed from the introduction's logical chain, not from the method diagram. Write these four statements first:

1. Background: what broad research context makes the task important?
2. Status quo: how do existing methods typically address it?
3. Problem: what important limitation remains?
4. Method direction: what new idea/framework/mechanism addresses the limitation?

If any statement is missing, do not draw the figure yet.

### 2. Match contribution type to figure strategy

#### New idea / new representation / small model

Use concrete examples to show what existing representations miss and what the proposed representation captures.

Canonical structure:

```text
input example -> existing representation and failure -> proposed representation and success
```

Lecture anchor: MuKEA moved from vague motorcycle examples to a final contrast between Knowledge Graph and Multimodal Knowledge, with entities and relations highlighted and the figure tied to the introduction.

#### New framework / large model

Use modular pipeline comparison. Every method row must use the same stages.

Canonical structure:

```text
method family -> input/data/domain -> representation/features -> learning/processing -> output/capability
```

Lecture anchor: ET-BERT reached its final version only after all compared frameworks were unified into the same processing pipeline.

#### Technical implementation detail

Use a precise example to expose the implementation-level limitation and show how the new mechanism changes the behavior.

Canonical structure:

```text
concrete failure case -> old mechanism behavior -> new mechanism behavior -> improved result
```

Lecture anchors: DualVD, DAM, and CogTree each use a motivation figure to foreground the key problem and research idea.

### 3. Select examples

Accept examples only if they satisfy all of the following:

- They are directly tied to the paper's central claim.
- They are easy for a reviewer to understand without extra context.
- They do not rely on controversial or biased assumptions.
- Together they cover the major cases claimed in the paper.
- They create a visible contrast between existing and proposed approaches.

Reject examples that are merely visually attractive, idiosyncratic, ambiguous, or unrelated to the contribution.

### 4. Make terminology exact

Use labels that match the actual technical object.

- Write "Knowledge Graph" when the object is a graph of entities and relations.
- Write "Multimodal Knowledge" when the contribution combines visual and textual modalities.
- Write the actual data type in input blocks, not the method name.
- Write the paper's own module or framework name when it is the innovation, not only generic backbone names.

### 5. Reduce reviewer effort

The figure should minimize search time. Use:

- boxes for entities/modules,
- labels for relations/arrows,
- consistent columns/rows,
- alignment across compared cases,
- concise text instead of long lists,
- symbols only when their semantics are obvious or defined.

### 6. Tie the figure to text

For each figure component, write the introduction sentence it supports. If no sentence exists, either revise the introduction or remove the component.

Recommended mapping:

| figure component | introduction role |
|---|---|
| task example | concrete grounding of background or demand |
| existing method block | related-work status quo |
| failure marker | limitation or unresolved challenge |
| proposed method block | contribution preview |
| success marker | claimed advantage |
| multiple examples | scope and generality claim |

### 7. Final acceptance criteria

A motivation figure is ready only when a non-author can answer these four questions after looking at it for less than one minute:

1. What problem is the paper solving?
2. Why are existing methods insufficient?
3. What is new about the paper?
4. How will the introduction explain this figure?

## Checklists and Templates

### Motivation Figure Design Brief

```markdown
# Motivation Figure Design Brief

## Contribution type
- New idea / representation:
- New framework:
- Technical implementation detail:

## Core problem
- Practical demand:
- Scientific/technical problem:
- Why important:

## Existing method limitation
- Existing method or representation:
- What it captures:
- What it misses:
- Why the missing part matters:

## Proposed innovation
- New idea/framework/mechanism:
- Exact contrast with existing methods:
- What problem it solves:

## Examples
| example | why representative | existing method failure | proposed method success | introduction paragraph |
|---|---|---|---|---|
| | | | | |

## Visual logic
- Left side:
- Middle:
- Right side:
- Rows/columns:
- Arrow semantics:
- Symbol semantics:
- Terms requiring definition:

## Figure-text alignment
- Background sentence:
- Status quo sentence:
- Limitation sentence:
- Method preview sentence:
```

### Motivation Figure Review Report

```markdown
# Motivation Figure Review Report

## Verdict
- Ready / needs revision:
- One-sentence reason:

## Core problem
- Is the solved problem explicit?
- Missing or unclear elements:
- Revision:

## Innovation contrast
- Existing method shown:
- Proposed method shown:
- Exact contrast:
- Revision:

## Examples
- Representative:
- Unambiguous:
- Covers claimed scope:
- Revision:

## Terminology and symbols
- Inaccurate terms:
- Undefined arrows/symbols:
- Replacement labels:

## Layout and reviewer effort
- Main confusion point:
- Simplification:
- Alignment/modularization fix:

## Introduction mapping
- Figure element without text support:
- Text claim without figure support:
- Fix:
```

### Figure-to-Introduction Alignment Map

```markdown
| introduction move | paragraph goal | figure element | exact wording to use in prose |
|---|---|---|---|
| background | | | |
| status quo | | | |
| limitation | | | |
| proposed idea | | | |
| contribution | | | |
```

### Rapid Quality Gate

Before delivering a revised figure plan, answer yes/no:

1. Can a non-author identify the problem?
2. Can a non-author identify why existing methods fail?
3. Is the proposed innovation visible without reading the method section?
4. Are examples representative and low-ambiguity?
5. Are all arrows and symbols semantically defined?
6. Are compared methods shown at the same abstraction level?
7. Does each figure element map to introduction prose?
8. Would removing any element improve clarity?

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-06-motivation-figure.md`
- Once this figure's content is designed, authoring the schema document and
  placeholder (and the human-only rendering gate) follow
  `14-figure-schema-and-rendering-gate.md`.
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
