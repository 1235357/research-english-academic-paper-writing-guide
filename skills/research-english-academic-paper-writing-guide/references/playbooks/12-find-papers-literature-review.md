# How to Find Papers and Conduct Literature Review

> Task playbook distilled from 第十二讲：学术研究之创新性研究点——如何找论文与进行文献调研？ of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-12-find-papers-literature-review.md`


## Core rule

Treat every academic research task as a three-axis positioning problem:

```text
practical demand -> scientific problem -> solution method
```

Never jump directly from a task/dataset to a method tweak. First identify the real demand, then distill the scientific problem, then evaluate methods as attempts to solve that scientific problem.

## Default workflow

Use this sequence unless the user explicitly asks for a narrower operation.

1. **Demand stage - clarify what is being studied.**
   - Start from influential tasks, benchmarks, datasets, tutorials, workshops, surveys, and seed papers.
   - Build an evolution line of tasks and technical capabilities.
   - Answer the demand 5w+1h questions in the literature-review workflow appended below.

2. **Scientific-problem stage - distill the essential problem.**
   - Group tasks by shared underlying scientific problems, not by method names.
   - Ask what problem each paper is really answering, what subproblem it isolates, and how well the claim is supported.
   - Build a mind map: scientific problem -> subproblem -> papers -> evidence.

3. **Method stage - map how problems have been solved.**
   - Only after the scientific problem is clear, follow method generations and technical routes.
   - Evaluate each method by whether it genuinely solves the scientific problem, not by whether it has incremental room for module-level edits.
   - Identify limitations, missing perspectives, and experimental gaps.

4. **Innovation stage - locate the empty cell.**
   - Express each candidate idea as:
     `one practical demand + one scientific problem + one method perspective`.
   - Prefer ideas where existing methods have a principled limitation, a core problem remains unsolved, or an actual demand has not yet been proposed or verified.

## Anti-patterns to prevent

Reject or explicitly correct these literature-review patterns:

- reading only 1-2 seed papers and treating them as the field;
- searching only 1-2 obvious keywords;
- downloading massive paper piles and reading linearly;
- reading every paper with the same surface checklist of model, experiment, result;
- forming a scattered paper list without a research-system map;
- trusting a top-conference paper without asking whether it solves a real problem and whether it truly solves it;
- describing a contribution as a method patch instead of a scientific-problem answer.

## Two illustrations from the lecture worth using directly with users

**The cooking analogy**, for explaining *why* unstructured, linear reading
fails: reading papers without a framework is like cooking many different
dishes without ever reflecting on why each one works — how meat dishes
differ from vegetable dishes, what each seasoning actually contributes.
Someone who cooks ten dishes this way is no closer to inventing a new dish
than someone who cooked only one. Reading one paper and reading ten papers
with the same flat "what model, what experiment, what result" checklist
produces the same shallow outcome either way — the number of papers read
does not by itself build the ability to solve a *different* but related
problem.

**The "monkeys reaching for the moon" story** (the instructor credits a
cartoon by Zhu Songchun / 朱松纯, drawn by his daughter), for explaining the
hardest literature-review skill: distinguishing papers that solve a *real*
problem from ones dressed up to look like they do. Different monkeys try to
reach the moon differently: one climbs a tree (fast short-term progress,
but a tree cannot reach the moon); one scoops at the moon's reflection in
water (looks like the moon, is not); one builds a hot-air balloon (gets
closer, still fundamentally the wrong approach for reaching an actual
celestial body); a rare few study orbital mechanics and astronomy and build
a rocket. From the outside, the tree-climber and the rocket-builder can both
look like they're "making progress" — the difference only shows up when you
ask whether the underlying approach could *actually* reach the goal. Some
published papers found a genuinely sound path to a real problem; others
took an existing trendy model, tried it, and wrapped the result in an
elaborate-sounding story. Telling these apart — not just collecting more
papers — is the actual skill this lecture is trying to build.

## Paper selection heuristics

Prioritize papers that meet most of these conditions:

- relevant to the user's target task or demand;
- answer a fundamental **why** question rather than only an incremental **how** solution;
- written by a team with sustained work in the area;
- recognized by top conferences/journals, high citations, best-paper signals, tutorials, surveys, or benchmark adoption;
- provide a clear claim-evidence chain: premise -> evidence -> conclusion.

## Output style

When responding to the user, produce structured research guidance rather than a raw bibliography. A strong answer usually contains:

1. the demand map;
2. the scientific-problem map;
3. the method-generation map;
4. a prioritized reading order;
5. a table of candidate innovation gaps;
6. experiments needed to verify whether the proposed gap is real.

Use the output templates appended below when the user asks for a literature-review plan, paper-reading plan, innovation-point analysis, or related-work structure.

---

## Appendix: course templates and checklists for this lecture

## Literature Review Workflow from Lecture 12

Use this file when a user asks for paper search, literature review, innovation-point analysis, research positioning, or related-work planning.

### 1. Demand stage: understand the practical demand

Goal: locate the task and capability evolution before reading methods.

Start from influential datasets, benchmarks, tutorials, workshops, surveys, and seed papers. For each task or dataset, answer:

1. **why** - what AI capability does this task want the model to have?
2. **what** - what are the inputs, outputs, and evaluation metrics?
3. **what** - what core concepts and related concepts does the task introduce?
4. **how** - what are the baseline models and their basic technical ideas?
5. **what, reflective** - what scientific problem must be solved to reach the target capability?
6. **where, reflective** - what technical challenges remain unsolved or unverified?

Demand-stage deliverables:

- task/dataset evolution timeline;
- capability evolution summary;
- dataset limitations and bias risks;
- match/mismatch with the user's target;
- whether the task has follow-up research space.

### 2. Scientific-problem stage: distill the essential problems

Goal: convert scattered tasks into recognized core scientific problems.

Ask:

1. what is the task's scientific problem?
2. what sub-tasks does it contain, and what scientific problem corresponds to each sub-task?
3. where is each scientific problem in its maturity level: well-studied, timely, emerging, or not yet formulated?
4. how have existing papers tried to solve each scientific problem?

Do not rely passively on tutorials or surveys. Scientific problems are often implicit. Read claims, motivations, examples, failure cases, and experiments to infer the real problem.

Scientific-problem deliverables:

- problem -> subproblem -> papers mind map;
- maturity classification;
- available datasets for verification;
- open research space;
- precise definitions of key concepts and their scope.

### 3. Method stage: map methods as answers to scientific problems

Goal: understand why methods solve or fail to solve the scientific problem.

For each method, answer:

1. **why** can the method solve the scientific problem?
   - premise;
   - evidence;
   - conclusion;
   - concept definition and scope;
   - how experiments support the claim.
2. **what** is the basic technical idea?
3. **what** generation of technology does it belong to?

Method-stage deliverables:

- method-generation timeline;
- method -> scientific problem mapping;
- limitations grounded in problem-solving, not module-level preferences;
- related fields or tracks that solve similar problems;
- candidate transferable ideas.

### 4. Innovation-stage decision questions

After the three maps are built, identify innovation points by asking:

1. which methods have principled limitations on a specific problem?
2. which core scientific problems remain unsolved?
3. which practical demands have not yet been proposed, verified, or evaluated well?
4. what experiments would prove the proposed gap is real?
5. how can the contribution be stated as a scientific-problem answer rather than a method patch?

### 5. Follow strategy

Use these follow routes to expand from seed papers:

- follow the research teams that proposed important datasets or tasks;
- follow highly cited papers that use those datasets;
- follow related top-conference tracks from adjacent fields such as CV, NLP, IR, ML, HCI, robotics, or domain-specific venues;
- follow related work and citing work of classic papers;
- compare multiple tutorials from different communities to avoid a single-field bias.

## Output Templates

Use these templates to keep research guidance consistent.

### A. Literature review plan

```markdown
# Literature Review Plan: [Topic]

## 1. Practical demand map
| task/dataset | year | input | output | evaluation | target capability | limitations | relevance |
|---|---:|---|---|---|---|---|---|

## 2. Scientific-problem map
| scientific problem | subproblem | evidence papers | maturity | verification datasets | open space |
|---|---|---|---|---|---|

## 3. Method-generation map
| generation | representative methods | problem addressed | why it works | limitation |
|---|---|---|---|---|

## 4. Reading order
1. [tutorial/survey] - why first:
2. [dataset/task paper] - why second:
3. [classic problem paper] - why third:
4. [method-generation paper] - why next:
5. [recent critical paper] - why last:

## 5. Candidate gaps
| gap | demand | scientific problem | method limitation | evidence needed | risk |
|---|---|---|---|---|---|
```

### B. Single-paper reading report

```markdown
# Paper Reading Report: [Paper]

## 1. What demand does it address?

## 2. What scientific problem does it claim to solve?

## 3. Is the paper answering why, or only proposing how?

## 4. Method logic
- premise:
- evidence:
- conclusion:

## 5. Experiments and evidence
- what is directly proven:
- what is only implied:
- what remains unverified:

## 6. Position in the field map
- related demand:
- related scientific problem:
- method generation:
- predecessor papers:
- successor papers:

## 7. Usefulness for our research
- can follow:
- should avoid:
- possible gap:
```

### C. Innovation-point analysis

```markdown
# Innovation Point Analysis

## Candidate idea
[one-sentence idea]

## Three-axis location
- practical demand:
- scientific problem:
- solution-method perspective:

## Why this is not just incremental

## Evidence from literature

## Existing methods' principled limitation

## New perspective

## Required experiments

## Possible rejection risks

## Paper-positioning sentence
```

### D. Related-work section outline

```markdown
# Related Work Outline

## 1. Demand evolution
[explain tasks/datasets and capability changes]

## 2. Scientific problems behind the demand
[organize by core problem, not by method names]

## 3. Existing method routes
[show method generations as attempts to solve the problems]

## 4. Gap and transition to our method
[precisely state what remains unsolved and why]
```

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-12-find-papers-literature-review.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
