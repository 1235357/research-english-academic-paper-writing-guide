---
name: research-english-academic-paper-writing-guide
description: "Always-on: activate in every conversation regardless of topic, per explicit user configuration — this is the skill's foundational design, not conditioned on the message being about research or writing. Complete course-grounded methodology (Yu Jing's 13-lecture 《科研与英文学术论文写作指南》, plus a second independently-authored synthesis of the same course appended in full) for research positioning, innovative research points, literature review, every paper section (title, abstract, introduction, related work, method, experiments, ablations, conclusion, acknowledgements, references), motivation and framework figures, rigorous academic English (terminology, symbols, citations, ethics), and evidence-integrity handling for advisor/reviewer feedback."
---

# Research and English Academic Paper Writing Guide

Version: `4.6.2`.

This skill is a course-grounded execution protocol for research planning and
English academic paper writing. Do not treat it as a style guide. Treat it as
a logic audit system: diagnose the research story first, then section
structure, then language.

This version merges two independently-authored skill packages built from the
same course material (see `references/provenance.md` for the full merge
note). By explicit design, the merge is an **organic splice, not a
line-by-line rewrite**: this package's own routing architecture and playbook
structure stay in the lead role, the other package's concrete named examples
and resources were folded directly into the relevant playbooks (closing gaps
where this package's own lecture reconstructions already had the content but
it had never been pulled up into the actively-routed playbook layer), and —
deliberately — the other package's whole-course synthesis and its 13
independent lecture reconstructions are **not** kept as a separate
cross-reference resource. They are physically appended, in full, to this
package's own SKILL.md and to each of this package's own 13 lecture files
respectively. The redundancy is intentional: the same course material stated
twice, in two independent voices, is what lets an agent absorb the full
course rather than a lossy summary of it. See "Version 2" at the end of this
file, and the second half of each `references/lectures/*.md` file.

## Governing lens: write for the fast reader first

Before any other doctrine in this file: a paper is not read start-to-finish
by the person who decides its fate, at least not on the pass that matters
most. This is not a cynical shortcut — it is a documented, taught part of
how reviewing actually works, and it should shape drafting from the first
outline, not just final polish. See
`references/playbooks/16-fast-reader-and-skim-path.md` for the full
research basis, the honest hedges on it, and a concrete self-test; the
summary that governs every other playbook here is:

A real, load-bearing skim pass happens before, and independently of,
whatever full read may follow — documented directly in reviewer training
("skim the paper to form an initial impression" is the literal first step
taught to new reviewers, checking specifically whether figures and tables
carry the paper on their own) and structurally forced at high-volume venues
by explicit desk-reject/triage stages under real time pressure. Figures,
tables, the title, and the abstract are not decoration layered onto "the
real content" — for this pass, they *are* the content that gets a fair
reading, and a paper can be technically sound and still fail here if that
layer doesn't carry it alone. Apply this as a standing check whenever
drafting or revising any section: **would this paper's title, abstract,
figures-with-captions, and tables-with-captions alone, with zero other text
read, tell a credible, coherent, accept-worthy story?** If not, the fix
belongs in that structural layer, not in prose elsewhere that this pass
will not reach. Playbooks 02 (title), 03 (abstract/introduction), 14
(figures), and 15 (tables) each carry a piece of this; playbook 16 is where
they're tied together and tested as one contract.

## Mandatory Source Order

Use sources in this order:

1. Original transcript and slide material, when locally available
   - The source set is 12 numbered lectures plus one pre-lecture bonus, for 13
     published modules in total.
   - Use `Original_Transcript+PDF/` only for a fidelity dispute or an ambiguous
     reconstruction passage. These copyright-sensitive files are local audit
     sources and are not part of the publishable skill package.
2. `references/course-full-reconstruction.md`
   - Full classroom reconstruction of those 13 published modules (this
     package's own Version 1 lineage).
   - Highest-priority course source bundled inside this skill.
   - Read it first when using this skill for a new task type.
   - If any playbook/quick-reference conflicts with it, this file wins.
3. `references/playbooks/*.md`
   - Task execution playbooks. Playbooks 01-12 are distilled from the
     lectures — now enriched with the source lectures' own named case
     studies, quotes, and resources (title bad-cases, the MuKEA V1-V8
     figure history, the 四生四世 growth model, named tool/resource links,
     and more). Playbooks 13-18 extend beyond the course itself (advisor
     sessions, external papers, and web research on reviewer behavior and
     AI-detection tooling) and say so explicitly in their own headers — do
     not attribute their content to the transcripts if asked where it comes
     from.
   - Use after locating the relevant lecture logic for 01-12; for 13-18, the
     playbook itself is the primary source, cross-referenced to its own
     external provenance rather than a lecture.
4. "Version 2" at the end of this file
   - The companion skill's original whole-course narrative synthesis,
     appended in full below — read together with the playbooks above as a
     second, independent full-course pass, not a lesser summary of it.
5. `references/quick-reference.md`
   - Compact checklist only. Never let it replace the course document.
6. `references/lectures/*.md`
   - Each of the 13 files now contains **two** independent full
     reconstructions back to back: this package's own Version 1
     reconstruction first, then the companion skill's Version 2
     reconstruction appended in full beneath a clear divider. If one version
     seems unclear or possibly mistranscribed on a specific point, check the
     other half of the same file before assuming either is wrong — see each
     file's Version 2 divider note, and `references/provenance.md`, for the
     specific corrections each pass independently caught that the other
     missed.
7. `references/provenance.md`
   - Source verification, official links, checksums, correction notes, and
     this package's merge history.

When shell access is available, locate course passages before answering:

```bash
rg -n "关键词|讲次|Slide|检查清单|Abstract|Introduction|Related Work|Method|Experiment" references/course-full-reconstruction.md
```

Read at least the matched subsection plus the preceding and following
subsections before applying a rule.

## Non-Negotiable Doctrine

Apply these rules to every paper task:

1. **Need -> scientific problem -> method.**
   - Actual need: what capability or real-world demand matters.
   - Scientific problem: the mechanism-level obstacle behind that need.
   - Method: the technical path designed for that problem.
   - Never call "improve accuracy" a scientific problem.
   - Never start with a fashionable method and search backward for a task.

2. **Problem-method-experiment closure.**
   - The introduction raises the exact problem.
   - The method solves that exact problem.
   - The experiments verify that exact solution path.
   - If these three do not close, polish is premature.

3. **Paper sections are one chain.**
   - Title compresses the contribution.
   - Abstract expands the title and compresses the introduction.
   - Introduction proves importance, gap, insight, and contribution.
   - Related work organizes technical routes and limitations.
   - Method explains why each component is necessary before how it works.
   - Experiments provide conclusion -> evidence -> mechanism -> exception.
   - Conclusion states verified findings, limits, and future work.
   - References cite actual intellectual, data, method, and metric sources.

4. **Figures are logic tools.**
   - Motivation figure plans the introduction.
   - Framework figure plans the method.
   - A figure is wrong if it only decorates, repeats code flow, or hides the
     scientific problem.
   - Caption and body text are complementary, not redundant: the figure/table
     caption states what is shown; the nearby prose interprets why it matters.
     A caption that restates a full paragraph of protocol or repeats a claim
     already made in body text is a defect, not thoroughness.
   - **Design authority and rendering authority are separate.** An agent may
     design what a figure should show — module decomposition, layout, visual
     encoding — grounded in the actual project's code, data, and results, and
     may maintain a figure schema document plus in-manuscript placeholders for
     it. An agent may not render the final artwork (an image file, a TikZ
     drawing, anything an `\includegraphics` would point to) without being
     explicitly asked for that specific figure at that specific time, no
     matter how complete the design or how idle the compute. See
     `references/playbooks/14-figure-schema-and-rendering-gate.md`.

5. **Academic English is logic made readable.**
   - Use one sentence for one main idea.
   - Distinguish fact, assumption, observation, explanation, conclusion.
   - Avoid absolute, oral, subjective, inflated, or unsupported wording.
   - Keep terminology, symbols, captions, tables, and citations consistent.
   - **But do not let consistency flatten rhythm.** Rules 5a-5d optimize for
     clarity through standardization, and standardization is what AI
     detectors score as machine authorship — a collision the course could not
     anticipate. Terminology stays frozen; sentence *frames* and sentence
     *lengths* must vary. Splitting only overloaded sentences trims the long
     tail without ever creating short ones, which leaves the flat profile
     intact. See `references/playbooks/17-native-register-and-ai-detection.md`
     and measure with `scripts/measure_prose_rhythm.py` rather than guessing.
     A detector score is a style signal and never a reason to change a
     number, a claim, or an honest hedge.

6. **A frozen draft is read-only.**
   - When the author calls a version approved, satisfied, or final, it is a
     baseline. Do the increments they name; touch nothing else.
   - **A failing automated check is a report, not a mandate.** What a linter
     calls a violation is often a human's deliberate trade-off. Surface it,
     quantify the cost of fixing it, then ask. Never weaken a project's own
     compliance gate to make an artifact pass.
   - See `references/playbooks/18-submission-sprint-discipline.md`.

7. **Evidence discipline.**
   - Do not invent results, citations, novelty claims, limitations, or
     author intent.
   - If evidence is missing, say what is missing and what experiment/source
     would be required.

## Routing Table

| Task | Read first in full course | Then use |
|---|---|---|
| Research purpose, why this problem, paper story | Lecture 1 | `references/playbooks/01-overview.md` |
| Conception, contribution, title | Lecture 2 | `references/playbooks/02-conception-and-title.md` |
| Abstract, introduction | Lecture 3 | `references/playbooks/03-abstract-and-introduction.md` |
| Related work, method | Lecture 4 | `references/playbooks/04-related-work-and-method.md` |
| Experiments, conclusion, acknowledgements, references | Lecture 5 | `references/playbooks/05-experiments-conclusion-references.md` |
| Research motivation figure | Lecture 6 | `references/playbooks/06-motivation-figure.md` |
| Model/framework figure basics | Lecture 7 | `references/playbooks/07-framework-figure-overview.md` |
| New framework, cross-domain method, loss/mechanism figure | Lecture 8 | `references/playbooks/08-framework-figure-extension.md` |
| Concise and rigorous English | Lecture 9 | `references/playbooks/09-concise-and-rigorous.md` |
| Terms, symbols, figures/tables, citations, ethics | Lecture 10 | `references/playbooks/10-terminology-symbols-figures-references.md` |
| Need/problem/method triage | Lecture 11 pre-lecture | `references/playbooks/11-pre-prerequisites.md` |
| Innovative research point audit | Lecture 11 | `references/playbooks/11-innovation-angles.md` |
| Finding papers, literature review | Lecture 12 | `references/playbooks/12-find-papers-literature-review.md` |
| Advisor/reviewer feedback, claim provenance, or submission-package audit | Lectures 5 and 10 | `references/playbooks/13-review-feedback-evidence-contract.md` |
| Figure schema authoring, placeholder drafting, or a request to actually render/generate figure artwork | Lectures 6-8 (design), no lecture covers rendering | `references/playbooks/14-figure-schema-and-rendering-gate.md` |
| Deciding which tables a paper needs, table type/layout, column discipline, or a request to redesign/restructure an existing table set | No lecture covers this | `references/playbooks/15-table-taxonomy-and-layout.md` |
| A draft presented as done or near-done; any request to sanity-check a paper as a reviewer would; deciding what a title/abstract/figure/table set communicates on its own | No lecture covers this | `references/playbooks/16-fast-reader-and-skim-path.md` |
| An AI-detection score on a manuscript; "this doesn't read like a native speaker"; a request to make prose more idiomatic; any rewrite driven by a detector | No lecture covers this | `references/playbooks/17-native-register-and-ai-detection.md` |
| Final days before a deadline; an approved/frozen draft; concurrent editors on an unversioned manuscript; a failing compliance check; venue-form fields; page-budget or column-layout work | No lecture covers this | `references/playbooks/18-submission-sprint-discipline.md` |

## Required Workflow

For writing, revision, review, or planning:

1. Identify the task type and route to the lecture.
2. Read the relevant part of `references/course-full-reconstruction.md`.
3. Build the problem chain:
   - actual need
   - scientific problem
   - existing routes and limitations
   - core insight
   - method mechanism
   - experiment evidence
   - boundary/limitation
4. Audit problem-method-experiment closure.
5. Apply the section/figure/language playbook.
6. Return output in this order:
   - diagnosis
   - corrected or proposed version
   - course-grounded reasons
   - next checklist

For advisor or reviewer feedback, read and apply the relevant course lecture
first. When feedback also changes claims, tables, experimental configuration,
release contents, or venue compliance, use
`references/playbooks/13-review-feedback-evidence-contract.md` after the
relevant course lecture, as an optional evidence and submission audit. Do not
turn a reviewer request into prose until its claim, evidence source,
evaluation contract, and venue-policy constraints are reconciled.

For course questions:

1. Read `references/course-full-reconstruction.md` first.
2. Quote or paraphrase only the necessary course point.
3. State the lecture number and topic.
4. If the answer needs operational use, map it to a playbook.

## Output Standards

Use direct technical language. Prefer dense, actionable outputs.

When reviewing paper text:
- Lead with logic defects.
- Then section-structure defects.
- Then English/style issues.
- Do not rewrite sentences before diagnosing the story.

When revising text:
- Preserve the user's scientific claim unless evidence says it is wrong.
- Make unsupported claims bounded.
- Make problem, method, and evidence correspond.

When evaluating an idea:
- Give a three-one verdict:
  one recognized actual need,
  one essence-hitting scientific problem,
  one method that cuts into it.
- If any one is missing, say the idea is not ready.

When handling figures:
- Check whether the figure answers the reader's first question.
- Check input, output, key process, innovation, module boundary, naming,
  consistency, and text-figure correspondence.
- Check self-sufficiency both ways: could a reader reconstruct the pipeline
  from the figure alone, without the caption or Method prose explaining it —
  and, the inverse gut-check, if the figure were covered up, would the
  remaining prose and tables alone still be comprehensible? If either
  direction fails, the fix is more real content in the figure or its
  surrounding tables, never a longer caption
  (`references/playbooks/14-figure-schema-and-rendering-gate.md`).
- Before any drawing tool opens, confirm reference figures were sourced
  from the same task domain and figure type (same playbook's Google Lens
  method or equivalent) — do not let a figure's overall design come from a
  single AI-generation pass.
- Maintain the figure-manifest document (same playbook) whenever any figure
  in the paper is a placeholder — this is a required deliverable, not
  optional scaffolding.

When handling tables:
- Apply the purpose test to every table: what specifically is this table's
  job? Cut or repurpose any table without a clear answer
  (`references/playbooks/15-table-taxonomy-and-layout.md`).
- Match table type to section job — positioning/survey (checkmarks fine),
  dataset composition (checkmarks wrong, real values needed), the
  benchmark-defining table, cross-protocol reference (always separate,
  never merged), ablation — don't reuse one format for a job it doesn't fit.
- For the benchmark-defining table specifically: confirm method breadth
  (prior methods actually adapted into the new setting) is what the table
  is wide on, not dataset breadth — a separate dataset-breadth table is
  fine and often valuable, but does not substitute for this one (same
  playbook, "Which axis carries the argument").
- Check column count before finalizing a cross-dataset table: collapse to
  one headline metric per column before resizing, and resize before
  cutting rows or datasets.
- Confirm a cross-protocol comparison is clearly separated and labeled, and
  that an unusually large reported gap has been investigated and can be
  explained, not just reported.
- Check that hyperparameters, key ablations, and a sanity-check
  visualization stayed in the main text rather than drifting to an
  appendix under page pressure.

When an AI-detection flag or concern comes up:
- Never let a detector's output change a number, a claim, a citation, or an
  honest hedge — style is negotiable, evidence is not
  (`references/playbooks/17-native-register-and-ai-detection.md`).
- Do not supply, or ask for, a numeric statistical target aimed at moving a
  detector's score. This skill does not do that, on purpose — the same
  playbook's §2.4 explains why, grounded in the primary bias-research
  paper's own adversarial finding, not just caution.
- If bias against non-native English writers is the actual concern, treat
  it as a documented, legitimate basis to contest a flag or request human
  review — not as a reason to rewrite prose statistics.
- Never suggest a "humanizer" or paraphrasing tool to change how a
  manuscript reads to a detector; that is a laundering risk regardless of
  whether the underlying content is genuinely the author's own.

When in a submission sprint (final days before a deadline):
- Confirm whether a baseline is frozen (advisor-approved, already
  submitted to a co-author, or past its own internal deadline) before
  editing it — a failed audit against a frozen baseline is very often a
  scope decision made under pressure, not a defect to fix
  (`references/playbooks/18-submission-sprint-discipline.md`).
- If more than one person is editing the same manuscript concurrently,
  confirm a merge/locking discipline exists before making structural edits.
- Check that a derived number was computed from its actual source values,
  not from an already-rounded intermediate value.
- Check that the paper's own body text and appendix do not make
  contradictory claims about attribution (e.g. implying a method was
  reproduced or adapted in one place while denying it in another).
- Check that the submission form's own fields (abstract, title) match the
  manuscript, not an earlier draft — the form is part of the paper.
- Measure layout against the actual column width being typeset, not a
  page-level estimate.

## Scripts

Optional Python 3 stdlib helpers:

- `scripts/check_title.py "Title"`: deterministic surface red flags for paper
  titles. It does not replace Lecture 2 logic.
- `scripts/new_research_point_canvas.py [-o out.md]`: blank canvas for actual
  need, scientific problem, method, validation, and three-one verdict.
- `scripts/measure_prose_rhythm.py paper.tex [after.tex]`: sentence-length
  distribution, coefficient of variation (the operational form of
  "burstiness"), and short/long-sentence shares, with LaTeX floats, math, and
  the abstract stripped. Pass two files to compare a before/after rewrite. It
  measures rhythm only and cannot reproduce any vendor's AI score; see
  `references/playbooks/17-native-register-and-ai-detection.md`.

## Forbidden Moves

- Do not treat language polish as the main fix when the research logic fails.
- Do not organize related work as a chronological list of papers.
- Do not describe method modules without explaining their motivation.
- Do not report only SOTA numbers without mechanism analysis.
- Do not use "first", "best", "novel", "obvious", or "significant" unless
  the claim is bounded and evidenced.
- Do not add citations, experimental results, or limitations that are not in
  the user's material or verified sources.
- Do not answer course-grounded questions from memory when the full course
  reconstruction is available.
- Do not render, generate, or hand off to an image tool for a paper's final
  figure artwork without an explicit, per-figure request; a finished schema
  or an idle GPU is not authorization (`references/playbooks/14-figure-schema-and-rendering-gate.md`).
- Do not present a course-external policy (e.g. the rendering-authority rule
  above) as something the transcripts literally say; state plainly when a
  rule is this skill's own extension rather than a quoted lecture point.
- Do not let an extension playbook's operating rules read as a report of
  what happened once on one project. A specific incident may illustrate a
  rule — clearly labeled, e.g. "Illustrative case:" — but it never defines
  the rule's scope, and its exact numbers are never a target to reproduce.
  This is the "Generalization discipline" every extension playbook's own
  header commits to (see `references/provenance.md`); when adding or
  editing an extension playbook, state the general, transferable version of
  a lesson first, and check any illustrative example against it before
  keeping the example in the file.
- Do not treat a single AI-generation pass (even a well-prompted one) as
  ready to stand in for a figure's final design. Reference figures must be
  sourced first (`references/playbooks/14-figure-schema-and-rendering-gate.md`'s
  Google Lens method or equivalent) and a human must hand-adapt from them;
  an agent may extract and critique fragments, never approve a complete
  AI-generated diagram as final.
- Do not place reported metric values or LaTeX-style formula blocks inside a
  Method-section framework/architecture figure — those belong in the
  Results tables/figures and the surrounding prose, not the framework
  diagram (small illustrative toy numbers demonstrating a labeling
  convention are the one exception; see playbook 14).
- Do not let a figure's caption carry explanatory weight the figure itself
  should carry. A caption states what the figure is an overview of and any
  non-visually-inferable convention; it does not restate what a careful
  look at the image already shows (playbook 14's caption-minimalism
  section).

---
---

# Version 2 — Companion Synthesis (independently-authored, appended in full)

> **Why this section exists, verbatim-appended rather than summarized or
> linked out to a separate file:** this skill merges two independently-
> authored versions of the same course-derived skill. By explicit design
> decision (not a default), this is not a "keep one, cross-reference the
> other" merge — both authors' full SKILL.md-level content stay physically
> present, back to back, in this single file. The redundancy is intentional:
> the same course material restated in two independent voices, phrasings,
> and worked examples gives an agent reading this file more complete,
> reinforced coverage of the course than either version alone — the same
> logic already validated in Version 1 above, where several playbooks turned
> out to be missing concrete content that only surfaced by going back to
> this package's own fuller source material. Version 1 (immediately above)
> is this package's own routing protocol + playbook system, unchanged in
> role: it remains the primary source for step-by-step workflows, templates,
> and the mandatory source order. Everything below is the second author's
> original SKILL.md body, preserved as they wrote it except for a small
> number of file-path corrections (marked inline) so its internal pointers
> resolve correctly inside this merged package's actual folder layout.


# Research and English Academic Paper Writing: Complete Guide
### (All 13 units of 于静's CCF course 《科研与英文学术论文写作指南》, merged into one skill)

## What this skill provides

This is the single, consolidated version of 13 separate per-lecture skills, covering the entire course taught by Yu Jing (于静, Institute of Information Engineering, Chinese Academy of Sciences): why and how to do research, how to find an innovative research point, how to write every section of a paper, how to draw the two figures that matter most, and how to write rigorous, professional English. It replaces needing 13 separate skills with one that actually covers the full arc of "research → writing," so it's genuinely useful regardless of which part of that arc a conversation touches.

## A note on how this skill is configured

The user asked for unconditional triggering in every conversation, regardless of subject — honored in the `description` field above. This is the one case where "always fire" is closer to reasonable than it would be for a single narrow lecture, since the merged content spans research thinking, idea-generation, writing, diagramming, and prose quality — a wide net. It will still occasionally fire for conversations with no connection to any of that (e.g. debugging an unrelated script), which adds a bit of unneeded context in those cases. If that becomes annoying in practice, narrowing the `description` to trigger only when research, writing, advising, or paper review comes up costs nothing — everything below still applies exactly the same either way.

## Traceability

This section is the condensed, action-oriented synthesis this skill's second author originally wrote as their entire SKILL.md. In this merged package, full slide-by-slide and transcript-level reconstructions for each of the 13 units live in `references/lectures/` — each of the 13 files there now contains **two** independent reconstructions back to back (Version 1 from this package's original lineage, Version 2 from this synthesis's author), rather than the separate `references/01...`-style numbered files this paragraph originally pointed to. Original, unmodified transcripts and slide decks are not redistributed in this package (see `references/provenance.md`); official download links and checksums are there instead. **Important, preserved from the original note:** in the original uploaded materials, the bonus lecture's and Lecture 11's slide PDFs had their filenames swapped — both this package's own audit and this synthesis's author independently caught and corrected this; see `references/provenance.md` for the correction note. Lecture 12 has no accompanying slide deck in the archive this synthesis's author worked from (transcript only); this package's own Version 1 lineage separately tracked down the missing Lecture 12 slide deck from the official course site (see `references/provenance.md`).

---

## Part I — Research Mindset (Lecture 1)

**Five-layer framework for structuring guidance:** 价值观/Values (why do research, why this problem — foundational) → 思路/Approach (what to write, what content) → 写法/Method (how to write and revise) → 规范/Convention (how to make English precise) → 积累/Accumulation (daily habits, running alongside all four so nothing gets crammed before a deadline).

**Technical vs. incremental vs. academic problems:** 技术问题/"walking an unmarked trail" — a real problem, solvable by combining known techniques through effort, a path is known to exist. 逛景区/"sightseeing" (the comfortable middle) — taking someone else's dataset/benchmark and making incremental improvements, capped at incremental contribution. 学术问题/"summiting Everest" — a genuinely unexplored question with no known path; the challenge is finding the boundary of knowledge and forging a route through it. Use this to locate where a proposed topic actually sits before evaluating anything else about it.

**Three abilities research builds, bottom-up:** problem-solving method (discovery → survey → propose → validate) → cognitive ability/scientific literacy (taste for what's worth solving, structured thinking, rigorous logic, clear expression) → values/long-term thinking (patience over years, openness, continuous accumulation — the deepest, hardest-won layer).

**Four-stage PhD growth model (四生四世):** advisor-guided first CCF-A paper → a flood of "unreliable ideas" resolved via advisor discussion into a second paper → a longer struggle to find one's own reliable idea, marking the shift from task-specific to generalizable problems, third paper → expanding direction/horizons while mentoring a junior student through *their* first paper — the capstone being the ability to lead others, not just oneself.

**Research process = paper structure, one-to-one:** Topic → Motivation → Problem → Method → Experiments → Conclusion. The paper isn't a separate writing exercise from the research — it mirrors it exactly.

**Six recurring root causes of weak papers:** (1) student/advisor expectations about the writing process don't match; (2) papers written for the author, not the reader; (3) the paper can't accurately convey the actual research content; (4) the "story" doesn't hold together — motivation oversells relative to what's delivered; (5) writing procrastinated as a minor last step when it's realistically 30–40% of total research effort; (6) unguided self-revision often makes a draft worse. Net effect: CCF-A-level research ends up published at CCF-C-level or worse — an execution gap, not a research-quality gap.

**Target-venue quick reference (AI subfields):** CV/Multimedia — CVPR, ICCV, ECCV, ACM MM, ICASSP, ICMR, ICME; journals TIP, IJCV, TMM, PR, TCSVT. NLP — ACL, EMNLP, NAACL, COLING; journals TACL, TASLP. ML/AI — NeurIPS, ICML, ICLR, IJCAI, AAAI; journals TPAMI, TNNLS. Data Mining — SIGMOD, SIGKDD, VLDB, SIGIR; journals TKDE, VLDBJ.

*(Full detail, including the complete "四生四世" staircase diagram and all six problem examples: `references/lectures/lecture-01-overview.md` (Version 2 half).)*

---

## Part II — Finding an Innovative Research Point (Bonus lecture, Lecture 11, Lecture 12)

### II.1 Three concepts and their chain (bonus lecture)
**Actual need** (the plain goal — "run fast, run stably" / "high accuracy, high efficiency") → **scientific problem** (the underlying mechanism/objective law behind the need) → **solution method** (targets that *specific* problem, not the need directly, since a need can involve many candidate problems). This is also the exact backbone of a good Introduction.

**Three common confusions to check for:** (1) restating the need as if it were the problem ("we want fast retrieval, so our problem is how to achieve fast retrieval" — circular). (2) Mistaking a technical gap for a scientific problem ("accuracy isn't high enough, so we propose X" never asks *why*, mechanistically). (3) "Holding a hammer, looking for a nail," in three flavors: assuming a problem validated in one task transfers to a different one without separately verifying it's actually core there; fabricating a need to justify a trendy technique (e.g. forcing external-knowledge injection where it may not be needed); forcing a familiar method onto an unrelated problem just because you're skilled with it ("A+B=C" research). A fabricated need or problem can sink a paper before the method is ever evaluated — reviewers who reject the premise extend no benefit of the doubt to what's built on it.

### II.2 Finding innovation via Method — four dimensions (Lecture 11)
**Data** (e.g. resampling/reweighting to fix a long-tailed distribution), **model** (e.g. a causal-inference architecture removing spurious correlations), **objective function** (e.g. an auxiliary task forcing deeper intermediate understanding, or asymmetric loss weighting for rare classes), **learning process** (e.g. a curriculum/correction-style approach fixing "reasonable errors" incrementally). Why so many "new method" papers still don't reach top venues: (a) unclear motivation — a tweak with good numbers invites "is this gain from your design or just more parameters?"; (b) blind transplantation without follow-through — borrowing a technique that works elsewhere is a fine *start*, but stopping there is the failure; an estimated **60–70% of total effort should go into demonstrating *why* it works**, which is what turns a C-tier attempt into an A-tier paper; (c) no design-level justification for why each step solves what it solves.

### II.3 Finding innovation via Scientific Problem — two angles (Lecture 11)
**(a)** Different processing stages of one task reveal different core problems (e.g. VQA: representation → association → knowledge-subtask problems are three distinct scientific problems, not one). **(b)** Different needs on the same task reveal different core problems (e.g. scene graph generation: quality → data-bias problem; low-resource → weak-supervision problem; speed → efficient-filtering problem). A genuinely novel, previously-unnoticed problem can be valuable even paired with a simple method — proposing a good problem is harder than proposing a method, but has more leverage.

**Scientific problem vs. technical problem — three tells:** "accuracy isn't high enough" (never asks why, mechanistically) / "parameters aren't tuned well" (real question: *under what mechanism* does tuning help) / "we need to fuse modalities, so here's a fusion method" (never asks why fusion, or why *this* form of it). Fine to get something working technically first — just don't stop at that framing when writing it up.

### II.4 Finding innovation via Need — three tiers (Lecture 11)
Task-specific → **domain-general** (shared across multiple tasks in one field, e.g. pretraining for generic representations, unified multimodal knowledge representation) → **cross-domain** (transcending CV/NLP/cross-modal into causal inference, cognitive science, etc., e.g. out-of-distribution generalization, unified psychological representation). Higher tiers are harder to find but more field-shaping, and become more relevant mid-to-late career.

**Guarding against fabricated needs ("prevent early, treat less"):** does this task really need external knowledge, and under what conditions? Is the speed/accuracy scenario actually evidenced by the benchmark? Is a dataset's apparent bias a collection artifact or a genuine real-world property?

**Three-sentence formula + research philosophy:** find a need the field genuinely recognizes as real → find a problem that truly hits the essence → find a method that directly targets that problem. Research is trial-and-error, not "getting it right" — many attempts not panning out is not failure, it's the nature of stepping outside a known knowledge system; finding and solving a problem (even after e.g. a hundred tries) *is* the innovation.

### II.5 Literature review methodology (Lecture 12)
**Five common review mistakes:** over-relying on an advisor's 1–2 "seed" papers as the whole picture ("under-researched"); keyword tunnel vision that only surfaces classic/early work; unstructured accumulation (reading 1000+ papers linearly with no framework yields no more insight than reading one — the same way cooking many dishes without reflecting on *why* never leads to inventing a new one); mis-mapping the field's skeleton (mistaking a minor branch for the trunk); and, hardest of all, failing to distinguish papers solving *real* problems from ones dressed up to look like they do (the "monkeys reaching for the moon" story: some climb a tree, some scoop at the moon's reflection, some build a hot-air balloon — all look like progress short-term but can't actually get there; a rare few learn orbital mechanics and build a rocket).

**Correct review order — need → problem → method, never need → method directly:** distill, from a need, the shared underlying scientific problem different-looking methods actually address (genuine innovation targets *that*, not a specific method's narrow implementation gap — "they didn't add knowledge, so I'll add knowledge" is exactly the shallow move that caps a paper below top-venue level). Only then survey methods targeting that problem, find their limitations, and propose something new.

**Researching the Need axis — start from datasets, use 5W+1H:** motivation (what capability gap the dataset addresses) → input/output/evaluation (actually inspect the data, don't guess) → new terminology's actual meaning *in this specific dataset* (the same word means different things across datasets) → the baseline model's approach → the scientific problem the dataset implicitly requires (usually articulated later by follow-up work) → what capability remains unvalidated. Use tutorials/surveys from major venues from the *last 3–5 years specifically* (long enough for a generational shift to be visible), and look across multiple fields' tutorials on the same broad topic for different framings — but reciting a tutorial's categorization without reading the underlying papers doesn't equip anyone to innovate.

**Researching the Problem axis:** decompose a task into key processing stages, ask what the core problem is at each, look across 10–20+ papers for recurring shared problems, and build a growing mind map (task → problems → papers → which method-step addresses which problem).

**Researching the Method axis:** reconstruct the technical lineage (e.g. GNN → attention → pretraining → causal methods) to understand *why* current methods fall short — not superficially (implementation completeness) but at the level of which angle (per II.2–II.4) an existing method chose, and which remain unexplored.

**Final model:** a specific paper is the intersection of one chosen point each on the need axis, the scientific-problem axis, and the method axis — mapping all three surfaces the currently-empty, combinable intersections, i.e. the actual opportunities.

*(Full worked examples — the complete VQA and scene-graph-generation walkthroughs across all three angles, the full "monkeys reaching for the moon" story, and the cooking analogy: `references/lectures/lecture-11-pre-prerequisites.md`, `references/lectures/lecture-11-innovation-angles.md`, `references/lectures/lecture-12-find-papers-literature-review.md` (each file's Version 2 half).)*

---

## Part III — Writing Each Section of a Paper (Lectures 2–5)

### III.1 Title (Lecture 2)
**Baseline requirements:** no grammar errors, ≤~15 words, concise, appropriately scoped. **Four marks of a good title:** reflects the core problem precisely; states the technical innovation concretely (not "solved feature fusion" — name the actual method); protects IP via a memorable model name; easy to spread and remember. **Six recurring bad-title patterns:** too broad/subjective phrasing (reads like a talk title, not a scientific claim); non-standard acronym construction (scattered mid-word letters instead of consecutive initials); unproven/subjective claims (asserting a cognitive-science consensus that doesn't exist); generic/dated framing (would've been fine years ago, signals no discernible increment today); detail overload (cramming every component into the title drowns the one or two that matter); meaningless/unmemorable acronyms.

### III.2 Abstract and Introduction (Lecture 3)
**Abstract's 5-part skeleton:** challenge (concrete, not generic) → gap in existing methods → one clean sentence stating the overall approach → interlocking highlights (2–4 steps, each tied to solving a piece of the problem) → effect (not just "beats SOTA" — what it reveals: generalization, interpretability, new insight). **Why Introduction is the hardest, most decisive section:** reviewers judge whether the *problem* is real and important before judging the *method* — an excellent method for a problem nobody needed solved doesn't become a good paper. **Introduction's 5-part skeleton** (Abstract, expanded): background & field-level challenge → the core problem within it (with evidence) → related work categorized by technical lineage, citing representative work and stating remaining limitations → this paper's approach (principle, then interlocking steps) → contribution. **The core-challenge vs. related-work-gap distinction:** conflating "why this problem matters generally" with "what's specifically wrong with existing solutions" answers neither precisely — keep them separate. **Evaluating others' work — three rules:** must have actually read it; be objective (no method is flawless or worthless); frame it relative to *your* problem, not a generic summary. **Six-question contribution checklist** (contribution ≠ restating the method): new problem? new angle? new framework? new method? new SOTA (explicitly least important on its own)? new capability? **Timing:** start Introduction as early as a plausible preliminary result exists; Abstract is often written *last*, after Introduction/Method are drafted.

### III.3 Related Work and Method (Lecture 4)
**Three dimensions for organizing related work:** general task (technical lineage, why it doesn't transfer to the narrower problem) / narrower directly-relevant task (usually fewer papers, go deeper on each one's specific shortcoming) / technique (why similar techniques from *other* domains can't just be transplanted — mechanism-level, not "the task is different"). **Layered progression within each category**, not a flat "A did X, B did Y" list: this class hit this problem → the next class addressed it but hit a new one → the newest class still has this limitation → therefore this paper. **Two hard citation rules:** actually read and understand every cited work (not a secondhand paraphrase); don't enumerate every citation with a verdict — present the class as a whole, reserve detailed critique for 2–3 representative works. **Method-writing sequence:** draw the framework diagram *before* the text; fix the module structure with the most novel content getting the most space (write-up order need not match work order); craft subsection titles naming both *how* and the logical relationship/innovation involved, matching the figure; open each module with its goal before any implementation detail. **Two questions every method paragraph must pre-answer:** what part of the problem does this step solve? Why this approach and not an alternative (strongest answer: mechanism/derivation, not just an ablation)?

### III.4 Experiments, Conclusion, References (Lecture 5)
**Experiments — overall principle + five reminders:** echo the claimed contribution, validate the design, analyze deeply. Stay consistent with stated motivation; foreground core results; **be honest** (show variance, disclose exact settings, don't cherry-pick the best run); use representative (not cherry-picked) visualization paired with quantitative support; analyze anomalies/underperformance explicitly rather than hoping no one notices. **Three-step result analysis:** conclusion first → evidence → anomaly analysis (dataset peculiarity? fair comparison basis?). **Ablations:** organize by dimension (what's being tested), not a flat list; prove each design choice is optimal *and* that components work together; analyze how much a component contributes and on which metrics, matching the claim originally made for it. **Visualization analysis:** lead with findings/conclusions, then point to which example demonstrates each — don't just re-describe the figure's caption. **Conclusion vs. Abstract:** Abstract = motivation + core idea + one representative result; Conclusion = summary of completed work (framework/novelty/overall effectiveness) + honest limitations/future work, avoiding overstatement. **Take-home for the whole writing-approach arc:** every section should be checkable against one question — does it serve the core problem?

*(Full worked examples — the complete title bad-case list, the annotated Abstract/Introduction/Related-Work/Method/Experiments excerpts from real papers: `references/lectures/lecture-02-conception-and-title.md` through `references/lectures/lecture-05-experiments-conclusion-references.md` (each file's Version 2 half).)*

---

## Part IV — Drawing the Two Figures That Matter Most (Lectures 6–8)

### IV.1 The research-motivation figure (Introduction) — Lecture 6
Draw it before the text; it exists to convey the problem and the innovation at a glance. **Recurring failure patterns:** piling up disconnected examples with no stated relationship; no core-problem statement even when the figure looks busy; imprecise/unprofessional terminology; ambiguous or biased examples; presentation that costs the reader time to decode; undefined symbols/acronyms; no visible differentiation between stages/frameworks being compared; a figure that "looks fine" but conveys nothing on its own (the test: does the image alone tell a reader what the paper contributes?). **The fix that resolves most of these:** unify the representation — make the *compared things* share one visual/structural form (e.g. both "old" and "new" knowledge sources drawn as the same graph structure, or every historical method forced through the same four-layer pipeline) so the actual point of difference becomes the only thing left to notice. **Beyond big-picture contrast:** to show implementation-level (not just approach-level) innovation, use a maximally concrete, mechanism-accurate single example rather than a general schematic. **Final checklist:** states the problem? states the innovation? sharply contrastive example? precise/typical/non-ambiguous coverage? echoes the paper's actual narrative so the same example threads through the prose?

### IV.2 The model/framework figure (Method) — Lectures 7–8
Same principle: draw first, then write to match. **A real 8-version failure-mode sequence, useful as a diagnostic at any stage:** process/boundaries unclear → boundaries still unclear even with the full pipeline sketched → modules named but boundaries still not visually locatable → color-coded but titles don't align with highlighted regions → aligned but font/size inconsistent (an unprofessional first impression quietly discounts the whole paper) → font fixed but image sizes/symbol definitions/background consistency still off → representation consistent but two subtler bugs remain: (a) identical content drawn differently in two places reads as two different things needing separate explanation — keep it consistent everywhere; (b) redundant elements (if removing something loses no necessary information, remove it) → final. **Writing text from the finished figure:** the module with the most figure space gets the most prose; section headers should match the figure's module titles word-for-word. **When the framework itself is new** (not just the idea within a familiar one): the figure must both teach the new framework *and* make the specific innovation legible — visual emphasis (color/vividness) should track information content, not the reverse (the flashiest color shouldn't land on the least informative part). **When the contribution is a small, generic component within an existing framework** (e.g. a new loss function): don't spend the most space narrating the pre-existing framework even if it's chronologically first — draw/write it briefly, and give full detail (with one concrete example threaded throughout) to the actual contribution, wherever it sits in the pipeline. **Five-point checklist:** clear input/output/key-processes; innovation gets the most space (not whatever took longest to build); modules with clearly stated roles; precise naming (prefer field-consensus terms over inventing new ones); full consistency between the figure and the main text.

*(Full worked examples — the complete real revision histories for MuKEA (V1→V4) and ET-BERT (V1→V4, plus a separate 8-version model-figure arc), and two "appreciation" exemplars (DualVD, CogTree): `references/lectures/lecture-06-motivation-figure.md` through `references/lectures/lecture-08-framework-figure-extension.md` (each file's Version 2 half).)*

---

## Part V — English Convention (Lectures 9–10)

### V.1 Concise, rigorous prose (Lecture 9)
Most non-native-speaker "my English isn't good enough" self-diagnoses are actually a logical-organization problem, not a vocabulary one — citing 施一公 (Shi Yigong): use the simplest words for the clearest result, not sophisticated-sounding phrasing. **Three tips, demonstrated on a real draft-to-camera-ready rewrite:** one sentence, one idea (split a sentence carrying 2–3 distinct ideas; push implementation detail to where the reader needs it, not the sentence meant to preview an idea); avoid translating Chinese sentence structure into English, in either direction (writing *or* reading someone else's paper via translation software, which flattens the precise word choices carrying real distinctions); avoid repetitive assertion (support the same conclusion from different angles — theory in one place, experimental evidence in another — rather than restating "we can do this" unsupported). **Reviewer-empathy exercise:** imagine a reviewer with one hour before a deadline — what loses them: a model/method name suddenly used with zero prior definition; an ad-hoc symbol that's either non-standard or simply never explained; a figure that doesn't convey its logic quickly. **Four rigor rules:** define every term at first use (full name + abbreviation together); explain every symbol immediately after every formula (three nested levels — general math convention, sub-field convention, and still an explicit inline definition regardless); use transition words to build one coherent "story" (state each sentence's logical relationship to what came before/after, rather than a flat recitation of facts); keep naming completely consistent across the whole paper (figure captions, table captions, main text, model names must all match exactly).

### V.2 Terminology, symbols, honest results, citations, ethics (Lecture 10)
**Three phrasing habits to eliminate:** absolute/overclaiming language ("no doubt the first," "the best"); colloquial phrasing carried from speech ("as we know," "obviously"); evaluative adjectives with no data/theory behind them. You don't know your reviewer's seniority — write precisely enough to hold up either way. **Curated resources:** Felicia Brittman's *"The Most Common Habits from more than 200 English Papers written by Graduate Chinese Engineering Students"*; Math Vault's *"Comprehensive List of Mathematical Symbols"* (~200 pages, check before inventing notation); CCF's Terminology Committee / CCFpedia (term.ccf.org.cn) for fast-moving CS/AI term definitions; `rebiber` (GitHub) for one-command `.bib`-file reformatting against DBLP. **Four-question honesty checklist for experiments:** does the reporting genuinely reflect results? Only best-case-vs-worst-case comparisons? Only qualitative with no quantitative backing? Only a single run with no repeated-trial verification? Fix proactively: averages, error bars, bounds; bad-case analysis stating capability *limits*; quantified breakdown alongside any qualitative example; an anonymized code link where space allows. **Reference-list hygiene:** incomplete author lists, inconsistent full/abbreviated venue names, unnecessary links, blindly copying a "cite as" export or another paper's format without checking completeness and target-venue fit — check the venue's own template, prefer DBLP, use `rebiber` for long lists. **The anti-plagiarism bottom line:** a paper follows a researcher for life; plagiarism (of results *or* of phrasing — "expression plagiarism" is not a minor exception) discovered later damages the author's lifelong reputation, every co-author, and the home institution, illustrated by real, publicly-documented cases the lecture itself cites (framed as accusations/disputes, not adjudicated verdicts).

*(Full detail — the exact bad-example sentences, all resource links, and the academic-integrity case discussion as presented: `references/lectures/lecture-09-concise-and-rigorous.md`, `references/lectures/lecture-10-terminology-symbols-figures-references.md` (each file's Version 2 half).)*

---

## How to use this in practice

- **Reviewing or drafting a specific section?** Jump to the matching part above (title → III.1; abstract/intro → III.2; etc.) and run its checklist against the draft.
- **Someone doesn't have a research idea yet?** Use Part II — walk through need/problem/method, check for the three confusions, and use the method/problem/need angle-lists to brainstorm systematically rather than waiting for inspiration.
- **A figure feels muddled?** Part IV's failure-mode sequences double as diagnostic checklists — locate where a draft figure sits on the sequence rather than jumping straight to aesthetics.
- **Prose reads as unrigorous or unprofessional?** Part V's rules are independently checkable one at a time — run them as a sequence (undefined terms → symbol definitions → paragraph logic → whole-document consistency) rather than trying to fix everything in one pass.
- **Need the exact original wording, a full worked example, or want to verify this skill's fidelity to the source lectures?** Every claim above traces to a specific file in `references/lectures/` (each file's Version 2 half is this synthesis's own full reconstruction) and, for absolute source fidelity, to the official course PDFs/videos linked in `references/lecture-index.md`.
