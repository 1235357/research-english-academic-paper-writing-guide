# Two-Phase Figure Workflow: Schema Authoring and the Human-Rendering Gate

> This playbook formalizes a workflow boundary that most of this course predates:
> AI image generation was not a mainstream paper-figure tool when Yu Jing's
> lectures were recorded, so Lectures 6-8 never discuss who or what physically
> renders a figure. Section "What the course actually grounds" below states
> precisely which parts of this playbook come from the transcripts and which
> parts are a general professional extension added for AI-assisted drawing
> workflows. Do not attribute the extension parts to the course itself.

> **Generalization discipline**: like playbook 13, this playbook is written
> to hold for any research project's figures. The one real-project mention
> below (a benchmark/dataset-construction figure a real AAAI-track
> submission needed beyond the course's two archetypes) is evidence that the
> course's two archetypes are a floor, not a ceiling — it is not a
> project-specific rule, and this playbook should never accumulate rules
> that only make sense for one project's specific figures.

## Core rule

**An agent may design what a figure should show. An agent may not render the
final artwork.** These are two different decisions with two different owners:

1. **Figure design** (what to draw, why, how it is organized) follows from the
   paper's actual source code, experiments, and results. An agent that has
   read the project is well positioned to do this well, and should.
2. **Figure rendering** (producing the actual image file — an AI-generated
   illustration, a hand-plotted chart PNG, anything an `\includegraphics` call
   would point to) is the paper author's decision. An agent must not do this
   on its own initiative just because the design is finished and the data is
   ready, and must not treat a standing "keep working" instruction as
   blanket authorization to start rendering artifacts it was not explicitly
   told to render. See `13-review-feedback-evidence-contract.md`'s
   "Rendering authority is separate from evidence readiness" for the
   enforcement side of this rule (evidence-card status, how to handle a
   collaborator's already-rendered files). This playbook covers the
   *authoring* side: what an agent should produce instead of a rendered image.

Until a human renders the real artwork, every figure in the manuscript stays a
placeholder (a boxed caption-plus-description stand-in, never TikZ or another
programmatic drawing that would itself constitute rendering). The placeholder
and the manuscript's prose must already be complete and internally consistent
— finishing the *text* around a figure does not require the figure itself to
exist yet.

**Tool choice matters, and is not neutral.** Favor whatever tool keeps every
element of a figure as an independently re-editable, decomposable object —
so a single module can be redrawn, recolored, or relabeled on its own,
across dozens of iterations, without rebuilding the whole figure. A
real advisor's explicit, repeated instruction on a real submission (see
Provenance) named PowerPoint specifically for this reason, over Illustrator
or Figma, whose typical export habits produce more "finished," harder to
decompose artwork. Treat PowerPoint as the default recommendation for this
reason — but confirm against the user's own advisor or venue convention
before treating a specific tool choice as universal; the generalizable
requirement is modular re-editability, not the specific application name.

**A framework/method figure carries no result numbers and no un-worked
formula blocks — and the two halves of this rule have different sourcing.**
The formula half is course-grounded, precisely: Lecture 8's transcript
states directly that a formula's *effect* belongs in the figure while the
formula itself belongs in the prose (see the Cross-validation subsection
below for the exact quote). The metric-values half — don't display the
paper's own reported accuracy/F1/etc. inside a framework figure — is
verified only against a real advisor's page-by-page review of accepted
papers (see Provenance), with no direct course parallel found; treat it as
session-sourced, not course-quoted, if a user asks where it comes from.
Neither half forbids small illustrative numbers used only to demonstrate a
labeling or scoring *convention* (e.g. a toy `0.12 / 0.81` pair showing how
a score column is read, or a `0/1` toy matrix cell showing a label
convention) — the CCGS worked example above uses exactly this kind of
illustrative number, and Lecture 8's own "real data throughout" principle
(below) is the reason why that is fine even though reported results and
raw formulas are not. The line is between "a real reported result or a
literal equation" (never in a framework figure) and "a toy number or a
formula's visible effect on real data" (fine, and often necessary for
self-sufficiency).

## What the course actually grounds

Verified directly against the Lecture 6/7/8/10 transcripts (2026-07-13 audit):

- **Grounded**: figures divide into a small number of jobs — a motivation
  figure (Lecture 6, lives in the Introduction) and a framework/method figure
  (Lectures 7-8, lives in the Method section). The course does not describe a
  results/ablation figure archetype; treat that as a natural but
  course-external extension when a paper needs one. (A real AAAI-track
  submission this skill was applied to needed a third figure job beyond
  these two — a benchmark/dataset-construction figure — confirming the
  course's two archetypes are a floor, not a ceiling, for what a real paper
  may need.)
- **Grounded**: a figure-quality checklist already exists in Lecture 8's
  closing summary and is reproduced in `07-framework-figure-overview.md` —
  input/output, key process, innovation emphasis, module boundaries,
  consistent naming, and figure-text consistency. Use that checklist, not a
  new one, when judging whether a schema is complete.
- **Grounded**: figure and body text should be **complementary, not
  redundant** — the figure carries the gist and the reader turns to the body
  text for implementation detail (Lecture 7); a good figure and its narrative
  should feel like one interwoven explanation, not two separate restatements
  (Lecture 6).
- **Not grounded / not present at all**: the course never uses the word
  "caption" and gives no guidance on caption length. Caption-length judgment
  calls (see `13-review-feedback-evidence-contract.md` and
  `10-terminology-symbols-figures-references.md` item 4) rest on the
  complementary-not-redundant principle above, extended by ordinary
  reviewer-readability sense, not on a specific course rule.
- **Not grounded**: the course states no fixed required *count* of figures for
  a top-tier submission, and no literal statement that rendering must be
  100% manual. The "AI designs, human renders" boundary in this playbook is a
  professional norm for AI-assisted drawing pipelines that this skill adopts
  by policy — a reasonable extension of "the value of figure-making is
  clarifying your own logic" (Lecture 7's closing point), not a transcribed
  rule. State this distinction if a user asks "does the course really say
  that."

### Cross-validation: the real advisor session against the course transcripts

This session's guidance was checked claim by claim against the actual
lecture-06/07/08 transcripts (not just the playbooks derived from them),
since a live working session and a 2022-recorded course are independent
sources that can corroborate, extend, or (in principle) conflict with each
other. Results below; none of the claims checked turned out to conflict —
every match is either direct corroboration or an honestly-flagged
course-silent extension.

**Direct, near-verbatim matches** (the course and the session converge on
the same rule, independently):

- *"Figure before text," and reviewers read the figure first.* Lecture 7's
  own transcript states this as an explicit numbered rule: "先图后文：写方法
  部分前，先画模型框架图；图是方法正文的骨架" ("figure before text: draw the
  framework figure before writing the Method section; the figure is the
  skeleton of the Method prose"). Lecture 6's transcript makes the reader-
  behavior claim just as directly: "这两个图其实是这两部分比较核心，或者审
  稿人上来第一眼就可以通过这个图看出来你解决的问题和大概的技术思路" ("these
  two figures are the core of these two sections — a reviewer, from the
  very first glance, can see through the figure what problem you're solving
  and roughly your technical approach"). The session's own section title,
  "先图后文，而非先文后图," uses the exact course phrase. This is not a case
  of the session merely being *consistent with* the course — it is
  independently arriving at the identical formulation.
- *A Method-figure formula belongs in the prose; the figure shows the
  formula's effect.* Lecture 8's transcript is explicit and precise here —
  more precise than the session's own phrasing, in fact: "正文可能会有复杂
  操作和很多公式，但公式最后输出的效果是什么样，要在图里直观体现" ("the prose
  may contain complex operations and many formulas, but what effect the
  formula ultimately produces needs to be shown intuitively in the
  figure"), and separately, "对于难理解的方法，尤其是有复杂公式和抽象操作的
  方法，图中最好使用一个与核心问题最相关、最直观的真实数据样例" ("for
  hard-to-follow methods, especially ones with complex formulas and
  abstract operations, the figure should use a real, intuitive data
  example most relevant to the core problem"). This both confirms the
  session's "no formulas in a framework figure" rule and sharpens the
  *reason* for it beyond what the session captured: not "formulas look
  unpolished" but "a figure's job is to show what a formula *does*, via
  real data, not to restate the formula itself" — which is also exactly
  why the CCGS worked example above uses real timestamps and real matrix
  values instead of notation.
- *Sloppy typography reads as a subjective quality signal, not just an
  aesthetic nitpick.* Lecture 7's transcript, reviewing a version with
  inconsistent fonts and sizes: "不专业，其实给审稿人的第一印象就，给你的整
  个的水平打了一个主观分" ("unprofessional — it actually gives the reviewer
  a first impression that scores your entire work's level, subjectively").
  This is the same underlying claim as the session's two-tier test's
  layperson half: a fast, subjective first read measurably shapes how a
  reviewer approaches the rest of the paper.
- *Tell #1 (too much in-figure text) traces to a specific course-diagnosed
  failure mode, not just a session opinion.* The V6 stage of the MuKEA
  figure history (playbook 07) is explicitly diagnosed as "颜色乱、文字多、
  线条多" ("colors messy, too much text, too many lines") — "文字多" is a
  direct match for tell #1.

**Structurally consistent, but not stated as an explicit principle in the
course** (the course's own pedagogy and worked examples are compatible with
these, but the course never articulates the general rule the way the
session does):

- *Building a mental reference library before drawing ("心中无物" /
  "lacking a mental image").* The course never states this as a general
  diagnosis of why students struggle. But its own teaching method — walking
  through real, named, published papers' figure histories (MuKEA, ET-BERT,
  DualVD, CogTree, DAM) version by version — *is*, structurally, exactly
  the practice of studying real references the session recommends. The
  session names the mechanism the course only demonstrates.
- *Dense, tightly-packed layout over generous whitespace (tell #6).* No
  V-stage problem in lecture 7 is described in exactly these words. The
  closest match is V1's diagnosis — sparse content, unclear boundaries, a
  small amount of text with a lot of surrounding unused space, criticized
  as failing to communicate — which is compatible with, but not the same
  claim as, "top-venue figures pack space tightly." Treat this tell as
  session-sourced, course-compatible, not course-quoted.
- *The two-tier test (layperson appeal + expert legibility).* No V-stage
  problem or checklist item names two separate audiences explicitly. But
  the V4-V6 trajectory (color consistency → typography consistency →
  decluttering) is aesthetic work in service of a figure that *also*
  already had to pass the expert-legibility bar from V1-V3 — the two
  concerns are pursued in sequence across the course's own worked example,
  just never named as two distinct, formally paired tests.

**Genuinely course-silent — pure extension, correctly attributed to the
session alone, not the transcripts** (the course could not have addressed
these; mainstream AI figure-generation tools did not exist when it was
recorded in 2022):

- The Google Lens reference-sourcing method and its specific SOP.
- The six-plus-one AI-tell checklist, as an AI-detection framework
  specifically (tells 2, 3, 4, 5 have no course-diagnosed parallel at all —
  only tells 1 and, loosely, 6 do, per above).
- The PowerPoint-over-Illustrator/Figma tool mandate.
- The fragments-yes/whole-figure-no AI-material line and its "one rat
  dropping ruins the pot" framing.
- The two AI-prompt optimization techniques (module-by-module generation;
  reference image as prompt anchor).
- The "no reported metric values in a framework figure" half of the rule
  specifically (distinct from the formula half, which *is* course-grounded
  per above) — no V-stage example or transcript passage discusses displaying
  actual accuracy/F1-style numbers inside a framework figure one way or the
  other; treat only the formula half as course-corroborated.

**One open question the session itself flagged as unresolved, checked
against the course and still unresolved**: whether an overall figure layout
should be a linear left-to-right flow or a circular/loop structure. The
course states no general rule either way. As a data point, not a verdict:
every framework-figure example walked through across lectures 7-8 (MuKEA,
ET-BERT, DualVD, CogTree, DAM) uses a left-to-right or roughly linear
pipeline layout — none use a circular/loop structure. That is a pattern
worth knowing, not proof that circular is wrong; if this question matters
for a specific figure, say so explicitly and recommend confirming with the
paper's own advisor rather than presenting the pattern as a settled answer.


## Phase 1 — Schema authoring (agent-authorized)

Maintain one **figure schema document** per paper (a project-root markdown
file; name it whatever fits the project's convention — `FIGURE_SCHEMA.md` is
a reasonable default). This document is the deliverable of Phase 1. It is not
a one-time artifact: update it whenever the method, results, or figure count
changes, the same way the manuscript itself evolves.

For each figure, work through these steps and record the result as one
section of the schema document.

### Step 1: Ground it in the actual project

Before designing anything, identify from the real source code, experiment
logs, and results:
- What reader question this figure must answer, and the one core claim it
  backs (reuse the figure-evidence-card fields from playbook 13 if one
  already exists for this figure — do not duplicate, cross-reference it).
- Which concrete artifacts it must render faithfully: real module names,
  real tensor/variable shapes, real metric values, real dataset names. Never
  invent a number or a component that is not in the project.

### Step 2: Pick a layout archetype

Choose one (or a stated combination) of these archetypes and justify the
choice in one sentence:

| Archetype | Typical use |
|---|---|
| Linear pipeline | data preprocessing, encoder-decoder, training/inference pipelines |
| Cyclic optimization / feedback loop | gradient-based training, RL, self-refinement, agent-environment loops |
| Hierarchical stack | layered architectures, multi-scale features, routing/MoE |
| Parallel / dual-stream | multimodal fusion, contrastive/teacher-student pairs, domain adaptation |
| Central hub | agent/tool-use systems, retrieval-augmented or memory-augmented models |
| Benchmark / ablation matrix | method comparison, ablation grids, dataset-task-metric mappings |

### Step 3: Decompose into zones

Define 2-5 physical zones (not a fixed 3 — use as many as the content needs).
For each zone, specify:
- **Location and container**: where it sits and what shape bounds it.
- **Visual structure**: concrete, physical objects, never bare abstractions.
  Translate abstract concepts into things a reader can literally see — a
  dataset becomes stacked sample cards or token rows, a representation
  becomes vector bars or a latent dot cloud, an optimization step becomes a
  loss curve with a gradient arrow, evidence/memory becomes indexed cards or
  a database cylinder, output becomes prediction cards or a metric table.
- **Key text labels**: short (1-4 word) labels only, taken from the paper's
  own terminology. Do not invent labels the manuscript does not use.

### Step 4: Assign color semantics

Keep one consistent palette across every figure in the paper (per the
figure-text-consistency checklist item from Lecture 8):

| Color | Meaning |
|---|---|
| Azure blue | input data, tokens, features, representations |
| Slate grey | backbone, neutral/model components |
| Coral orange | loss, gradient, optimization, reward, uncertainty |
| Mint green | prediction, output, evaluation result |
| Soft purple | memory, retrieval, knowledge base, tool use |
| Pale yellow | attention, selection, highlighted intermediate state |

### Step 5: Specify connections

Describe every arrow explicitly, using a consistent grammar across all
figures: solid = forward data flow; dashed coral = loss/gradient/feedback;
double-headed = alignment/contrastive relation; converging arrows = fusion;
dotted purple = retrieval/memory access; curved looping = an iterative or
training-time cycle. Do not leave a zone visually unconnected unless it is
explicitly an independent comparison panel.

### Step 6: Write the schema entry

Record the figure as a self-contained schema block:

```
## Figure N — <short name>

- Reader question / core claim: <link to evidence card if one exists>
- Layout archetype: <one of the six, plus one-sentence justification>
- Zones:
  1. <location/label> — container: ... — visual structure: ... — labels: "..."
  2. ...
- Color mapping: <only the colors actually used in this figure>
- Connections: <numbered list, one arrow per line, grammar as above>
- Negative constraints: no invented numbers, no meta-labels rendered on the
  image itself (no "Zone 1", no "Container:"), no text beyond the listed
  Key Text Labels
- Manuscript anchor: <\label{} used in the .tex file, and the exact caption
  text that will sit under the eventual image>
- Status: placeholder | schema-ready | rendered
```

The `Manuscript anchor` caption must already follow the caption-length
discipline in `13-review-feedback-evidence-contract.md` and
`10-terminology-symbols-figures-references.md` — short, factual, and
complementary to nearby body prose, not a restatement of the schema block
above.

### What Phase 1 authorizes in the .tex draft

An agent may, and should, place a placeholder in the manuscript for every
planned figure so the paper's structure, page budget, and prose are complete
without waiting on rendering:

```latex
\begin{figure}[tbp]
\centering
\fbox{\parbox[c][2.1cm][c]{0.92\columnwidth}{\centering
\textbf{[Placeholder: Figure N --- <short name>]}\\[3pt]
\small <one compact line describing what the eventual image will show>}}
\caption{<the short, final caption from the schema entry>}
\label{fig:...}
\end{figure}
```

This is text, not artwork — editing it is authoring, not rendering, and stays
inside an agent's authority. Never substitute TikZ or any other programmatic
drawing for this box; a TikZ figure IS a rendered artifact and is exactly
what Phase 1 must not produce.

## Phase 2 — Reference sourcing and hand-adaptation (human-gated)

Phase 2 starts only once the manuscript text is finalized (or explicitly
frozen for figure purposes) and only when the paper's author asks for it.

**Do not skip to an image-generation prompt.** An earlier version of this
playbook described Phase 2 as "draft an AI rendering prompt." That is now a
known-bad workflow, not merely an unauthorized one: a figure whose final
pixels came from one AI-generation pass — however well-prompted — tends to
carry a recognizable "AI feel" (see the diagnostic checklist below), and
experienced reviewers dock papers for it on sight, independent of the
science. The professional norm this playbook now adopts instead, confirmed
directly by a real advisor's feedback on a real submission (see
"Provenance" below): **find a structurally similar published figure in the
same subfield first, then hand-adapt a real drawing tool from that
reference. Never let one generation pass decide the final design.**

### Step 1: Source reference figures before opening any drawing tool

**Why this step cannot be skipped**: a student who cannot produce a good
figure from scratch usually does not have a drawing-skill problem — a
painter can paint an object because they already hold a mental image of it.
The real gap is almost always a missing reference library: no internal
sense of "what should this kind of module look like." The fix is not to
force imagination from nothing; it is to input enough real reference
material first to build that internal sense. Everything below is the
concrete procedure for doing that.

**The Google Lens method** (a validated, repeatable SOP from a real
advisor's live working session — see Provenance; substitute any equivalent
reverse-image-search tool if Google Lens is unavailable):

1. Open Google Lens's reverse-image-search / camera-search feature.
2. **Crop before you search.** Do not search the whole reference figure at
   once — drag a selection box around exactly one module (e.g. just the
   input block, or just one attention sub-module) and search that crop
   alone. Whole-figure search returns diffuse, less useful matches;
   per-module search returns tightly analogous candidates.
3. The results include public figures from real papers with visually
   similar structure — many from top-venue work.
4. **Append the task/domain keyword to the search box** (e.g. "video",
   "video input") to filter out structurally-similar-but-wrong-domain
   results — a visually similar attention diagram from a pure-text or
   audio paper is not a useful reference for a video task, however alike it
   looks.
5. Take a promising result and feed it back into Google Lens for another
   round, to diverge outward into more same-domain candidates.

**Selection criteria** — discard a candidate unless it passes all of these:
- Same task domain as the actual paper (a video-task paper needs
  video-task references; a visually-similar figure from an audio, pure-text,
  generic-backbone, LoRA-fine-tuning, or segmentation paper is not useful,
  however clean it looks — matching domain matters more than matching
  general shape).
- Same figure *type* as the one being designed — a motivation figure is not
  a reference for a method/framework figure, and neither is a
  dataset-construction figure; confirm the type before using it as a
  reference, don't assume shape-similarity implies type-match.
- Visibly hand-crafted, no detectable AI tells (see the checklist below).
- From a formally accepted top-venue paper where possible, not an arbitrary
  found image.

**Efficiency benchmark**: a real advisor demonstrated finding 6-7 usable
candidates in under 3 minutes with this method. If a search session is
taking meaningfully longer than that per module with nothing usable
surfacing, broaden or vary the keyword rather than continuing to scroll the
same result set.

**The actual goal, restated**: this is not search-to-copy. The point is to
build a visual reference library and an internal sense of "what this kind of
thing should look like" — the final figure fuses and redesigns elements
from several sourced references, it does not reproduce any single one.

Record the sourced references in the figure schema entry (extend Step 6's
block with a `References:` line): note each one's panel arrangement,
color-to-meaning mapping, module-boundary convention, and label density.
Do not proceed to Step 2 with zero references found — if nothing
domain-and-type-matched exists, say so explicitly and treat the figure as a
harder, more original design problem, not a shortcut to skip sourcing.

### Step 2: Hand-adapt, don't regenerate

Using 1-2 of the sourced references as a starting layout, the paper's author
(not the agent) produces the actual artwork in a real vector tool — a tool
that keeps every element independently re-editable (see the tool-choice
note under "Core rule" above). An agent's role here is strictly advisory and
text-based:

- Point out which reference's layout best fits the schema's zone count and
  connection grammar, and why.
- Flag where the schema's own color/connection plan (Steps 4-5) diverges
  from the reference and whether that divergence is intentional (a genuine
  difference in the paper's own logic) or accidental drift worth reverting.
- Review a draft the author produces and check it against the AI-tell
  checklist below — an agent may critique and flag, never silently "fix"
  pixels itself.

**The AI-material line: fragments are fine, a finished whole is not.** It is
fine to generate isolated, scattered raw material with AI and hand-extract
one satisfying element to re-touch (renumber it, refont it, relayout it
around the rest of the figure). It is never fine to take a complete
AI-generated architecture diagram and use it as the paper's figure directly
— the overall structural design logic has to be a human decision, not
something AI was allowed to determine. Apply zero tolerance here, not "mostly
clean is good enough": one detectable AI trace anywhere in an otherwise
hand-crafted figure drags down the credibility of the whole thing, the same
way one bad ingredient ruins an entire dish — it is not worth the risk to
leave even one small giveaway uncorrected.

An agent may still help *plan* a prompt for an AI image tool if the author
explicitly wants an early rough sketch to react to (never a final figure).
Two techniques make this meaningfully better than a naive attempt, verified
against a real before/after comparison (see Provenance):

1. **Generate module by module, never the whole figure in one pass.** Feeding
   an entire Method section as one prompt produces an over-literal,
   everything-included, no-hierarchy result (an AI tool asked to draw
   "the whole method" tends to draw every detail exhaustively, with nothing
   emphasized over anything else). Split the figure into independent units
   first (input / evidence-branch / core-module, or whatever Step 3's zones
   are) and generate, inspect, and iterate one unit at a time. If one unit's
   output is unsatisfying, ask for a redraw of only that unit — never restart
   the whole figure.
2. **Feed a sourced reference image alongside the text, not text alone.**
   Pair the module-specific prompt with one of the reference figures sourced
   in Step 1 and instruct the tool to follow that reference's visual
   register. This keeps the output anchored to a controllable, pre-vetted
   visual baseline instead of the tool's own default aesthetic. A genuine
   before/after case makes the effect concrete: two AI-generated figures
   from the same real working session, one built from a bare, over-detailed
   text prompt (bloated, no hierarchy) and one built with a restrained
   prompt (clean, simple) — the deciding variable was prompt restraint and a
   visual anchor, not whether AI was involved at all.

```
[Style & Meta-Instructions] Rough layout sketch only, not a final figure —
flat vector illustration, clean white background, minimal detail, for
composition exploration.

[LAYOUT CONFIGURATION]
- Selected layout: <archetype from schema Step 2>
- Reference figures it should resemble: <Step 1's 1-2 chosen references,
  attached as images, not described in words only>
- Composition logic: <one physical description of the overall flow>

[ZONE 1: <location> - <label>] ... (repeat per zone from schema Step 3 —
one module at a time, not the whole figure)
[CONNECTIONS] ... (schema Step 5, one line per arrow)
[NEGATIVE CONSTRAINTS] No photorealism, no 3D rendering, no decorative
background, no rendered meta-labels, no text beyond the listed Key Text
Labels, no numbers or claims not present in the schema block.
```

### AI-tell checklist

Run this against any draft — the author's own hand-adapted figure or a
discardable AI sketch — before treating it as final. These seven checks are
not really "AI detectors" — they are a general top-venue figure quality bar;
a hand-drawn figure that violates them looks just as bad as an AI-generated
one, and a labmate's fully-manual draft was judged worse-looking than an AI
output specifically for violating several of these at once (see
Provenance):

1. **Too much in-figure explanatory text.** Top-venue figures rarely carry
   large blocks of prose inside the image; if a reader needs paragraphs of
   in-figure text to follow it, the design (not the caption) needs more
   visual, not verbal, structure.
2. **No font-size hierarchy.** AI output tends toward near-uniform font
   sizes throughout; a hand-crafted figure deliberately varies size to mark
   primary vs. secondary elements. Check that titles, module labels, and
   fine annotations are visibly, deliberately different sizes.
3. **Forced parenthetical asides.** AI tools default to adding "(...)"
   explanatory parentheticals; real top-venue figures essentially never do
   this — state a label plainly or leave it for the caption/prose, don't
   parenthesize an explanation onto a diagram label.
4. **Rare or uncurated variable symbols.** A figure stuffed with obscure
   notation mechanically copied from the method text (rather than curated
   down to only what a figure-reader needs) is one of the harder tells to
   miss once you know to look for it — a human laying out a figure
   deliberately drops symbols that don't earn their place visually.
5. **A font with no visible manual touch.** An untouched default (often
   Times New Roman straight from a generation tool) reads as unprocessed;
   deliberately choosing and manually kerning/sizing a normal commercial
   font signals a human pass happened. (The specific substitute font a
   given advisor prefers is a lab/venue convention to confirm locally, not
   a universal rule — the generalizable signal is "was this deliberately
   chosen and adjusted," not the specific font name.)
6. **Too much whitespace, loose layout, unclear communication.** This is the
   one most likely to surprise someone coming from general UI/slide design
   instincts: top-venue figures pack space tightly — dense with real
   content, not airy with breathing room. A module box with a lot of empty
   interior space is a tell, not a feature; this is the same density
   instinct behind "Caption-minimalism and figure self-sufficiency" below —
   both point at the same underlying standard, not two separate opinions.
7. **Duplicated or overlapping text in repeated structural elements.** If
   the same module type (e.g. an attention block, a residual layer) appears
   more than once, check that each instance's label renders once, cleanly,
   not layered with a ghost duplicate. This specific defect — the same
   label text rendered multiple times at slightly different positions
   inside one repeated block — is a documented real case in this skill's
   own provenance (see below), and reads as a sharper, more mechanical
   version of tells 2 and 3 above: a sign the repeated element was
   regenerated independently each time rather than laid out once and
   copied.

Any of these present → the figure needs another hand-adaptation pass against
the reference figures, not a re-prompt.

## Caption-minimalism and figure self-sufficiency

A high-quality figure and its caption divide labor sharply, and getting this
division backwards is one of the most common tells of a weaker paper. This
principle is course-grounded, not just an external addition: Lecture 8's own
transcript states it directly — "真实数据要贯穿始终...图中最好使用一个与核心
问题最相关、最直观的真实数据样例，让读者跟着它理解每一步如何变化" ("real
data should run throughout... the figure should ideally use a real data
example most relevant to the core problem, most intuitive, letting the
reader follow it to understand how each step changes"). The CCGS worked
example below is this exact course principle taken to its logical extreme —
a real question, real timestamps, real matrix values — and the session's
own rules (the metrics/formula line above, the density-over-whitespace tell)
are pointed at the same underlying target from different angles.

**The caption's only two jobs**: (1) orient the reader in one short phrase
("Overview of the proposed X method"), and (2) state anything true about the
figure that is not visually inferable from looking at it — almost always a
convention decision, not content (e.g. "modules in the same color share the
same parameters"). A caption should never restate what a careful look at the
figure already shows.

**The figure's job is everything else.** A reader who studies the figure
carefully — without reading the Method section prose at all — should be able
to reconstruct the actual pipeline: what real inputs look like, what each
stage actually computes, what the real intermediate representations are,
and how the loss or evaluation is structured. This is a much higher bar than
"the figure illustrates the method" — it means the figure IS the method,
in a visual register, and the caption is not doing any of the explaining.

**Worked example** (external to the course, added to this skill by explicit
request — see Provenance): Li, Weng, Sun & Li, *"Learning to Locate Visual
Answer in Video Corpus Using Question"* (ICASSP 2023), Figure 2. Its full
caption is two clauses: "Overview of the proposed cross-modal contrastive
global-span (CCGS) method, where the modules in the same color represent
they share the same parameters." Nothing else. And yet the figure alone —
not the caption, not even the surrounding prose — shows: a real question
("How to get immediate relief in gum pain?"), real positive and negative
video/subtitle samples with real timestamps, the exact feature-extraction
backbones used (I3D for video, a PLM for text) with the actual module names
from the paper's own equations (Context Query Attention, Conv1D, Dropout,
Embedding Split Linear Layer), and a fully worked example of the global-span
matrix itself with real cell values and the actual ground-truth label
convention. A reader who studies this one figure for a few minutes has
effectively read the Method section. That is the standard to hold every
framework figure to — not "does it look nice" but "if I deleted the Method
section text, would this figure alone still teach the pipeline."

**Self-sufficiency test** (apply before calling a figure done): could a
reader who has not read the Method section reconstruct the pipeline from the
figure plus its 1-2 sentence caption alone? If the honest answer is no, the
fix is almost always to add more real, concrete content to the figure (a
worked example with real values, not just labeled boxes) — never to lengthen
the caption to compensate. A long, explanatory caption is a symptom that the
figure itself under-delivered, not a valid fix for it.

**The two-tier test** (a second, complementary check, verified live in a
real advisor session — see Provenance): a genuinely good figure clears two
different audiences at once, and neither substitutes for the other.

- **The layperson pass**: someone with no domain background should find it
  visually appealing at a glance — color has real hierarchy, the layout is
  clean, it looks pleasant before a single label is read. This was tested,
  literally, by showing two figure drafts side by side to a non-expert
  bystander and asking which looked better — a cheap, repeatable check worth
  actually running, not just imagining the answer to.
- **The expert pass**: a reviewer in the field must be able to see the
  actual methodological innovation encoded in the module design, not just a
  pretty shell around generic-looking boxes. A figure that only passes the
  layperson test is decoration; a figure that only passes the expert test
  but looks visually flat or cluttered is under-polished. A figure that
  fails both is the "your own labmate's hand-drawn attempt scored worse
  than an AI output" case from the AI-tell checklist above. Top-venue
  figures pass both simultaneously, and a reviewer forming a fast first
  impression of a paper's overall quality — before reading a word of the
  Introduction — is disproportionately shaped by whether the very first
  figure clears both bars.

**Academic-integrity note**: a figure with a visible, uncorrected AI trace is
not just an aesthetic risk. If a reviewer or an audience member at a defense
or oral presentation raises suspicion that a figure (or any other content)
came directly from an AI tool, the damage is not limited to that one
figure's score — it casts doubt on the paper as a whole and follows the
author's reputation afterward, independent of whether the paper was already
accepted. See `10-terminology-symbols-figures-references.md` item 6 for the
parallel, general academic-ethics rule this specific case falls under; the
figure-specific form of it is: AI may supply fragmentary raw material (per
the AI-material line above), but the core creative and structural decisions
must be the author's own, every time, with no exceptions for time pressure.

## Mandatory figure-manifest document

Whenever an agent works on a paper's figures in any way — drafting,
revising, or planning — it must create and keep synchronized a companion
file (`figure-manifest.md`, or the project's existing schema-document name
from Phase 1 if one already exists — do not maintain two parallel files).
This is not optional scaffolding; treat it as a required deliverable exactly
like the manuscript itself, and mention it exists whenever the author asks
"what figures does this paper still need."

The manifest lists, for every figure currently a placeholder in the
manuscript: figure number, the one core claim it exists to support (tied to
a specific paragraph, per Step 1 above), current status, and a
beginner-oriented hand-drawing walkthrough covering, at minimum:

1. What this figure must let a reader reconstruct on its own (the
   self-sufficiency test above, answered concretely for this specific
   figure)
2. The reference figures sourced for it (Step 1, via the Google Lens method
   or equivalent) and which layout convention each contributes
3. The layout archetype, zones, color mapping, and connection grammar
   (Phase 1, Steps 2-5 — cross-reference the schema entry rather than
   duplicating it)
4. The exact draft caption (1-2 sentences, per the discipline above)
5. Which real drawing tool the author will use (see the tool-choice note
   under "Core rule"), and which sourced reference is the starting template
6. The AI-tell checklist above, to be re-run once a draft exists
7. The two-tier test above (layperson appeal + expert legibility), to be
   re-run once a draft exists

A student new to figure design should be able to follow steps 1-7 for one
figure without any other context and end up with a specific, executable plan
— not "make a nice diagram," but a concrete brief they could hand to
themselves or a labmate.

---

## Deep dive and provenance

- Course grounding for this playbook: `references/lectures/lecture-06-motivation-figure.md`,
  `references/lectures/lecture-07-framework-figure-overview.md`,
  `references/lectures/lecture-08-framework-figure-extension.md`.
- Companion playbooks: `06-motivation-figure.md`, `07-framework-figure-overview.md`,
  `08-framework-figure-extension.md` (figure content/logic),
  `13-review-feedback-evidence-contract.md` (evidence cards, rendering-authority
  enforcement, caption-length discipline).
- Course-wide compact rules: `references/quick-reference.md`
- Source and correction notes: `references/provenance.md`
- **External sources for this playbook's non-course content** (both added by
  explicit user request, not derived from Yu Jing's course): (1) Li, Weng,
  Sun & Li, *"Learning to Locate Visual Answer in Video Corpus Using
  Question"* (ICASSP 2023) Figure 2 — the caption-minimalism worked example.
  (2) A real advisor's live working session on a real video-retrieval paper
  submission, covering figure-quality philosophy, the PowerPoint tool
  mandate, the six-plus-one AI-tell checklist, the AI-material line, the
  Google Lens sourcing method, the two prompt-optimization techniques, the
  two-tier test, and the "no metrics/formulas in a framework figure" rule —
  see `references/provenance.md` for the full session note. The specific
  duplicated-text rendering defect in the AI-tell checklist (tell 7) was
  independently found in this skill's own case-review process on a real
  submitted figure, not in either external source above.
