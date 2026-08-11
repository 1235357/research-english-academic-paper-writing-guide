# English Academic Paper Writing Standards: Terminology, Symbols, Figures, and References

> Task playbook distilled from 第十讲：英文学术论文之英文规范——术语、符号、图表、文献规范 of Yu Jing's course
> 《科研与英文学术论文写作指南》. Full classroom reconstruction:
> `references/lectures/lecture-10-terminology-symbols-figures-references.md`


## Purpose

Apply the standards from lecture 10 of *Guide to Research and English Academic Paper Writing* as a standing academic-writing guardrail. Treat the skill as a quality-control layer: improve precision, professionalism, source traceability, reproducibility, and academic ethics whenever academic content appears.

## Mandatory review sequence

Use this sequence for drafts, revisions, paper reviews, paper outlines, figure/table captions, experiment sections, reference lists, rebuttals, and related academic-writing advice.

1. **Professional academic wording**
   - Remove or qualify absolutist wording such as `no doubt`, `the first`, `the best`, `always`, `never`, and unsupported `sota` claims.
   - Remove colloquial wording such as `as we know`, `obviously`, `it is easy to see`, and conversational exaggeration.
   - Remove subjective adjectives such as `good`, `excellent`, `powerful`, `enough`, or `robust` unless evidence, scope, and metric are stated.
   - Prefer bounded claims: `to the best of our knowledge`, `under this setting`, `on this benchmark`, `among the compared methods`, and metric-based evidence.

2. **Symbols and equations**
   - Check that every symbol is defined on first use.
   - Preserve one-to-one mapping between symbol and meaning.
   - Distinguish scalars, vectors, matrices, sets, functions, distributions, indices, modalities, layers, classes, and time steps.
   - Follow both general mathematical notation and the conventions used by classic papers in the target field.

3. **Standard terminology**
   - Treat terms as concepts with boundaries, not just translations.
   - Verify the intension, extension, and field-specific consensus of core terms.
   - Do not casually interchange terms such as representation, embedding, feature, latent variable, knowledge, reasoning, interpretability, explanation, fusion, and alignment.
   - If a term is used in a nonstandard way, define the deviation explicitly and cite the relevant work.

4. **Objective figures, tables, and experimental reporting**
   - Detect cherry-picking: do not show only the author's best cases and competitors' worst cases.
   - Pair qualitative examples with quantitative analysis: proportions, grouped metrics, ablations, confidence intervals, variance, error bars, or repeated-run statistics where appropriate.
   - Require limitation and bad-case analysis to clarify what the method can and cannot do.
   - Ask whether performance gains are actually caused by the claimed mechanism; decompose the data or metrics to support this.
   - Encourage reproducibility: clear implementation details, hyperparameters, model components, code, anonymous links, or supplementary material.

5. **Reference citation hygiene**
   - Follow the target venue or journal template, not Google Scholar defaults or copied formats from another paper.
   - Prefer official bibliographic sources such as DBLP, ACL Anthology, IEEE/ACM pages, publisher pages, or venue proceedings.
   - Check authors, order, title case, venue name, year, pages, DOI, publisher, address, arXiv-vs-camera-ready status, and BibTeX keys.
   - For many references, suggest using a tool such as rebiber to normalize BibTeX, then require manual checking.

6. **Academic ethics**
   - Treat plagiarism as a red line: results, figures, tables, code, text, problem framing, and ideas all require integrity and attribution.
   - Never suggest hiding unfavorable results, fabricating repeatability, omitting contradictory evidence, or copying expression from papers.
   - Encourage personal expression banks and collocation tools for language improvement rather than copying sentences from existing papers.
   - The lecture is emphatic that this is not a minor point: a paper follows
     its author for life, "expression plagiarism" (copying phrasing, not just
     results) is not treated as a lesser offense than results plagiarism, and
     a plagiarism finding damages every co-author and the home institution,
     not only the first author. The lecture illustrates this with real,
     publicly-documented top-venue plagiarism disputes — treat these as
     accusations/disputes rather than adjudicated verdicts when discussing
     them, and do not fabricate or guess at case specifics that are not
     independently verified.

### Named resources from the lecture

Point users to these specific resources rather than only generic advice —
these are the lecture's own recommendations, not generic substitutes:

- **Felicia Brittman, *"The Most Common Habits from more than 200 English
  Papers written by Graduate Chinese Engineering Students"*** — a curated
  list of the specific phrasing habits this lecture is built around fixing.
- **Math Vault, *"Comprehensive List of Mathematical Symbols"***
  (`https://mathvault.ca/wp-content/uploads/Comprehensive-List-of-Mathematical-Symbols.pdf`)
  — check this before inventing new notation. Note: the lecture verbally
  describes this as "one or two hundred pages," but the document itself is
  actually about 28 pages; treat it as a fast lookup reference, not a
  hundreds-of-pages tome, and don't repeat the inflated page count.
- **CCFpedia / CCF Terminology Committee** (`https://term.ccf.org.cn/`) —
  for fast-moving CS/AI terms, since intension and extension shift quickly;
  entries include concept boundaries, context, and references, not just a
  bilingual gloss.
- **`rebiber`** (`https://github.com/yuchenlin/rebiber`) — one-command
  BibTeX normalization against DBLP/ACL Anthology, particularly good for
  converting an arXiv-version citation into its formal-publication form once
  a paper is officially published. Command shape:
  `rebiber -i /path/to/input.bib -o /path/to/output.bib`.
- **A collocation/usage checker** (the lecture calls out a tool an assistant
  found, referred to in the transcript as "Lingo") for questions like
  article choice (a/an/the) or which preposition pairs with a given word,
  based on statistics over large academic corpora — useful for exactly the
  kind of small usage error a expression bank alone won't catch.

## Output pattern

When reviewing a user's academic text, use this compact structure unless the user asks for another format:

1. **diagnosis**: list the most serious issues by the six standards above.
2. **revision**: provide a polished version or targeted replacements.
3. **rationale**: explain why each revision is more professional, precise, or ethical.
4. **final checklist**: give actionable checks before submission.

When the user only asks a conceptual question, answer directly but still apply the standards silently: avoid overclaiming, define terms, and state uncertainty or needed verification.

---

## Appendix: course templates and checklists for this lecture

## Lecture 10 Checklist: English Academic Paper Writing Standards

Use this checklist before submission or when reviewing any academic draft.

### 1. Professional academic wording

- Remove unsupported absolute claims: no doubt, the first, the best, always, never.
- Replace colloquial expressions: as we know, obviously, easy to see, countless ways.
- Replace subjective adjectives with evidence: good, excellent, powerful, enough, robust.
- Add scope to claims: benchmark, setting, compared methods, metric, dataset, assumptions.

### 2. Symbols and equations

- Define each symbol at first occurrence.
- Keep one symbol for one concept and one concept for one symbol.
- Distinguish scalars, vectors, matrices, sets, functions, random variables, and indices.
- Match the target field's notation in classic papers.
- Explain equations in prose before or after the formula.

### 3. Standard terminology

- Define core terms by field consensus, not personal intuition.
- Check term boundaries: what the term includes and excludes.
- Avoid mixing near-synonyms unless they truly mean the same thing in context.
- Cite classic or authoritative work for important concepts.

### 4. Objective figures and tables

- Do not cherry-pick only best cases for your method or worst cases for baselines.
- Include quantitative analysis for qualitative examples.
- Use repeated runs, mean/variance, error bars, or significance checks where appropriate.
- Show bad cases and limitations.
- Ensure figure/table captions explain what is measured and why it supports the claim.
- Provide enough model and experiment detail for reproducibility.

### 5. Reference citation hygiene

- Follow the target venue or journal template.
- Do not trust Google Scholar export without checking.
- Prefer DBLP, ACL Anthology, IEEE/ACM/publisher pages, or official proceedings.
- Check complete authors, title, venue, year, pages, DOI, address, publisher, and arXiv-to-camera-ready updates.
- Normalize BibTeX with tools if helpful, then manually verify.

### 6. Academic ethics

- Do not copy results, figures, tables, code, text, or reasoning without attribution.
- Do not select visualizations or metrics in a way that misleads readers.
- Build a personal expression bank; do not paste sentences from papers.
- Cite sources for ideas, problem framing, methods, datasets, and reused assets.

---

## Deep dive and provenance

- Full classroom reconstruction (Chinese, slide-by-slide + transcript appendix): `references/lectures/lecture-10-terminology-symbols-figures-references.md`
- Course-wide compact rules: `references/quick-reference.md`
- All lectures with official video/slides links: `references/lecture-index.md`
- Source and correction notes: `references/provenance.md`
