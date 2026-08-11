# Abstract and Introduction

> Task playbook distilled from 第三讲：英文学术论文之写作思路——摘要和引言 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-03-abstract-and-introduction.md`


## Core doctrine

Apply the Lecture 3 rule set before drafting, revising, or judging any research-paper text:

```text
title -> abstract -> introduction
problem -> method -> experiment
```

The abstract is the expansion of the title and the compression of the introduction. The introduction is the expansion of the abstract and the hardest part of the paper because it must prove that the research problem is real, important, specific, and worth solving.

A strong paper makes problem, method, and experiment mutually responsive. A weak paper lets them each tell a separate story.

## Mandatory workflow

1. **Reconstruct the paper story first.** Identify the real task, the field need, the core challenge, the specific solvable problem, the current-method limitations, the proposed method idea, the method steps, the evidence, and the field-level contribution.

2. **Check problem-method-experiment alignment.**
   - Problem: justified, specific, and grounded in motivation.
   - Method: designed for that problem; every step has an explicit goal.
   - Experiment: proves method components and analyzes the original motivation.

3. **For abstracts, use the five-slot structure.**
   - Task/challenge.
   - Existing-method limitation.
   - Core method idea.
   - Concrete technical highlights in logical order.
   - Effects plus broader value.

4. **For introductions, use the five-part structure.**
   - Research background and challenge.
   - Problem and cause.
   - Related work and insufficiency.
   - This paper's research idea.
   - Main contributions.

5. **Classify related work by technical route.** Do not write chronological lists such as "A did..., B did..., C did...". Group methods by shared technical logic, explain representative work, and evaluate limitations accurately, objectively, and professionally.

6. **Explain method purpose before method details.** State the one-sentence top-level idea before modules. For each module or step, explain what it does, why it is needed, and which challenge or limitation it answers.

7. **Lift contributions above method steps.** Contributions may be a new problem, new perspective, new framework, new method, new SOTA, new capability, new interpretability evidence, or new experimental proof. Do not treat SOTA alone as the main contribution unless the analysis proves the gain comes from solving the stated problem.

## Drafting guidance

When drafting an abstract, produce a compact logic chain rather than a module list. Prefer this sequence:

```text
X is important, but ...
Existing methods ..., but ...
We propose ..., based on ...
Specifically, we first ..., then ..., and finally ...
Experiments show ..., and analysis demonstrates ...
```

When drafting an introduction, expand the abstract into paragraphs that prove the logic. Ensure that the last sentence of a related-work/problem paragraph naturally leads into the proposed method paragraph.

## Review checklist

Before finalizing, answer:

- What exact challenge does the paper solve?
- Is the challenge specific enough to be testable?
- What is the limitation of existing methods?
- Is that limitation evaluated accurately and professionally?
- What is the top-level method idea?
- Which method step addresses which limitation?
- Which experiment proves each method step?
- What contribution remains beyond "we achieve SOTA"?
- Can the abstract be derived by compressing the introduction?
- Does the paper avoid the weak pattern: "everyone studies it -> step1/step2/step3 -> SOTA"?

---

## Appendix: course templates and checklists for this lecture

## Lecture 3 Templates and Checklists  
### Abstract and Introduction

This reference distills Yu Jing's Lecture 3 rules into reusable writing procedures.

---

### 1. Non-negotiable writing doctrine

Always enforce the following chain:

```text
problem -> method -> experiment
```

A strong paper makes the three parts mutually responsive:

- Problem: justified, specific, and grounded in research motivation.
- Method: designed for the problem, with each step having an explicit goal.
- Experiment: proves each method component and analyzes each motivation.

Reject writing where:

- The problem is only "many people study this, so we study it."
- The method is only "step1 -> step2 -> step3."
- The experiment is only "we achieve SOTA" without analysis.
- Problem, method, and experiment each tell separate stories.

---

### 2. Abstract five-slot template

Use this for drafting, revising, or diagnosing abstracts.

```text
[Task/Challenge]
X is important for Y, but remains challenging because ...

[Existing-method limitation]
Existing methods usually ..., but they fail to ...

[Core idea]
To address this problem, we propose ..., which ...

[Technical highlights]
Specifically, we first ..., then ..., and finally ...

[Effects and contribution]
Experiments on ... show ..., and further analysis demonstrates ...
```

Mandatory slots:

1. Task and challenge.
2. Existing-method problem.
3. One-sentence method idea.
4. Core technical highlights in logical order.
5. Effects plus field-level value.

Do not start with module details. Give the top-level idea first.

---

### 3. Introduction five-part template

#### Part 1: Background and challenge

Write only the background needed to motivate the paper. Explain:

- why the field/task matters,
- what the central challenge is,
- why that challenge matters for the task.

Avoid generic background.

#### Part 2: Problem and cause

Convert the broad challenge into a specific, solvable research problem. Distinguish:

- task-level challenge,
- existing-method limitations.

#### Part 3: Related work and insufficiency

Classify existing work by technical line. Do not list chronologically.

For each group:

```text
Methods in this line typically ...
They improve ...
However, they still ...
```

Evaluate accurately, professionally, and objectively.

#### Part 4: This paper's research idea

First state the large idea:

```text
We address this problem from the perspective of ...
```

Then describe the main components. For every component, state:

- what it does,
- why it is needed,
- which challenge or limitation it answers.

#### Part 5: Contributions

Do not repeat method details. Lift the method into field-level contributions:

- new problem,
- new perspective,
- new framework,
- new method,
- new SOTA,
- new capability,
- new interpretability or evidence.

SOTA is not enough unless analysis proves the improvement comes from solving the stated problem.

---

### 4. Abstract checklist

- [ ] Does the first sentence specify the task/challenge?
- [ ] Is the challenge specific rather than generic?
- [ ] Is the existing-method limitation clearly connected to the challenge?
- [ ] Is the core method idea stated before details?
- [ ] Do the technical highlights form a logical sequence?
- [ ] Does each highlight explain how it helps solve the problem?
- [ ] Does the ending state effect and broader value?
- [ ] Does it avoid overclaiming?
- [ ] Is it concise and logically complete?

---

### 5. Introduction checklist

- [ ] Is the background focused?
- [ ] Is the field/task importance justified?
- [ ] Is the task-level challenge explicit?
- [ ] Is the paper's research problem specific and solvable?
- [ ] Are related methods classified by technical route?
- [ ] Are representative works cited without exhaustive listing?
- [ ] Are limitations described accurately and professionally?
- [ ] Does the proposed method directly respond to the challenge?
- [ ] Does every method step have a purpose?
- [ ] Are contributions lifted beyond method steps?
- [ ] Do experiments later prove the stated motivations?
- [ ] Does the whole paper form a problem-method-experiment loop?

---

### 6. Revision prompts

When reviewing a draft, ask:

1. What exact challenge does this paper claim to solve?
2. Which sentence states the limitation of current methods?
3. Which sentence states the method's top-level idea?
4. Which method components correspond to which stated limitations?
5. Which experiments prove each component?
6. What contribution remains if we remove the phrase "achieves SOTA"?
7. Does the introduction make the abstract almost write itself?

---

### 6b. The lecture's own worked examples, by name

The abstract walkthrough above is modeled on **"Unbiased Scene Graph
Generation from Biased Training"** (CVPR 2020, Hanwang Zhang's group) — the
instructor picked it because its abstract cleanly chains challenge, existing-
method limitation, method idea, technical highlights, and effect into one
logical sequence, worth reading directly as a template. The introduction
walkthrough (and the "Bad-to-good transformations" below) is modeled on
**Mucko** (*Multi-Layer Cross-Modal Knowledge Reasoning for Fact-based
Visual Question Answering*, IJCAI 2020) — its core challenge is selecting
question-oriented, information-complementary evidence across visual,
semantic, and factual knowledge without introducing irrelevant noise, which
is why the "Better" examples below reference visual/semantic/factual
modalities specifically rather than generic "multimodal fusion."

### 7. Bad-to-good transformations

#### Bad problem statement

```text
Multimodal fusion is challenging.
```

Better:

```text
The key challenge is to select question-oriented and information-complementary evidence across visual, semantic, and factual modalities without introducing irrelevant knowledge noise.
```

#### Bad method description

```text
We propose a model with three modules: A, B, and C.
```

Better:

```text
We first construct a unified structured representation so that heterogeneous evidence can be compared under the same reasoning framework. We then select intra-modal evidence and aggregate cross-modal complementary evidence to support question-oriented inference.
```

#### Bad contribution

```text
We propose a new network and achieve SOTA.
```

Better:

```text
We formulate the evidence-selection bottleneck in fact-based VQA and propose a multi-layer heterogeneous graph reasoning framework that explicitly models visual, semantic, and factual evidence, yielding both performance gains and interpretable modality-level reasoning evidence.
```

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-03-abstract-and-introduction.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
