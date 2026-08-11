# Related Work and Method

> Task playbook distilled from 第四讲：英文学术论文之写作思路——相关工作和方法 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-04-related-work-and-method.md`


## Core behavior

Use this skill to audit, rewrite, or plan the Related Work and Method/Methodology parts of an English academic paper according to Yu Jing's lecture-four standard: do not list papers or steps; build a coherent chain from topic to problem to method to contribution, and make problem-method-experiment mutually responsive.

Always start by identifying the paper's actual task, exact research problem, method family, core contribution, and intended reader/reviewer. Then apply the workflows below.

## Workflow

1. **Establish the paper focus**
   - Extract the task/domain, target scientific or technical problem, method family, claimed novelty, and evaluation goal.
   - Separate actual demand, scientific problem, technical method, and implementation detail.
   - Ask for missing paper context only when the section cannot be judged from the given material.

2. **Related Work workflow**
   - Build the Related Work dimensions from the paper itself: task-related topics, problem-related work, and method-related work.
   - Reject bibliography-like paragraphs that say only "A did X, B did Y, C did Z".
   - Group prior work by routes, mechanisms, assumptions, data settings, or limitations.
   - For each route, state the shared idea, representative works, what problem it solved, what remains unsolved for this paper's target problem, and how the current work differs.
   - Ensure Related Work complements Introduction: Introduction motivates the problem; Related Work systematically positions the work.

3. **Method workflow**
   - Require a problem formulation before module details: task, inputs, outputs, external resources, prediction target, and notation.
   - Require a framework-level overview before formulas or implementation steps.
   - Map figure modules to section/subsection headings. The figure, headings, equations, and prose must locate each other.
   - For every module, state motivation, goal, input, output, design, connection to previous/next modules, and why this design is preferable to plausible alternatives.
   - Split long modules into subheadings such as question-guided node attention, edge attention, and graph convolution when the procedure is complex.
   - Allocate space according to novelty: core innovation gets detailed explanation; routine preprocessing and standard losses stay concise.

4. **Problem-method-experiment consistency check**
   - Verify that each method module traces back to a stated problem or motivation.
   - Verify that each key design is supported by theory, mechanism explanation, ablation, visualization, or analysis.
   - Flag SOTA-only experiments that do not explain why the method works.

5. **Output format**
   - For an audit: produce "Major structural issues", "Related Work fixes", "Method fixes", and "Concrete rewrite plan".
   - For rewriting: preserve technical meaning, rewrite into route-based Related Work or motivation-first Method prose, and label any assumptions.
   - For planning: produce section headings, paragraph purposes, and the logic each paragraph must establish.

## Non-negotiable lecture principles

- Related Work includes only papers needed to understand the current paper's themes and problem. Do not include every paper the author has read.
- Related Work must classify and synthesize. It must not become a reading list.
- Same-topic work must be grouped into methods/routes and summarized for current-paper relevance.
- Every Related Work subsection should end by connecting existing limitations to the current paper's difference or contribution.
- Method should be written from the reader/reviewer perspective, not from the author's implementation chronology.
- Method begins with mathematical or formal problem definition, then model overview, then module details.
- Module headings should expose implementation logic and novelty, and should correspond to the framework figure.
- Every process first explains its motivation and goal, then details the design.
- For each non-obvious design, explain why this design is used rather than alternatives such as concatenation, bilinear mapping, simple fusion, or a generic model variant.

---

## Appendix: course templates and checklists for this lecture

## Lecture Core: Related Work and Method

This reference distills lecture four of "Research and English Academic Paper Writing Guide" into reusable standards.

### 1. Related Work: what to cover

Related Work must cover the work needed to understand the current paper, not every paper the author has read. Identify three layers:

1. **Task-related work**: the broader task or domain. Example: Visual Question Answering.
2. **Problem-related work**: prior attempts at the exact challenge emphasized in the paper. Example: Fact-based Visual Question Answering methods that introduce or reason over external facts.
3. **Method-related work**: technical families used by the paper. Example: Heterogeneous Graph Neural Networks.

Only include other dimensions such as data, loss functions, or optimization when they are essential to the paper's problem or contribution.

### 2. Related Work: how to write

Use classification and synthesis:

- Divide the literature into dimensions or routes.
- Within one theme, summarize the technical route and representative works.
- State what problem the route solved.
- State what remains insufficient for the current paper's target problem.
- End by distinguishing the current work.

Avoid list-like prose:

```text
A proposed ..., B proposed ..., C proposed ... .
```

Prefer synthesis:

```text
Existing methods can be broadly grouped into ... . Early methods ... . Later methods ... . However, for [current problem], these methods still ... . In contrast, our work ... .
```

### 3. Related Work vs Introduction

- **Introduction** uses existing work to motivate the paper's challenge and contribution.
- **Related Work** uses existing work to systematically locate the paper among task, problem, and method traditions.

If the two sections repeat, compress the Introduction around the central motivation and expand Related Work around categorized comparison.

### 4. MuCKO case pattern

The lecture's case paper, MuCKO, uses three Related Work dimensions:

1. **Visual Question Answering**: broad VQA routes such as CNN-RNN, global features, attention, and graph-structured visual reasoning. The limitation is that these do not sufficiently solve external-knowledge and fine-grained multimodal evidence needs.
2. **Fact-based Visual Question Answering**: direct FVQA work such as query-mapping and learning-based methods. The limitation is that visual information may be used only for fact retrieval or provided wholesale, introducing noise.
3. **Heterogeneous Graph Neural Networks**: method-family work. The limitation is that conventional heterogeneous graphs usually model typed nodes and edges in one unified graph, while MuCKO uses multiple modality-specific graph layers.

### 5. Method: required structure

A Method section should follow this order:

1. Problem formulation: task, input, output, external resources, answer space, notation.
2. Model overview: framework modules and their connections.
3. Module-level subsections: motivation, goal, input/output, design, equations, and connection.
4. Learning/training: concise unless it is part of the novelty.

### 6. Method: module rules

For every module, answer:

- What problem does this module solve?
- Why is the module necessary?
- What does it take as input and produce as output?
- What is the core operation?
- How does it connect to previous and next modules?
- Why this design instead of plausible alternatives?

### 7. Figure-text consistency

The framework figure should define the writing structure. Section headings, module names, and formulas should correspond to figure elements. A reviewer should be able to move from figure to text and from text to figure without searching.

### 8. High-level vs weak writing

High-level writing: problem, method, and experiments respond to one another.

Weak writing: problem, method, and experiments each speak independently. Symptoms include generic motivation, step-by-step method lists, and SOTA-only experiments without analysis.

## Templates and Checklists: Related Work and Method

### Related Work planning template

```text
Paper task/domain:
Exact research problem:
Core method family:
Main contribution:

Related Work dimensions:
1. [Broad task-related work]
   Purpose:
   Routes to compare:
   Limitation to connect:

2. [Exact problem-related work]
   Purpose:
   Routes to compare:
   Limitation to connect:

3. [Method-related work]
   Purpose:
   Routes to compare:
   Limitation to connect:
```

### Related Work paragraph template

```text
[Topic sentence: define the family and why it matters to the current paper.]
Existing studies can be broadly grouped into [route A] and [route B]. [Route A] methods [shared mechanism], which [benefit]. However, [limitation under current paper's problem]. [Route B] methods address this by [mechanism], but they still [remaining gap]. Different from these methods, our work [current distinction/contribution].
```

### Related Work audit checklist

- Does every cited work serve the current paper's task, problem, or method?
- Are works grouped by route/mechanism instead of listed by author?
- Does each group state its limitation for the current target problem?
- Does the section explain the current work's difference from prior work?
- Is there unnecessary overlap with Introduction?
- Are all cited works actually understood well enough to evaluate from this paper's angle?

### Method opening template

```text
Given [input symbols], the task aims to [objective]. Formally, [define candidate set / knowledge base / labels / outputs]. During inference, [prediction rule].

As illustrated in Figure X, our method consists of [module 1], [module 2], and [module 3]. [Module 1] aims to ... . [Module 2] then ... . Finally, [module 3] ... .
```

### Method module template

```text
### [Module Name]

Motivation and goal. [State why this module is needed and what exact subproblem it solves.]

Input/output. Given [input], this module produces [output].

Design. To achieve this goal, we [operation]. [Equation/algorithm if needed.]

Connection. The resulting [output] is passed to [next module] to [next purpose].

Design rationale. Compared with [alternative], this design better fits [problem property] because [mechanism/theory/evidence].
```

### Method audit checklist

- Is problem formulation present before method details?
- Are all variables and inputs/outputs defined before use?
- Is there a model overview before equations?
- Do section headings align with the framework figure?
- Does every module begin with motivation and target?
- Does every module have clear input/output boundaries?
- Are long procedures split into smaller titled steps?
- Is space allocated according to novelty?
- Are plausible alternatives discussed or experimentally tested?
- Do experiments verify each key design, not only overall SOTA?

### Rewrite patterns

#### Bad Related Work pattern

```text
A proposed method X. B proposed method Y. C proposed method Z. These methods have limitations.
```

#### Better Related Work pattern

```text
Prior work on [topic] mainly follows two routes. The first route [shared idea] and is effective for [setting], but it assumes [assumption] and therefore struggles with [current problem]. The second route [shared idea] relaxes this assumption by [mechanism], yet it still [remaining gap]. Our method differs by [specific distinction].
```

#### Bad Method pattern

```text
First, we extract features. Second, we concatenate them. Third, we feed them into a classifier.
```

#### Better Method pattern

```text
To address [subproblem], we first construct [representation] so that [desired property]. Given [input], the module outputs [output]. Instead of simple concatenation, we use [design] because [problem-specific rationale]. This representation is then used by [next module] to [purpose].
```

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-04-related-work-and-method.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
