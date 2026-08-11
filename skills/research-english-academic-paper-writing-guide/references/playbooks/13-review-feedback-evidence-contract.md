# Reviewer Feedback, Evidence Contracts, and Submission-Safe Revision

> Task playbook for advisor or reviewer comments that change a paper's claims,
> experiments, tables, citation surface, code release, or submission posture.

> **Generalization discipline**: this playbook extends beyond the course
> itself, distilled from real paper-submission experience. Every rule below
> is written and reviewed to hold for *any* research paper, not one project
> — a "live case" or numeric example inside a rule (e.g. under "Full-scope
> validation before a blanket methodology claim") illustrates the rule, it
> is never the rule's scope. If a future revision to this file only makes
> sense for one specific project or dataset, that is a defect: generalize it
> or move it out of this skill.

## Operating principle

Reviewer feedback is not a sentence-level to-do list. Treat it as a request to
reconcile five surfaces before revising prose:

```text
claim -> evaluation contract -> code path -> result artifact -> venue policy
```

If one link is missing, narrow the claim or run the missing experiment. Never
repair an evidence conflict by changing only the wording.

## Mandatory triage

1. Transcribe each comment into a requirement with an exact source location.
   Keep the reviewer's words separate from author interpretation and from the
   proposed response. A request inferred from an image or annotation is not a
   verbatim reviewer requirement.
   When source files permit it, extract native annotation objects before using
   a transcript or student-authored summary. Record author, creation time,
   page or paragraph anchor, object ID, and exact text. Treat screenshots and
   summaries as secondary evidence unless they can be matched to those objects.
2. Classify it as a claim, method, result, table/figure, citation, release, or
   venue-policy requirement.
   Mark conditional or ambiguous feedback as optional or pending confirmation;
   do not silently promote it to a mandatory reviewer request.
3. Make a **claim ledger** before editing. Each row must name: the sentence or
   table cell, metric, split, seed count, evaluation contract, code entrypoint,
   result/log path, and the required revision.
4. Resolve P0 conflicts first: leakage, unsupported result, incompatible
   protocol, wrong dataset metadata, stale compiled artifact, broken citation,
   anonymization, or a venue-policy violation. Style work comes later.

Use this minimum claim-ledger schema. Add project-specific columns only after
these evidence joins remain explicit:

| Claim or table cell | Metric or event | Split | Seed and checkpoint selection | Evaluation contract | Code entrypoint | Result artifact | Required revision and status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Exact manuscript location | Implemented event and denominator | Named evaluation split | Seeds, selected epoch, score, and tie rule | Observable inputs, oracle access, horizon, and aggregation | Reproducible command or function | Immutable full-precision row or log | Narrow, rerun, exclude, or verified |

Permission is not evidence. An advisor's approval to use a model name, claim,
or release wording does not establish that the implementation or experiment
supports it. Configurations, logs, checkpoints, and result artifacts establish
experimental facts; venue documents establish submission policy.

### Review-artifact identity ledger

Before marking a feedback item resolved, record the reviewed artifact hash,
page, native annotation ID, author/time, highlighted text, exact comment,
source revision or commit, current source lines, rebuilt PDF hash, and
resolution status. A comment mapped only through similar wording is `mapped`,
not `resolved`. If the reviewed PDF and current source come from different
builds, report the drift explicitly and re-check the rebuilt PDF before
closure.

## Contract discipline

Do not mix incompatible evaluation contracts in a headline, average, ablation,
or conclusion. Two eligibility rules can both be valid (for example, a route
that commits to one evidence instance before downstream scoring, versus a
route that fuses evidence globally before scoring) while still answering
different questions. State exactly what reaches the downstream stage at
inference, and label every result table with that contract.

For a task whose headline metric is a joint success over a conditioning event
and a conditioned event, use the matching decomposition:

\[
\Pr(\text{headline success})=\Pr(E\cap P)=\Pr(E)\Pr(P\mid E),
\]

where \(E\) is the stated conditioning event (for example, correct evidence
selection) and \(P\) is the stated conditioned event (for example, a correct
downstream prediction given that evidence). Do not substitute a
conditioned-only, oracle-conditioned, train-cache, unconditioned, or
multi-positive diagnostic for the declared headline contract.

## Table and citation rules

- Every dataset, method, and metric source named in a table needs a citation at
  first appearance. Do not hide sources behind “and related sources.”
- Use one row per dataset or method when the row makes a distinct provenance,
  construction, coverage, or result claim. Do not group names to make an
  incomplete evaluation look complete.
- Never write “and related sources” in a claim-bearing table. Name and cite
  every included source, or remove it from that table.
- Use checkmarks only for binary, defined properties. Put nuanced construction
  details in the text, caption, or a dataset card.
- Define every checkmark, cross, dash, boldface, underline, and best/second-best
  convention in the caption or table note. A dash must mean one declared state,
  such as not reported or not applicable, never an ambiguous mixture.
- Captions state inputs, contract, split, seed/statistic, metric definition,
  comparability limits, and whether a value is a diagnostic.
- Separate native benchmark results, converted external coverage, and published
  reference-only numbers when their features, labels, splits, or protocols
  differ.
- Do not turn a source paper’s table layout into a source of copied claims,
  numbers, or wording.

### Comparison eligibility

Before placing a published or newly collected value in the same result block,
classify it as **comparison-eligible** only when the task output, observable
inputs, split, horizon, features, supervision, oracle information, metric
definition, and aggregation statistic are compatible. If any field differs,
put the number in a clearly labeled reference-only block or omit it. Do not use
boldface or ranking across incompatible contracts.

For a benchmark spanning many sources, maintain a dataset-coverage matrix. It
must show one status for every source: completed comparable result, completed
diagnostic, reference-only, blocked with reason, or not yet run. Missing values
stay explicit. They never become inferred values or disappear through row
grouping.

### Checkpoint-coherent result rows

A reported model row must be a **checkpoint-coherent row**. Apply the declared
checkpoint-selection rule once within each seed and read every metric for that
seed from the same selected epoch and artifact. Never assemble a row from
per-metric maxima, mix one metric's maximum with the headline metric from
another epoch, or join metrics from incompatible caches, label vocabularies,
budgets, or model states. Such a composite describes no evaluated checkpoint.

For a paired intervention, align paired seeds, candidate sets, validation
examples, selection rule, and repetition count. Report missing paired seeds
explicitly; do not average an unpaired condition into a paired delta. When a
selection metric has a zero-score tie or any other tie across epochs, apply the
predeclared deterministic tie rule and disclose the tie. A zero-score tie does
not provide informative model selection merely because an epoch can be named.

Prefer machine-readable, full-precision result ledgers. If a seed has only a
rounded console log, do not combine it with full-precision JSONL records to
claim an exact mean or standard deviation. Recover the immutable artifact or
rerun the evaluation. Otherwise label the value as rounded and incomplete.
Keep a ledger with run path, seed, selected epoch, selection score, tie rule,
sample count, and the exact source row for every table cell.

The metric name must match the scored event. For example, an exact-selection
plus exact-downstream-outcome success is not also a localization metric. If
the paper claims selection, localization, and downstream success jointly,
report a localization-gated conjunction (name it explicitly, e.g.
Success@IoU-$\tau$) and define its denominator and threshold. Do not expand
the prose definition of a legacy metric without changing the implementation,
table label, and result artifact together.

### Full-scope validation before a blanket methodology claim

A methodology sentence in the main text ("we use encoder/backbone/component
X") is a claim about every reported number, not just the subset that was
validated when the sentence was written. Component-swap equivalence measured
on a handful of cells does not transfer to the remaining, unvalidated cells --
even with an explicit collaborator sign-off to state the swap in writing, and
even when the tested subset showed sub-1pp, statistically indistinguishable
results. A live case: a text-encoder swap tested equivalent on 4 of roughly 40
result cells, and the main text was updated to name the new encoder as *the*
encoder before the remaining cells were retrained. Once the full retrain
landed, the new encoder collapsed retrieval R@1 by 10-41 points on most of the
newly tested cells, while being genuinely *better* than the original on one
further cell -- the blanket claim was wrong in both directions at once, on a
component the paper had already told readers was safe. Two defenses, not one:
(1) do not write a universal architecture-description sentence until every
cell it will describe has been validated, or (2) if a claim must be written
before full validation completes (e.g., under real deadline pressure), scope
the sentence explicitly to the validated subset and treat it as provisional --
re-open and re-verify that exact sentence the moment broader evidence lands,
rather than trusting that a small validated sample generalizes. Report the
result per-cell if it turns out dataset-dependent; do not average a mixed
outcome into a single "safe" or "unsafe" verdict.

### Dataset census and imported-number provenance

Before redesigning a dataset or result table, build a **dataset census** from
the repository rather than from the draft. Reconcile every dataset named by a
builder, configuration, manifest/cache, result log, table, and bibliography.
Give each item one canonical name, citation, task role, construction lineage,
train/validation/test counts, result status, and exclusion reason. A paper may
call a table complete only when the census and the table have the same scope.

| Canonical dataset | Citation | Task role | Construction lineage | Train validation and test counts | Result status | Exclusion reason |
| --- | --- | --- | --- | --- | --- | --- |
| One repository-resolved name | Primary dataset source | Headline, diagnostic, transfer, or reference-only | Builder, manifest, cache, and feature provenance | Explicit counts for every available split | Comparable, diagnostic, reference-only, blocked, or not run | Required whenever the item is outside table scope |

For every numeric value transcribed from another paper, record the primary
paper, source table or page, task, split, horizon, features, supervision,
metric, and aggregation. Double-check the transcription against the primary
source. Do not import a number from a survey, repository README, search snippet,
or another paper's comparison table when the original paper is available.
Never rank, bold, average, or describe numbers as wins across incompatible
protocols. Table layout may inspire presentation; it cannot establish numeric
provenance or comparability.

### Exemplar-format transfer gate

When a reviewer provides a paper as a formatting exemplar, first extract a
**structure-only ledger**: table hierarchy, row granularity, header grouping,
symbol semantics, caption contract, and finding-to-evidence order. Do not copy
claims, values, wording, colors, packages, spacing hacks, URLs, or macros.
Before adopting any LaTeX device, check it against the target venue's current
template and package rules. Verify that the rendered minimum font remains
legible. If compatibility is unverified, reproduce the structure with packages
already permitted by the target template.

When the exemplar is supplied as a source archive (an arXiv `.tar.gz`), extract
it and grep the real `.tex`/`.sty` files for the device in question (e.g., a
checkmark/cross symbol pair) rather than approximating the markup from a
rendered PDF or screenshot. A rendered checkmark could come from `pifont`,
`amssymb`, a custom Unicode glyph, or a colored image; only the source reveals
which, and whether it depends on a package the target venue forbids.

## Claim-driven experiment expansion

Translate requests such as “add more experiments” or “use the idle compute” into
a **claim-driven experiment queue**. Each job must name the manuscript claim it
can support or falsify, the closest control, evaluation contract, dataset and
split, seeds, metric, expected decision, result/log destination, resource
budget, and stop condition. Run P0 contract repairs and matched distinguishing
tests before broad sweeps or fashionable modules.

| Manuscript claim | Closest control | Evaluation contract | Dataset and split | Seeds | Metric and decision rule | Result or log destination | Resource budget | Stop condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claim to support or falsify | Minimal matched alternative | Inputs, oracle access, horizon, and aggregation | Canonical dataset and named split | Planned aligned seeds | Promotion, narrowing, or retirement rule | Immutable machine-readable artifact | Time, accelerator, storage, and run cap | Evidence-complete, falsified, invalid, or budget cap |

Resource availability is a scheduling signal, not evidence of contribution
or a reason to launch redundant runs. Check existing jobs, cache lineage,
completed logs, and protocol compatibility before dispatch. Mark failed,
mismatched, superseded, and duplicate runs explicitly. Promote a result only
after all planned seeds finish, the control is valid, the log is parseable,
and the claim ledger points to the exact artifact. A negative result should
narrow the claim or retire the route; it must not disappear from the decision
record.

Separate the update budget from corpus coverage. Limiting updates per epoch is
not equivalent to permanently limiting the dataset. Audit the loader before
running: ordered subset selection can preserve the requested update count
while silently removing tasks or labels. For a budget-matched study, sample
from the full corpus with a predeclared seeded or stratified rule unless
reduced-corpus exposure is the intended intervention. Record full-corpus and
selected-subset sample, task and label coverage. If a subset is biased,
quarantine the run as an invalid control and rerun;
do not explain the resulting collapse as a method limitation. On an
action-labeled dataset this is task and action coverage.

## Artifact and provenance gate

Before claiming a revision is ready, verify all of the following:

1. The source TeX, bibliography, supplementary source, and compiled PDF agree.
   A newer TeX file than its compiled PDF is an unverified draft.
   A generated artifact is stale whenever its declared inputs have changed
   since generation, regardless of whether the old PDF still compiles.
2. The cited model/configuration matches the result artifact. Do not rename a
   run of one component as a different, newer-sounding component or baseline
   without matched provenance.
   A backbone claim must resolve encoder, configuration, checkpoint, and
   result artifact as one chain. Record the exact model identifier, frozen or
   trainable status, cache provenance, seed, and evaluation command. A small or
   null performance difference does not authorize a text-only rename.
3. The cache actually contains every negative type, annotation, class, and
   split claimed in the manuscript.
4. Checkpoint selection and reported evaluation are described honestly. A
   validation-selected result is not a locked test result.
5. A build has no undefined citations/references and no layout warning that
   makes a table unreadable.
6. When the venue caps main content at page $N$ and reserves pages beyond $N$
   for references only, total page count is not sufficient evidence of
   compliance. Extract page-by-page text from the compiled PDF and confirm
   main content ends by page $N$ and every later page is references only. A
   two-column-wide table or figure near the boundary can spill onto a
   references-only page even when the total page count looks correct; check
   for this specifically, not just the last page number.
   A `\flushbottom`-style layout (common in official conference styles)
   absorbs small, sentence-level trims without moving any page break, so a
   string of minor edits can leave the boundary violation unchanged. Verify by
   recompiling and re-checking the page-by-page boundary after every
   substantive edit; do not assume a small trim helped. If content still
   spills past the boundary, first try reordering or repositioning the
   spilling float, then reduce its own vertical footprint, and only then trim
   earlier content; a structural change (float position, figure/table height)
   crosses the threshold more reliably than further wording edits.
7. Re-verify template compliance against the venue's *current, freshly
   downloaded* author kit, not a cached copy or memory of an earlier
   revision. Diff the venue-provided style file against the one in the
   project by checksum; a mismatch means the project's template drifted and
   every format claim below it is unverified. Extract that same kit's own
   submission-template file and read its literal forbidden-package list and
   "must not" statements verbatim — do not infer them from general venue
   familiarity, since specific prohibitions (a forbidden package, a font
   package the current style file already auto-loads, a required
   `\setcounter` value) change between template revisions. Then scan the
   actual source for every forbidden package, `\pagestyle`/`\thispagestyle`
   commands, and any macro that alters spacing, margins, or fonts outside a
   single table/figure environment. Check the compiled PDF's font table for
   unembedded or Type 3 fonts, and scan its raw bytes for embedded-link and
   bookmark markers even when no hyperlink package was knowingly loaded.
8. After a large-scale rewrite that reorders sections, treat every
   hard-coded cross-reference in a *separately compiled* companion document
   (an appendix or supplement that cites the main paper by written section
   number rather than a shared `\ref`) as suspect. These do not error at
   compile time — the label still resolves, the number is just wrong — so
   they can only be caught by re-deriving the true current section numbers
   from the rewritten source and diffing every hard-coded citation against
   them. Do the same check in the opposite direction after any
   companion-document rewrite.
9. In a long, iteratively grown appendix or supplement compiled with
   standard LaTeX's `\appendix` command, count `\section{}` commands before
   adding another one. `\appendix` defaults `\thesection` to `\Alph{section}`
   (letters A-Z only); the 27th section fails with a fatal
   "Counter too large" error that reports at whatever `\ref` or `\section`
   call happens to trigger it, which reads like a citation or cross-reference
   bug and is not one. Nothing warns as the count approaches 26. Fix by
   adding `\renewcommand{\thesection}{\arabic{section}}` immediately after
   `\appendix` before the count ever matters, rather than diagnosing this
   from scratch once it fires. A single fatal error at this stage can also
   suppress the rest of that compilation pass's output entirely (zero pages),
   which can look like a much larger regression than the one-line fix it is.

When a venue's deadline appears twice with different clock times or dates
across two sources, check for an AoE (UTC-12) vs. local-time conversion
before treating them as a contradiction; an AoE end-of-day deadline lands on
the *next* calendar date in most time zones ahead of UTC. Report the
reconciled, local-time-appropriate figure to the user rather than either raw
number.

When a user says a newer, already-compiling revision is worse than an older
backup or manually-written version, diff the two files directly before doing
anything else. A revision that compiles clean and passes every automated
check can still have quietly traded real content density for page budget --
a full baseline table collapsed into a pointer to the supplement, a
multi-control robustness paragraph collapsed into one vague sentence, a
caption's comparability caveat dropped -- none of which trips a compiler
warning. "Compiles and looks similar in page count" is not evidence that a
rewrite preserved everything the backup had; only a direct diff shows that.

When fixing the horizontal alignment of two independently-centered tables or
sub-tables stacked in one float (e.g. a component ladder above a related
per-row PLAN-metric table), do not wrap the misaligned block in
`\begin{flushleft}...\end{flushleft}`: it is a list-like environment that
adds its own paragraph spacing above and below, which can silently push the
page count over a hard venue limit even though the alignment fix itself is
correct. Use `\noindent\makebox[\linewidth][l]{...}` around the tabular
instead -- a zero-height horizontal box that left-aligns content without
adding vertical space. Recompile and recheck the page count after either
fix; do not assume a purely-visual alignment change is layout-neutral.

## Main-text space must match contribution weight, not writing order

A reviewer's complaint that "the method feels thin" or "results are hard to
assess without the supplement" is often a space-allocation defect, not a
missing-content defect: the material may already exist in the paper, just in
the wrong place. Diagnose it directly rather than guessing. Count words per
section (`\section`/`\subsection`) and compare against the paper's own claimed
contributions. Treat a section describing the paper's core contribution being
markedly smaller than a section describing supporting infrastructure, or a
small fraction of the combined Experiments prose, as a signal worth checking
rather than an automatic verdict -- some papers legitimately foreground a
benchmark or dataset as the contribution, in which case the size ordering
should point the other way. When the core-contribution section is thin
relative to its claimed weight, pull real architectural or mathematical
detail already sitting in the supplement's corresponding section into the
main text (a loss formula, a layer count, an attention configuration) rather
than inventing new content or leaving that section as a one-line pointer to
"supplementary material."

Symmetrically, once a claim is fully carried by a table or figure, prose
should not re-narrate its numbers; it should state the one-sentence
interpretation a rushed reviewer needs and stop. A paragraph that walks
through four or five individual values from a table the reader can already
see is spending main-text space on redundant transcription instead of
argument. The reviewer must be able to assess technical soundness, novelty,
and headline results from the main text alone; nothing load-bearing for
those three judgments should live only in the supplement.

## Language and finding discipline

- Enforce one sentence, one core meaning. Split method naming, task definition,
  objective, mechanism, and result when they compete for the same sentence.
- Treat a sentence above roughly 35 words or with multiple semicolon/relative
  clauses as a review trigger, not an automatic error. Preserve necessary
  technical qualifiers while removing clause stacking.
- Write experimental findings as conclusion, evidence, mechanism, and boundary.
  A styled “Finding” box does not create a finding; it may contain only a claim
  already supported by a cited table, figure, or result artifact.
- Do not use *borrow, adapt, or imitate* as the contribution's main narrative.
  Cite related work and compare it directly along task, output, supervision,
  mechanism, and evaluation axes. If reuse is technically material, disclose
  it precisely without making the new contribution sound like relabeling.

### Title-level mechanism gate

Treat a title or method-name claim such as *one-step*, *iterative*, *online*,
*causal*, or *training-free* as a technical claim, not branding. At first use,
define the counted unit or operational condition. State what is held fixed and
what the closest alternative does differently. Then provide a matched,
distinguishing experiment with compatible inputs, supervision, compute budget,
selection rule, and evaluation contract. Report the predicted advantage and
its boundary. If neither a precise definition nor this evidence exists, use a
mechanism-neutral name until the evidence is complete.

## Figure evidence cards

Create a **figure evidence card** before reserving or revising each figure. The
card records: reader question, one core claim, source artifact, exact values or
examples, comparison contract, visual encoding, caption, body-text anchor, and
status (`placeholder`, `data-ready`, or `rendered`). A placeholder is acceptable
only when its caption and drawing contract do not imply unrun evidence.

Reconcile all figure evidence cards as one portfolio before submission. Every
number, example, arrow, module label, and causal statement must resolve to the
same source/result contract used by the text. Placeholder status must remain
visible in the ledger; a polished caption must never make an unrendered or
unrun figure appear complete.

### Rendering authority is separate from evidence readiness

An agent's job on a figure ends at the evidence card and drawing contract: the
reader question, core claim, module decomposition, visual encoding, and exact
values/examples the artist needs. Producing the final rendered image (a
generated illustration, a hand-plotted chart image, or any file an
`\includegraphics` call would point to) is a separate decision that belongs to
the paper's author, not something an agent should do on its own initiative
merely because the data or design is ready. A figure being `data-ready` in the
evidence-card ledger authorizes writing a complete drawing contract; it does
not by itself authorize replacing a placeholder with rendered output. If a
collaborator or an earlier pass already rendered figures without this
authorization, treat that as a pending decision to surface, not as settled
progress to build on -- ask before continuing to use the rendered files, and
be ready to revert to placeholders bound to the same drawing contract.

Use separate figures for separate jobs: task motivation, benchmark
construction, method mechanism, controlled route comparison, and failure or
necessity analysis. The framework figure gives the largest visual area to the
actual contribution. Conventional encoders and preprocessing stay visually
subordinate. Figure labels, module names, symbols, captions, and body text must
match exactly.

## Submission and release safety

Official submission policy outranks a local preference for a repository link.
When a venue prohibits web pointers, prepare an anonymized, reproducible code
and data package through the permitted submission channel rather than inserting
a URL into the manuscript. Check the current official policy, not memory.

Before hosting any "anonymous" artifact under a code-hosting account, verify
the account itself is anonymous, not just that a provided credential can
authenticate to it. Authenticating as an account proves ownership; it says
nothing about whether that account's public profile is anonymous. Fetch the
account's own public profile fields (display name, organization, email,
personal site/blog, bio, location) before trusting it for anonymized
hosting, even when the repository being created is private. A private
repository does not anonymize its owning account. When in doubt, prefer a
path with no code-hosting account in the loop at all (a local, sanitized
archive uploaded through the venue's own supplementary-material channel) over
constructing a fresh anonymous account, since it removes the identity-account
risk surface entirely rather than relocating it.

Freeze a package inventory before archive creation. It must list every included
file, its role, license or redistribution status, and checksum. Run a secret
scan over files, archive members, metadata, generated logs, and version-control
history; then extract the final archive into a clean directory and execute its
documented smoke test. If full raw data cannot legally or practically be
included, ship permitted manifests, acquisition instructions, and any venue-
allowed representative subset without claiming that the complete raw data is
inside the package.

| Path | Role | License or redistribution status | Checksum |
| --- | --- | --- | --- |
| Relative anonymous archive path | Why reviewers need the file | Permission, source, and any exclusion boundary | Digest computed from the final frozen member |

Never place a credential, token, private URL, absolute home path, author name,
commit identity, acknowledgment, or unredacted log in an anonymous artifact.
Do not use a credential found in reviewer material. Ask the holder to revoke
and rotate it; prepare only files that are safe to distribute.

## Output pattern

Return, in order:

1. P0 evidence conflicts and their exact impact on claims.
2. A claim ledger or compact table map.
3. Corrected prose/table/figure plan, with each claim tied to an artifact.
4. Experiments required before promotion, including controls and invalid runs
   to exclude.
5. A submission-safe release checklist.

## Revision order

Use this fail-closed order for a substantial advisor revision:

1. freeze the exact review sources and transcribe requirements;
2. detect source/TeX/PDF/result drift;
3. build the claim ledger and comparison-contract map;
4. run or exclude the required experiments;
5. redesign tables and figure evidence cards from verified artifacts;
6. revise prose with one sentence, one core meaning;
7. rebuild, scan citations/references/layout, and refresh hashes and status.

Do not publish, tag, or release a revised skill or manuscript package before
the final validation rerun uses the exact artifacts being released.

## Common failure modes

| Failure | Required correction |
| --- | --- |
| A reviewer asks for a modern encoder | Report a matched control or rerun; do not text-replace the encoder. |
| A request asks for a code URL | Check current venue policy before adding a web pointer. |
| A credential successfully authenticates to a hosting account meant for anonymous release | That proves ownership, not anonymity; fetch the account's own public profile before trusting it, and prefer no code-hosting account at all over relocating the risk to a fresh one. |
| A table becomes too dense | Use defined binary columns, citations, and caption scope; move prose to the body. |
| A strong result uses another contract | Put it in a separately named table and do not use it to prove the main task. |
| A table row uses each metric's best epoch | Rebuild a checkpoint-coherent row from one predeclared selection rule. |
| A quick self-extraction script reads the last logged epoch for speed | A "quick sanity check" is still a reported number once it reaches a table; grep the training log's own best-checkpoint selection line or use the project's declared selection rule, not the tail of a metrics file, even under time pressure. |
| One prose sentence quotes an accuracy figure from one experiment report and a cost/timing figure from a follow-up correction of the same experiment | Before combining two numbers into one sentence, confirm both come from the same run/cache lineage, not just a plausible-looking pair from reports on the same topic; re-check immediately after writing the sentence, since this recurs even right after writing the rule itself. |
| A true limitation gets stated once as method context, once as a bolded Limitations item, and once again in the Conclusion | Deleting or softening the fact is not allowed; instead state it exactly once, in neutral prose, and move mechanism/numbers to the supplement (see `05-experiments-conclusion-references.md`, "Limitation density and placement"). |
| Paired conditions have different seed sets | Report only aligned pairs or run the missing seeds; do not call the aggregate paired. |
| A data-partition budget uses the sorted first N files | Audit task/label coverage and rerun with seeded full-corpus sampling or a declared stratified subset. |
| A PDF looks clean | Rebuild from the current TeX and scan the log; visual appearance cannot prove provenance. |
| A template's rule is recalled from memory or an earlier revision | Download the current official author kit and diff its style file and forbidden-package list against the project before trusting any format claim. |
| Adding one more appendix section suddenly produces zero PDF pages and a fatal error at an unrelated `\ref` | Count `\section{}` commands; past 26 under default `\appendix` (`\Alph{section}`), add `\renewcommand{\thesection}{\arabic{section}}` right after `\appendix`. |
| A large rewrite reorders sections | Re-derive true section numbers from the rewritten source and diff every hard-coded cross-reference in any separately compiled companion document; compile success does not catch a wrong-but-valid label. |
| Two sources give different deadline clock times | Check for an AoE-vs-local-time conversion before reporting a contradiction. |
| Figure/table data is ready and a drawing contract exists | That authorizes writing the contract, not rendering the final image; rendering is the paper author's decision unless explicitly delegated. |
| A user says a newer, compiling revision is worse than an older backup | Diff the two files directly; page-budget trimming can silently drop real content (baseline tables, robustness paragraphs, caption caveats) without tripping any compiler warning. |
| Two stacked, independently-centered sub-tables in one float misalign | Use `\noindent\makebox[\linewidth][l]{...}` around the tabular, not `\begin{flushleft}`, which adds paragraph spacing and can silently blow the page budget. |

## Deep dive

- Experiments, conclusions, and references: `05-experiments-conclusion-references.md`
- Terminology, tables, citations, and ethics: `10-terminology-symbols-figures-references.md`
- Full course reconstruction: `../course-full-reconstruction.md`
