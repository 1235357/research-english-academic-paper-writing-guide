# Writing Ideas for English Academic Papers: Conception and Title

> Task playbook distilled from 第二讲：英文学术论文之写作思路——立意和标题 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-02-conception-and-title.md`


## Purpose

Apply Lecture 2 of Yu Jing's *Guide to Scientific Research and English Academic Paper Writing* as a reusable research-writing lens. Treat every academic writing or research-framing task as a problem of aligning conception, core problem, technical innovation, method design, experiments, and title.

## Mandatory First Pass

For any relevant user request, first identify these six elements before drafting or revising text:

1. The actual task or application setting.
2. The core scientific problem, not just the surface need.
3. The technical innovation or capability breakthrough.
4. The method mechanism and why each step exists.
5. The experiment evidence needed to prove the method and analyze the motivation.
6. The title boundary: what the paper claims and what it does not claim.

If the user only asks for a title, still infer or ask for the missing elements. If enough context is available, proceed with explicit assumptions.

## A-level Paper Orientation

Favor the A-level pattern from the lecture:

- Focus on field frontiers and essential problems.
- Avoid merely chasing hot tasks or hot methods.
- Design methods for core challenges, not incremental modifications for small metric gains.
- Make problem, method, and experiments mutually responsive.
- Explain why each method step exists and what problem it solves.
- Analyze experimental improvement, not just state SOTA.

Reject or revise C-level patterns:

- "Everyone studies this, so I study it."
- "step1 -> step2 -> step3" without motivation.
- "We reach SOTA" without analysis.
- Generic method-for-task titles that reveal no specific innovation.

## Title Workflow

When generating or reviewing a title:

1. Check basic requirements: standard English form, concise language, appropriate scope, roughly 15 words or fewer when possible.
2. Check whether the title reflects the core problem.
3. Check whether it highlights the technical innovation.
4. Check whether a model or method name protects the contribution and is easy to remember.
5. Remove unsupported claims, hype, subjective language, and excessive details.
6. Prefer one of these forms when suitable:
   - `ModelName: Core Technical Mechanism for Target Task`
   - `ModelName: Representation/Learning Framework for Target Task`
   - `Verb1, Verb2, and Verb3: Strategy for Target Task`
   - `Capability + Target Task`

Use the title evaluation checklist appended below for detailed review criteria. Use `scripts/check_title.py` for quick deterministic checks when working in a local/code environment.

## Output Style

When producing academic writing advice, give actionable revisions and explain the reason using the lecture's terms: core problem, technical innovation, problem-method-experiment correspondence, specificity, evidence, scope, and memorability.

When reconstructing or citing the lecture, never embed slide images. Describe slide visuals in words.

---

## Appendix: course templates and checklists for this lecture

## Lecture 2 Method Guide: From Conception to Title

### Core Principle
Before writing a title, identify whether the work is built around a core scientific problem or merely follows a hot topic. A-level paper writing begins before writing: it begins when the author chooses a problem and designs a method around it.

### A-level vs C-level Orientation
A-level orientation:
- Focus on the research frontier.
- Explore essential problems.
- Design methods for core challenges.
- Seek generalizable or broadly useful methods.
- Align problem, method, and experiments.

C-level orientation:
- Chase popular tasks or methods.
- Solve surface-level problems.
- Make small incremental modifications to popular models.
- Optimize for a small metric gain on specific datasets.
- Describe problem, method, and experiments as disconnected sections.

### Problem-Method-Experiment Alignment
For any paper draft or idea, enforce this alignment:
- Problem: evidence-based and specific.
- Method: each step has a clear target and answers part of the problem.
- Experiment: each experiment verifies a method design or analyzes a motivation.

### Use in Agent Workflows
When asked to generate or review a paper title, introduction outline, paper contribution statement, research proposal, abstract, or rebuttal framing, first identify:
1. actual need/task;
2. scientific problem;
3. technical innovation;
4. method mechanism;
5. experiment evidence;
6. title boundary.

Then generate or revise the requested text so it reinforces the same core line.

## Title Evaluation Checklist from Lecture 2

Use this checklist whenever reviewing, generating, or revising an English academic paper title.

### 1. Basic Requirements
- Keep the title concise; use approximately 15 words or fewer when possible.
- Use standard English grammar and capitalization.
- Use concise, precise language.
- Keep the scope appropriate for one paper; avoid thesis-scale titles.

### 2. Good Title Requirements
- Reflect the core problem: make the task, scientific problem, or shared challenge visible.
- Highlight technical innovation: state the specific mechanism, representation, learning framework, or capability breakthrough.
- Protect intellectual contribution: use a memorable method/model name when appropriate.
- Support memory and transmission: make the title easy to read, pronounce, remember, and cite.

### 3. Red Flags
- Too broad: slogans such as "from shallow to deeper" that do not specify a concrete mechanism.
- Non-standard acronym construction: strange mid-word capitalization or discontinuous letter extraction.
- Unsupported claim: phrases like "understanding like humans" without objective scientific basis.
- No visible innovation: mature method name + mature task name, with no specific mechanism.
- Too redundant: packing every module, loss, framework, and adjective into the title.
- Hard to remember: acronyms that are difficult to pronounce or have no semantic connection.

### 3b. Worked Bad-Title Cases from the Lecture

These are the lecture's own six bad-title examples (drawn from the
instructor's own students' drafts), each with the exact defect. Use these as
calibration anchors — a title with the same *shape* of problem, even in a
different field, should be flagged the same way.

1. *"From shallow to deeper: compositional reasoning over graphs for visual
   question answering"* — too broad/abstract; reads like a talk or tutorial
   title, not an objective scientific claim.
2. *"PERT: adaPtive Evidence-driven Reasoning neTwork for..."* — non-standard
   acronym: letters are pulled from the *middle* of words ("adaP**t**ive",
   "neT**w**ork") rather than consecutive initials. An acronym should be
   readable and its letters should come from a consistent, findable position.
3. *"Understanding like humans: multimodal representation for..."* — asserts
   an unproven cognitive-science claim (how humans understand is not a
   settled scientific consensus). A claim like this can motivate a method in
   prose (with citations) but must not appear as an assertion in the title.
4. *"Graph Neural Networks for Image-Text Matching"* — technically correct
   and grammatical, but generic/dated: this exact "method-for-task" framing
   would have signaled real novelty around 2016-2017, when GNNs were new to
   the task; after years of follow-up work it now signals no discernible
   increment.
5. *"A Plug-and-Play novel Tree Loss Function for Unbiased Scene Graph
   Generation based on Upgraded Transformer framework"* — detail overload:
   every component (plug-and-play, novel, tree loss, unbiased, upgraded
   Transformer) is crammed in, so no single element reads as *the*
   contribution. State the one or two ideas that actually matter.
6. *"KBGN: Knowledge-Bridge Graph Network for Adaptive Vision-Text Reasoning
   in Visual Dialogue"* — structurally fine, but "KBGN" carries no semantic
   meaning and is hard to pronounce, which works against memorability and
   spread even though nothing else is wrong.

### 3c. Worked Good-Title Cases from the Lecture

From the instructor's own CCF-A papers — each pairs a memorable model name
with a task-plus-mechanism description:

- *MuKEA: Multimodal Knowledge Extraction and Accumulation for
  Knowledge-based Visual Question Answering* (CVPR 2022)
- *ET-BERT: A Contextualized Datagram Representation with Pre-training
  Transformers for Encrypted Traffic Classification* (WWW 2022)
- *CogTree: Cognition Tree Loss for Unbiased Scene Graph Generation*
  (IJCAI 2021)
- *DualVD: An Adaptive Dual Encoding Model for Deep Visual Understanding in
  Visual Dialogue* (AAAI 2020) — note: the course slide itself renders this
  as "DualDV"; the published paper's actual title uses "DualVD". When citing
  this case, use the correct published form unless you are explicitly
  transcribing the slide verbatim.
- *Mucko: Multi-Layer Cross-Modal Knowledge Reasoning for Fact-based Visual
  Question Answering* (IJCAI 2020)
- *DAM: Deliberation, Abandon and Memory Networks for Generating Detailed
  and Non-repetitive Responses in Visual Dialogue* (IJCAI 2020)

Plus a cross-field set the lecture highlights as exemplary from outside the
instructor's own work: *Zero-Shot Text-to-Image Generation* (DALL·E),
*Swin Transformer: Hierarchical Vision Transformer using Shifted Windows*
(ICCV 2021 best paper), *Sketch, Ground, and Refine: Top-Down Dense Video
Captioning* (CVPR), *BERT: Pre-training of Deep Bidirectional Transformers
for Language Understanding* (NAACL 2019), *Knowledgeable Prompt-tuning*
(ACL 2022), and *A Simple Framework for Contrastive Learning of Visual
Representations* (SimCLR, ICML 2020). Each names the task, states the
mechanism or key property (zero-shot, hierarchical + shifted windows,
sketch-ground-refine), and pairs it with a pronounceable model name where
one is used.

### 4. Review Questions
Ask these in order:
1. What core problem does the title claim to solve?
2. Is the problem specific enough and central enough?
3. What technical innovation is visible in the title?
4. Does the title communicate the boundary of the contribution?
5. Can a reviewer remember and repeat the title or method name after reading it once?
6. Does the title avoid hype, subjectivity, and unsupported claims?

### 5. Rewriting Template
Use one of these patterns:
- `ModelName: Core Technical Mechanism for Target Task`
- `ModelName: Representation/Learning Framework for Target Task`
- `Verb1, Verb2, and Verb3: Strategy for Target Task`
- `Capability + Target Task`

Do not force a template if it hides the real contribution. The title must first serve the scientific problem and innovation.

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-02-conception-and-title.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
- Helper script: `scripts/check_title.py "Your Title"` — deterministic title red-flag checks.
