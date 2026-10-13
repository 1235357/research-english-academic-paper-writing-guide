# Current course review: scope, evidence and reconstruction errata

Reviewed 2026-10-13. This is an editorial application layer, not a new lecture
or a silent correction of the instructor's words. All 13 bundled lecture
files and both full-course copies remain byte-identical. Coverage comprises
the complete Markdown reconstructions, including both versions and their
transcript sections; it does not establish original slide-pixel/audio fidelity
or third-party redistribution rights. Lecture 10 labels its transcript section
as lightly edited. Identical lecture bodies in the full-course copies were
matched exactly; their additional integration prose was also read.

For **what the instructor said**, consult the original teaching artifacts
when available, then the preserved reconstructions and the errata below.
For **how to apply the skill now**, these named corrections take precedence
over conflicting archive reading protocols, companion synthesis, playbooks
and quick-reference wording. This is a bounded exception, not authority to
ignore the course or invent corrections. Read the relevant lecture together
with the applicable note; unresolved source conflicts remain uncertain.

## A. Contribution-appropriate scope

The course mainly demonstrates comparative ML method papers. Its five-slot
abstract, problem-method-experiment chain, A/C venue contrast and module-based
checks are teaching heuristics for that setting, not universal admission rules.
Lecture 3 itself extends the five slots to all paper types (transcript and V2
§2); this note deliberately qualifies that source advice for application.

- Match evidence to the claim: comparative methods need fair relevant
  baselines and controlled component tests where separable; new tasks/data
  need a justified need, construction/annotation/evaluation validity and
  suitable baselines; theory needs proofs under stated assumptions; systems
  need appropriate measurements; diagnostic, negative-result and exploratory
  work need scoped questions and tests that can fail. SOTA and ablations are
  not mandatory when they do not test the contribution.
- Do not fabricate a method, positive result, weakness in prior work or
  mechanism to fill a writing template. Respect the actual genre and venue.
- Method-first exploration and transfer are legitimate starts (Lecture 11,
  transcript: transfer is a good beginning; V2 §§1.2/2.2). Investigate whether
  the gain is real and why; do not invent a need after the fact or claim the
  discovery chronology was problem-first when it was not.
- A real need can be established by new evidence, not only existing consensus
  (Lecture 11, new-task/dataset discussion). Engineering delivery can be a
  valuable user goal without claiming a new scientific mechanism.
- The 四生四世 paper counts are explicitly figurative (Lecture 1 transcript,
  “虚数”; V2 growth discussion). Do not infer independence/seniority from
  publication count, venue tier or one mentoring request. Calibrate to demonstrated
  skills, requested support and academic or industry goals, including
  CS/LLM/MLE/FDE employment where relevant to the user.
- The major-venue list is historical, not a current ranking or acceptance
  predictor. Verify current official scope, contribution types, review criteria
  and deadlines for an actual submission decision.

## B. Evidence strength and honest illustration

Lectures 4 and 5 sometimes call for proving a choice “optimal”; Lecture 5
also uses strong causal wording for ablations and visualizations. Preserve
those quotations as source wording, but apply the following limits:

- A test may support, weaken or falsify a claim. Finite comparisons do not
  establish global optimality. State tested settings, alternatives, controls,
  uncertainty and the boundary of inference.
- Separate observation, candidate explanation and independently tested
  mechanism. A plausible rationale, attention map, selected example or
  subgroup gain does not alone identify the claimed causal mechanism;
  causal conclusions require suitable controls/identifying assumptions.
- The unnamed human-memory example in Lecture 11 is an instructor-reported
  qualitative analogy, not a verified primary study or ML mechanism proof.
  It may inspire an auxiliary-objective hypothesis; test matched controls,
  intermediate predictions, negative transfer and falsifying outcomes.
- For the Lecture 2 human-understanding title example, a cognitive analogy
  may inspire a labeled hypothesis. Cite the precise supported finding,
  distinguish it from the ML analogy, and do not assert an unsupported
  human-like mechanism in either title or prose. V2's suggestion that
  “unproven conclusions” can serve as a basis with citations is ambiguous
  relative to the transcript's explicit warning.
- Label figures/cases as observed results, cited findings, or conceptual
  schematics/expected behavior. Never invent prior-method failure or proposed
  success for contrast. A representative illustration is not population-level
  evaluation; report selection, quantitative coverage and failures where relevant.
- Keep figure structure legible: principal inputs/outputs, module boundaries,
  arrows and claims must be clear in the figure with its caption. Linked
  Method text may supply indispensable implementation/reproduction detail
  (Lecture 7 transcript and V2 §1). Do not hide misleading or illegible
  figure content in prose, or demand full reproducibility from an image alone.
- Concise routine-method coverage does not permit omitting reproducibility
  conditions. Preserve data/splits, preprocessing, prompts, optimization,
  hyperparameters and compute needed to interpret/reproduce results in an
  appropriate methods, appendix or artifact location (compare Lecture 10's
  explicit code/supplement recommendation).

## C. Literature and communication safeguards

- Inspect authorized available data/artifacts, not just their paper: sample,
  schema/labels, splits and official evaluator. For LLM evaluations inspect
  acceptable-answer multiplicity and prompt/context/scoring rules. Record
  observed versus documented versus inferred; unavailable artifacts mean
  document-only knowledge, not completed inspection (Lecture 12 transcript,
  dataset discussion; V2 §4).
- Prioritize relevance and claim-evidence quality. Team history, venue,
  citations and adoption are discovery cues or tie-breakers, never a majority
  checklist that compensates for weak relevance (Lecture 12 V2 §6).
- Technical evolution may be chronological. Reject an unstructured
  author-by-author list, not chronology itself (Lecture 3 transcript).
- The instructor's experience of students' logical-writing problems is not
  a diagnosis of all non-native writers. Inspect actual language and logic.
  One main idea per sentence allows necessary names, data and supporting detail.
- The integrity warning covers both text and result plagiarism; it does not
  establish identical severity or sanctions. Preserve attribution and assess
  actual conduct under the relevant policy, without turning historical
  allegations into adjudicated findings.

The MuKEA/ET-BERT examples do not define an exhaustive contribution taxonomy or
link novelty to model size. Explain pretraining/fine-tuning only for frameworks
that actually use them. Align comparable roles without forcing every method into
the same stages; preserve absent stages and differences in input access,
supervision, compute and evaluation. Keep standard names for borrowed components.
A quick non-author comprehension check is useful, but a one-minute cutoff is an
editorial heuristic, not a source-derived universal acceptance gate.

## D. Reconstruction errata (archival text unchanged)

| Location | Reading correction |
| --- | --- |
| Bonus lecture V1 opening and §§8–10, versus its V2 source note | V1 still combines the bonus transcript with the formal lecture's 20-page slide deck. V2 uses the corrected 9-page bonus deck. The historical filename-swap note does not erase the residual mixed V1 content; attribute those formal-slide sections to Lecture 11. |
| Lecture 11 V2 scientific/technical table, last two rows | Those rows are reversed relative to their headers. Use its surrounding prose, V1 table and formal slide transcription: tuning/fusion descriptions are technical; the why/mechanism questions are scientific. |
| Lecture 9 ET-BERT worked example | The overloaded opening and the later 44-word detail sentence are distinct. The transcript describes model/task/name together, then the objective. Archived exact rewrite quotes differ; paraphrase, do not invent an exact three-sentence rewrite. |
| Lecture 10 V1 §2 table, figure row | “不 cherry-pick，只展示 best case” drops a negation. Its main figure section and transcript explicitly reject best-case-only presentation. |
| Lecture 10 V2 §6 bibliography example heading | The listed “and et al.” references are bad examples, as the following discussion says, not a correct template. |
| Lecture 10 Math Vault page count | The checked PDF has 28 pages (see dated SKILL correction), not the transcript/V2's approximately 200-page estimate. Do not generalize to other editions. |
| Lecture 12 V2 statement that no slide deck was available | This describes that author's original archive. V1 includes 39 later-fetched official slides; the provenance note already explains the lineage. |
| Companion synthesis figure-history pointer | MuKEA motivation: V1–V4; MuKEA framework: V1–V8. ET-BERT motivation: V1–V3; ET-BERT framework: V1–V4. The eight-version framework sequence is not ET-BERT. |

Unresolved visual-transcription conflicts require the original slide before an
exact recreation: Lecture 6 differs on which side contains `clock → London` and
on a motorcycle label; Lecture 8 differs on fine-tuning task labels and CogTree
layout. Do not guess which reconstruction is correct. Unchanged task inputs and
outputs do not by themselves rule out a new architecture/framework; historical
priority and universal-compatibility assertions require paper-level verification.

These notes correct operational use and identified reading conflicts. They
do not independently verify the historical papers' empirical claims.
