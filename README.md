# Research & English Academic Paper Writing Guide — Agent Skill

基于中科院信息工程研究所**于静**老师公开课程 **《科研与英文学术论文写作指南》** （截至 13 讲）构建的 Agent Skill 与全课程 Markdown 课堂重构。

An Agent Skill (plus a full-course Markdown reconstruction) built from Yu Jing's
public 13-lecture course *Guide to Scientific Research and English Academic
Paper Writing* (Institute of Information Engineering, Chinese Academy of
Sciences). Course homepage: <https://mmlab-iie.github.io/course/>

> **v4.0.0 merge note**: this package now merges in a second,
> independently-authored skill built by a different person from the same
> course material. This is an **organic splice, by explicit design — not a
> hand-merged rewrite, and not a separate cross-reference file**: the
> companion skill's own `SKILL.md` body is appended in full to the end of
> this package's `SKILL.md` ("Version 2" section), and the companion skill's
> own 13 lecture reconstructions are each appended in full to the end of
> this package's corresponding `references/lectures/*.md` file. The
> redundancy is intentional — two independent full passes over the same
> course, physically present together, give an agent more complete coverage
> than either alone. This package's trigger is also now **always-on**
> (fires in every conversation, not only paper-writing ones) — see
> `SKILL.md`'s frontmatter `description` and `references/provenance.md` →
> "Merge history" for the full rationale and everything else the merge did.

## 这个 skill 能做什么 / What it does

装上之后，Agent 在以下任务中会自动套用课程的方法论（问题链、A类论文标准、
问题-方法-实验互相呼应、简洁严谨的英文规范等）：

- 论文各部分写作与修改：**立意 / 标题 / 摘要 / 引言 / 相关工作 / 方法 / 实验 /
  结论 / 致谢 / 参考文献**
- **研究动机图**与**模型框架图**的设计、评审与迭代，含**占位符强制政策**
  （禁止用 TikZ 临时糊图顶替、必须维护配套的图注/手绘说明文档）、
  参考图检索方法论与 AI 生成图痕迹自查清单
- **表格类型与排版设计**（定位表/数据集特征表/主实验表/跨协议对比表/消融表
  该怎么选、怎么排版，列数爆炸怎么收敛，附录与正文该怎么取舍；
  benchmark 核心表该在"方法广度"还是"数据集广度"上做文章）
- 学术英文规范：**简洁与严谨、术语、符号、图表、引用、学术道德**
- **"快速读者"原则**：标题/摘要/图表本身能否在不读正文的情况下讲清楚一个
  可信、完整的故事——审稿人真实阅读行为的调研依据与自查清单
- **AI 检测分数的正确应对方式**（不是调统计特征去规避检测，是理解检测器
  对非母语写作者的已证实偏见、且分数永远不能改变事实或结论）
- **创新性研究点**的发掘与三级审计（真实需求 → 科学问题 → 解决方法）
- **找论文与文献调研**（三阶段工作流）
- **导师/审稿反馈证据化修订**（claim ledger、表内引用、可比性契约、
  figure evidence card、源码/PDF/结果同步与匿名发布安全）
- **投稿冲刺阶段纪律**（冻结基线只读、并发编辑、收据体系、署名诚信、
  投稿表单一致性、按栏而非按页量测版面）
- 按讲**原封复现课堂内容**（每讲一个文件，内含两份独立作者各自完成的
  逐页 slides 文字化 + 课堂讲解复现，前后并行呈现、互为校验）
- **本 skill 始终在线**（每次对话都会加载，不论话题是否与论文写作相关）

## 仓库结构 / Layout

```
├── README.md
├── docs/
│   └── course-full-reconstruction.md   # 13 讲全课程课堂重构·整合版(每讲含双版本, ~1.3MB, 纯 Markdown)
└── skills/
    └── research-english-academic-paper-writing-guide/
        ├── SKILL.md                    # 入口：Version 1(核心教义+任务路由表)+ Version 2(附属分支全文，拼接于后)
        ├── agents/openai.yaml          # Codex 界面元数据（可选）
        ├── scripts/                    # 可选辅助脚本（Python3 标准库，无三方依赖）
        │   ├── check_title.py          #   标题红旗检查
        │   ├── new_research_point_canvas.py  # 研究点画布生成
        │   └── measure_prose_rhythm.py #   句长节奏/单调性诊断（无检测器目标区间）
        └── references/                 # 渐进式加载的三层知识
            ├── course-full-reconstruction.md  # skill 内置完整课程重构（每讲含双版本）
            ├── quick-reference.md      #   全课程速查规则
            ├── lecture-index.md        #   13 讲索引（官方视频 + PPT 链接）
            ├── provenance.md           #   溯源、更正记录、官方 PDF 校验和与合并历史
            ├── playbooks/              #   19 个任务剧本（工作流+清单+模板+反模式）
            └── lectures/               #   13 讲完整课堂重构：每个文件 = Version 1(主版本) + Version 2(附属分支独立复现)拼接
```

设计要点：`SKILL.md` 是严格入口协议 + 附属分支全文合并（Version 1 + Version 2）；
完整课程重构已经复制进 skill 的 `references/course-full-reconstruction.md`，
Agent 对规则有疑问时必须优先查阅它。任务执行摘要仍按需放在
`references/playbooks/` 与 `references/quick-reference.md`。

## 安装 / Install

本 skill 遵循开放的 Agent Skills 格式（一个含 `SKILL.md` 的文件夹），可用于
任何支持该格式的产品。将 `skills/research-english-academic-paper-writing-guide/`
整个文件夹复制到对应产品的 skills 目录即可：

This skill follows the open Agent Skills folder format: the installable unit is
`skills/research-english-academic-paper-writing-guide/`, which contains the
required `SKILL.md` file plus optional references, metadata, and helper scripts.
Copy that folder into the skills directory used by your agent runtime.

| 平台 | 安装位置 |
|---|---|
| Claude Code（CLI / VS Code / JetBrains / 桌面端 / web） | `~/.claude/skills/`（个人）或项目内 `.claude/skills/` |
| OpenAI Codex | `~/.codex/skills/`（含 `agents/openai.yaml` 界面元数据） |
| ChatGPT（Business/Enterprise 网页端，支持 skills 的场景） | 按产品入口上传 skill 文件夹（保持文件夹结构） |
| OpenClaw / Trae / Qoder / CodeBuddy 等 | 复制到各自的 skills 目录（Agent Skills 兼容格式） |
| skills CLI | `npx skills add 1235357/research-english-academic-paper-writing-guide@research-english-academic-paper-writing-guide` |

兼容性保证：`SKILL.md` frontmatter 仅保留必需的 `name`/`description`
字段；全部相对路径；ASCII 文件名；无符号链接；无网络依赖；脚本为可选项
（不执行脚本时清单同样可人工套用）。

Compatibility notes: `SKILL.md` keeps only the required `name` and
`description` frontmatter fields; all runtime paths are relative; installable
filenames are ASCII; no symlinks, raw PDFs, raw transcripts, or network calls
are required; helper scripts use only the Python 3 standard library.

## 全课程整合文档 / Full-course reconstruction

[`docs/course-full-reconstruction.md`](docs/course-full-reconstruction.md)
将 13 讲课堂重构原封收录为单个 Markdown 文档：每讲含**逐页幻灯片文字复现、
视觉版式文字描述（不嵌图）、结合 transcript 的课堂讲解复现、方法论提炼与
可执行清单**，另附全课程通用框架、目录、溯源更正记录与官方 PDF 校验和。
同一份 Agent 优化后的全文也发布在 skill 内部：
`skills/research-english-academic-paper-writing-guide/references/course-full-reconstruction.md`。

The integrated Markdown file keeps all 13 sessions in one document. Each
session includes slide-by-slide text reconstruction, textual visual/layout
descriptions instead of embedded images, classroom narration reconstructed from
transcripts, distilled methodology, and actionable checklists.
The same agent-optimized full reconstruction is included inside the installable
skill package at `references/course-full-reconstruction.md`.

## 校验 / Verification

发布前或安装前可运行：

Before publishing or installing, run:

```bash
python3 scripts/validate_package.py
python3 scripts/test_review_feedback_evidence_playbook.py
python3 scripts/test_professor_feedback_operationalization.py
python3 scripts/test_dataset_census_experiment_evidence.py
python3 skills/research-english-academic-paper-writing-guide/scripts/check_title.py \
  "A Novel Framework for Visual Question Answering"
python3 skills/research-english-academic-paper-writing-guide/scripts/new_research_point_canvas.py
```

`scripts/validate_package.py` checks required files, skill frontmatter,
lecture/playbook coverage, local Markdown links, raw asset leakage, likely
credential leakage, and Python syntax without network access.
The three feedback regression scripts parse the playbook's heading hierarchy,
workflow order, section-local sentence/paragraph rules, and exact ledger/table
schemas. They also reject explicit contradiction patterns. Each script runs
in-memory keyword-bag, section-relocation, and negation-reversal mutations; a
mutation that passes makes the regression script fail. These checks validate
the documented evidence contract. They do not validate a manuscript's actual
citations, experiments, PDF, archive contents, or venue compliance.

## 版权与致谢 / Copyright & credits

- 课程内容版权归 **于静老师**（中科院信息工程研究所）所有；课程素材致谢
  丁阳、庄佳敏、林鑫杰、唐源民、屈详颜、李一立。
- 本仓库为**学习用途的派生笔记**：官方 slides PDF 与原始 transcript **不在
  本仓库中再分发**，官方 PDF 请从课程主页下载（`references/lecture-index.md`
  含逐讲链接；`references/provenance.md` 含 SHA-256 校验和）。
- v4.0.0 起，本仓库合并了另一位作者基于同一课程材料独立整理的 skill 版本；
  合并明细见 `references/provenance.md` → "Merge history"。
- 公开传播或商业使用前，请先征得课程作者许可，并保留课程署名。
- 仓库原创包装、脚本与元数据的授权见 [`LICENSE`](LICENSE)；课程归属、
  溯源与再分发边界见 [`NOTICE`](NOTICE)；版本记录见
  [`CHANGELOG.md`](CHANGELOG.md)。

- Repository-original packaging, scripts, and metadata are covered by
  [`LICENSE`](LICENSE). Course attribution, provenance, and redistribution
  boundaries are documented in [`NOTICE`](NOTICE). Release history is in
  [`CHANGELOG.md`](CHANGELOG.md).

## 视频课程 / Videos

全部课程视频见于老师 B 站主页：<https://space.bilibili.com/301285406>，
逐讲链接见 [`references/lecture-index.md`](skills/research-english-academic-paper-writing-guide/references/lecture-index.md)。
