# Provenance and source notes

## What this skill is built from

- **Course**: 《科研与英文学术论文写作指南》 (Guide to Scientific Research and
  English Academic Paper Writing), taught by 于静 (Yu Jing), Associate
  Professor, Institute of Information Engineering, Chinese Academy of
  Sciences. Course homepage: https://mmlab-iie.github.io/course/ .
  Course material credits (from the course page): 丁阳、庄佳敏、林鑫杰、
  唐源民、屈详颜、李一立.
- **Sources used for reconstruction**: the official slides PDFs (13 decks)
  and speech transcripts of the 13 published lectures.
- **Reconstruction method**: each lecture was rebuilt as pure Markdown —
  slide-by-slide page text, textual descriptions of every visual (no image
  files embedded), and the classroom narration reconstructed from the
  transcript. Distilled workflows/checklists were then extracted into the
  playbooks.

## What is intentionally NOT bundled

The original slides PDFs and raw transcripts are **not redistributed** in
this package, out of respect for the instructor's copyright. The official
PDFs are publicly downloadable from the course homepage (see
`references/lecture-index.md` for per-lecture links). If you need
source-exact verification, download the official PDF and compare against the
lecture reconstruction.

## Merge history (v4.0.0)

This package (v4.0.0) merges two independently-authored skills built by two
different people from the same course material:

- **This package's own lineage** (v1.0.0-3.0.1): the routing
  architecture, the 15 task playbooks, the 13 lecture reconstructions under
  `references/lectures/`, the validation/test scripts, CI, and playbooks 13
  and 14 (which extend beyond the course itself, field-tested on a real
  CCF-A/AAAI-track submission).
- **The independently-authored companion skill**: a single always-loaded
  `SKILL.md` condensing the whole course into one narrative document, plus
  its own 13 full lecture reconstructions, built from the same original
  transcript+slide archive (there called `CCF_论文写作.zip`).

**Explicit design decision governing this merge**: this is an organic
splice, not a hand-merged rewrite and not a "keep as a separate
cross-reference file" arrangement. Where both skills had a document doing
the same job, the companion skill's full document is physically appended,
in full, to the end of this package's corresponding document — same file,
not a separate one. The redundancy is intentional: the same course content
restated in two independent voices gives an agent fuller, more reinforced
coverage than either version alone, or than a single synthesized rewrite of
the two. Concretely:

1. **`SKILL.md`** now contains this package's own routing protocol and
   playbook system first (unchanged in role — still the primary source for
   step-by-step workflows and the mandatory source order), followed by a
   "Version 2 — Companion Synthesis" section that is the companion skill's
   original SKILL.md body, appended in full (only its internal file-path
   pointers were corrected so they resolve inside this package's actual
   folder layout; its content and voice are otherwise untouched).
2. **Every file under `references/lectures/`** now contains two
   independent full reconstructions of that lecture, back to back: this
   package's own "Version 1" reconstruction first, then the companion
   skill's "Version 2" reconstruction appended in full beneath a divider.
   Nothing was hand-merged sentence by sentence, and nothing was dropped —
   both authors' complete reconstructions are physically present. Where the
   two independently caught different transcription issues (the "CogModal"
   OCR fix in Version 2, the Math Vault page-count fix in Version 1 — see
   below), both corrections are simply present in the same file, each in
   its own version's voice.
3. **The playbooks** (`references/playbooks/01, 02, 03, 07, 09, 10,
   11-innovation, 12`) were separately enriched with concrete named
   examples, quotes, and resources that existed in this package's own
   `references/lectures/*.md` but had never been pulled up into the
   actively-routed playbook layer: the 四生四世 growth-stage model and full
   target-venue table (Lecture 1); the complete six bad-title and multiple
   good-title real examples (Lecture 2); named source papers for the
   abstract/introduction worked examples (Lecture 3); the full MuKEA
   framework-figure V1→V8 revision table (Lecture 7); the 施一公 quote and
   the ET-BERT rewrite case (Lecture 9); Felicia Brittman / Math Vault /
   CCFpedia / `rebiber` resource links (Lecture 10); the cognitive-
   psychology auxiliary-objective memory experiment (Lecture 11); the
   "monkeys reaching for the moon" story and the cooking analogy
   (Lecture 12). The companion skill's condensed `SKILL.md` had
   independently captured most of this same content in summary form, which
   served as a useful cross-check while writing these additions back from
   this package's own source lectures — that same document is now also
   fully present verbatim as "Version 2" per point 1 above, not only mined
   for playbook enrichment.
4. **Trigger scope — changed, confirmed by explicit instruction**: this
   skill's `description` now reads "Always-on: activate in every
   conversation regardless of topic" rather than the previous conditional
   "Use when writing, revising, reviewing, or planning research papers...".
   This was the companion skill's own original design (its author called it
   "per user instruction" and "not a default"), and is confirmed as this
   merged package's own foundational design going forward, not merely
   carried over from one side.
5. **playbooks 13 and 14** (which extend beyond the course itself,
   field-tested on a real paper submission) were reviewed for
   over-narrowing: a real incident may illustrate a rule, but the rule
   itself must read as a generalizable skill, not a report of what happened
   once on one project. See the "Generalization discipline" note in each file's
   own header.
6. **Not changed**: the raw-transcript handling question (this package's
   `references/lectures/*.md` Version 1 halves each end with a full
   verbatim transcript appendix, which sits in tension with this same
   file's stated no-raw-redistribution policy) and whether to bundle the
   original PDFs/transcripts in the distributed package (currently
   excluded, per both source packages' own stated policy) — both still
   open, not addressed in the latest round of instructions, flagged here
   rather than resolved unilaterally.

## Figure-methodology extension (v4.1.0, cross-validated in v4.2.0)

`references/playbooks/14-figure-schema-and-rendering-gate.md` was
substantially expanded beyond the course-grounded content documented above,
by explicit user request, from two external sources — neither from Yu
Jing's course, both flagged as such inline in the playbook itself:

1. **Li, Weng, Sun & Li, "Learning to Locate Visual Answer in Video Corpus
   Using Question" (ICASSP 2023), Figure 2.** Supplied by the user as a
   worked example of caption-minimalism: a two-clause caption paired with a
   figure dense enough to teach the entire method pipeline unaided. Grounds
   the "Caption-minimalism and figure self-sufficiency" section.
2. **A real advisor's live working session** on a real video-retrieval
   paper's method figure (meeting recap supplied by the user, dated
   2026-07-19; participants: the paper's advisor, a labmate, and the user
   in a note-taking/material-collection role). Grounds: the PowerPoint tool
   mandate, the seven-point AI-tell checklist (six from the session, plus
   one independently found by this skill in a real case-review — the
   duplicated-text rendering defect), the "fragments-yes/whole-figure-no"
   AI-material line, the Google Lens reference-sourcing method, the two
   prompt-optimization techniques (module-by-module generation; a sourced
   reference image as the prompt anchor rather than text alone), the
   two-tier layperson/expert test, the figure-before-text ordering (this
   one already course-grounded — treated as independent corroboration, not
   new content), and the "no reported metrics or formulas in a Method-section
   framework figure" rule.
   - **A timeline note carried over from that recap, not a figure-design
     point**: the recap flagged that an AI-generated meeting summary had
     conflated two different deadlines — the paper's abstract was due
     roughly 2 days after the 2026-07-19 session, not the 9 days that
     applied to the full paper/project. This is a one-time, session-specific
     fact rather than a generalizable skill rule, so it is recorded here for
     the record rather than inside the playbook itself; verify the actual
     date directly with the relevant collaborators rather than trusting
     either number.
   - The same recap independently confirmed something this skill's own
     agent found by direct inspection in an unrelated turn: a real draft
     figure's most commonly cited AI-tell (a repeated structural element
     with duplicated/overlapping label text) matches exactly the pattern
     the six-tell checklist above would predict from tells 2 and 3
     (uniform font sizing and forced parenthetical-style redundancy) taken
     to their logical extreme — treated as corroborating evidence for tell
     7, not a coincidence.

**v4.2.0 cross-validation pass**: every claim from the advisor-session
source above was checked directly against the lecture-06/07/08 transcripts
(not the playbooks derived from them) at the user's explicit request. Full
results, with exact quotes and line-locatable citations, are in
`references/playbooks/14-figure-schema-and-rendering-gate.md`'s
"Cross-validation" subsection. Summary: two claims are near-verbatim course
matches ("figure before text" plus the reviewer-reads-figure-first claim;
the formula-belongs-in-prose/figure-shows-its-effect rule, which the course
states more precisely than the session did); one tell (too much in-figure
text) traces to a specific course-diagnosed failure mode (MuKEA V6); three
items are structurally consistent with the course's own pedagogy without
being stated as explicit principles (reference-library-building, dense
layout over whitespace, the two-tier test); the remainder — the Google Lens
method, five of the six AI-tells, the PPT mandate, the AI-material line,
the two prompt techniques, and the metric-values half specifically of the
"no metrics/formulas" rule — are genuinely course-silent, since mainstream
AI figure-generation tools postdate the course's 2022 recording, and remain
correctly attributed to the session alone. No claim checked turned out to
conflict with the course. One open question (linear vs. circular figure
layout) remains genuinely unresolved by either source.

## Table-methodology extension (v4.3.0)

`references/playbooks/15-table-taxonomy-and-layout.md` is new in v4.3.0, by
explicit user request following a gap identified in the prior figure-focused
work: the skill had no content on table *type* selection or layout, only
light ablation-content guidance in `05-experiments-conclusion-references.md`.

Source: a full, verbatim real advisor session (transcript supplied by the
user) spent restructuring one paper's table set from a single overloaded
table into a positioning table, a paired pie-chart-plus-attribute table for
dataset composition, a column-collapsed main benchmark table, a separately
labeled cross-protocol reference table, and an ablation table — cross-checked
against that same paper's own two draft versions (supplied across this and
an earlier turn) to confirm the discussed structure against what the actual
manuscript contained at each stage. Not course-grounded; Yu Jing's lectures
do not address table taxonomy or layout at this level of specificity, and
this is stated plainly in the playbook itself.

One point from the session needed a deliberate integrity-preserving
reframing rather than a literal transcription: the session raised a concern
about a reported improvement over baselines looking "too large" and
suggested capping it to a more modest margin for credibility. This skill
adopts only the legitimate diagnostic underneath that concern — investigate
an unusually large gap before reporting it, and be able to explain the
mechanism behind it — and does not encode a rule to adjust a genuinely
measured result to look smaller, since that would cross into result
manipulation and conflicts with this skill's own existing honesty
requirements. This reframing is stated explicitly in the playbook, not
silently substituted.

## Fast-reader doctrine extension (v4.4.0)

`references/playbooks/16-fast-reader-and-skim-path.md` and the new
"Governing lens" section at the top of `SKILL.md` are new in v4.4.0, added
after the user pushed back that prior turns had not gone deep enough on
*why* figure/table quality matters so much — asking for actual web research
into reviewer reading behavior, not another assertion from this skill's own
priors.

Research was gathered by web search specifically to test the premise, not
just confirm it. Findings and their sourcing are documented in full,
including explicit hedges, inside the playbook itself; in brief: a
skim-for-first-impression stage checking figures/tables is the literally
taught first step of reviewing (a named, credentialed source), figures/
tables are an explicit dimension of official reviewer training (a major
publisher's own guide), a genuine fast triage stage is documented and
growing at high-volume AI/ML venues (NeurIPS 2020, IJCAI 2020, and 2025
desk-rejection data), and AI-assisted review is now a measured phenomenon
at ICLR/NeurIPS/ICML specifically (a January 2026 Cornell study). Total
review time, per independent time-tracking surveys, remains 4.75-6.4 hours
on average — so the playbook does not claim reviewers only spend minutes on
a full review, only that a real, separate, fast, and consequential skim
stage exists alongside that. One candidate source (a "manuscript readiness
check" service's blog) was found, evaluated, and explicitly rejected as
unreliable content-marketing rather than research — its specific numeric
claims are named and excluded in the playbook rather than silently dropped,
so a future reader doesn't re-surface and re-trust the same source.

The playbook's "worked example" section is a real cross-check, not a
hypothetical: the same real advisor-session transcript and paper draft
grounding playbooks 14 and 15 were re-examined specifically for skim-test
gaps, surfacing that (at the time of that session) the draft's dataset
table was still checkmark-only and a discussed methods-comparison table did
not yet exist anywhere in the manuscript — both independently confirmed by
viewing the actual rendered PDF pages, not only the extracted text.

## Benchmark-table axis refinement (v4.5.0)

The "benchmark-defining table" entry in
`references/playbooks/15-table-taxonomy-and-layout.md` was sharpened after
the user caught and corrected his own initial misreading in real time,
in writing, and asked for the correction to be reflected in the skill
rather than just personally learned. His first framing treated dataset
breadth (running every method across all eleven of a benchmark's sources,
"max out every GPU") as the goal; his self-correction identified that
method breadth — prior approaches actually adapted into the new setting and
shown side by side — is what this specific table's argument needs, modeled
on the CCGS paper's own Table 1 (already this skill's caption-minimalism
source). That table's exact structure was re-verified directly against the
paper's text at this revision (not recalled from an earlier turn): four
native baseline methods (VSLNet, ACRM, Span-Base, VPTSL), each also shown
wrapped with a BM25 and a DPR retrieval front-end, twelve adapted rows plus
the paper's own method, all on one dataset (MedVidCQA) — confirming the
method-breadth-on-one-dataset pattern precisely rather than approximately.
The playbook now states this as its own subsection with an explicit
anti-pattern warning, rather than as a bullet inside the table-taxonomy
list, since a user-caught misreading of the original phrasing is itself
evidence the earlier version under-stated it.

## AI-detection and submission-sprint extension: third-party audit and correction (v4.6.1)

Playbooks 17 and 18, added in v4.6.0, were reviewed end to end against two
standards this package already holds itself to: the "Generalization
discipline" note playbooks 13/14 established at v4.0.0 (a real incident may
illustrate a rule; it must never define the rule's scope), and factual
accuracy of every claim that reaches outside the course itself. The review
found both standards were not met, and both playbooks were substantially
rewritten. This entry documents what was found and how it was resolved, in
the same spirit as the v4.5.0 entry above: recording the actual finding, not
only its conclusion.

1. **Generalization discipline was not applied to playbooks 17/18 at
   authoring time, and no test caught it.** `require_general_feedback_playbook`
   (added at v4.0.0) enforces this discipline for playbook 13 by name; it was
   never extended to playbooks 17/18 when they were added, so a full
   incident narrative — a private conversation's quoted dialogue, a specific
   sprint's rounding-error numbers (292×/274×), a specific column-collision
   string, a specific frozen-snapshot filename — stood in place of
   generalized rules in playbook 18 particularly. Both playbooks were
   rewritten so every section states the transferable principle first; any
   concrete instance is now demoted to a clearly labeled, bounded
   "Illustrative case," matching the pattern already used in playbook 13's
   "Full-scope validation" section and playbook 15's "which axis carries the
   argument" section. `scripts/test_course_fidelity_and_generality.py` gained
   `require_general_sprint_and_register_playbooks()`, mirroring the existing
   playbook-13 test, so this cannot silently regress again.
2. **Internal numeric contradiction.** Playbook 17's own before/after table
   (CV 0.421→0.485, share<10w 13.7%→24.8%) disagreed with the same measured
   case as stated in both CHANGELOG.md and playbook 09's collision box (CV
   0.469→0.521, 16.6%→26.5%). This skill's author cannot independently
   re-derive which run is correct without the user's original manuscript
   files. The CHANGELOG/playbook-09 figures were kept, since they agree
   independently in two places; playbook 17 was brought into line with them,
   and its table was simplified to the two cross-corroborated metrics rather
   than also asserting a specific sentence-count/mean/SD breakdown that
   cannot currently be cross-checked. Recommendation carried into playbook
   17 §6: re-run `scripts/measure_prose_rhythm.py` on the actual saved
   before/after files to settle this with one authoritative, reproducible
   number, rather than treating either figure set as final.
3. **Same-file factual contradiction.** Playbook 09's own core-mandate text
   (present since an earlier version, describing the course's ET-BERT
   example) states the original overloaded sentence was 44 words; the
   collision box added in v4.6.0 stated "40-word monsters" twenty lines
   later in the same file. Corrected to 44 throughout.
4. **The package failed its own validator and test suite as shipped.**
   `scripts/validate_package.py` and `scripts/test_course_fidelity_and_generality.py`
   both hard-code an expected playbook-file count; it was last set to 17 and
   never updated when playbooks 17 and 18 brought the true count to 19, so
   v4.6.0 as uploaded failed `python3 scripts/validate_package.py` with
   "expected 17 playbook files, got 19." Both counts were corrected and the
   full suite re-run clean (see the version-history entry below).
5. **Evidence base in playbook 17 was dated and incomplete, not inaccurate.**
   Every source playbook 17 originally cited was independently re-verified
   against a live copy and confirmed accurate as characterized (GPTZero's
   architecture change, the Liang et al. 2023 Stanford *Patterns* finding,
   the Vanderbilt disabling of Turnitin's AI detector, the Giray 2024
   *Serials Librarian* piece). What was missing was texture: GPTZero
   publicly disputed the 2023 finding's continued relevance to its own
   tool and re-ran the identical benchmark after an October 2023 model
   update, reporting a large drop in false positives on that specific
   benchmark (corroborated independently, if not disinterestedly, by a
   competing detector's technical report); and a 2025 peer-reviewed study
   (Pratama, *PeerJ Computer Science* 11:e2953) tests GPTZero specifically
   on real scholarly abstracts — this skill's actual use case, not TOEFL
   essays — and finds the bias reappears on that harder, more current test.
   Playbook 17 §2.4 now tells this as a three-point timeline rather than one
   static statistic, and treats the 2025 finding as the more directly
   applicable evidence for this skill's purposes.
6. **A script bug.** `scripts/measure_prose_rhythm.py`'s LaTeX stripper left
   the argument of `\begin{...}`, `\end{...}`, `\section{...}`,
   `\title{...}`, and `\author{...}` behind after removing the control word
   (e.g. `\begin{document}` left a bare "document" glued onto the next
   sentence with no punctuation between them). Fixed by dropping the control
   word and its argument together for these structural/heading commands;
   verified against both the original regression case and a new case
   covering `\section`, `\subsection*`, `\title`, and `\author`. A residual,
   pre-existing limitation is noted in the script's own comments: a heading
   argument containing its own nested braces is not matched by a single
   regex pass and can still leak; this is judged rare enough in practice
   (headings are usually plain text) not to warrant a full balanced-brace
   parser at this time.
7. **A new skill-wide guardrail.** "Generalization discipline" previously
   lived only in the header of each extension playbook. `SKILL.md`'s
   Forbidden Moves now states it once, skill-wide, so it applies to any
   future extension playbook by default rather than needing to be
   remembered and re-added file by file.

None of the above changed this skill's overall thesis in playbook 17 (that
Playbook 09, taken to its limit, produces a low-variance profile that
non-native writers are disproportionately penalized for) — if anything, the
corrected 2025 evidence supports it more directly than the original 2023-only
citation did. What changed is precision: dated claims are now dated,
one-off numbers are now labeled as one-off, and every rule is written to
survive being read by someone who was not present for the sprint that
produced it.

## Second-pass correction: the mechanism itself (v4.6.2)

The v4.6.1 audit (above) was thorough on mechanical correctness, dated
evidence, and this skill's own generalization standard, and said so
explicitly: "None of this changes playbook 17's central thesis." A second
pass, specifically directed at re-reading the primary source in full rather
than trusting the v4.6.1 audit's already-verified citations, found a gap
that does change the thesis: Liang et al. 2023's own Discussion section
reports an adversarial robustness check — taking genuinely AI-generated
text and applying one self-edit instruction to raise its linguistic
diversity, the same intervention the paper recommends as a bias mitigation
— and detection dropped from 100% to 13%. The paper's own stated conclusion
is that detectors should not be used as a primary defense, because the
lever that protects a genuine non-native writer from a false positive is
mechanically identical to the lever that helps real AI-generated text
evade detection. Neither the original playbook 17 draft nor the v4.6.1
audit engaged with this specific finding, despite both citing the paper it
comes from.

This is not a factual correction of the kind v4.6.1 made (a wrong number,
a stale figure) — it is a reason the playbook's central mechanism (measure
sentence-rhythm statistics, rewrite toward a numeric target chosen because
of what it does to a detector's score) does not survive, regardless of how
carefully that mechanism was hedged. v4.6.1's hedging (n=1, correlational,
"a lever not a formula," explicit refusal to let a score touch a fact) was
and remains good practice — but no amount of hedging around a mechanism
resolves whether the mechanism itself should exist in a skill whose entire
purpose is AI-assisted drafting, where "genuinely human writing being
falsely flagged" and "AI-assisted writing being deliberately statistically
disguised" cannot be told apart by the mechanism itself.

What changed in this pass: `references/playbooks/17-native-register-and-ai-detection.md`'s
R1 was extended to state the boundary explicitly and explain why; R2 was
rewritten from a numeric target table ("directional targets: CV 0.50-0.75,
short-sentence share 20-30%...") into a pure monotony-diagnostic with no
target band; §2.4 was rewritten to lead with the adversarial-robustness
finding as the reason for that boundary, not a footnote; the Sources entry
for Liang et al. now flags this specifically. `scripts/measure_prose_rhythm.py`
was rewritten to match: the `TARGET_CV` / `TARGET_SHORT_PCT` / `TARGET_LONG_PCT`
constants and the LOW/HIGH/ok verdict against them were removed and replaced
with a monotony-only flag that has no "correct" band to report against.
R3-R7, the "what NOT to do" list, and the honest-limits section were kept
as-is: none of them depend on the target-zone mechanism, and R1's evidence-
contract rule, the humanizer-tool prohibition, and the frozen-section
discipline are sound regardless of this correction. Playbook 18 was
re-checked against this skill's own generalization standard (the same test
`references/provenance.md`'s earlier entries already state and playbook
13's automated test already enforces) and found to already meet it after
v4.6.1's rewrite — no further change made there.

## Correction notes carried over from source auditing

1. **Lecture 11 / bonus-lecture filename swap**: in the originally collected
   archive, the slide PDFs of 第十一讲 and 第十一讲前加餐 had swapped
   filenames. Pairing was corrected by PDF title-page content: the 20-page
   deck is 第十一讲, the 9-page deck is the 加餐.
2. **Lecture 12 slides**: missing from the original archive; obtained from
   the official course link (`static/13.pdf`).
3. **Official numbering quirk**: on the course page, the bonus lecture's PDF
   is `12.pdf`, lecture 11's is `11.pdf`, lecture 12's is `13.pdf`.

## Integrity checksums of the original slide PDFs

SHA-256 checksums of the source decks used for reconstruction (for
verification against your own downloads):

<!-- CHECKSUMS:BEGIN -->
| 讲次 | SHA-256 (official slides PDF) | Size (bytes) |
|---|---|---:|
| 第一讲：学术研究与英文学术论文写作概述 | `d154619ac833b9665ccefe28069565150d9a77f2cea2976c014b334dd7e5f356` | 30717561 |
| 第二讲：英文学术论文之写作思路——立意和标题 | `6dcb9eb583ae2356ac0aea79f788ce7919611d2a813ea27de7f1b09d792c5585` | 4421934 |
| 第三讲：英文学术论文之写作思路——摘要和引言 | `a93ee6e9617fca1586979c4d667340ed929f36402cbb754d0463afb859662466` | 8658897 |
| 第四讲：英文学术论文之写作思路——相关工作和方法 | `73cb3d4055ef72554f1f8b660c576bfab7507aae83da68c1e40dcfef96f9b6af` | 7743093 |
| 第五讲：英文学术论文之写作思路——实验、结论和参考文献 | `c8592fd0ce9c4ad3535a2e9490f7463cd64299f460d824b6c90d8fd5ba4b724d` | 10921031 |
| 第六讲：英文学术论文之写作思路——研究动机图绘制 | `853b2b0f442605d7b4439ddc6657bf8e5ef93a70e83a1252d0f2846f8150e6c7` | 10511345 |
| 第七讲：英文学术论文之写作思路——模型框架图绘制概述 | `17d8cb20beac2f5f644fabd306dcf00501b0dfe2581295f78b871a5ca86d977f` | 10231547 |
| 第八讲：英文学术论文之写作思路——模型框架图绘制延伸 | `0a49e49cfc306fbfbf912b99a2c9da6a2a766502911cf05468884b87edfbc337` | 5209184 |
| 第九讲：英文学术论文之英文规范——如何做到简洁与严谨 | `e2ac8126b3c8ecba9d1c868b171b9d5ee5c57fe1568bbf7d66ce73ef542e710e` | 3898008 |
| 第十讲：英文学术论文之英文规范——术语、符号、图表、文献规范 | `4bc6852360b72890fedee601e0e9d80695e675e3c88e88acf163674883e1b6ed` | 20988006 |
| 第十一讲前加餐：思考创新性研究点前务必知道的那些事儿 | `dd3c5a81f483ddda55720be8f7c19300594eacb11013cb3565f6bf38cccb896b` | 19780904 |
| 第十一讲：学术研究之创新性研究点——从哪些角度思考创新性研究点？ | `775dd7f7e6f6fba7dfc01e12f3fa7937f345b20e6f088cd84db5abd845dbaa42` | 10033683 |
| 第十二讲：学术研究之创新性研究点——如何找论文与进行文献调研？ | `814f4ff8116ddeac38b12ad3c033d0e33c330e3d7fa534be12c46651355a1e51` | 26752751 |
<!-- CHECKSUMS:END -->
