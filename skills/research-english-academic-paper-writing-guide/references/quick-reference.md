# Course-wide quick reference

Compact rules distilled from the whole course. For task-specific workflows
use `references/playbooks/`; for full lectures use `references/lectures/`.

## 1. Separate three concepts

- **Actual need (需求)**: the real task demand — accurate, fast, robust,
  interpretable, safe, useful in an application.
- **Scientific problem (科学问题)**: the mechanism-level challenge behind
  that need.
- **Solution method (方法)**: the technical path designed to address the
  scientific problem.

Never replace a scientific problem with a metric target such as "improve
accuracy". Never start from a trendy method and look for a task to attach it
to.

## 2. Problem chain template (use before writing or revising)

1. In this field/task, the broad background is ...
2. The actual need is ...
3. The scientific problem behind this need is ...
4. Existing work mainly follows ...
5. These methods cannot solve ... because ...
6. The key insight of this work is ...
7. The method implements the insight through ...
8. Experiments verify ...
9. The boundary or limitation is ...

## 3. A-level versus ordinary papers

A strong paper: focuses on a frontier or essential problem; designs the
method around the core challenge; explains why each component is necessary;
verifies motivation, mechanism, and boundaries; and keeps title, abstract,
introduction, method, and experiments telling one story.

A weak paper: follows a hot topic without a clear scientific problem; makes
a small incremental change; reports only SOTA or small gains; lacks
analysis; confuses background need, related-work limitation, and its own
problem. The classic C-level pattern to reject: "everyone studies it →
step1/step2/step3 → we reach SOTA".

## 4. Section checklists

### Title
- States the problem or task addressed.
- Reflects the key innovation without being overly technical.
- Concise (≈15 words or fewer), no vague/inflated wording, no unverified
  absolute-novelty claims.
- A memorable model/method name plus subtitle often protects the
  contribution.

### Abstract (five slots, ≈200 words)
1. Task challenge or motivation.
2. Existing method line and its limitation.
3. Key insight or proposed method.
4. Concrete technical highlights in logical order.
5. Main evidence plus broader value.

The abstract is the expansion of the title and the compression of the
introduction.

### Introduction (five parts)
1. Broad background → 2. important need/challenge → 3. existing work and its
dominant assumption → 4. the unresolved scientific problem → 5. this paper's
insight, method, and contributions.

Common failures: background too broad and never narrows; related-work issues
repeated without the paper's distinct gap; method appears unmotivated;
contributions list modules rather than scientific value.

### Related work
Write by dimensions (task-, problem-, method-related; technical route or
assumption; data/model/objective/learning strategy), never a chronological
list. For each group: shared idea → limitation → relation to this paper.
End each group by connecting the limitation to this paper's difference.

### Method
Define first: task and notation, input/output, core challenge, overview,
modules with motivations. For every component answer: why needed, what
problem it solves, how it works, how it connects to other components, how it
will be verified. Avoid a step-by-step engineering recipe with no
motivation. Allocate space by novelty, not by implementation effort.

### Experiments
Required evidence: overall effectiveness; fair baselines grouped by route;
ablation for each core component (grouped by design dimension); analysis of
why the method works; qualitative/visualization evidence with statistics;
robustness/generalization/interpretability when claimed; limitations.
Analysis order: conclusion first → supporting evidence → mechanism →
exceptions. Be honest: no cherry-picked runs or examples.

### Conclusion and references
Conclusion: restate problem and insight, summarize verified findings, state
limitations and future work without weakening the contribution; do not
repeat the abstract. References: cite actual sources of ideas, tasks,
datasets, metrics, baselines, claims; no decorative citations; check format,
names, venues, years against official bibliographic sources.

## 5. Academic English norms

**Concise:** one sentence, one main idea; direct subject–verb–object;
remove repetition; do not translate Chinese sentence patterns literally;
avoid stacked clauses.

**Rigorous:** distinguish facts, assumptions, observations, explanations,
conclusions. Useful patterns: "we observe that ...", "existing methods often
assume ..., which may fail when ...", "to address this issue, we ...",
"the results show that ...", "this suggests ..., but it does not imply ...".

**Avoid:** absolute claims (best, first, completely, obviously); oral
phrases (as we all know, it is easy to see); subjective praise without
evidence (excellent, powerful); attacks on prior work.

**Terminology and symbols:** standard field terms; define symbols at first
use; one symbol per concept and one concept per term; figure/table labels
must match the text.

**Figures/tables/ethics:** complete captions; labeled axes, units, metrics;
fair comparisons; no misleading scales; never fabricate experiments,
citations, data, or claims; disclose limitations; respect authorship, code,
dataset, and license requirements.

## 6. The two figures

**Research motivation figure** (plans the introduction): background/task
context → existing assumption or dominant path → key challenge or
contradiction → the paper's insight → why the direction is necessary.
Check: does it show the core scientific problem rather than a surface metric
goal? Can a reader infer the introduction logic from the figure alone?

**Model framework figure** (plans the method): input/output → main modules →
information flow → key innovation → relation to the problem chain.
Check: main line identifiable in seconds; details layered; every module has
a stated motivation; figure structure mirrors the method section headings.

**Cross-domain/new-framework methods:** first answer how domain data becomes
a valid input representation, what learning/pretraining objective is used,
how downstream adaptation works, why the framework suits this domain, and
what is new beyond applying a known framework.

## 7. Innovation and literature review

**Innovation from three levels:** actual need (real, field-recognized, not
pseudo-need) → scientific problem (well-studied / timely / emerging / not
yet formulated) → solution method. Method-level dimensions to search:
- Data: bias, imbalance, missing information, noise, annotation cost,
  distribution shift.
- Model: architecture, representation, reasoning path, causal mechanism,
  modularity, interpretability.
- Objective: loss definition, optimization target, constraints,
  regularization, objective–task alignment.
- Learning: supervised/weakly/self-supervised, contrastive,
  pretraining/fine-tuning, transfer, continual, active.

**Three-stage literature review:**
1. Find core papers, clarify the task (tutorials, surveys, benchmarks,
   high-citation papers; 5W1H) → understand the real need and boundary.
2. Read fast to map scientific problems and method routes (title, abstract,
   intro, method overview, figures, tables) → know what has been tried.
3. Read deeply to locate limitations and design experiments (line-by-line,
   code when needed) → formulate the innovation point and its validation.

**Survey output template:** task and real need → core scientific problems →
method taxonomy → representative papers → unresolved limitations → possible
innovation points → experiments needed to verify each point.

## 8. Revision rhythm (deadline discipline)

| When | Artifact | Content |
|---|---|---|
| Project start | Project slides | Motivation and planned method |
| Reliable results | Paper framework | Contributions, method framework, experiments, introduction plan |
| One month before deadline | Paper draft | Complete content, covered experiments, figures/tables |
| One week before | Paper revision | Experiments, logic, language, figures/tables; 10+ passes |
| Deadline | Submission | The best version your effort can reach |

Maintain daily accumulation lists: Paper List, Idea List, Math List,
English List, Code List.
