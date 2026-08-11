# Table Taxonomy and Layout

> Task playbook for deciding which tables a paper needs, what each one's job
> is, and how to lay each one out — a companion to
> `14-figure-schema-and-rendering-gate.md`, not a duplicate of it. This
> content is external to Yu Jing's course (see Provenance) and was added by
> explicit user request after a real advisor session spent most of its time
> restructuring one paper's table set.

## Core rule

A fast reader — a rushed reviewer skimming for a first impression, and
explicitly also an AI-assisted review pass — does not absorb a paper by
reading every sentence and every reported number. They absorb it by
scanning the figures and tables and asking whether those alone communicate
what the paper is doing and why it's credible. This is not a cynical
shortcut particular to lazy reviewers; it is the actual, dominant read path,
confirmed directly in a real advisor session (see Provenance): "如果我把这
个图遮住，我看这东西有什么用啊？我没这些图，我纯这种数值，就是你现在的文
章内容，我看不懂啊" ("if I cover up this figure, what use is this thing? Without
these figures, purely these numbers — that's your current paper's content
— I can't understand it"). Table design is not secondary polish on top of
"the real content" — for a fast reader, the tables and figures *are* the
content that actually gets read carefully. Under-investing in table design
relative to prose is therefore a real risk, not a matter of taste, and is
exactly the gap this playbook exists to close: a paper's technical
substance can be fully sound and still under-perform on this axis if the
tables don't carry it.

**The purpose test — apply to every table before keeping it**: ask directly
what this specific table's job is. If the honest answer is "no clear
purpose" or "it seemed like it should be here," cut it or fold its useful
rows into a table that does have a clear job. A real example of this test
in action: a comparison table using a prior, easier-protocol method's
self-reported numbers was kept in a paper with no clear reason: once asked
"what is the point of including this," the honest answer was "no real
purpose," and the fix was either to cut it or repurpose it with an explicit,
narrower job (see "Cross-protocol tables" below) — not to keep it by
default because removing a table feels like a loss.

## Table taxonomy: match the table type to the section's job

A paper introducing a new task, benchmark, or dataset typically needs
several *structurally different* tables, not several copies of the same
format with different numbers in them. Using the wrong type for a section
is a common, avoidable failure:

1. **Positioning / survey table** (typically Table 1, referenced from both
   Introduction and Related Work). Compares the paper's setting against
   prior settings on a small set of defining properties (e.g. does the
   setting require self-retrieval? window localization? a legal/redacted
   query?). Checkmarks (✓/✗) are the *right* choice here — the table's job
   is a qualitative capability comparison, not a results comparison, and a
   checkmark is the correct information density for that job. This table's
   deeper purpose is to set up a later results table's own row
   categorization — pick the category labels here deliberately, since a
   later table will inherit them.
2. **Dataset composition / characteristics table**, usually paired with a
   distribution chart (a pie chart is the most common choice, though any
   real proportion chart works) rather than standing alone. The chart
   answers "what is the overall composition of the benchmark" at a glance;
   the paired table answers "what are the actual attributes and their
   values for each piece of it." **Checkmarks are the wrong choice here** —
   this table's job is to convey real characteristics, not yes/no
   properties, so a bare ✓ that doesn't reveal an actual attribute value or
   distribution fails the table's purpose even if it looks tidy. A row a
   reader cannot interpret without asking someone should be cut, not left
   in for completeness.
3. **The benchmark-defining table** (the paper's actual headline evidence
   — the table that argues the new method or task needed to exist at all).
   Its job is narrower than "show results": it must demonstrate that prior
   methods, actually forced to attempt the new setting, fall short. That
   requires two things most drafts skip past: **(a)** each cited prior
   method has to be genuinely adapted or extended into the new setting first
   — this is a real research step, not a table-formatting step — and **(b)**
   the axis that carries this table's argument is *how many different
   adapted methods* are shown side by side, not *how many datasets*. See
   "Which axis carries the argument" below — this is the single most
   commonly misjudged table in a benchmark paper, worth its own subsection
   rather than a bullet.
4. **Cross-protocol reference table** — see "Cross-protocol tables" below;
   always separate from the main benchmark table, never merged into it.
5. **Ablation table(s)**. Playbook 05 already covers ablation *content*
   (organize by dimension, prove necessity and synergy); this playbook adds
   the layout discipline (below) and one content-completeness check worth
   restating here because it recurred directly in a real session: an
   ablation table is frequently *judged incomplete* by a careful reviewer
   for missing exactly the things that are cheap to add and expensive to
   omit — hyperparameter settings, a swapped-backbone/encoder control, and
   a loss-convergence or qualitative visualization sitting next to the
   numbers. Treat "did we ablate enough, and can a reader see the
   hyperparameters used" as a standing question every time this table is
   reviewed, not a one-time checklist item.

## Which axis carries the argument: methods, not datasets

A benchmark-introducing paper's central table is answering one specific
question: *why couldn't an existing method just do this?* That question is
answered by breadth of adapted prior methods shown failing under the new
setting's actual demands, not by breadth of datasets the paper's own method
happens to run on. Conflating the two is a natural, tempting mistake — more
datasets and more GPU-hours running every combination *feels* like more
rigor — but it does not carry this specific table's argument, and chasing
it can crowd out the table that actually would.

**The worked example** (verified directly against the actual paper, not
recalled from memory): Li, Weng, Sun & Li, "Learning to Locate Visual Answer
in Video Corpus Using Question" (already this playbook's and playbook 14's
caption-minimalism source) makes exactly this move in its own Table 1. The
new setting (retrieving an answer from a corpus, not a single given video)
didn't exist as a fair test for prior single-video methods, so the authors
did the adaptation work themselves: four *native* baselines spanning
visual-based, textual-based, and cross-modal method families (VSLNet, ACRM,
Span-Base, VPTSL), then the same four again wrapped with a BM25 retrieval
front-end, then the same four again wrapped with a DPR retrieval front-end
— twelve adapted-baseline rows from four underlying methods, plus the
paper's own method as a thirteenth — **all evaluated on one dataset**
(MedVidCQA), not spread across many. Method breadth (four base methods ×
three retrieval conditions) is what makes the table's argument legible at a
glance; the dataset axis stays deliberately narrow so the method comparison
isn't diluted across it.

**The anti-pattern this corrects, stated plainly so it's recognizable**: the
instinct to read "we need a strong benchmark-defining table" as "run every
available method across every available dataset, maximize compute
utilization, and let the resulting table demonstrate thoroughness through
sheer size." That instinct produces a table that is wide in the wrong
dimension. If a paper already has a separate, genuine dataset-breadth
contribution (e.g. "we built a unified benchmark from eleven diverse
sources"), that breadth deserves its own table (the main-results-by-dataset
table in the taxonomy above) — it does not also need to host every adapted
baseline method, and the benchmark-defining table does not need to run on
every one of those eleven sources to make its point. Two different
arguments, two different tables, each narrow on the axis the other one
carries.

**Where the adaptation work actually has to happen**: forcing a prior
method built for an easier, evidence-given setting to attempt a harder,
retrieval-required one is a real methods contribution in itself (pairing it
with a retrieval front-end, as CCGS did with BM25/DPR, is one concrete
pattern) — usually most feasible on whatever narrow, tightly-controlled
diagnostic scope a paper already has for its own ablations (see the
ablation-table entry above), rather than requiring the full dataset roster.
Building this table is a research task to plan for early, not a
table-formatting pass to do once results already exist — it changes what
experiments need to be run, not just how existing numbers get displayed.

**Skim-test connection** (playbook 16): a reader looking at only this table
should see, without reading a word of surrounding prose, that several
genuinely different prior approaches were tried and fall short, and that
the paper's own method does not. That story is told by row diversity, not
column count — a wide table of eleven dataset columns for one method proves
robustness, not necessity.

## Column discipline: collapse before you explode

A benchmark spanning many datasets, each evaluated on multiple metrics and
multiple task variants (e.g. a short-horizon and long-horizon setting),
produces a column count that multiplies fast: 11 datasets × 2 task variants
× 2 metrics is 44 columns before anything else is added. This is a real,
recurring failure mode, not a hypothetical one. Two disciplines address it,
in order of preference:

1. **Collapse to one headline metric per dataset column.** If the paper
   already has a single strict metric that best captures "did this fully
   succeed" (as opposed to a partial-credit or component metric), use that
   one metric in the main cross-dataset table and move the other metrics to
   a supplementary table or the per-dataset detail table. Do not report two
   metrics per dataset column "just in case" if one metric already
   subsumes what a reader needs from this specific table.
2. **If the table still cannot fit, resize it, don't truncate it.** A wide
   table can span both columns of a two-column layout (rather than staying
   single-column and getting cramped), and its font/cell size can be
   mechanically shrunk (LaTeX's own table-scaling commands handle this) — do
   this before cutting rows or datasets to make a table fit. A single-column
   detail table (e.g. the per-method-detail table that a benchmark's Table 1
   sets up) is the right default for anything that is *not* the main
   headline comparison, to leave column-spanning treatment available for
   the table that actually needs it.

**Missing-capability cells get a dash, not a blank or an omission** — but
confirm the method genuinely cannot support that column before using the
dash. If a method could plausibly be adapted or simulated to produce a
(weaker, honestly-labeled) number for that column, do that instead of
defaulting to a dash for convenience; reserve the dash for cases that are
genuinely inapplicable, and say so if asked why a specific cell is a dash
rather than a number.

**Secondary annotations get a superscript, not a new row or column.** If a
handful of cells need a caveat (e.g. "this method's original release lacks
one specific supervision signal"), mark those specific cells with a
superscript symbol and explain it once in the table's footnote — do not add
a whole extra row or column to carry information that only applies to a
few cells.

## Cross-protocol tables: never silently merge

If a comparison table's numbers come from a *different* evaluation protocol
than the paper's own headline setting (for example, numbers self-reported
by prior work under an easier, evidence-already-given protocol, being shown
alongside a harder, evidence-must-be-retrieved protocol this paper
introduces), that comparison must live in its own, clearly-labeled table —
never merged into the paper's own benchmark table as if the numbers were
earned under the same conditions. State explicitly, in the table's own
caption or the surrounding prose, that these are reference-only numbers
under a different protocol, not a ranked comparison. This is a
comparability/integrity requirement, not a formatting preference: a reader
who cannot tell that two columns were measured under different rules can be
actively misled about what the paper's own contribution demonstrates.

If it's useful to also show how the paper's own method performs under that
easier, prior protocol (e.g. to show the method degrades gracefully rather
than only to inflate a number), that is a legitimate, separate thing to
show — as its own row in that same separated table, framed modestly (e.g.
"can also operate under the prior, easier protocol, though not tuned or
guaranteed to lead there") rather than presented as an additional win.

**A note on suspiciously large gaps over baselines.** A real advisor
session raised a version of this concern directly, cautioning against a
reported improvement that looks implausibly large, on the reasoning that an
oversized gap reads as suspicious (possibly overfit or the result of an
unfair comparison) to a reviewer. This skill adopts the underlying,
legitimate form of that concern rather than the literal instruction:
**investigate an unusually large measured gap before reporting it** — check
for a bug, an unintentionally unfair baseline setup (mismatched budget,
undertuned baseline, data leakage), or a genuinely narrow condition under
which the gap holds — and be ready to explain, in the prose, *why* the gap
is real and that size. What this playbook does not endorse is adjusting a
genuinely-measured result to make it look more modest for credibility
alone; if a large gap is real and its cause is understood, report it
honestly and explain the mechanism, consistent with this skill's existing
honesty requirements (`04-related-work-and-method.md`,
`05-experiments-conclusion-references.md`).

## Appendix vs. main text: comprehension beats completeness

Under page pressure, the instinct is to move content to the appendix to
make room. The wrong content gets moved, routinely: "你附录放了很多，但不
一定会看附录，所以你要把附录东西移到正文" ("you put a lot in the appendix,
but people don't necessarily read the appendix, so you need to move
appendix content into the main text") — and, more sharply, "该出现的内容
没有出现，不该出现内容你反而在附录出现了，有点本末倒置" ("content that
should appear didn't appear; content that shouldn't need to appear [in the
main text] instead appeared in the appendix — that's backwards").

**Priority order when trimming for space** (cut from the bottom of this
list first, never the top):
1. Hyperparameter settings, key ablations, and any qualitative/visualization
   figure that lets a reader sanity-check a claimed result — these stay in
   the main text even under pressure, because a reader who never opens the
   appendix should still be able to verify the paper's central claims.
   These are also close to the least visible items to cut, because their
   absence teaches a reviewer nothing except that a table looks
   incomplete — see the ablation-completeness check above.
2. Detailed per-dataset breakdowns, secondary metrics, and extended
   discussion — natural candidates for a single-column detail table or a
   supplementary section, cross-referenced from the main text.
3. Derivations, proofs, and exhaustive construction details — the correct,
   lowest-cost material to move to an appendix, since a reader can follow
   the paper's argument without reproducing the derivation themselves.

**When a table or figure won't fit and something has to give, adjust
scope, not comprehension.** A real advisor session stated this ordering
directly, in the context of a paper's Method section running long: get the
tables and figures (the harder-to-retrofit, page-expensive layer) into
their final shape *first*, then write or trim the Method prose to match
what the actual experiments and figures can support — including, if
necessary, narrowing a claim to match an experiment that exists rather than
promising an experiment that doesn't ("你要补这个实验，但你没这个实验，那我
就把方法改成没有这个实验" — "if you need to add an experiment you don't have,
adjust the method to not require it"). This inverts a common default
instinct (finalize the prose, then fit visuals around it) and is worth
naming explicitly so it doesn't get silently skipped: tables and figures
are not decoration applied after the technical content is locked, they are
part of deciding what the technical content can honestly claim.

## Table-figure correspondence

A results table and a nearby qualitative/visualization figure should use
the *same* category and method labels, not paraphrased or re-abbreviated
versions of each other. If a table's row categories are named one way and
a figure discussing the same categories uses different wording, a reader
has to do translation work that a well-designed pair would not require.
When a paper's task has enough internal structure that a single
Introduction-level motivation figure cannot carry it alone (e.g. a
multi-stage or multi-round task), consider a second, dedicated
task-structure figure positioned near the Experiments section, re-grounding
the reader visually right before the results tables — not a duplicate of
the motivation figure, but a closer, more mechanism-level illustration that
the results tables can then visibly reference.

## Provenance

Every claim in this playbook traces to one real advisor session (verbatim
transcript supplied by the user), cross-checked against this paper's own
two draft versions supplied in the same and an earlier turn — not to Yu
Jing's course, which does not address table taxonomy or layout at this
level of specificity. See `references/provenance.md` for the full session
note. Treat this playbook the same way as
`14-figure-schema-and-rendering-gate.md`'s external content: correctly
attributed to a real working session, not presented as a transcribed
course rule if a user asks where it comes from.
