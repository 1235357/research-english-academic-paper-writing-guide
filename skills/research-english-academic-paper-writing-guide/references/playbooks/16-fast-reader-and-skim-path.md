# The Fast-Reader Contract: Writing for the Skim That Decides

> This playbook is the governing lens `SKILL.md` points to. It is external to
> Yu Jing's course (which teaches how to make any given figure or section
> good, not how reviewing time gets allocated across a paper) and is built
> from actual web research, not from the user's or this skill's own
> assumptions about reviewer behavior — including one source found and
> explicitly rejected during that research. See Provenance for exactly what
> is well-supported versus honestly uncertain.

## Why this playbook exists

A user directly posed the dilemma this playbook addresses: if a reviewer
read every sentence of a paper carefully, a technically sound paper would
be accepted — but in practice, submission volume means reviewers
triage hard, and a paper's fate is disproportionately decided by whether
its figures, tables, and structural framing alone communicate the work.
This is a real, researchable question, not a rhetorical complaint, and it
deserved an actual literature check rather than another confident assertion
layered on top of the ones already in this skill.

## What the research actually supports (and what it doesn't)

**Well-supported, from multiple independent sources**:

- **A skim-for-first-impression pass is literally the taught first step of
  reviewing, not an informal shortcut.** A named, credentialed source (Kathy
  Gould, PhD, Professor of Cell and Developmental Biology, in a documented
  talk to Vanderbilt postdocs) teaches new reviewers to "skim the paper to
  form an initial impression" *before* reading section by section, and lists
  "do the figures and tables add to the paper" as one of the first questions
  to ask during that initial skim — full detailed section-by-section reading
  is the *second* stage, not the first.
- **Figures and tables are an explicit, named dimension of official reviewer
  training**, not an informal heuristic — a major publisher's (Wiley) own
  step-by-step reviewer guide asks reviewers directly whether "tables,
  figures, and images effectively support the manuscript's findings," as a
  standing question independent of the prose.
- **Some reviewers reportedly engage with figures and tables and skip
  substantial portions of the surrounding prose entirely** — multiple
  academic-writing-guidance sources (independent of each other) converge on
  this specific claim: readers, including reviewers, "turn their attention
  to the tables and figures before they read the entire text," and some
  "look only at these display items and not at the rest of the manuscript."
  This is practitioner guidance from academic editing services, not a
  peer-reviewed study — treat it as corroborating, not as a rigorously
  measured statistic.
- **A genuine, fast, high-stakes triage stage exists at high-volume AI
  venues, and is growing, not shrinking.** NeurIPS 2020's Area Chairs
  skimmed over 9,000 submissions to identify obvious rejects, with roughly
  11% receiving a summary reject this way; IJCAI 2020 ran a comparable
  process. A 2025 arXiv paper on ICLR desk-rejection notes that submission
  volume growth has pushed CVPR, ICCV, KDD, AAAI, IJCAI, and WSDM toward
  strict per-author submission limits and automatic desk-rejection of
  excess submissions by ID order — i.e., some papers now never reach a
  content-based read at all regardless of quality. This is squarely the
  submission-volume pressure the user described, and it is specific to
  exactly the AI/ML venue landscape this skill targets.
- **The Introduction section alone is reportedly a strong predictor of
  review outcome** — a cited empirical study (Vincent-Lamarre and Larivière,
  2021, per a survey paper's summary) found that a model using only the
  Introduction's text performed best among single-section predictors of
  review outcome, ahead of models using other individual sections. The same
  summary reports the surprising secondary finding that accepted papers'
  prose measured as *less* readable than rejected papers' — read this as
  "dense, technically substantive writing is not penalized," not as
  "obscure writing helps"; it does not license writing worse prose.
- **AI-assisted reviewing is now a measured, real phenomenon at the exact
  venues this skill targets, not a hypothetical.** A January 2026 study
  ("Do LLMs Favor LLMs? Quantifying Interaction Effects in Peer Review,"
  Cornell) analyzed over 125,000 paper-review pairs across ICLR, NeurIPS,
  and ICML and found a measurable interaction effect: LLM-assisted reviews
  appear to score LLM-assisted papers more favorably than minimal-LLM-use
  papers, on average. Treat this as evidence that AI-assisted review is
  real and growing at these venues, not as evidence for any specific
  mechanism to exploit — this skill does not turn this into "write to game
  an AI reviewer," only into "the fast-skim dynamic below is not shrinking
  as review gets more AI-assisted, it may be sharpening."

**Explicitly not supported, and rejected during this research rather than
quietly used**: a search surfaced a source (a blog attributed to a
"manuscript readiness check" service) making very specific, quotable claims
— reviewers "form a provisional accept-or-reject judgment in the first 10
minutes," "look at the last figure before the methods" at "Nature-tier"
journals — with an identical, templated "submission readiness check takes
about 5 minutes" sentence reused verbatim across otherwise-unrelated
journal-specific pages, alongside a pitch for the same service's paid
diagnostic tool. That pattern (templated claims, reused across pages,
attached to a product pitch) is a content-marketing tell, not a research
finding, and this playbook does not repeat those specific numbers
(the "10 minutes," "look at the last figure before methods") as fact. The
directionally similar but better-supported claim above (skim-first is the
taught first stage, not that it takes exactly 10 minutes) is what this
skill actually relies on.

**The honest synthesis, holding both the "hours" data and the "minutes"
data without contradiction**: independent time-tracking surveys (Publons,
Sense About Science, and a controlled study on ReviewFlow) consistently
report 4.75-6.4 hours as the average *total* time a full review takes — so
"reviewers only spend five minutes" is not an accurate description of the
whole process and this skill does not claim it is. What the research
supports instead is narrower and, for drafting purposes, just as
consequential: (1) a separate, genuinely fast (minutes, not hours)
desk-reject/triage stage exists at high-volume venues and can end a paper's
chances before any full read happens; and (2) even within a full multi-hour
review, the taught methodology explicitly front-loads a skim of the
figures/tables/abstract for an initial impression before the detailed,
section-by-section pass — so that initial impression very plausibly
anchors how the following hours of reading go, even though no source found
here rigorously measures the size of that anchoring effect. Design for the
fast pass because it is real and load-bearing, not because it is the only
pass that happens.

## The skim self-test

Apply this whenever a draft, or a revision, is presented as close to done.
Read *only* the title, the abstract, every figure with its caption, every
table with its caption, and the section headers — skip every other sentence
of prose, deliberately, the way the research above says a real first pass
often does.

Then answer, honestly, in this order:
1. Does this convey what problem is being solved and why it matters, without
   reading the Introduction?
2. Does this convey what the method actually does — not just that it exists
   — without reading the Method section's prose? (This is playbook 14's
   figure self-sufficiency test, restated as a whole-paper check rather than
   a single-figure check.)
3. Does this convey what the results actually show and whether they're
   credible, without reading the Experiments prose? (This is playbook 15's
   table taxonomy and column discipline, restated the same way.)
4. Would a reader stop here with a positive, coherent impression — or would
   they stop here confused, or unconvinced, regardless of how good the
   skipped prose is?

**A failure at this test is a structural problem, not a prose problem.**
The fix is never "explain it better in the text nearby" — by construction,
this pass does not read that text. The fix is one of: a missing or
under-detailed figure (playbook 14), a table carrying the wrong kind of
information for its job (playbook 15), a title that doesn't state the
technical contribution (playbook 02), or an abstract/introduction that
doesn't chain need → problem → method → result cleanly on its own (playbook
03). Do not accept "it's explained in Section 4" as a fix to a skim-test
failure; that explanation will not be read on the pass that matters most.

## Worked example: applying this to a real in-progress paper

Cross-referencing a real advisor session's live table/figure critique
(playbooks 14 and 15's source) against that same paper's own draft, page by
page, surfaced exactly this kind of structural gap, concretely — not a
hypothetical:

- The draft's Table 2 was, at the time of the session, still a checkmark-only
  dataset-coverage table (✓/✗ across nine property columns) — exactly the
  format playbook 15 flags as wrong for a dataset-composition table, since a
  checkmark alone fails the skim self-test's third question: a reader
  skimming only tables cannot tell *what the actual attribute values are*,
  only that some property is present. The session's own proposed fix (a
  paired distribution chart plus a real-attribute-value table) is what
  playbook 15 now documents as the correct type for this job.
- The session discussed a methods-comparison table (multiple prior methods
  as rows, all eleven datasets as columns, one collapsed headline metric)
  that, cross-checked against the actual draft, **did not yet exist as a
  table anywhere in the manuscript** — the draft's own Table 3 shows only
  the paper's *own* method across datasets on four metrics, not a
  cross-method comparison. A reader doing only the skim self-test would
  have no table answering "how does this compare to prior work, in one
  place" — that gap is invisible if you only read the surrounding prose,
  which does discuss the comparison in words, but is exactly the kind of
  gap this self-test is built to surface, since the skim does not read that
  prose.
- Every figure in the same draft was, correctly, still a placeholder
  (per playbook 14's placeholder-first policy) — so the skim self-test
  could not yet be run in full on the figures layer, only planned against
  each placeholder's stated content description. This is the right state
  to be in mid-draft; the self-test is meant to be re-run once real figures
  replace the placeholders, not substituted for by inspecting placeholder
  text alone.

This is the intended use of this playbook: not a one-time audit, but a
standing check re-applied every time a table, figure, title, or abstract
changes, since any one of those changing can flip the answer to the
self-test's four questions.

## Provenance

The research summarized above was gathered by web search at the user's
explicit request, specifically to test (not simply confirm) the premise
that reviewers primarily engage with a paper's figures/tables/structural
framing under real time pressure. Sources cited by name where the source
itself is named and credible (Kathy Gould/Vanderbilt, Wiley's official
reviewer guide, the NeurIPS/IJCAI desk-reject process, the Cornell LLM-
peer-review study, Vincent-Lamarre and Larivière 2021 as cited in a survey
paper); sources used as corroborating-but-not-rigorous where that is the
honest characterization (academic-editing-service blogs); one source
identified and explicitly excluded as unreliable content-marketing rather
than research. This playbook's "worked example" section cross-references
the same real advisor-session transcript and the same paper's own draft
PDF that ground playbooks 14 and 15 — see `references/provenance.md` for
those sessions' full detail.
