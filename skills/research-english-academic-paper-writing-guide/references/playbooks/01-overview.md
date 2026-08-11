# Academic Research and English Academic Paper Writing Overview

> Task playbook distilled from 第一讲：学术研究与英文学术论文写作概述 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-01-overview.md`


## Purpose

Apply Lecture 1 of Yu Jing's course `科研与英文学术论文写作指南` as an always-on lens for academic research and English paper-writing tasks.

The lecture's core stance is: before polishing language, diagnose the research value, problem choice, writing logic, reader/reviewer perspective, story closure, revision path, and daily accumulation behind the paper.

## Always-on operating rule

For every relevant response, apply the lecture's stack in this order unless the user explicitly requests only a narrow edit:

1. **Why / values**: Why do this research? Why this problem? Is it a technical problem, incremental work, or academic research?
2. **What / writing logic**: What should be written? What is the role of each paper section? Does the paper map Topic -> Motivation -> Problem -> Method -> Experiments -> Conclusion?
3. **How / writing and revision**: How should the draft be written, revised, and made reviewer-readable?
4. **Norms / English expression**: Only after the logic is sound, improve English for clarity, concision, and rigor.
5. **Accumulation**: Identify what should be accumulated daily instead of being rushed before a deadline.

## Research diagnosis workflow

When the user asks about a research idea, paper plan, proposal, title, abstract, introduction, method, experiment design, or revision, respond using this diagnostic sequence:

1. Classify the work:
   - **Technical problem - walking a wild road**: a practical scenario problem can be solved by combining existing techniques.
   - **Incremental research - touring a scenic route**: work improves on given datasets, metrics, benchmarks, or models but may remain an incremental route.
   - **Academic research - climbing Everest**: work explores a question/path at the boundary of knowledge where no existing route is given.
2. Build the research-to-paper map:
   - Topic = research field / object.
   - Motivation = why this problem matters.
   - Problem = the small, precise unsolved problem found through literature.
   - Method = whether the method is novel enough, good enough, and feasible enough.
   - Experiments = whether evidence is comprehensive and explains strength/weakness plus how/when/why.
   - Conclusion = what is learned, limited, and left open.
3. Check the story closure:
   - Does Abstract/Introduction raise exactly the problem Method/Experiments solve?
   - Are claims, mechanisms, and evidence aligned?
   - Would a reviewer see the same contribution the author sees?
4. Check revision and deadline risk:
   - Is the draft getting clearer across versions, or merely accumulating edits?
   - Is writing being treated as a serious part of the research output, not a last-minute wrapper?

## Paper-writing guidance

When helping write or revise academic text:

- Do not start by rewriting sentences if the problem is actually research logic.
- First identify what a reader/reviewer must understand and in what order.
- Preserve the chain: background -> motivation -> precise problem -> method idea -> evidence -> contribution.
- Flag overlarge claims when experiments or methods cannot support them.
- Make the contribution explicit enough that it cannot be mistaken for a lower-level incremental result.
- After the logic is fixed, polish English for simplicity, rigor, and clean academic tone.

## Classroom reconstruction rule

When reconstructing or summarizing this lecture:

- Do not embed images or link to extracted PNG/JPEG files.
- Convert every slide's visual element into text: slide title, visible text, table contents, visual layout, and teaching function.
- Preserve the transcript's oral logic when the user asks for a faithful reconstruction.
- Use `references/lectures/lecture-01-overview.md` as the canonical markdown reconstruction.

## Default output template for paper help

Use this structure when appropriate:

```markdown
## 1. Why / research positioning
[technical vs incremental vs academic diagnosis]

## 2. Topic -> Motivation -> Problem -> Method -> Experiments -> Conclusion
[map the current work into the lecture framework]

## 3. Story closure check
[where the paper fails or succeeds in making Abstract/Introduction/Method/Experiments align]

## 4. Reader/reviewer perspective
[what a reviewer will understand, miss, or question]

## 5. Revision actions
[ordered actions: logic first, evidence second, English polish last]
```

---

## Appendix: course templates and checklists for this lecture

## Lecture 1 Knowledge Base

Use this reference to apply the first lecture of Yu Jing's course "科研与英文学术论文写作指南" to research and paper-writing tasks.

### Always-on stance

When helping with research or academic writing, do not start from sentence polishing. Start from the lecture's Why -> What -> How stack: values and problem choice, writing logic, writing/revision method, English norms, and daily accumulation.

### Core doctrine

- The first lecture answers Why: why do research and why choose a specific problem.
- High-level academic writing depends first on logic, reader orientation, problem-method-experiment closure, and research value; English polish is downstream.
- Research and paper writing are aligned: Topic -> Motivation -> Problem -> Method -> Experiments -> Conclusion.
- A common failure is turning CCF-A-level research content into a CCF-C-level paper because the story, reader perspective, and evidence chain are weak.

### Three types of work

| Type | Lecture metaphor | Agent behavior |
| --- | --- | --- |
| Technical problem | walking a wild road | Help combine existing methods and make a working path, but do not overclaim academic novelty. |
| Incremental research | touring a scenic route | Identify if the work is only improving on given datasets/metrics/models; push for deeper problem formulation. |
| Academic research | climbing Everest | Ask what boundary of knowledge is being explored and what problem/path did not previously exist. |

### The four-stage growth arc ("四生四世") — use to calibrate advice by career stage

The lecture frames PhD-level growth as four escalating stages, each capped by
a CCF-A paper. Use this to calibrate how much independence to expect from the
user and what kind of help is actually useful at their stage:

1. **Early stage**: advisor-guided. The advisor helps locate the research
   direction, the problem, and a feasible technical route. The user pushes
   one problem to its limit and publishes their first CCF-A. Expect to help
   with execution and diagnosis more than independent problem-selection.
2. **Second stage**: many "unreliable ideas" surface after the first paper.
   The user still cannot independently judge which idea is strong enough for
   a top venue, so they keep discussing with an advisor to converge on the
   next one, then push it to a second CCF-A. Expect to help filter and
   pressure-test candidate ideas, not just execute a chosen one.
3. **Mid stage**: the user stops being satisfied with incremental work and
   spends a long stretch exploring more essential, deeper problems (often
   longer and less certain than the earlier stages) before finding one worth
   a third CCF-A. Expect to help with open-ended problem discovery, not just
   polishing an already-chosen direction.
4. **Late stage**: the user broadens direction and horizon, prepares for
   post-graduation choices (faculty job, research direction for the next
   5-10 years), and — critically — starts training a junior student from
   zero to their own first CCF-A. This is the stage where independent
   team-leading ability matters, not just personal research output.

Do not assume every user is at the early stage. A user mentoring a junior
student, or asking how to evaluate someone else's early-stage idea, is
probably operating at the late stage and needs different help (delegation,
review, teaching) rather than a from-scratch problem-selection walkthrough.

### Target-venue reference (the lecture's own scope, plus adjacent AI subfields)

Use this table to sanity-check whether a stated target venue matches the
paper's actual maturity level (A-class venues expect the A-level orientation
above; a paper that only clears the C-level bar should target accordingly,
not be pushed toward an A-venue submission it is not ready for):

| Direction | Top conferences | Top journals |
| --- | --- | --- |
| Computer Vision / Multimedia | CVPR, ICCV, ECCV, ACM MM, ICASSP, ICMR, ICME (plus ChinaMM, PRCV domestically) | TIP, IJCV, TMM, PR, TCSVT, TOMCCAP, CVIU |
| NLP | ACL, EMNLP, NAACL, COLING, CoNLL, AACL (plus CCL, CCKS, NLPCC, CWMT domestically) | TACL, TASLP, TALLIP, Computer Speech and Language |
| ML / AI | NeurIPS, ICML, ICLR, IJCAI, AAAI | TPAMI, TNNLS |
| Data Mining | SIGMOD, SIGKDD, VLDB, ICDE, SIGIR, CIKM, WWW, WSDM | TKDE, VLDBJ, TKDD |

The lecture's own examples are AI-focused, but the instructor is explicit
that the underlying research logic (how to think about problems, how to
argue for them in writing) transfers across fields even when section
emphasis and structure differ by domain — do not withhold this playbook's
logic-audit approach just because a user's field isn't AI/CS.

### Research value checklist

1. What is the real problem or need?
2. Is the problem merely a task/benchmark improvement, or does it expose a deeper scientific question?
3. What existing path, dataset, metric, or model is being inherited?
4. What is genuinely not solved yet?
5. Can the method be judged as novel enough, good enough, and feasible enough?
6. Can experiments answer How, When, and Why rather than only report a better number?

### Paper diagnosis checklist

- Does the student/author expectation align with advisor/reviewer expectations?
- Is the paper written for the reader, not only for the author?
- Does the writing accurately express the actual research content?
- Does the paper story close the loop from Abstract/Introduction to Method/Experiments?
- Is revision directional, or is the paper getting worse over drafts?
- Was writing planned early enough to avoid deadline compression?

### Response pattern for academic writing help

When asked to help with a paper, proposal, abstract, intro, method, experiment section, title, or research idea, respond using this sequence unless the user explicitly requests a narrower edit:

1. Identify Topic, Motivation, Problem, Method, Experiments, Conclusion.
2. Diagnose whether the work is technical, incremental, or academic in the lecture's sense.
3. Check reader/reviewer perspective: what would be unclear to someone outside the project?
4. Check story closure: does each claim made early have evidence and mechanism later?
5. Then polish language, concision, and wording.

### Source map

- Slide 01: 封面：第一讲：学术研究与英文学术论文写作概述
- Slide 02: 教师与研究组：认知启发的跨模态智能研究组（GogModal）
- Slide 03: 系列报告主要内容
- Slide 04: 为何如此讲英文学术论文写作？
- Slide 05: 进入第一讲主题：学术研究与论文写作
- Slide 06: 什么是学术研究？技术、科研、学术的三种比喻
- Slide 07: 为什么要做学术研究？常见动机的引入
- Slide 08: 为什么要做学术研究？三层能力：方法论、认知力、价值观
- Slide 09: 学术研究修炼之路——四生四世
- Slide 10: 学术研究修炼之路——第一篇论文的诞生
- Slide 11: 我们的论文出了什么问题？认识不一致
- Slide 12: 我们的论文出了什么问题？写给自己看，别人看不懂
- Slide 13: 我们的论文出了什么问题？无法准确表达研究内容
- Slide 14: 我们的论文出了什么问题？Story难以自圆其说
- Slide 15: 我们的论文出了什么问题？写作拖延，赶不上deadline
- Slide 16: 我们的论文出了什么问题？不知道如何逐步完善
- Slide 17: 我们的论文出了什么问题？高水平研究内容被写成低水平论文
- Slide 18: 我们的论文出了什么问题——小结
- Slide 19: 我们的目标——AI领域主要会议及期刊
- Slide 20: 结束页：交流方式

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-01-overview.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
