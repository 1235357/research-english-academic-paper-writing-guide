# Submission-Sprint Discipline: Frozen Baselines, Concurrent Editors, Venue Forms

> **Provenance note.** No lecture in Yu Jing's course covers this. It is
> **this skill's own extension**, distilled from real submission-sprint
> experience in which most of the wasted effort came not from writing
> quality but from process failures in the final 48 hours. Cite it as an
> extension, not as a transcribed lecture point.

> **Generalization discipline** (the same commitment playbooks 13–17 make,
> restated here because it governs this file specifically): every numbered
> rule below must hold for *any* submission sprint, not one project. Where a
> section includes an "Illustrative case," that case is bounded and
> optional context for *why* the rule exists — it is never the rule's
> scope, and its specific numbers are not targets to reproduce. If a future
> edit to this file only makes sense given one specific paper's numbers,
> that is a defect — generalize it or move it out of this skill.

The course ends at "the paper is written." Real submissions end 48 hours
later, after layout wars, concurrent editors, and a venue form nobody
re-read. Those hours destroy more value than prose quality does.

---

## 1. The frozen-baseline rule (the single most expensive lesson)

**When an author says a version is approved, satisfied, or frozen, that
version is a baseline. Do not touch it except for work the author
explicitly names.**

This holds even when an automated check flags something on the frozen
version. A check can be correct about *what* it detected and wrong about
what that detection *means*: a tight column, a `trim/clip`, a 1pt gap can
each be a considered trade-off a human made deliberately to fit a hard page
budget, not a defect to fix. Treating every finding a linter produces as a
mandate — rather than as one input for a human to weigh — is the single
most expensive category of error a submission-sprint agent can make,
because it spends effort undoing a decision that was already correct, and
it can consume hours an author does not have left to notice and revert.

**Illustrative case:** on one project, an author confirmed satisfaction
with a collaborator's layout work; an automated audit subsequently reported
several "failures" on that exact version, which were then "fixed" without
checking back first. Every one of the audit's findings turned out to be a
deliberate space-saving trade-off the author had already made on purpose.

### Operating rules

- **R1.** An approved version is read-only. Increments must be named by the
  author, not inferred from a linter.
- **R2. A failing check is a report, not a mandate.** Surface it, quantify
  it, say what fixing it would cost — then stop and ask. Never let a tool's
  opinion silently override a human's already-made decision.
- **R3.** Look for approved-snapshot naming (a filename carrying a version
  tag or date) before editing. Its existence means someone froze that state
  deliberately, whether or not the project uses formal version control.
- **R4.** Never weaken a project's own compliance gate to make an artifact
  pass it. If a gate is relaxed even temporarily to accommodate one change,
  track the relaxation explicitly and revert it in the same pass that
  reverts the change — an untracked relaxation can silently outlive the
  reason for it. If a gate seems wrong on its merits, escalate it; do not
  quietly edit the ruler to fit the measurement.

---

## 2. Concurrent editors on an unversioned manuscript

Paper directories are frequently **not** under version control while
several people and agents edit them at once. Every rule in this section
follows from one fact: without version control, "who changed what, and
why" is not recoverable after the fact unless you capture it *before* the
next edit lands on top of it.

- **R5.** Check file-modification time and diff against your own
  last-known state *before every edit session*. A concurrent pass by
  someone else, made in good faith to fix one thing, can silently revert
  several others in the same window — including substantive content, not
  only formatting. Diffing before you start is the only way to catch this
  before you build on top of a silent regression.
- **R6.** Never let two agents write the same file concurrently. Give each
  a disjoint file, or have them return **exact old→new patches** for one
  owner to apply serially.
- **R7.** Diff every concurrent change before accepting it wholesale.
  Reverts arrive bundled with genuine improvements in the same diff; you
  must separate the two, not accept or reject the whole thing on net
  impression.
- **R8.** When you find your own work overwritten, verify the *reason*
  before restoring it. Not every revert is a mistake — a value can have
  been correctly deleted because it disagreed with its receipt, even while
  other, unrelated content was wrongly removed in the same pass.

---

## 3. Receipts, and the two failure modes that survive them

A receipt discipline — every reported number traceable to a generated
file, never hand-edited — is necessary, and catches most fabrication and
transcription errors by construction. Two classes of error survive a
receipt discipline that is otherwise being followed correctly, and both are
worth checking explicitly rather than assumed away.

### 3.1 Superseded receipts

A receipt is a snapshot at the time it was generated; if the underlying run
is repeated or corrected later, an old receipt can still be sitting in the
same location, indistinguishable at a glance from the current one.

- **R9.** When two receipts exist for the same result, compare `generated`
  timestamps and per-source provenance *before* using either — do not
  default to whichever was found first. A `_v2`, or any version-like suffix,
  in a filename is a warning to check, not a detail to skip past.

**Illustrative case:** two receipts existed for one experiment. The one
found first was used; a second, generated ten hours later with fuller
per-seed provenance, held a materially different value. Nothing about
either file's name or location made this obvious without opening both.

### 3.2 Rounded intermediates in derived figures

A derived quantity — a ratio, a speedup, a percentage change — computed
from an already-rounded intermediate value can differ materially from the
same quantity computed from the unrounded source, and the discrepancy is
invisible unless someone recomputes it from the source numbers directly.

- **R10.** Compute every derived quantity from unrounded sources, and use
  one rounding convention consistently for every derived number in a single
  table. Mixed rounding conventions inside one table — some entries clearly
  computed from rounded intermediates, others from exact ones — are the
  tell that this happened.

**Illustrative case:** a headline ratio was published as roughly double
digits higher than its correct value, traced to one division that used a
rounded intermediate instead of the exact source value; a sibling number in
the same table, computed correctly, made the inconsistency detectable once
someone checked both derivations side by side.

---

## 4. Attribution integrity: the charge that is not about performance

A wrong number is a performance defect. A description of *what a result
represents* that is inconsistent between two documents in the same
submission package is an integrity defect, and it is far more damaging to
a paper's credibility than a weak result — because a reader who notices it
stops trusting every other claim in the package, not just the one sentence
that was wrong.

This defect is specifically dangerous because it is **invisible within
either document read alone** and only appears when a reader cross-references
the main paper against the supplement, the code release, or both. Nothing
about either document individually looks wrong.

**Illustrative case:** a main-paper table footnote described a baseline in
wording that reads as "we reproduced and improved a specific cited system,"
while the supplement stated plainly that no external method had been
reproduced — the row was in fact the authors' own system, built to follow
the same general paradigm as the cited work, not a port of its code. A
reader of the main paper alone would conclude a reproduction was run; nothing
in the main paper contradicted that reading on its own.

- **R11.** For every baseline, state explicitly which of these is true:
  (a) we ran the original authors' code, (b) we reimplemented their
  published method ourselves, (c) we built our own system that follows
  their general paradigm without reproducing their specific method. The
  wording must match across the paper, the supplement, and any code
  release — not merely be individually defensible in each.
- **R12.** Phrases like "enhanced SOTA," "adapted," or "matched baseline"
  are ambiguous by default between the three categories in R11. Attach the
  specific claim explicitly; often the fix is a single added word that
  moves the claim from implementation-level to paradigm-level, or vice
  versa, to match what was actually done.
- **R13.** Before submitting, search the supplement specifically for
  sentences that could contradict main-paper attribution language. This
  class of defect is undetectable by reading either document in isolation.

---

## 5. The venue form is part of the paper

A submission platform's own form fields — abstract, TL;DR, title — are a
separate copy of that content, not a mirror that updates itself. Once the
manuscript's abstract changes, the form's copy is stale until someone
re-pastes it, and nothing prompts that step automatically.

- **R14.** Treat the submission form as a reviewed artifact in its own
  right. Diff its abstract against the compiled PDF's abstract, verbatim,
  as a required step before submitting — not as an afterthought once the
  PDF is finalized.
- **R15.** Any terminology change made in the manuscript — a renamed
  method, a term an advisor asked to be dropped — must be swept through the
  form fields too, not only the manuscript body. A reviewer who searches
  for a term and finds it in the form but not the paper, or vice versa,
  sees an inconsistency the authors should have caught.
- **R16.** Check every checkbox attestation on the form for items only a
  human can verify — co-author profile completeness, conflict-of-interest
  declarations, and similar. An agent cannot confirm these are true and
  must say so explicitly rather than let them pass silently; at some
  venues, an incomplete attestation is grounds for desk rejection on its
  own, independent of the paper's content.

---

## 6. Layout is measurable; stop eyeballing it

Recurring layout defects are caught reliably only by measurement — reading
a rendered page, or trusting a page-level summary statistic, misses defects
that a per-column or per-element measurement catches directly.

- **R17. Measure per column, not per page.** A page-level "last content
  position" reading can look full while one column specifically holds a
  large unused gap, because the *other* column is full and the page-level
  average hides the imbalance. (Illustrative case: a page-level reading
  showed no problem while one column alone held roughly 140pt of unused
  space.) Compute the last content position for each column separately.
- **R18. Detect column or text-span collisions numerically, not visually.**
  Merge text spans whose gap falls below a small threshold (on the order of
  half a point) and flag any merged span that contains two or more separate
  numeric values. (Illustrative case: three distinct numbers rendered
  visually adjacent had fused into one unreadable digit string that no
  compiler warning reported and that corrupted any attempt to copy the
  text.) This class of defect does not show up in a compile log and is easy
  to miss on a quick visual pass.
- **R19. Measure table fill ratio** against the available text-block width,
  rather than eyeballing whether a table "looks full." A table sitting
  meaningfully under 100% fill is wasting width that could carry another
  column or a wider caption.
- **R20.** Verify the *content/references boundary* explicitly: which page
  does the bibliography actually start on? A page-count limit that applies
  only to content, not references, can be silently violated even when the
  total page count looks compliant.
- **R21.** After any float or spacing change, re-render and inspect the
  actual output — do not assume a fix held. The same layout defect can
  regress more than once across a sprint if a later, unrelated change
  touches the same region.

---

## 7. Sequencing under a hard page limit

Late in a sprint, the page budget becomes the binding constraint on nearly
every other edit. The rules below follow from treating page budget as a
resource to measure and allocate, not a constraint to discover by
surprise.

- **R22.** Measure the actual slack before making edits: how many
  characters of net change can be absorbed before a page boundary flips?
  This figure is specific to the current layout and will differ across
  papers and even across drafts of the same paper — measure it fresh each
  time rather than assuming a prior value still holds.
- **R23.** Prefer **substitution over addition** under a tight budget.
  Replacing a long phrase with a shorter one that points to more detail
  elsewhere (a cross-reference, an appendix pointer) buys space while
  preserving — or adding — content, rather than only cutting it.
- **R24.** Freed space is not automatically a win; it is a hole until
  something fills it deliberately. Shortening one section can silently pull
  unrelated content (such as the reference list) onto a content page in a
  way that changes what counts against a content-page limit. Refill freed
  space with the strongest available material rather than leaving it as an
  unplanned gap.
- **R25.** Do the rhythm/register pass (Playbook 17) **last** in the
  sequence. It is usually net space-neutral-to-shorter, so doing it last
  perturbs an already-tight layout the least — but verify page count
  afterward regardless of expectation.

---

## 8. Positioning: main paper claims, supplement explains

Where a limitation is placed, and how many times it is repeated, changes
how a reader weighs it — independent of whether the underlying fact is
disclosed at all. The general principle: the main text should carry the
paper's strongest, most complete case for its contribution; a limitation
belongs in the location where it is most informative, generally the
supplement, explained as a structural property of the setting rather than
restated as an apology; and it should be stated once, not scattered
through the paper as if instinctively hedging. This is not a license to
hide a result — every fact stays in the paper. What changes is location,
repetition, and voice, never presence.

- **R26.** State each limitation **once**, in its single most informative
  location. A result that falls below a benchmark floor, repeated
  separately in the abstract, introduction, results, and conclusion, reads
  as anxiety rather than honesty — and dilutes the one place a careful
  reader would actually want the full explanation.
- **R27.** Where a limitation is explained, explain it **mechanistically**
  — as a property of the method or setting, not as a confession. "The
  approach cannot recover an exact boundary because its scoring function
  takes the mean of two endpoint estimates, so the arg-max is always a
  single point" is a structural fact a reader can evaluate. "Our
  localization is weak" is a value judgment that invites the reader to
  simply agree with it.
- **R28.** Deleting a limitation entirely, so that it appears nowhere, is
  out of bounds regardless of page pressure. Moving it to its single best
  location, and stating it once, is the correct move; removing it is not
  an option R23's "substitution over addition" licenses.
- **R29.** Do not report a negative or null control as an empirical finding
  when it is actually a structural identity of the architecture. A control
  that returns identical results under a manipulation that should matter
  (for example, an input reordering) can indicate the manipulation was
  provably inert for that architecture — a fact about the design, not a
  discovery about robustness. Publishing the null result as a finding
  invites a careful reviewer to derive the identity independently and
  conclude the authors mistook a tautology for a result.
