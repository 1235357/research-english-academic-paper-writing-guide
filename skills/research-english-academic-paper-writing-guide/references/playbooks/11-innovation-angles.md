# From Which Angles to Think About Innovative Research Points

> Task playbook distilled from 第十一讲：学术研究之创新性研究点——从哪些角度思考创新性研究点？ of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-11-innovation-angles.md`


## Purpose

Use this skill to turn an early research idea, paper draft, method design, or experiment plan into a rigorous academic argument using the Lecture 11 framework from Yu Jing's course `科研与英文学术论文写作指南`.

The core chain is:

```text
real demand -> scientific problem -> solution method -> validation evidence
```

Never let a research idea stop at a method name or a performance improvement. Always force the idea to explain the demand, the essence-hitting scientific problem, and the mechanism by which the method cuts into that problem.

## Workflow

1. **Classify the user's idea.** Decide whether it currently starts from a real demand, a scientific problem, or a solution method.
2. **Recover the missing levels.** If the user only provides a method, infer or ask for the real demand and scientific problem. If the user only provides a demand, derive the scientific problem and possible method families.
3. **Audit the demand.** Reject pseudo-demand. Ask whether the demand is field-recognized, scenario-grounded, and not merely a dataset artifact.
4. **Audit the scientific problem.** Rewrite technical-problem wording into mechanism-level scientific-problem wording.
5. **Audit the method.** Map every method component to data, model, objective function, or learning method. Require a mechanism explanation for why it works.
6. **Design validation.** Require SOTA comparison, ablation, and at least one mechanism-oriented analysis.
7. **Return an actionable paper logic.** Output a refined research point, introduction chain, method rationale, and experiment checklist.

## Mandatory Standards

A valid innovative research point must satisfy the three-one standard:

1. one field-recognized real demand;
2. one essence-hitting scientific problem;
3. one effective method that cuts into the problem.

Reject or revise ideas that confuse:

- real demand with scientific problem;
- scientific problem with technical problem;
- true demand with pseudo-demand;
- method transfer with real innovation.

## Response Pattern

When analyzing a user's research idea, respond with:

```markdown
## Diagnosis
[identify whether the current idea is demand-level, problem-level, or method-level]

## Reconstructed Logic Chain
- Real demand: ...
- Scientific problem: ...
- Solution method: ...
- Validation evidence: ...

## Three-One Verdict
- Field-recognized real demand: pass / weak / missing
- Essence-hitting scientific problem: pass / weak / missing
- Effective method cutting into the problem: pass / weak / missing

## Revision
[rewrite the research point as a stronger one-sentence academic claim]

## Experiments Needed
[list mechanism-oriented experiments, not only SOTA]

## Risks
[list pseudo-demand, method-first, technical-report, or under-analysis risks]
```

## Style

Be strict and diagnostic. Preserve the user's research direction when possible, but do not flatter weak logic. Prefer concrete rewrites and checklists over abstract advice.

---

## Appendix: course templates and checklists for this lecture

## Lecture 11 Framework: Finding Innovative Research Points

Use this reference when applying the skill to a user's paper idea, research direction, introduction draft, method section, experiment plan, or literature-review notes.

### Core chain

Every research point must be audited as:

```text
real demand -> scientific problem -> solution method -> validation evidence
```

Do not allow the user to collapse these levels.

### Three innovation sources

#### 1. Innovation from solution method

Use when the task and scientific problem are already established.

Check four dimensions:

| dimension | audit question | valid contribution pattern |
| --- | --- | --- |
| data | does the bottleneck come from data bias, noise, scarcity, sampling, annotation, or distribution shift? | resampling, relabeling, weak supervision, synthetic data, data filtering, data rebalancing |
| model | does the model need a new structure or mechanism to learn the right evidence and suppress spurious correlation? | causal modeling, hierarchy, graph modeling, modular reasoning, stable representation |
| objective function | does the learning signal reward the wrong behavior or ignore important cases? | reweighting, auxiliary tasks, contrastive losses, curriculum losses, task-specific constraints |
| learning method | is the one-shot learning process unsuitable for the task? | feedback learning, curriculum learning, reinforcement learning, iterative correction, teacher-student learning |

Never stop at `method works`. Require the mechanism explaining why it works.

**Why auxiliary objectives work — a cognitive-psychology anchor for the
objective-function row.** The lecture motivates auxiliary/multi-task
objectives with a real memory experiment: subjects are shown a list of
words to memorize. One group simply memorizes and recalls; a second group,
while memorizing, must also classify each word's emotional valence
(positive / negative / neutral) before later recall. The second group
recalls significantly more accurately — being forced to process the
material one level deeper, even via a nominally unrelated side task,
strengthens retention of the primary task. The machine-learning parallel:
an auxiliary task that forces a model to process its representation more
deeply (not just optimize the headline objective directly) can improve
performance on the main task itself, which is the mechanism-level reason
"add an auxiliary task" is a real contribution and not just complexity for
its own sake. When a user proposes an auxiliary loss or multi-task setup,
ask what deeper processing it forces, not just whether it improves a
number.

#### 2. Innovation from scientific problem

Use when the task is known but the user may be able to define a better problem.

Two routes:

1. Same task, different processing perspectives.
   - Example: visual question answering can involve unified cross-modal representation, cross-modal association, or common-sense knowledge selection.
2. Same task, different real demands.
   - Example: scene graph generation can target high quality, low resource, or fast generation; each produces a different scientific problem.

Reject technical-problem wording:

| technical or weak wording | scientific-problem wording |
| --- | --- |
| model accuracy is low | why is the model accuracy low? what mechanism causes the failure? |
| tune model parameters | under what conditions or mechanisms can the model be optimized? |
| fuse features | why and how should features be fused to solve the core problem? |

#### 3. Innovation from real demand

Use when the user is defining a new task, dataset, benchmark, setting, or research direction.

Demand levels:

1. task-specific demand: faster, more accurate, less annotation, better robustness in a specific task;
2. field-general demand: common needs across many tasks in a field, such as pretraining, knowledge use, zero-shot reasoning;
3. cross-domain universal demand: stability, reliability, safety, interpretability, generalization.

Reject pseudo-demand by asking:

- is this demand recognized by the field or only invented to justify the method?
- is it a real-world/field need or just a dataset artifact?
- what scenario requires this demand?
- what literature or benchmark shows this demand matters?

### Three-one standard

A strong research point must contain:

1. one field-recognized real demand;
2. one essence-hitting scientific problem;
3. one effective method that cuts into the problem.

If any item is missing, help the user revise the research point before writing.

## Research Point Canvas

Copy this canvas when a user wants to develop a research idea.

### 1. Real Demand

- Task/domain:
- Real scenario:
- Who needs it or why the field recognizes it:
- Evidence from literature/benchmarks/applications:
- Why it is not merely a dataset artifact:

### 2. Scientific Problem

- Observed failure or bottleneck:
- Underlying mechanism or cause:
- Why existing methods do not solve it:
- Whether the problem is well-studied, timely, emerging, or not yet proposed:

### 3. Solution Method

- Data-level design:
- Model-level design:
- Objective-function design:
- Learning-method design:
- Which design is the central contribution:

### 4. Mechanism Explanation

- Why this method should solve this scientific problem:
- What assumptions it relies on:
- What would falsify the claimed mechanism:

### 5. Experiments

- SOTA comparison:
- Ablation:
- Mechanism/diagnostic analysis:
- Robustness or generalization:
- Error analysis:

### 6. Paper Story

- Title candidate:
- Abstract one-sentence summary:
- Introduction logic chain:
- Main contribution bullets:

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-11-innovation-angles.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
- Helper script: `scripts/new_research_point_canvas.py [-o out.md]` — generate a blank research-point canvas.
