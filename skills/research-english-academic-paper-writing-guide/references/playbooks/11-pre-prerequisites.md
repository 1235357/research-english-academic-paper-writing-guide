# Prerequisites for Thinking About Innovative Research Points

> Task playbook distilled from 第十一讲前加餐：思考创新性研究点前务必知道的那些事儿 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-11-pre-prerequisites.md`


## Purpose

Apply Yu Jing's lecture framework for turning early research ideas into defensible academic work. Treat every research or paper-writing task as a chain:

```text
real need -> scientific problem -> solution method -> experiment -> paper writing
```

The goal is to prevent shallow innovation claims, pseudo-needs, method chasing, and introduction logic that cannot convince reviewers.

## Default workflow

1. **Identify the real need.** State the task-level, domain-level, or cross-domain need. Ask whether the need is field-recognized and scenario-grounded.
2. **Identify the scientific problem.** Convert the need into an essence-level question about cause, mechanism, condition, representation, association, generalization, bias, or efficiency.
3. **Identify the method.** Explain whether the method contributes through data, model, objective/loss, or learning framework, and why it targets the scientific problem.
4. **Check the evidence.** Require mechanism-oriented experiments, ablations, visualizations, or analysis, not only sota results.
5. **Express the paper logic.** For introductions and summaries, use: real need -> scientific problem -> existing gap -> proposed method -> evidence.

## Mandatory diagnostic questions

Use these questions whenever evaluating a user's idea, draft, title, abstract, introduction, method section, experiment section, or research plan:

- is the stated demand a real field-recognized need, or a pseudo-need invented to justify a method?
- is the stated problem a scientific problem, or merely a demand, performance symptom, parameter-tuning issue, or technical gap?
- is the method designed around the scientific problem, or is it an "a task + b method = c method" combination?
- can every method component be tied to a contribution toward solving the scientific problem?
- do the experiments explain why the method works, or do they only report performance?

## Common corrections

| weak expression | diagnose as | stronger direction |
| --- | --- | --- |
| this task needs to be faster | demand, not scientific problem | ask what mechanism causes inefficiency and what must be filtered, represented, or approximated |
| this model has low accuracy | technical symptom | ask why accuracy drops under specific data/task/model conditions |
| this task needs feature fusion | unsupported demand | ask why fusion is needed and what kind of fusion matches the task mechanism |
| this dataset has bias | possible pseudo-need | ask whether the bias is a dataset collection artifact or a general task-level problem |
| we add knowledge to this task | method-first framing | ask whether knowledge is needed, when it is needed, and how it changes reasoning or representation |

## Response pattern

When the user asks for research help, structure the answer around this compact audit unless a different format is explicitly required:

```markdown
## 1. real need
[state the need and whether it is credible]

## 2. scientific problem
[rewrite the essence-level problem]

## 3. solution method
[explain the data/model/objective/learning-method route]

## 4. evidence needed
[list the experiments or analyses needed to support the claim]

## 5. paper-writing expression
[give a directly usable sentence or paragraph for the paper]
```

---

## Appendix: course templates and checklists for this lecture

## Lecture framework: real need, scientific problem, effective method

This reference distills the lecture into reusable decision rules for research and academic writing tasks.

### Core chain

Always analyze research ideas through this chain:

```text
real need -> scientific problem -> solution method -> experiment -> paper writing
```

Do not let the chain collapse into method chasing or slogan-level problem statements.

### Definitions

- **real need**: a field-recognized task, application, or capability requirement, such as accuracy, speed, quality, low-resource use, stability, reliability, or cross-domain generality. It must be grounded in a real scenario, not invented to justify a method.
- **scientific problem**: the underlying mechanism, cause, condition, or essential bottleneck behind the need. It should ask why, under what conditions, what mechanism, or what form of representation/association/generalization is required.
- **solution method**: a data, model, objective/loss, learning framework, or experimental design that directly targets the scientific problem.

### Three-one thinking

Before endorsing a research idea, require:

1. one field-recognized real need;
2. one essence-level scientific problem;
3. one effective method that directly targets the problem.

### Common failure modes

- mistaking a demand for a problem: "the task needs fast retrieval" is not a scientific problem.
- mistaking a technical issue for a scientific problem: "the model accuracy is low" is not enough; ask why and under which conditions.
- forcing a known problem into another task because the tasks look related.
- forcing a fashionable method into a task and calling it innovation: "task a + method b = method c".
- creating pseudo-needs, such as claiming a task lacks knowledge without proving when knowledge is needed.
- reporting only sota without analyzing why the method works.

### Research idea audit workflow

1. **state the real need**: identify the task level, domain level, or cross-domain level need. Ask whether it is field-recognized and scenario-grounded.
2. **state the scientific problem**: convert the need into an essence-level bottleneck. Ask why the bottleneck exists and what mechanism must be understood.
3. **state the method**: identify whether the contribution is in data, model, objective/loss, or learning method. Explain why the method should solve the scientific problem.
4. **state the evidence**: require experiments that analyze causes, mechanisms, and conditions, not only performance scores.
5. **state the writing logic**: in the introduction, present need -> scientific problem -> existing method gap -> proposed method.

### Positive formulation examples

| weak formulation | stronger formulation |
| --- | --- |
| this model has low accuracy | why does this model have low accuracy under these data/task conditions? |
| this task needs feature fusion | why does this task need feature fusion, and what kind of fusion matches the task mechanism? |
| this dataset is biased | is the bias caused by data collection, or is it a general task-level bias that affects model behavior? |
| this task lacks knowledge | does the task actually require external knowledge, and under what scenario does knowledge help? |

### Output style for research coaching

When using this skill in answers, prefer:

- a compact diagnosis of demand/problem/method;
- a table separating real need, scientific problem, method, evidence, and writing expression;
- explicit warnings about pseudo-demand, technical-problem confusion, and a+b=c method composition;
- one improved formulation the user can directly put into a paper introduction.

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-11-pre-prerequisites.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
