# Model Framework Diagram Drawing Overview

> Task playbook distilled from 第七讲：英文学术论文之写作思路——模型框架图绘制概述 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-07-framework-figure-overview.md`


## Operating principle

Always apply this skill by default when helping with academic research writing, especially method sections and model/framework diagrams. Treat the model framework figure as the logic skeleton for the method section, not as a decorative illustration.

## Mandatory workflow

1. Identify the paper's core challenge and the method's actual innovation before drawing or editing the figure.
2. Decompose the method into modules. For each module, state the sub-problem it solves, its input, output, variables, and algorithmic role.
3. Draft the full input-to-output pipeline before polishing. Include training/test differences when relevant.
4. Name every important variable, embedding, matrix, distribution, operator, prediction, and loss.
5. Draw module boundaries explicitly. Align module titles, background regions, arrows, and textual explanation.
6. Enforce visual consistency: same concept means same color, shape, symbol, granularity, and naming throughout the figure.
7. Remove redundant elements; keep only information that changes reader understanding.
8. Use the final figure as the outline of the Methodology section. Map figure modules to section headings and submodules to paragraphs or subheadings.
9. Preserve versions and record what each revision fixed, especially for first-paper or first-figure workflows.

## Review questions to ask every time

Ask these questions in the reader or reviewer voice:

- What is each element?
- What problem does each module solve?
- How does each module solve it?
- Where is the technical innovation?
- Where are the module boundaries?
- What are the training and testing flows?
- Are symbols, colors, vectors, image sizes, and text styles consistent?
- Is any content redundant?
- Does the Methodology section follow the same structure as the figure?

## Output style

When producing feedback, organize it as: `core logic`, `module decomposition`, `figure clarity`, `symbol/visual consistency`, `figure-to-text alignment`, and `next revision actions`. For a draft figure or method section, prioritize logic and boundary fixes before typography or color polish.

---

## Appendix: course templates and checklists for this lecture

## model framework diagram review checklist

Use this checklist when planning, reviewing, or rewriting a paper's model/framework figure and the corresponding method section.

### core questions

1. What core challenge does the method solve?
2. How is the method decomposed into modules?
3. Which sub-problem does each module solve?
4. What are the input, output, and intermediate variables of each module?
5. Which parts are routine preprocessing/encoding and which parts are the paper's actual innovation?
6. Can the reader identify training and testing flows when they differ?
7. Can the reader map the figure to the method section headings?

### figure revision sequence

1. Draft the full input-to-output pipeline.
2. Label every important variable, embedding, matrix, distribution, operator, and loss.
3. Draw module boundaries before polishing colors.
4. Align module titles with exact module ranges.
5. Use a consistent visual language: same concept, same color, same shape, same granularity.
6. Add legends for operators such as matrix product, dot product, pooling, sampling, and loss symbols.
7. Normalize typography, sizes, spacing, and line routing.
8. Remove redundant elements that do not change understanding.
9. Preserve every version and record what was fixed.
10. Use the final figure as the outline for the Methodology section.

### The lecture's worked example: MuKEA's framework figure, V1 through V8

The entire lecture is organized around one real revision history — a
student's MuKEA framework figure evolving from a rough first sketch to the
final camera-ready version, roughly 20+ real intermediate versions
compressed into 8 representative snapshots. The instructor's own framing:
polishing colors/fonts is not the point; the point is that a figure's job is
to fast-track the reader's understanding of the paper's logic and
innovation, and to make the text passages that can't be conveyed visually
easy to locate. Use this table as a diagnostic: find which row a draft
figure most resembles, and apply that row's "next step."

| Version | Goal / change made | Main progress | Main problem | Next revision |
| --- | --- | --- | --- | --- |
| V1 | Intuitively record model input/output | Shows input-awareness; question and image enter the pipeline | Process unclear; module boundaries unclear; unclear how the problem gets solved; text/figures too small | Enlarge key information; add output, train/test flow, key modules, and the innovation |
| V2 | Sketch the full implementation process | Process more complete; starts using field-standard symbols (embedding, matrix, loss) | Module boundaries still unclear; still can't see what problem is solved; wrapped terms and layout impede reading | State what every symbol is; make the method decomposition and each step's role explicit |
| V3 | Define process goals and variable names; detail each stage; avoid crossing lines | All intermediate results/processes are named; begins dividing into two key modules | Module boundaries still unclear; algorithmic logic still not explicit enough | Use module boundaries, background color, and titles to make key-process scope explicit |
| V4 | Color-code modules, emphasize module titles | Stronger sense of module partitioning | Titles don't align with modules; layout not intuitive | Align titles to background regions; make module boundaries legible at a glance |
| V5 | Make title layout more consistent overall | Title-module correspondence improves | Font inconsistent; formatting non-standard; image sizes inconsistent | Unify font, font size, image size, and local details |
| V6 | Consistent font/size, standard-looking layout | Formal standardization improves | Colors messy, too much text, too many lines; important symbols unannotated; same-symbol backgrounds inconsistent | Reduce information density; unify symbol backgrounds; add necessary annotations |
| V7 | Consistent representation for identical content, symbols annotated | Same-type info now color-consistent; symbol explanations more standard | Identical content doesn't correspond front-to-back; inconsistent vector counts; redundant elements | Remove redundancy; ensure identical concepts look identical everywhere in the figure |
| V8 | Final version | Modules, variables, symbols, layout, and figure-text correspondence all basically clear | Usable directly as the skeleton for writing the Methodology section | Write the Method section against the framework figure, keeping module-to-heading correspondence exact |

The instructor's own closing point on this arc: the final version did not
appear out of nowhere — it took roughly 20+ real intermediate versions from
the first draft (October) to the final one (November). Tell users this
directly when they're discouraged by how rough a first figure draft looks:
many revisions is the normal path, not a sign something is wrong.

### warning signs from lecture 7

- "what is this?" means labels, symbols, or examples are underspecified.
- "what problem does this solve?" means module motivation is missing.
- "how is it solved?" means algorithmic logic is not visible enough.
- "where are module boundaries?" means titles, backgrounds, and arrows are misaligned.
- "too many colors/text/lines" means the figure is visually noisy.
- "same content is inconsistent" means the reader may infer a new concept where none exists.
- "redundant elements" means the figure can be simplified without information loss.

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-07-framework-figure-overview.md`
- Once this figure's content is designed, authoring the schema document and
  placeholder (and the human-only rendering gate) follow
  `14-figure-schema-and-rendering-gate.md`.
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
