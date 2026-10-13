# How to Be Concise and Rigorous

> Task playbook distilled from 第九讲：英文学术论文之英文规范——如何做到简洁与严谨 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-09-concise-and-rigorous.md`


## Core mandate

Always apply the Lecture 9 principle: use the simplest language to express the clearest meaning, and use explicit narrative logic so a rushed reviewer can understand the paper without guessing.

The instructor reports that many students' apparent language problems involve
logical organization. This is teaching experience, not a diagnosis of all
non-native writers: inspect the actual text for both language and logic. The
Shi Yigong example emphasizes clear communication using simple words rather
than unnecessary sophistication.

In the ET-BERT example, the overloaded opening and a later 44-word detail
sentence are distinct. The transcript describes stating model/task/name together,
then the objective. Archived exact rewrites differ, so paraphrase unless the slide
is checked. Split where comprehension improves; do not impose a three-sentence
rewrite or treat one main idea as excluding necessary names, data and support.

> ### Rhythm is a readability check, not authorship evidence
>
> Keep the course's clarity and terminology rules. Review monotonous sentence
> frames where they weaken emphasis, but do not assume these rules cause a
> detector flag. Playbook 17 records a self-reported, single-manuscript case
> and dated detector-bias research; neither validates sentence-length CV as
> a predictor of a current classifier's output.
>
> Use `scripts/measure_prose_rhythm.py` only as a descriptive aid. Preserve
> scientific meaning and honest uncertainty; there is no statistical profile
> or detector score to optimize toward.

## Default workflow

When working on academic writing, run two passes before producing the final answer.

### Pass 1: Concise expression

1. Enforce one sentence, one core meaning.
2. Split overloaded sentences into: method/task, objective, innovation, and core method idea.
   Also consider a shorter standalone judgment when a mid-length sentence
   combines a claim and support and the split improves emphasis (Playbook 17
   R3). Do not split solely to increase a statistic or change a detector score.
3. Remove details that belong in the Method section when revising Abstract or Introduction.
4. Avoid Chinese-to-English translation patterns such as comma chains, vague clause stacking, and repeated claims.
5. Replace repeated claims with different support: motivation, mechanism, formula, experiment, or analysis.

### Pass 2: Rigorous narrative logic

1. Define every technical term, abbreviation, model name, and variable before or at first use.
2. After every formula, explain symbols, parameters, inputs, operations, representation sources, and next-step usage.
3. Use explicit transitions to build the story: problem, existing attempts, insufficiency, real requirement, proposed method, concrete steps, and result.
4. Check that figure text, captions, table captions, body text, method names, variables, and metrics are semantically identical.
5. Stress-test the writing from the reviewer's perspective: if a reviewer has one hour before the deadline, no sentence, formula, or figure should require guesswork.

## Revision style

When revising user text:

- Preserve the scientific meaning.
- Prefer clear academic English over ornate phrasing.
- Explain the reason for major changes.
- When useful, return a structured diagnosis with: problem, rewrite, and rationale.
- Do not simply polish vocabulary if the real issue is logic, undefined terms, overloaded sentences, or inconsistent names.

---

## Appendix: course templates and checklists for this lecture

## Concise and Rigorous Academic Writing Checklist

Use this checklist whenever revising, reviewing, or drafting English academic papers.

### 1. Concise expression

#### Sentence-level rules

- Enforce one sentence, one core meaning.
- Split any sentence that simultaneously names a method, states the task, explains motivation, lists implementation details, and claims contributions.
- Prefer a sequence such as:
  1. Name the method and task.
  2. State the method objective.
  3. State the core innovation.
  4. Summarize the method idea.
- Remove implementation detail from Introduction unless it directly explains the core contribution.
- Avoid Chinese-to-English direct translation patterns: comma chains, overloaded clauses, and vague connectors.

#### Repetition rules

- Do not repeat the same claim in Abstract, Introduction, Method, and Experiment.
- Support the same conclusion from different evidence levels:
  - problem analysis in Introduction;
  - mechanism or formula in Method;
  - result and ablation in Experiment;
  - causality and limitation in Analysis.

### 2. Rigorous narrative logic

#### Term definition rules

- Define every technical term, model name, variable name, and abbreviation before or at first use.
- For model names, provide: full name, abbreviation, task, and core concept.
- Do not assume reviewers remember an early non-standard symbol definition if the symbol conflicts with field conventions.

#### Formula rules

After every formula, add a concentrated symbol explanation:

- learned parameters;
- inputs and embeddings;
- variables and dimensions when relevant;
- operations such as concatenation or summation;
- where each representation comes from;
- how the result is used in the next step.

#### Paragraph and section rules

Use explicit transitions to build the paper story:

```text
To alleviate the above problem, ...
However, these methods only ...
In fact, solving this problem requires ...
In this work, we propose ...
Specifically, we first ...
Based on the above representation, we ...
Then, we ...
```

Before finalizing, ask for each paragraph:

- What is this paragraph's job?
- How does it connect to the previous paragraph?
- What does it prepare the reader to understand next?

#### Figure and table rules

- Ensure figure text, figure captions, table captions, and body text use the same names.
- Ensure the figure makes input, output, key process, and innovation visible.
- Ensure tables report metrics and method names exactly as discussed in the text.
- Never leave the reviewer guessing whether a figure, table, and paragraph refer to the same model.

### 3. Reviewer-stress test

Assume the reviewer has one hour before the deadline. The draft must pass this test:

- A reviewer can understand the task and method from the title, abstract, section openings, figures, captions, and tables.
- A reviewer never encounters an undefined model name, symbol, or abbreviation.
- A reviewer can identify the contribution without reconstructing it from implementation details.
- A reviewer can match each experimental result to the exact model/component it evaluates.

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-09-concise-and-rigorous.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
