# Changelog

## 4.6.2 - 2026-08-04

A second, more targeted correction pass over playbook 17, specifically:
re-reading Liang et al. 2023 (this playbook's own central citation) in
full, rather than trusting that the 4.6.1 audit had already fully mined it.
It hadn't — the 4.6.1 audit was thorough on mechanical correctness, dated
evidence, and this skill's generalization standard, and said explicitly
that none of it changed playbook 17's thesis. This pass found something
that does. See `references/provenance.md` → "Second-pass correction: the
mechanism itself" for the full reasoning; summary:

- Liang et al.'s own Discussion section reports an adversarial robustness
  check: applying the paper's own recommended bias-mitigation technique
  (raise linguistic diversity) to genuinely AI-generated text dropped
  detection from 100% to 13%. The paper's own conclusion is that detectors
  should not be used as a primary defense, because the lever protecting a
  genuine non-native writer from a false positive is mechanically identical
  to the lever that helps real AI-generated text evade detection.
- On that basis, `references/playbooks/17-native-register-and-ai-detection.md`'s
  R2 was rewritten from a numeric target table (CV 0.50-0.75, short-sentence
  share 20-30%, etc.) into a pure monotony diagnostic with no target band;
  R1 now states and explains this boundary directly; §2.4 leads with the
  adversarial-robustness finding rather than burying it.
- `scripts/measure_prose_rhythm.py` was rewritten to match: removed the
  `TARGET_CV`/`TARGET_SHORT_PCT`/`TARGET_LONG_PCT` constants and the
  LOW/HIGH/ok verdict against them, replaced with a monotony-only flag with
  no "correct" band. Also fixed, independently of the mechanism question: a
  LaTeX-stripping edge case where `\section{...}` headings and
  `\begin{document}`/`\end{document}` markers could leave stray heading
  words glued onto adjacent sentences; verified against both a plain-text
  and a LaTeX test case with float/table environments present.
- R3-R7, the "what NOT to do" list, and the honest-limits section are
  unchanged — none of them depend on the removed mechanism, and were sound
  before and after this pass.
- Playbook 18 was re-checked against this skill's own generalization
  standard and found to already meet it (v4.6.1's rewrite of it holds); no
  further change made there this pass.
- Version bumped to `4.6.2` in `SKILL.md`.

## 4.6.1 - 2026-08-04

Third-party correction pass over the 4.6.0 additions, run from the
perspective of an independent reviewer checking two things: whether every
claim reaching outside the course is factually accurate and current, and
whether every extension playbook actually generalizes rather than reporting
one project's incidents. Full findings in `references/provenance.md` under
"AI-detection and submission-sprint extension: third-party audit and
correction (v4.6.1)". Summary:

- **Rewrote playbooks 17 and 18** so every section leads with the
  transferable principle; concrete instances are now bounded, clearly
  labeled "Illustrative case" asides, never the rule's scope. This was
  already a standard the package held playbook 13 to (`references/provenance.md`,
  v4.0.0's "Generalization pass" — now consistently called "Generalization
  discipline" everywhere); it had not been extended to 17/18. Removed or
  generalized: verbatim personal quotes, a specific frozen-snapshot
  filename, and several sprint-specific numbers that were standing in for
  general rules (a rounding-error ratio, a column-collision string, a
  layout-gap measurement).
- **Fixed an internal numeric contradiction**: playbook 17's own table
  (CV 0.421→0.485) disagreed with CHANGELOG 4.6.0 and playbook 09's box
  (CV 0.469→0.521) for the same measured case. Reconciled to the latter,
  which two independent locations already agreed on; playbook 17 now says
  so explicitly and recommends re-measuring the source files to settle it
  with one authoritative run.
- **Fixed a same-file contradiction** in playbook 09: its own established
  ET-BERT example says 44 words; the new collision box said "40-word
  monsters." Corrected to 44.
- **Enriched and dated the AI-detection evidence in playbook 17.** Every
  originally cited source was independently re-verified as accurate. Added:
  GPTZero's own October 2023 public response disputing the Liang et al.
  (2023) finding's continued relevance to its updated model, and a 2025
  peer-reviewed study (Pratama, *PeerJ Computer Science* 11:e2953) that
  tests GPTZero specifically on real scholarly abstracts and finds the bias
  reappears on that harder, more current, more directly relevant test.
  Section 2.4 now tells this as a dated three-point timeline instead of one
  static 2023 statistic.
- **Fixed a script bug** in `scripts/measure_prose_rhythm.py`: the LaTeX
  stripper left `\begin{...}`/`\section{...}`/`\title{...}`/`\author{...}`
  arguments (e.g. the word "document") glued onto adjacent prose after
  removing the control word. Fixed and regression-tested.
- **`scripts/validate_package.py` and the test suite were themselves
  out of date**: both hard-code an expected playbook count, last set to 17
  and never updated when 17/18 brought the true count to 19 — meaning
  4.6.0 shipped failing its own validator. Corrected to 19; extended
  `test_course_fidelity_and_generality.py` with a new
  `require_general_sprint_and_register_playbooks()` check so playbooks
  17/18 are held to the same generalization standard playbook 13 already
  was, closing the gap that let this ship unguarded the first time.
- **Added a skill-wide guardrail**: `SKILL.md`'s Forbidden Moves now states
  the generalization-discipline principle once, for any future extension
  playbook, rather than leaving it to be remembered per-file.

None of this changes playbook 17's central thesis; the corrected evidence
supports it more directly than the original citation did. What changed is
precision, not direction.

## 4.6.0 - 2026-08-03

Adds two playbooks distilled from a CCF-A submission sprint, plus the
measurement script the first of them depends on. Both are flagged in-file as
this skill's own extensions, not transcribed lecture points.

### New: `references/playbooks/17-native-register-and-ai-detection.md`

Written after text produced by faithfully applying Playbook 09 was scored
100% AI-generated by GPTZero.

- Names the collision directly: Playbook 09 optimizes for *clarity through
  standardization* — simplest words, one idea per sentence, frozen
  terminology, explicit transitions — and standardization is precisely what
  detectors score as machine authorship. Playbook 09 is not wrong; it is
  incomplete, because it never says how much rhythmic variance to leave.
- Isolates the mechanical gap: "split overloaded sentences" is
  threshold-triggered, so it trims the long tail and never touches the 10–29
  word band where the mass sits. Trimming the tail does not create short
  sentences.
- Records the measured before/after on the real manuscript: CV 0.469 → 0.521,
  short-sentence share 16.6% → 26.5%, with SD essentially unchanged — the
  rewrite worked entirely by manufacturing short sentences from mid-length
  ones. Surface clichés were not the problem: the flagged draft contained one
  `Additionally` and three em-dashes in total.
- Corrects the folk explanation: GPTZero has not used perplexity/burstiness
  directly since autumn 2023, having moved to a trained classifier. They
  remain useful self-computable proxies, not the mechanism.
- Carries the finding that matters most for this skill's audience: detectors
  are documented to over-flag non-native writers (61.3% false-positive rate on
  TOEFL essays in the Stanford study), because adhering to standard syntax
  *is* a low-perplexity signature. This skill's users are the over-flagged
  population, and this skill's advice moves them further into it.
- Hard rule: a detector score never justifies changing a number, a claim, or
  an honest hedge. Style is negotiable; evidence is not.

### New: `references/playbooks/18-submission-sprint-discipline.md`

The course ends at "the paper is written"; submissions end 48 hours later.

- **Frozen baselines.** An approved version is read-only. A failing automated
  check is a report, not a mandate — what a linter calls a violation is often
  a deliberate human trade-off. Never weaken a project's own compliance gate
  to make an artifact pass.
- **Concurrent editors** on unversioned manuscripts: diff before every session;
  never let two agents write one file; separate genuine improvements from
  bundled reverts.
- **Receipt failure modes that survive a receipt discipline**: superseded
  receipts (two files, ten hours apart, different values), and rounded
  intermediates in derived figures (a published 292× that recomputed to 274×
  from unrounded sources, beside a sibling number computed correctly).
- **Attribution integrity**: main paper implied a baseline was a port of a
  cited system; the supplement said it was not. An integrity charge, invisible
  within either document alone.
- **The venue form is part of the paper**: the live submission form held a
  stale abstract containing terminology the advisor had banned.
- **Layout is measurable**: per-column fill (a page-level reading concealed a
  141.9pt hole), numeric column-collision detection (three values fused into
  `31.5133.3334.11`), table fill ratio, and the content/references page
  boundary.
- **Positioning**: state each limitation once, in its most informative place;
  explain mechanism in the supplement rather than repeating confession in the
  body; never report an architectural identity as a finding.

### New: `scripts/measure_prose_rhythm.py`

Sentence-length distribution, CV, and short/long shares, with LaTeX floats,
math, and the abstract stripped; accepts two files to compare a rewrite.
Prints targets and a diagnosis, and states in its own output that it measures
rhythm only and cannot reproduce any vendor's score.

### Updated

- `SKILL.md`: two routing-table entries; doctrine 5 gains the
  consistency-versus-rhythm boundary; new doctrine 6 "A frozen draft is
  read-only" (subsequent items renumbered); scripts section documents the new
  helper.
- `references/playbooks/09-concise-and-rigorous.md`: opens with the known
  collision and forward-references Playbook 17; Pass 1 step 2 extended to
  require manufacturing short sentences, not only splitting overloaded ones.

## 4.5.0 - 2026-07-23

Sharpens `references/playbooks/15-table-taxonomy-and-layout.md`'s
"benchmark-defining table" entry into its own subsection, "Which axis
carries the argument: methods, not datasets," after the user caught his own
initial misreading in real time and asked for the correction to be captured
in the skill.

- The benchmark-defining table's job is to show prior methods, actually
  adapted into the new setting, falling short — that requires real
  adaptation work (e.g. pairing a prior method with a retrieval front-end)
  as a research step, not a table-formatting step, and the table's argument
  is carried by how many different adapted methods it shows, not how many
  datasets.
- Re-verified the CCGS worked example precisely against the paper's own
  text rather than recalling it: four native baselines (VSLNet, ACRM,
  Span-Base, VPTSL), each also wrapped with BM25 and DPR retrieval, twelve
  adapted rows plus the paper's own method, all on one dataset.
- Named the anti-pattern explicitly: treating "run every method across
  every dataset, maximize compute" as the goal produces a table wide in the
  wrong dimension. Dataset breadth is a real, separate contribution when a
  paper has one — it gets its own table, not fusion into this one.
- Added the same distinction to `SKILL.md`'s "When handling tables"
  checklist and cross-referenced it to playbook 16's skim test.
- No file or count changes; `scripts/validate_package.py` and all four
  `scripts/test_*.py` contract scripts still pass unchanged.

## 4.4.0 - 2026-07-22

Adds `references/playbooks/16-fast-reader-and-skim-path.md` and a new
"Governing lens" section at the top of `SKILL.md`, after the user pushed
back that the v4.1-4.3 figure/table work hadn't gone deep enough on *why*
this matters — requesting actual web research into reviewer reading
behavior rather than another assertion from this skill's own priors, plus a
genuine visual re-check (rendered PDF pages, not just extracted text) of
the real paper draft grounding playbooks 14/15.

- Research findings, properly hedged and sourced: a skim-for-first-
  impression stage checking figures/tables first is the literally-taught
  first step of reviewing (Kathy Gould/Vanderbilt); figures/tables are an
  explicit dimension of official reviewer training (Wiley's own guide); a
  genuine, growing fast-triage stage exists at high-volume AI/ML venues
  (NeurIPS 2020 and IJCAI 2020 summary-reject data; 2025 desk-rejection
  trends at CVPR/ICCV/KDD/AAAI/IJCAI/WSDM); AI-assisted review is now
  measured at ICLR/NeurIPS/ICML specifically (a January 2026 Cornell
  study); total review time remains 4.75-6.4 hours on average per
  independent time-tracking surveys, so this skill does not claim reviewers
  only spend minutes on a full review — only that a real, separate, fast,
  consequential skim stage exists alongside that.
- One candidate source (a "manuscript readiness check" service's blog, with
  templated claims reused verbatim across unrelated journal pages and a
  paid-tool pitch attached) was found, evaluated, and explicitly excluded
  as content-marketing rather than research; its specific numeric claims
  are named and rejected in the playbook, not silently dropped.
- New operational tool: the skim self-test (read only title, abstract,
  figures+captions, tables+captions, and section headers — does this alone
  tell a credible, coherent, accept-worthy story?). A failure is always a
  structural fix (title, abstract/intro, a figure, or a table), never "add
  an explanation in the prose nearby," since the skim does not read that
  prose.
- A real worked example: re-checking the real advisor-session transcript
  and the same paper's actual draft PDF (rendered pages viewed directly,
  not only extracted text) surfaced that, at the time of that session, the
  dataset table was still checkmark-only and a discussed methods-comparison
  table did not exist anywhere in the manuscript — concrete, verifiable
  gaps, not hypothetical ones.
- `scripts/validate_package.py` updated: playbook count 16 → 17; playbook
  16 added to required files. All four `scripts/test_*.py` contract scripts
  pass unchanged.

## 4.3.0 - 2026-07-22

Adds `references/playbooks/15-table-taxonomy-and-layout.md`, a new
playbook covering which tables a paper needs and how to lay each one out —
a gap identified after the figure-focused v4.1.0/v4.2.0 work: only light
ablation-content guidance existed before (in
`05-experiments-conclusion-references.md`), nothing on table type selection
or layout. Source: a full real advisor-session transcript restructuring one
paper's table set, cross-checked against that paper's own two draft
versions. Not course-grounded, stated as such in the playbook itself.

- Table taxonomy by section job: positioning/survey (checkmarks correct
  here), dataset composition (checkmarks wrong, needs real attribute
  values, paired with a distribution chart), main benchmark, cross-protocol
  reference, ablation — matching table type to job, not reusing one format
  everywhere.
- Column discipline: collapse to one headline metric per column before
  resizing a table, resize before cutting rows/datasets.
- Cross-protocol tables must stay separate and clearly labeled from the
  paper's own benchmark table — never silently merged.
- A reframed, integrity-preserving version of one session point: investigate
  an unusually large reported gap before reporting it and be able to explain
  why it's real; this skill does not encode "cap the number for
  credibility," since that would be result manipulation (see
  `references/provenance.md` for the explicit reframing note).
- Appendix-vs-main-text priority order under page pressure (hyperparameters,
  key ablations, and sanity-check visualizations stay in the main text;
  derivations/proofs move to the appendix, not the reverse) and the
  workflow-order point that tables/figures should reach final shape before
  the Method prose is finalized around them, not after.
- Table-figure correspondence: shared category/method labels between a
  results table and its nearby qualitative figure; a second, dedicated
  task-structure figure near Experiments for tasks too structurally complex
  for one Introduction-level motivation figure to carry alone.
- `SKILL.md`: added a routing-table row for playbook 15, a "When handling
  tables" checklist paired with "When handling figures," and an inverse
  self-sufficiency gut-check ("if the figure were covered up, would the
  remaining text/tables still be comprehensible?").
- `scripts/validate_package.py` updated: playbook count 15 → 16; playbook
  15 added to required files. All four `scripts/test_*.py` contract scripts
  pass unchanged.

## 4.2.0 - 2026-07-20

Cross-validates the v4.1.0 advisor-session content against the actual
lecture-06/07/08 transcripts, claim by claim, by explicit user request.
Full results in `references/playbooks/14-figure-schema-and-rendering-gate.md`'s
new "Cross-validation" subsection; summary in `references/provenance.md`.

- Found two near-verbatim course/session matches, both now cited with exact
  transcript quotes: "figure before text" plus the reviewer-reads-the-
  figure-first claim (Lectures 6 and 7); the rule that a formula's *effect*
  belongs in the figure while the formula itself belongs in the prose
  (Lecture 8) — this is the course's own, more precisely-reasoned version of
  the session's "no formulas in a framework figure" rule.
- Split the "no metrics/formulas" rule into its two halves for sourcing
  accuracy: the formula half is now course-cited; the reported-metric-values
  half remains session-only, with no course parallel found, and is labeled
  as such.
- Traced AI-tell #1 (too much in-figure text) to a specific course-diagnosed
  failure mode: the MuKEA V6 stage in playbook 07's own revision table.
- Added a course citation to caption-minimalism / figure self-sufficiency:
  Lecture 8's own "real data should run throughout" principle, which the
  CCGS worked example (external) demonstrates taken to its logical extreme.
- Explicitly flagged what remains genuinely course-silent (correctly
  attributed to the advisor session alone, not the transcripts): the Google
  Lens method, five of the six AI-tells, the PPT tool mandate, the
  AI-material line, the two prompt-optimization techniques, and the
  metric-values half of the figure-content rule — all postdate or fall
  outside the scope of a course recorded in 2022.
- Left one open question open rather than fabricating an answer: linear vs.
  circular figure layout, flagged unresolved in the original session and
  still unaddressed by the course; noted only that every framework-figure
  example the course walks through happens to use a linear layout, as a
  data point, not a verdict.

## 4.1.0 - 2026-07-19

Substantially expands `references/playbooks/14-figure-schema-and-rendering-gate.md`
with figure-methodology content beyond the course itself, by explicit user
request, from two external sources (both flagged inline, not attributed to
Yu Jing's course — see `references/provenance.md` → "Figure-methodology
extension" for the full source note):

- **Caption-minimalism and figure self-sufficiency**: a high-quality
  figure's caption should not explain the figure's content — it should only
  orient the reader and state non-visually-inferable conventions. The
  figure itself should let a reader reconstruct the method without reading
  the caption or the Method prose. Worked example added: Li, Weng, Sun &
  Li, "Learning to Locate Visual Answer in Video Corpus Using Question"
  (ICASSP 2023), Figure 2.
- **Phase 2 rewritten**: replaced an earlier "draft an AI-generation prompt"
  workflow with reference-sourcing and hand-adaptation, since a
  single-pass AI-generated figure reliably carries a detectable "AI feel"
  that costs review scores independent of the science. New content: the
  Google Lens partial-crop reference-sourcing method; a seven-point
  AI-tell checklist (six from a real advisor's session, plus one this
  skill independently found in a real case review — duplicated/overlapping
  text in repeated structural elements); the "fragments-yes/whole-figure-no"
  AI-material line; two prompt-optimization techniques for the cases where
  an AI sketch is still explicitly requested (module-by-module generation;
  a sourced reference image as the prompt anchor, never text alone); the
  two-tier layperson/expert test.
- **New hard rules**: a Method-section framework figure carries no reported
  metric values and no formula blocks (illustrative toy numbers are the one
  exception); tool choice should favor modular re-editability, with
  PowerPoint named as a real advisor's explicit, repeated requirement;
  captions must not carry explanatory weight the figure itself should
  carry. All three added to `SKILL.md`'s Forbidden Moves and the figure
  checklist in "When handling figures."
- **Mandatory figure-manifest document** requirement clarified to 7 steps
  (added the two-tier test) and cross-referenced from `SKILL.md`.
- Version bumped to `4.1.0` in `SKILL.md`'s frontmatter body.

## 4.0.0 - 2026-07-18

Merges an independently-authored companion skill (built by a second person
from the same course transcripts+slides, packaged separately as
`research-and-english-academic-paper-writing-guide`) into this package, by
explicit design as an **organic splice, not a hand-merged rewrite**: where
both skills had a document doing the same job, the companion skill's
version is physically appended, in full, to the end of this package's
corresponding document (same file), rather than kept as a separate
cross-reference file. The redundancy is intentional — two independent full
passes over the same course give an agent more complete, reinforced
coverage than either alone.

- **`SKILL.md`**: appended the companion skill's entire original body
  (its whole-course narrative synthesis, Parts I-V) as a new "Version 2 —
  Companion Synthesis" section after this package's own routing protocol
  and playbook system (which keeps its original role, unchanged, as the
  primary source for workflows and the mandatory source order). Only the
  companion section's internal file-path pointers were corrected to resolve
  inside this package's layout; its content and voice are otherwise
  untouched.
- **Trigger scope — changed**: `SKILL.md`'s `description` now reads
  "Always-on: activate in every conversation regardless of topic" (was:
  "Use when writing, revising, reviewing, or planning research papers...").
  This was the companion skill's own original design and is confirmed as
  this package's foundational design going forward.
- **`references/lectures/*.md`** (all 13 files): each file now contains
  two independent full reconstructions of that lecture back to back — this
  package's own "Version 1" first, then the companion skill's "Version 2"
  appended in full beneath a divider. Nothing hand-merged, nothing dropped;
  where the two independently caught different transcription issues (the
  "CogModal" OCR fix in Version 2, the Math Vault page-count fix in
  Version 1), both are simply present, each in its own version's voice.
  `references/course-full-reconstruction.md` (and its `docs/` copy) were
  regenerated the same way, so the single-document course view stays
  consistent with the per-lecture files.
- Enriched `references/playbooks/01, 02, 03, 07, 09, 10, 11-innovation, 12`
  with concrete named examples, quotes, and resource links that existed in
  this package's own `references/lectures/*.md` reconstructions but had
  never been pulled up into the actively-routed playbook layer (the
  companion skill's condensed `SKILL.md` — now also fully present as
  "Version 2" above — had independently captured most of the same content
  in summary form, useful as a cross-check while writing these additions).
  See `references/provenance.md` → "Merge history" for the full
  per-playbook list.
- Added an explicit "Generalization discipline" note to playbooks 13 and 14
  confirming a review pass: both were already written as generalizable
  rules with real-project details used only as illustrations (a "live
  case", never the rule's scope), consistent with this package's standing
  design bar — reviewed and confirmed, not rewritten.
- Cleaned up a dangling session-specific wiki-link
  (`[[cvspp-integration-sweep-20260713]]`) in playbook 14 that would not
  resolve for a reader without that external note; replaced with the
  self-contained fact it was referencing.
- Still open, not addressed in this pass: the raw-transcript-appendix
  question inside each lecture file's Version 1 half (sits in tension with
  this same file's stated no-raw-redistribution policy) and whether to
  bundle the original PDFs/transcripts in the distributed package
  (currently excluded, per both source packages' own stated policy) —
  flagged in `references/provenance.md`, not resolved unilaterally.
- `scripts/validate_package.py` updated: frontmatter check now accepts an
  "Always-on" description prefix alongside "Use when "; per-lecture-file
  heading check now expects exactly 3 top-level headings (Version 1 +
  Version 2 divider + Version 2's own title); course-full-reconstruction.md
  heading count updated 15 → 41 to match. All four `scripts/test_*.py`
  contract scripts pass unchanged; the merge did not touch playbook 13's
  structure, which those scripts validate.

## 3.0.1 - 2026-07-13

Fixes a packaging bug in the v3.0.0 (and, retroactively, v2.9.0) release: the
repository holds two copies of the full course reconstruction —
`docs/course-full-reconstruction.md` (edited throughout this cycle's fidelity
audits) and `skills/research-english-academic-paper-writing-guide/references/
course-full-reconstruction.md` (the copy actually packaged and shipped inside
the skill). Only the `docs/` copy was being edited and synced to the locally
*installed* skill; the packaged copy under `skills/.../references/` was never
updated, so both the v2.9.0 and v3.0.0 GitHub releases shipped a stale course
reconstruction that was missing the Lecture-11-PDF-swap fix and this cycle's
four-lecture fidelity fixes, even though the changelog for those versions
described them as done. `scripts/validate_package.py` already had a check for
exactly this drift ("skill course-full-reconstruction.md must match
docs/course-full-reconstruction.md") — it was simply never run before
tagging. Ran it now: it also caught a second, unrelated staleness bug
(the playbook-count check still expected 14 files, not 15, after playbook 14
was added). Both are fixed; the validator and all four contract/test scripts
in `scripts/` now pass clean. Lesson: run `scripts/validate_package.py` (and
the `scripts/test_*.py` contract suite) before every tag, not just before a
first release — a passing validator that never gets invoked provides no
protection.

## 3.0.0 - 2026-07-13

Formalizes a two-phase figure workflow (agent authors a schema, human alone
renders) as a new dedicated playbook, and applies caption/prose discipline to
a live CCF-A submission after real advisor feedback ("body text is a bit
messy, table/figure captions are a bit long").

- **New playbook**: `14-figure-schema-and-rendering-gate.md`. Phase 1 (agent
  work): read the actual project source/data/results and author a structured
  figure-schema document per paper — layout-archetype selection (linear
  pipeline, cyclic loop, hierarchical stack, parallel/dual-stream, central
  hub, benchmark/ablation matrix), zone decomposition, a fixed color-semantic
  palette, an explicit arrow/connection grammar, and short course-terminology
  text labels — plus a matching in-manuscript placeholder. Phase 2 (human-only,
  gated): rendering the actual artwork, which an agent may help *prompt* for
  if explicitly asked, but never produce or hand off to a tool on its own
  initiative. Before writing this playbook, dispatched a dedicated transcript
  audit (Lectures 6-8, plus Lecture 10) to check the premise before codifying
  it: the "rendering must be 100% human" framing and a fixed required figure
  count are **not** literal transcript claims (AI figure generation postdates
  the course) — they are this skill's own professional-norm extension. What
  *is* transcript-grounded and reused directly: the existing figure-quality
  checklist (input/output/key-process/innovation/module-boundary/naming/
  consistency, already in `07-framework-figure-overview.md`) and the
  "figure and body text are complementary, not redundant" principle. The
  playbook states this provenance split explicitly rather than presenting the
  extension as course content — consistent with this skill's own evidence-
  discipline doctrine.
- Extended `SKILL.md`'s "Figures are logic tools" doctrine item and Forbidden
  Moves list with the caption-redundancy rule and the render-authority rule,
  and added a Routing Table row pointing figure-schema/rendering requests to
  the new playbook.
- Applied the new caption discipline to a real submission
  (`CVSPP_AAAI/论文/main.tex`): every figure/table caption was cut to 1-2
  sentences, with any genuinely load-bearing caveat that had been living only
  in a caption (checkpoint-selection detail, an encoder-swap exception, a
  cross-table comparability warning) moved into the nearby body paragraph
  instead of being dropped. The paper's worst offender was a ~140-word,
  9-sentence table caption; after the full pass across all 9 captions plus
  five overloaded body sentences split under the Lecture 9 "one sentence, one
  idea" rule, the paper still compiled at the same 9-page budget with zero
  new undefined references — trimming redundant caption text more than paid
  for the prose that had to move. Also fixed one incidental anonymity leak
  found in passing: an internal experiment-tracking codename ("cycle52
  ledger") had been left in the submission's body text.
- Finished the 2.9.0 fidelity re-audit's six rate-limited lectures (1, 4, 5,
  10, 12, and Lecture 11's main deck), completing full 13/13 coverage for the
  first time this cycle. One lecture (12) and one (1) came back fully clean.
  The other four had small, concretely-sourced fixes applied: Lecture 4 (a
  dropped point that Related Work subsections should differ in critique
  *depth* by relevance, not just length; a silently "corrected" slide typo
  now marked `[sic]` since the block is presented as verbatim); Lecture 5 (an
  ablation example that had imported a term, "事实知识", from a different
  slide's example; a dropped caveat that the full worked ablation example
  came from a journal paper's page budget, not a conference paper's); Lecture
  10 (three dropped specifics: the named reviewers on the "who reviews you"
  slide were genericized away, an author's patent-examiner/guest-professor
  background was dropped, and a named rhetorical citation was replaced with
  generic wording); Lecture 11's main deck (a dropped multi-task/auxiliary-
  objective-learning angle, including the cognitive-psychology memory
  experiment the instructor uses to motivate it, that existed only in the raw
  transcript appendix and never made it into the curated write-up). None of
  the six were fabrications or cross-lecture contamination; all were
  narrowing/genericizing losses from the reconstruction pass, consistent with
  the failure pattern this cycle's audits keep finding.

## 2.9.0 - 2026-07-13

Independent fidelity re-audit (found real drift 2.8.0 missed) and two new
LaTeX/authority lessons from live CVSPP incidents.

- Re-ran an independent fidelity audit against the original transcripts and
  slide PDFs, one dedicated pass per module, rather than trusting 2.8.0's
  "remains authoritative and unchanged" verdict. That verdict was wrong for
  at least one module: the pre-Lecture-11 bonus unit's PDF and the main
  Lecture-11 PDF were (and, until this pass, still are) swapped in the
  source manifest -- the file named as the bonus unit actually contained the
  20-page main lecture, and vice versa. A previous pass noticed the mismatch
  (the "wrong" cover-page title appeared) but explained it away instead of
  opening the other candidate file, and built roughly 300 lines of the bonus
  unit's writeup (its "where do research points come from" sections and its
  full slide-by-slide walkthrough, plus a tagline in its overview) from the
  wrong deck. Fixed at the root: the two source PDF filenames are swapped
  back to match their actual content (their paired `.transcript.txt` files
  were never mislabeled, only the PDFs were), and the affected sections are
  rewritten from the correct 9-page deck. Six other modules received small,
  concretely-sourced fixes (a dropped generic teaching example, dropped
  concrete before/after examples, a slide's silently-corrected typo left
  unflagged, an omitted fourth item in a four-part figure correspondence, a
  two-panel example flattened into one, and a real missing "three tips on
  symbol notation" passage). Five modules could not be re-audited this pass
  due to hitting a session-level API rate limit; they remain to be re-checked.
- Synced the locally *installed* skill (`~/.claude/skills/...`) forward to
  this repository's state. It had been running on the initial 2026-07-08
  install (v2.0.0) the entire time since, five versions and a full new
  playbook (`13-review-feedback-evidence-contract.md`) behind the repo copy,
  with no automatic sync step between the two. Every skill invocation in the
  interim used the stale, less-complete v2.0.0 guidance. Lesson: a versioned
  skill repository can drift arbitrarily far from its installed/active copy
  with no signal that this happened; check installed-vs-repo version numbers
  directly rather than assuming repo improvements are already in effect.
- Added a rule that rendering a figure's final artwork is an authorization
  decision separate from the figure's data/evidence readiness; an agent may
  write a complete drawing contract once data is ready, but must not treat
  that as license to also produce the rendered file, and must treat any
  already-rendered figure it did not produce itself as a pending decision to
  surface rather than settled progress to build on.
- Added a rule that a user's claim "the newer revision is worse than my
  backup" should be checked with a direct file diff before any other action;
  page-budget trimming can quietly remove a full baseline table, collapse a
  multi-control robustness paragraph into one vague sentence, or drop a
  caption's comparability caveat, none of which a compiler or automated
  check flags.
- Added a narrow LaTeX fix for a recurring alignment bug: when two
  independently-`\centering`-ed sub-tables are stacked in one float, wrapping
  the misaligned one in `\begin{flushleft}` does left-align it but also adds
  paragraph spacing that can silently push a page count over a hard venue
  limit; `\noindent\makebox[\linewidth][l]{...}` fixes the alignment with no
  added vertical space. Grounded in a live case: the `flushleft` fix moved a
  9-page AAAI submission to 10 pages; the `makebox` fix held it at 9.

## 2.8.0 - 2026-07-12

Course-fidelity and generality correction.

- Re-audited all 13 published modules against the original transcripts and
  slides. The course reconstruction remains authoritative and unchanged.
- Clarified that the source is 12 numbered lectures plus one pre-lecture bonus,
  not a numbered Lecture 13.
- Restored Lecture 5's conclusion rule: a conclusion briefly states verified
  findings, a consequential capability boundary, and future work. Repetition
  should be synthesized, not prohibited by deleting the boundary.
- Made the reviewer-evidence playbook subordinate to the relevant lecture and
  removed project-specific model, metric, accelerator, data-loader, and LaTeX
  incidents from its universal rules.
- Added a regression test that protects course fidelity, source hierarchy,
  version coherence, and the domain-general boundary of the reusable skill.

## 2.7.0 - 2026-07-12

Scope-of-validation discipline for methodology claims, and a source-archive
note for exemplar tables.

- Added a rule that a main-text methodology sentence ("we use encoder X")
  describes every reported number, not just the subset validated when the
  sentence was written: component-swap equivalence on a handful of cells does
  not transfer to the rest of the table, even with explicit sign-off to state
  it in writing. Grounded in a live case: a text-encoder swap validated
  equivalent on 4 of ~40 cells, written into the main text as the described
  encoder, then found on full retrain to collapse retrieval by 10-41 points on
  most of the remaining cells while being genuinely better on one further
  cell -- wrong in both directions on a component the paper had already told
  readers was safe. Prescribes two defenses: validate full scope before
  writing a universal sentence, or scope the sentence to the validated subset
  and treat it as provisional until broader evidence lands.
- Added a note to the exemplar-format transfer gate: when the exemplar is a
  source archive, extract and grep the real `.tex`/`.sty` for the device in
  question (e.g., a checkmark symbol pair) rather than approximating markup
  from a rendered PDF, since the source reveals the exact package dependency
  a rendered image cannot.

## 2.6.0 - 2026-07-12

Main-text space allocation and a repeat checkpoint-coherence slip.

- Added a rule that main-text space must match contribution weight: count
  words per section and compare against claimed contributions. A Method
  section should not be smaller than supporting infrastructure sections or
  a small fraction of combined Experiments prose; pull real detail already
  in the supplement (a loss formula, a layer count) into the main text
  rather than leaving Method as a pointer. Once a table/figure fully carries
  a claim, prose should give the one-sentence interpretation and stop, not
  re-narrate the values. Grounded in a real case: quantified word counts
  showed Method at 516 words against combined Experiments prose above 2200
  and a Benchmark Construction section longer than Method itself.
- Added a second, more specific failure-mode example for the
  checkpoint-coherence rule: combining an accuracy figure from one
  experiment report with a cost/timing figure from a later correction of
  the *same* experiment reads as consistent but mixes two different run
  lineages. Caught this recurring in the same session that first wrote the
  general rule, within hours -- worth flagging that the abstract rule alone
  does not reliably stop the mistake under writing-speed pressure.

## 2.5.0 - 2026-07-12

Long-appendix section-counter ceiling.

- Added a rule for iteratively grown appendices compiled with `\appendix`:
  its default `\thesection` (`\Alph{section}`) silently caps at 26 sections
  with no warning, then fails fatally on the 27th with a "Counter too
  large" error reported at whatever unrelated `\ref`/`\section` call
  happens to trigger it -- easy to misread as a citation bug, and capable
  of suppressing an entire compilation pass's output (zero pages). Fix by
  switching to `\renewcommand{\thesection}{\arabic{section}}` right after
  `\appendix`, before the section count ever approaches the ceiling. Found
  live: adding one more appendix section to an already-large CVSPP
  appendix (28 total) tripped this exact failure.

## 2.4.0 - 2026-07-11

Limitation density and placement.

- Added a rule to `05-experiments-conclusion-references.md` distinguishing
  limitation *honesty* (never negotiable) from limitation *density and
  placement* (a real craft decision): state each true limitation exactly
  once, in neutral prose, never repeated across method context, a bolded
  Limitations callout, and the Conclusion's opening sentences. Close the
  Conclusion with the paper's strongest verified findings first, and at
  most one short, unemotional pointer to where the supplement discusses
  scope. Reframe supplementary limitations as the boundary conditions of a
  documented design choice, not confessions of failure.
  Grounded in an observed case: an AI-reviewed submission moved from
  recommend-accept to recommend-reject across two revisions with identical
  underlying results, and the largest identifiable difference was a newly
  doubled, bolded restatement of one true limitation that the earlier,
  accepted revision had stated only once in passing.
- Cross-referenced this rule from playbook 13's failure-modes table.

## 2.3.0 - 2026-07-11

Anonymous-hosting identity gap, caught in live use.

- Added a rule that a credential authenticating to a code-hosting account
  proves ownership, not anonymity: fetch the account's own public profile
  (name, organization, email, blog, bio, location) before trusting it for
  anonymized release, even when the repository itself is set to private.
  Caught this in practice after creating a "private, therefore safe" release
  repository under an account whose public profile carried a real name,
  institution, and university email — a genuine near-miss on double-blind
  anonymity that a private-repo flag alone did nothing to prevent. Prefer a
  path with no code-hosting account in the loop (a local sanitized archive
  through the venue's own supplementary-material upload) over relocating the
  same risk to a freshly registered account.

## 2.2.0 - 2026-07-11

Author-kit and cross-reference verification round.

- Added a rule to re-verify template compliance against a freshly downloaded
  copy of the venue's *current* author kit rather than memory or a cached
  copy: diff the style file by checksum, read that kit's own forbidden-
  package list and "must not" statements verbatim, then scan the source for
  every forbidden package, stray `\pagestyle` command, and any macro that
  alters spacing/margins/fonts outside a single table or figure. Check the
  compiled PDF's font table for unembedded or Type 3 fonts and scan its raw
  bytes for embedded-link/bookmark markers even when no hyperlink package
  was knowingly loaded.
- Added a rule to treat every hard-coded cross-reference in a separately
  compiled companion document (an appendix citing the main paper by written
  section number) as suspect after any large rewrite that reorders
  sections, since a wrong section number does not fail to compile — only a
  direct re-derivation and diff against the rewritten source catches it.
- Added a note to check for an AoE-vs-local-time conversion before treating
  two differently worded deadline dates/times from independent sources as a
  contradiction.

## 2.1.0 - 2026-07-10

Evidence-contract revision release candidate.

- Added a reviewer-feedback playbook that converts advisor comments into a
  claim ledger before prose revision.
- Added native-annotation source hierarchy, conditional-feedback tracking, and
  the rule that reviewer or advisor permission cannot substitute for artifacts.
- Added fail-closed checks for incompatible evaluation contracts, table
  citations, source/TeX/PDF drift, official submission-policy conflicts, and
  credential handling.
- Required one row per claim-bearing dataset/method, banned hidden
  ``and related sources`` groupings, and separated comparison-eligible values
  from reference-only numbers.
- Added encoder/configuration/checkpoint/result provenance, one-sentence-one-
  meaning revision, dataset coverage statuses, and figure evidence cards.
- Added a title-level mechanism gate: technical labels such as “one-step” now
  require an operational definition and a matched distinguishing experiment.
- Added direct-difference framing for related work and fail-closed stale-
  generated-artifact detection.
- Added a final artifact validation order so hashes, PDFs, tables, citations,
  and release contents are checked together immediately before publication.
- Added a repository-derived dataset census and primary-source numeric
  provenance contract before any “complete” table claim.
- Added a review-artifact identity ledger that joins native annotation IDs,
  reviewed/source revisions, and rebuilt-PDF hashes before feedback is marked
  resolved.
- Added a structure-only exemplar-transfer gate for reviewer-supplied papers,
  including venue-package compatibility and minimum rendered-font checks.
- Added a claim-driven experiment queue with controls, seeds, resource budget,
  stop conditions, failed-run accounting, and a ban on treating GPU use as
  research evidence.
- Added full figure-card reconciliation plus anonymous ZIP inventory, license,
  checksum, secret-scan, clean-extraction, and smoke-test gates.
- Added checkpoint-coherent result-row rules that prohibit per-metric epoch
  maxima and mixed cache/model states, require paired-seed alignment and
  deterministic zero-score tie disclosure, reject exact SD claims from rounded
  console logs, and bind metric names to their implemented joint events.
- Added a data-exposure audit that separates per-epoch update budget from
  corpus coverage and rejects sorted-prefix shard truncation when it removes
  task or action support.
- Replaced token-presence regression checks with Markdown-aware tests for
  heading/workflow order, section-local semantic co-occurrence, exact claim-
  ledger/dataset-census/experiment-queue/release-inventory schemas, and
  forbidden contradictions. Each test now proves fail-closed behavior against
  keyword-bag, section-relocation, and negation-reversal mutations; these tests
  validate the playbook contract, not a manuscript or submission artifact.
- Added package-validator coverage and CI execution for the new playbook tests.
- Added a page-boundary verification rule: confirm a venue's main-content page
  cap by reading the compiled PDF page by page, not just its total page count,
  since a two-column float can spill onto a references-only page unnoticed;
  and a note that `\flushbottom`-style layouts absorb small trims without
  moving page breaks, so boundary violations need a structural fix (float
  reposition or resize) rather than further wording edits.

## 2.0.0 - 2026-07-08

Major skill-package release.

- Added the complete full-course reconstruction to the installable skill at
  `references/course-full-reconstruction.md`.
- Added an Agent reading protocol to the course reconstruction so agents can
  search and read the 11k-line document by lecture, task, and uncertainty.
- Rewrote `SKILL.md` as a strict execution protocol: mandatory source order,
  course-first reading, doctrine, task routing, output standards, scripts, and
  forbidden moves.
- Updated OpenAI/Codex metadata so the default prompt explicitly requires
  consulting the full course reconstruction first.
- Prepared the release process for a versioned skill zip asset:
  `research-english-academic-paper-writing-guide-skill-v2.0.0.zip`.

## 1.0.0 - 2026-07-08

Initial publishable release candidate.

- Added a single cross-platform Agent Skill entrypoint:
  `skills/research-english-academic-paper-writing-guide/SKILL.md`.
- Added 13 lecture reconstructions under `references/lectures/`.
- Added 13 operational playbooks under `references/playbooks/`.
- Added a single integrated Markdown course reconstruction:
  `docs/course-full-reconstruction.md`.
- Added provenance notes and official slide checksums.
- Excluded raw PDFs, raw transcripts, and image assets from the final repo.
- Added lightweight helper scripts for title checks and research-point canvases.
- Added repository-level license, notice, package validation, and CI metadata.
