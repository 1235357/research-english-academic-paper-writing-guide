# 第四讲 英文学术论文之写作思路——相关工作和方法：课堂 Markdown 重构

> 课程：科研与英文学术论文写作指南  
> 讲次：第四讲  
> 英文标题：Related Work and Method  
> 教师：于静，副研究员，中国科学院信息工程研究所  
> 课件来源：`《英文学术论文写作指南》第四讲 英文学术论文之写作思路——相关工作和方法.pdf`  
> transcript 来源：`《英文学术论文写作指南》第四讲 英文学术论文之写作思路——相关工作和方法.transcript.txt`  
> 文档生成日期：2026-07-08  
> 约束：本文档仅使用 Markdown 文字复现课程，不嵌入、不链接、不引用 PNG/JPEG 等图片。

---

## 0. 本讲的中心命题

这一讲承接第三讲“摘要和引言”，专门回答论文中两个最容易写成“流水账”的部分：**Related Work** 与 **Method / Methodology**。整堂课的核心不是给出某种固定模板，而是训练一种审稿人视角下的论文组织能力：

- **Related Work** 不是“把所有看过的论文列出来”，而是围绕本文主题、本文问题、本文方法，把已有工作归类、比较、递进，并最终引出“本文与现有工作的区别和贡献”。
- **Method** 不是“按实现步骤把模型从头到尾罗列一遍”，而是先界定问题和符号，再用框架图与小标题组织核心创新模块，逐步说明每个模块的目标、动机、实现、与前后模块的关系，以及为什么这样设计。
- 高水平论文的共性是：**问题—方法—实验相互呼应**。方法中的每一步都针对问题，实验中的每一组验证都回应方法或动机；图、标题、公式、文字叙述之间相互定位，降低审稿人理解成本。

本讲主要使用 IJCAI 2020 论文 **“Mucko: Multi-Layer Cross-Modal Knowledge Reasoning for Fact-based Visual Question Answering”** 作为贯穿案例。该论文的任务是基于事实知识的视觉问答；方法将图像表示成视觉、语义、事实三层多模态异构图，并通过 intra-modal 与 cross-modal 图卷积选择与问题相关、且模态间互补的证据。

---

## 1. 资料核验与溯源索引

### 1.1 本地原始资料

| 资料 | 文件名 | 用途 |
|---|---|---|
| 原始 slides PDF | `《英文学术论文写作指南》第四讲 英文学术论文之写作思路——相关工作和方法.pdf` | 视觉复现每页课件标题、要点、框架图、标注和手写批注。 |
| 原始 transcript | `《英文学术论文写作指南》第四讲 英文学术论文之写作思路——相关工作和方法.transcript.txt` | 复原教师讲解顺序、口语化解释、重点提醒与实践建议。 |

### 1.2 线上辅助核验资料

- 官方课程主页：`https://mmlab-iie.github.io/course/`。主页列出课程“科研与英文学术论文写作指南”、教师信息、课程定位、报告大纲、每讲视频和 PPT 链接；第四讲对应“英文学术论文之写作思路：相关工作和方法”。
- 官方第四讲 PPT：`https://mmlab-iie.github.io/course/static/4.pdf`。与本地上传 PDF 为同一讲次、同一 8 页课件。
- 案例论文 arXiv：`https://arxiv.org/abs/2006.09073`。标题为 “Mucko: Multi-Layer Cross-Modal Knowledge Reasoning for Fact-based Visual Question Answering”，作者包括 Zihao Zhu、Jing Yu、Yujing Wang、Yajing Sun、Yue Hu、Qi Wu，论文摘要和正文中包含本讲课件引用的 Related Work 与 Methodology 结构。

---

## 2. 课堂总结构

```text
第四讲：Related Work and Method

A. 相关工作怎么写
   1. 为什么 Related Work 容易和 Introduction 重复
   2. Related Work 应覆盖哪些维度
      - 本文主题相关的工作
      - 本文问题相关的工作
      - 本文方法相关的工作
   3. 如何从不同维度划分主题
   4. 如何在同一主题下归纳技术路线和问题
   5. 如何总结现有方法局限，并引出本文区别和贡献
   6. MuCKO 论文 Related Work 案例：
      - Visual Question Answering
      - Fact-based Visual Question Answering
      - Heterogeneous Graph Neural Networks

B. 方法怎么写
   1. 总原则：换位思考，从读者/审稿人角度出发
   2. 问题建模：用标准数学语言定义任务、输入、输出、测试方式
   3. 模型框架图：先画框架图，再写方法文字
   4. 模型介绍：
      - 框架图清晰定义模块，突出创新点
      - 小标题突出方法特色、用途、创新性，且与图对应
      - 总体介绍突出模块间关联
      - 分模块介绍突出模块设计动机
      - 精简表达，善用公式和理论分析
   5. CCF-A 与 CCF-C 写法对比
   6. MuCKO Methodology 案例：
      - Multi-Modal Heterogeneous Graph Construction
      - Cross-Modal Heterogeneous Graph Reasoning
      - Intra-Modal Knowledge Selection
      - Cross-Modal Knowledge Reasoning
      - Learning
```

---

## 3. Slide-by-slide 文字复现

### Slide 1：课程封面

页面顶部为蓝色横幅，左上角写“科研与英文学术论文写作”。中间大标题为：

```text
第四讲 英文学术论文之写作思路
——相关工作和方法
```

下方写教师和单位：

```text
于静 副研究员
中国科学院信息工程研究所
课程主页：https://mmlab-iie.github.io/course/
2022.07 @ Bilibili
```

底部展示中国科学院信息工程研究所与中国科学院大学标识。此页承担讲次定位作用：本讲属于“英文论文写作思路”部分，主题是论文结构中的 **Related Work** 与 **Method**。

---

### Slide 2：一篇论文的组成——相关工作：基本要求

页面标题：

```text
一篇论文的组成——相关工作
```

中心小标题：

```text
基本要求
```

左侧列出 Related Work 的六个基本要求：

1. **包括理解本文的所有主题**  
   “理解本文”意味着读者需要知道你的任务背景、核心概念、技术传统和必要术语。Related Work 不是按作者名堆叠，而是帮助读者进入你的问题域。
2. **包括问题相关的所有工作**  
   这里的“所有”不是指所有看过的论文，而是指与本文要解决的具体问题真正相关的工作。
3. **从不同维度划分主题**  
   维度可以是任务维度、问题维度、方法维度、技术路线维度，也可以是数据/模型/目标函数/学习方式等维度。
4. **同一主题方法归类**  
   同一主题下不能只列 A、B、C 做了什么，而要归纳为若干路线：例如模板检索、学习式推理、图推理、跨模态推理等。
5. **总结问题**  
   每一类方法最后都要落到“仍有什么问题没有解决”。
6. **引出本研究的区别和贡献**  
   Related Work 的终点不是“已有方法很多”，而是“因此本文做了什么不同的事情”。

右侧红色手写式警示语：

```text
不要所有看过的论文！
不要罗列写上的论文！
```

这一页明确了 Related Work 的边界：它不是 bibliography 的堆砌，也不是阅读记录，而是论文论证结构的一部分。

---

### Slide 3：相关工作案例：MuCKO 的三个维度

页面标题仍为：

```text
一篇论文的组成——相关工作
```

课件主体由三个论文片段与三个彩色标注组成，展示 MuCKO 论文 Related Work 的组织方式。

#### 左侧红框：视觉问答方法

红色标签：

```text
视觉问答方法
```

论文片段标题为：

```text
Visual Question Answering.
```

这部分先总结传统 VQA 的典型路线：CNN-RNN 架构、全局视觉特征、注意力机制、图结构表示图像对象与关系。随后指出这些路线在面向知识型视觉问答时的不足：仅捕捉自然语言语义，缺少与视觉信息的细粒度关联；因此本文进一步从 visual、semantic、factual 三个视角用多层图表示图像，收集不同模态的细粒度证据。

课堂要点：这不是只讲“VQA 有哪些论文”，而是要解释：为什么传统 VQA 方法无法直接解决本文的 FVQA 问题。

#### 右上绿框：基于知识的视觉问答方法

绿色标签：

```text
基于知识的视觉问答方法
```

论文片段标题为：

```text
Fact-based Visual Question Answering.
```

这部分更贴近本文问题，指出人类可以结合视觉观察与外部知识回答问题，但算法仍困难。已有 FVQA 方法通常从 fact graph 选择实体作为答案，可分为 query-mapping based methods 与 learning based methods。课件中重点高亮已有方法的限制：视觉信息只被整体提供，可能为预测引入冗余信息；本文通过多层图与跨模态异构图推理捕捉最相关的互补证据。

课堂要点：越接近本文问题的 Related Work，需要越具体地指出代表工作“好在哪里、不足在哪里、本文解决哪一环”。

#### 右下橙框：异构图神经网络方法

橙色标签：

```text
异构图神经网络方法
```

论文片段标题为：

```text
Heterogeneous Graph Neural Networks.
```

这部分从方法维度组织相关工作：图神经网络与异构图神经网络已有大量工作，但已有异构图通常在统一图上建模不同节点和边；本文的异构图由多个子图层组成，每一层来自不同模态。因此本文提出 intra-modal 与 cross-modal graph convolutions 来处理多模态异构图。

页面右侧蓝色手写批注：

```text
方法写完后可动笔！
```

这句批注是本讲 Related Work 写作顺序的重要提醒：当方法已经写完，作者更清楚自己的技术主题、核心模块、创新边界和需要对比的路线，此时写 Related Work 往往更准确。

---

### Slide 4：一篇论文的组成——方法：基本要求

页面标题：

```text
一篇论文的组成——方法
```

中心小标题：

```text
基本要求（最容易部分，可以先写）
```

页面以树状结构展示 Method 的写作要点。

#### 总原则

```text
总原则：换位思考，从读者角度出发
```

读者包括导师、同学、审稿人和领域同行。方法写作不是把自己实现过的步骤复述出来，而是让读者最快理解：你解决了什么问题、模块如何划分、创新在哪里、为什么这样设计。

#### 问题建模

```text
问题建模
├── 数学语言描述
└── 确定研究目标
```

这要求在 Method 入口处定义清楚：任务是什么、输入是什么、输出是什么、知识库或数据结构是什么、测试时如何预测、目标是什么。符号和任务定义必须标准、边界清楚。

#### 模型介绍

```text
模型介绍
├── 模型框架图，清晰定义模块，突出创新之处
├── 小标题确定，突出方法特色、用途、创新性，图文一致
├── 模型总体介绍，突出模块间关联
├── 分模块介绍，突出模块设计动机
└── 精简表达，善用公式，理论分析
```

这一页的关键思想是：**先用框架图搭好方法逻辑，再让文字、标题、公式围绕框架图展开**。如果方法部分写得长但没有边界、没有模块目标、没有动机说明，审稿人很难判断贡献。

---

### Slide 5：CCF-A 与 CCF-C 写法对比

页面标题：

```text
一篇论文的组成——方法
```

页面左右对比 CCF-A 与 CCF-C 论文在方法写作上的差异。

#### 左侧：CCF-A

绿色标题：

```text
CCF-A
```

核心特征：

```text
问题-方法-实验，相互呼应
```

具体表现：

- **动机：有理有据，足够具体**  
  每个模块为什么存在、要解决什么问题，都能从前文问题或动机推出来。
- **方法：针对问题设计，每一步设计目标明确**  
  方法不是 step1、step2、step3 的简单堆砌，而是每一步都有对应的目标和功能。
- **根据重点，重新组织方法介绍思路**  
  不一定按实验实现顺序写，而要按创新重点和读者理解路径组织。
- **标题和图突出创新性和重点，相互呼应**  
  读者看标题与图就能定位模块；读文字时能找到对应细节。
- **每一步方法设计都有理可依**  
  设计需要原理解释、机理说明、数学推导或实验支撑。
- **实验：针对方法逐一证明，针对动机逐一分析**  
  实验不是只报告 SOTA，而是验证方法为什么有效。

#### 右侧：CCF-C

红色标题：

```text
CCF-C
```

典型问题：

```text
问题-方法-实验，各为其说
```

具体表现：

- **动机：大家都在研究，所以我研究**  
  动机泛泛而谈，没有真正指向科学问题或技术挑战。
- **方法：step1 -> step2 -> step3**  
  只是按顺序描述模块，不解释为什么这样做，也不说明每一步解决什么问题。
- **实验：达到了 SOTA，缺乏分析**  
  只说明效果好，缺少消融、机理、失败案例、适用边界等分析。

这页的对比不是评价会议级别，而是强调一种论文组织标准：高水平方法写作要让问题、方法、实验形成闭环。

---

### Slide 6：MuCKO 方法框架图示例

页面标题：

```text
一篇论文的组成——方法
```

页面上方写：

```text
IJCAI 2020
Mucko: Multi-Layer Cross-Modal Knowledge Reasoning for Fact-based Visual Question Answering
```

页面主体是 MuCKO 论文 Figure 2 的框架图，文字复现如下：

```text
输入：
- Image
- Question
- Knowledge base of facts
- DenseCap

模块 1：Multi-Modal Heterogeneous Graph Construction
- Object Regions
- Visual Graph
- Candidate Facts
- Fact Graph
- Dense Captions
- Semantic Graph

模块 2：Cross-Modal Heterogeneous Graph Reasoning
- Intra-Modal Knowledge Selection
- Cross-Modal Knowledge Reasoning
- Visual-to-Fact Conv.
- Semantic-to-Fact Conv.
- Fact-to-Fact Aggr.

输出：
- Answer
```

图注文字：

```text
Figure 2: An overview of our model. The model contains two modules: Multi-modal Heterogeneous Graph Construction aims to depict an image by multiple layers of graphs and Cross-modal Heterogeneous Graph Reasoning supports intra-modal and cross-modal evidence selection.
```

课堂强调：框架图不仅是装饰，而是 Method 的骨架。每个框、箭头、模块名都应该能在正文中找到对应小节、公式和解释。

---

### Slide 7：MuCKO Methodology 文字与图的对应关系

页面标题：

```text
一篇论文的组成——方法
```

页面左侧是 MuCKO 框架图与 Method 文字片段，右侧是 3.2、3.3、3.4 等方法小节的局部截图。课件用不同颜色框强调 Method 写作的组织原则。

#### 橙色框：整体介绍模型设计思路

标注文字：

```text
整体介绍模型设计思路
```

对应正文第一段应完成两件事：定义任务与符号；概述模型包含哪些模块以及它们如何衔接。

#### 红色框：小节标题与框架图对应

高亮的小节包括：

```text
3.1 Multi-Modal Graph Construction
3.2 Intra-Modal Knowledge Selection
3.3 Cross-Modal Knowledge Reasoning
3.4 Learning
```

课件旁边红色要点：

```text
标题突出创新点和过程
表达逻辑一致
图文一致
```

这说明小标题不是随便命名的，它需要告诉读者“这一部分如何实现、实现什么、为什么是创新”。

#### 绿色框：每个过程开头先说明动机和目标

左下绿色中文批注：

```text
每一个过程首先介绍背后的动机和目标
```

这对应 Method 每个小节开头的目标句，例如：

- 为什么要构建 visual graph：FVQA 问题通常 grounded in visual objects and relationships。
- 为什么要构建 semantic graph：自然语言抽象能桥接视觉对象与问题/事实概念。
- 为什么要做 intra-modal selection：每层图包含模态特定知识，先独立选择与问题相关的证据。
- 为什么要做 cross-modal reasoning：答案来自 fact graph，因此需要把视觉与语义互补信息汇聚到 fact graph。

#### 蓝色框：复杂过程再分小标题

蓝色标注：

```text
具体过程分小标题
```

被圈出的细分标题包括：

```text
Question-guided Node Attention
Question-guided Edge Attention
Intra-Modal Graph Convolution
```

课堂含义：当一个小节内部过程复杂、篇幅较长时，继续用加粗小标题或三级标题拆解。读者即使只扫标题，也能知道算法流程。

#### 右侧蓝色手写提示

```text
注意：
动机？
其他方式？
```

这是对方法写作最关键的审稿问题：

1. 这一模块为什么需要存在？
2. 为什么要用这个实现，而不是拼接、双线性映射、简单融合、其他注意力或其他 GNN 变体？
3. 是否能从问题机理、数学性质、模型归纳偏置或实验消融解释选择？

---

### Slide 8：联系方式与交流渠道

页面大标题：

```text
欢迎大家在B站、知乎专栏、邮件留言交流！
```

页面文字：

```text
于静
邮箱：yujing02@iie.ac.cn
课程主页：https://mmlab-iie.github.io/course/
研究组主页：https://mmlab-iie.github.io/
知乎专栏：https://www.zhihu.com/column/c_1284803871596797952
```

页面右侧有三个二维码，其标题分别为：

```text
课程主页
研究组主页
知乎专栏
```

底部显示中国科学院信息工程研究所与中国科学院大学标识。

---

## 4. 课堂逐段复盘：Related Work

### 4.1 由摘要和引言过渡到相关工作

教师开场先指出：前面已经讲完论文的摘要和引言，下面进入 Related Work。许多初学者的问题是：在 Introduction 里已经介绍过现有方法，到了 Related Work 又继续介绍现有方法，二者写出来非常重复，读者看不出差别。

本讲要解决的正是这个问题：**Related Work 到底需要突出什么内容？**

在 Introduction 中，现有方法通常服务于“提出研究动机”：领域背景是什么，已有方法走到哪里，本文要解决的核心挑战是什么。Introduction 的写法强调“导入问题”。而 Related Work 的写法强调“系统定位”：围绕本文主题、问题、方法，把相关工作归类，说明每类方法的技术脉络、代表性进展、未解决问题，以及本文相对它们的区别。

因此，Related Work 和 Introduction 的区别可以概括为：

| 维度 | Introduction 中的现有方法 | Related Work 中的现有方法 |
|---|---|---|
| 主要目的 | 引出本文问题、动机和贡献 | 系统定位本文在已有研究中的位置 |
| 组织方式 | 从背景到挑战的线性叙事 | 按主题/问题/方法维度分类归纳 |
| 细节程度 | 只保留与动机强相关的关键工作 | 更充分比较代表性路线和不足 |
| 终点 | “因此本文要解决 X” | “因此本文与已有方法的区别是 Y” |

### 4.2 Related Work 首先要覆盖“理解本文的所有主题”

教师强调，写 Related Work 前必须真正理解本文工作包含哪些主题。主题不是单一的，它至少可以从任务和方法两个层面拆解。

以本讲的 MuCKO 论文为例：

- 任务主题：Visual Question Answering，Fact-based Visual Question Answering。
- 方法主题：Graph Neural Networks，Heterogeneous Graph Neural Networks，Cross-modal Reasoning。

如果读者不了解 VQA，就不理解为什么“看图回答问题”需要视觉与语言联合建模；如果不了解 FVQA，就不理解为什么还需要外部知识；如果不了解异构图神经网络，就不理解本文方法为什么把不同模态表示成多层图并做图卷积推理。

所以 Related Work 的第一个维度是：**帮助读者理解本文所涉及的所有必要主题**。但“必要”有边界：只写理解本文必须知道的主题，不写与本文无关的泛泛背景。

### 4.3 第二个维度：问题相关的工作

教师进一步区分“主题相关”与“问题相关”。一个任务内部可能有许多不同问题。例如知识型视觉问答可能涉及：

- 数据集构建问题；
- 数据偏置问题；
- 外部知识引入问题；
- 视觉信息与事实知识融合问题；
- 推理过程中的噪声与冗余问题；
- 模型优化或损失设计问题。

如果本文 Introduction 最终强调的挑战是“如何在视觉、语义、事实三类信息中选择与问题相关且互补的证据”，那么 Related Work 就应该围绕这个挑战介绍问题相关工作，而不是把所有 FVQA 的数据、优化、损失函数、模型微调论文都放进来。

课堂原意可以概括为一句写作原则：**Related Work 不是写“这个任务中所有东西”，而是写“本文要解决的问题所依赖的那些东西”。**

### 4.4 第三个维度：方法相关的工作

除了任务和问题，Related Work 还需要覆盖本文方法所依赖或对比的技术路线。MuCKO 使用图神经网络，尤其是异构图推理，因此需要讨论 Heterogeneous Graph Neural Networks。

但教师提醒：图神经网络发展很久，相关工作很多，不可能全部罗列。写方法相关工作时要问：

1. 我的工作到底用到图神经网络的哪一方面？
2. 现有异构图神经网络通常解决什么类型的数据或任务？
3. 它们为什么不能直接迁移到本文问题？
4. 本文在技术实现细节上与它们有什么差异？

MuCKO 的关键差异不是“任务不一样”这么简单，而是：已有异构图方法通常在统一图中处理不同类型节点和边；而本文的图由多层子图构成，每一层来自不同模态，因此需要 intra-modal 与 cross-modal 的图卷积机制。

这说明 Related Work 的创新定位必须落到**方法细节与问题约束的对应关系**，不能只说“别人做 NLP，我们做 VQA”。

### 4.5 写 Related Work 的组织动作：划分、归类、总结、引出

教师将 Related Work 的写作动作拆成四步：

#### 第一步：划分不同维度

先决定 Related Work 分成哪几个主题或小节。MuCKO 分为：

```text
Visual Question Answering
Fact-based Visual Question Answering
Heterogeneous Graph Neural Networks
```

这三个小节分别对应：大任务背景、本文直接问题、本文关键技术。

#### 第二步：同一主题下归纳技术路线

同一主题下不能按论文逐篇罗列，而要总结路线。例如 FVQA 部分可归纳为：

- query-mapping based methods；
- learning based methods；
- fact graph reasoning；
- visual information used only for retrieval vs introduced into reasoning。

#### 第三步：总结每类方法的问题

每类方法的介绍都要落脚于“它在本文问题上还缺什么”。例如：

- 传统 VQA 注意力方法能够关注视觉对象，但可能忽略对象间关系。
- 图结构 VQA 方法能建模关系，但自然语言语义与视觉细粒度关联不足。
- FVQA 方法能引入事实知识，但视觉信息可能只用于 fact retrieval，或以整体方式提供给所有节点，带来冗余噪声。
- 现有异构图方法能处理不同节点和边，但不适用于多模态、多层子图的结构约束。

#### 第四步：引出本文区别和贡献

每个小节最后都应该为本文让路。例如：

```text
因此，我们将图像表示为来自 visual、semantic、factual 三个视角的多层图，并通过跨模态异构图推理选择与问题最相关的互补证据。
```

这就是 Related Work 的终点：不是“已有工作有什么”，而是“已有工作为什么不足以解决本文问题，因此本文如何不同”。

### 4.6 两个关键提醒

#### 提醒一：引用的工作必须真正看过、理解过

教师强调，Related Work 深不深入，取决于作者是否真正理解引用论文。只从别人论文里复制一句“某某做了什么”无法写出有针对性的比较，因为同一篇论文从不同角度看，评价会完全不同。

你必须知道：

- 这篇工作解决了什么问题；
- 它在你当前问题上好在哪里；
- 它在你当前问题上不足在哪里；
- 你的工作与它的关系是继承、扩展、修正、替代，还是解决另一个约束。

#### 提醒二：不要罗列论文，要整体介绍思想

错误写法：

```text
A proposed ...; B proposed ...; C proposed ...; however, these methods have problems.
```

更好的写法：

```text
Existing approaches can be broadly grouped into ... . Early methods ... . Later learning-based methods ... . However, when applied to [the paper's target problem], these methods still ... . Therefore, we ... .
```

Related Work 当然可以具体展开两三篇代表性工作，但展开的目的不是“显示我读了”，而是用代表工作说明技术路线的演进、差异和未解决问题。

### 4.7 MuCKO Related Work 的三段式逻辑

#### 4.7.1 Visual Question Answering：从大任务到本文需要的多层证据

这一节先介绍传统 VQA：CNN-RNN 架构、全局视觉特征、注意力机制、图结构表示对象关系。随后指出这些方法在 FVQA 场景下的不足：它们主要处理可由可见内容回答的问题，或者只在视觉/语言内部建模，缺少外部事实知识与视觉语义的细粒度关联。

因此本文进一步提出：从 visual、semantic、factual 三个角度表示图像，收集多模态证据。

#### 4.7.2 Fact-based Visual Question Answering：从直接相关问题到本文核心挑战

这一节更聚焦于 FVQA。已有方法一般从 fact graph 中选择一个实体作为答案，分为 query mapping 和 learning based methods。问题在于：某些方法把视觉信息用于提取事实，但没有在推理过程中引入视觉信息；另一些方法虽然使用视觉信息，但以整体形式提供给每个图节点，可能引入冗余信息。

本文的落点是：通过多层图和跨模态异构图推理，从不同层中捕获与问题最相关的互补证据。

#### 4.7.3 Heterogeneous Graph Neural Networks：从技术传统到本文方法差异

这一节从 GNN 与 heterogeneous graph 的发展说起，但并不罗列所有 GNN 工作。重点是指出：已有异构图方法通常把不同类型的节点和边放在一个统一图中，而本文的异构图结构是多层子图，每层来自不同模态。

因此，本文的技术差异是为这种多模态多层图结构设计 intra-modal 与 cross-modal graph convolutions。

### 4.8 Related Work 可以在 Method 写完后动笔

课件第 3 页右侧手写批注“方法写完后可动笔！”对应教师讲解：当你写完方法后，会更清楚本文涉及哪些任务、哪些技术、哪些模块、哪些创新点，因此更容易反推 Related Work 应该有哪些维度。

实操顺序可以是：

```text
先完成核心方法草稿与框架图
→ 确定方法涉及的任务、问题、技术路线
→ 设计 Related Work 小节
→ 回到 Introduction 检查动机是否一致
→ 再回 Method 检查术语和模块名是否一致
```

---

## 5. 课堂逐段复盘：Method / Methodology

### 5.1 Method 是“最容易部分”，但不是“随便写的部分”

课件第 4 页写“基本要求（最容易部分，可以先写）”。教师的意思不是方法没有难度，而是相对于 Abstract、Introduction、Related Work，Method 的素材最明确：它来自你自己设计的模型、算法、流程和实现。

但初学者常犯的错误是：因为方法是自己做的，就按自己实现过程从头到尾写，结果变成 step1、step2、step3，缺少问题动机、模块边界和创新重点。

Method 写作的总原则是：**从读者和审稿人的角度出发，在最短时间内让他们理解你的模型思路与贡献亮点。**

### 5.2 第一步：问题建模

在真正介绍模型前，需要先完成问题定义。问题定义至少包含：

- 任务是什么；
- 输入是什么；
- 输出是什么；
- 需要使用哪些外部资源或先验；
- 预测目标是什么；
- 测试阶段如何选择答案；
- 主要符号如何定义。

以 MuCKO 为例，Methodology 开头定义：给定图像 `I` 和问题 `Q`，任务是在外部事实知识库的帮助下预测答案 `A`；事实以三元组 `<e1, r, e2>` 形式存在，其中 `e1` 是图像中的视觉概念，`e2` 是属性或短语，`r` 表示二者关系；关键是从 supporting fact 中选择正确实体作为预测答案。

这类定义的作用是给后续所有模块建立共同语言。没有问题建模，读者不知道你的图节点、边、卷积、注意力、答案预测到底服务于什么目标。

### 5.3 第二步：先画框架图，再写正文

教师反复强调：她习惯让学生先画框架图，再基于框架图逻辑写论文语言。原因有三点：

1. 框架图迫使作者明确模块边界。  
   每个框代表一个过程，每条箭头代表信息流；如果图画不清楚，文字通常也写不清楚。
2. 框架图帮助防止返工。  
   先确定整体逻辑，再写正文，能够避免写了一大段后发现模块顺序、标题和创新重点不对。
3. 框架图让图文自洽。  
   正文小节标题、公式、模块名要与图中结构对应，读者才能快速定位。

框架图不是可有可无的装饰，而是 Method 的“目录 + 证据地图”。

### 5.4 第三步：清晰界定方法过程之间的边界

教师指出，方法中每个具体过程的边界都要清楚。这个边界包含两层：

1. **实现过程的边界**：这个模块输入什么、输出什么、执行什么操作，与前后模块如何连接。
2. **问题解决环节的边界**：这个模块解决整体问题中的哪一部分，为什么这一部分需要单独设计。

例如 MuCKO 将核心方法分为两大模块：

```text
Multi-Modal Heterogeneous Graph Construction
Cross-Modal Heterogeneous Graph Reasoning
```

第一个模块解决“如何统一表示视觉、语义、事实信息”；第二个模块解决“如何在推理过程中选择问题相关且模态互补的证据”。这两个模块分别对应本文两大创新环节。

### 5.5 第四步：解释每一步解决什么问题，为什么能解决

Method 不能只写：

```text
We first ..., then ..., finally ... .
```

还必须写：

```text
We do this because ... .
This step aims to ... .
This design enables ... .
Compared with ..., it avoids ... .
```

教师特别提醒：审稿人常问“为什么不用其他方式？”例如为什么不用双线性映射、拼接、简单融合、其他图网络结构？实验消融可以证明某种方式效果更好，但更有力的解释是从原理、机理、数学推导或归纳偏置上说明为什么当前设计适合本文问题。

### 5.6 CCF-A 写法：问题—方法—实验互相呼应

高水平论文在方法部分通常具备三个闭环：

#### 闭环一：问题与方法呼应

每个方法模块都能追溯到 Introduction 或 Problem Formulation 中提出的问题。例如：

```text
问题：FVQA 需要视觉、语义、事实三种证据，但直接整体融合会引入冗余噪声。
方法：构建多层异构图，并用 question-guided intra-modal selection 与 cross-modal reasoning 选择相关互补证据。
```

#### 闭环二：图与文呼应

图中的模块名、箭头、层级结构与正文小节标题一致。读者看图能知道正文在哪里；看正文能回到图中定位信息流。

#### 闭环三：方法与实验呼应

实验不只是证明性能高，还要证明每个关键模块有效。例如：

- 去掉 semantic graph 是否下降？
- 去掉 fact graph 是否下降？
- 去掉 intra-modal selection 是否下降？
- cross-modal reasoning 是否优于简单拼接？
- 注意力可视化是否支持“question-oriented evidence selection”的解释？

### 5.7 CCF-C 常见问题：各为其说

低质量方法写作的典型问题是“问题—方法—实验，各为其说”：

- Introduction 说的动机很泛：大家都在研究，所以我研究。
- Method 只写 step1、step2、step3，不解释每一步为何必要。
- Experiment 只报告达到了 SOTA，不分析为什么达到，不验证模块作用。

这种写法让审稿人无法判断创新性：即使性能不错，也会被质疑是否只是工程组合。

---

## 6. MuCKO Methodology 案例复盘

### 6.1 先整体介绍模型设计思路

MuCKO Methodology 入口先完成两件事：

1. **问题定义**：输入图像、问题和外部事实知识库，输出答案；事实以三元组组织。
2. **方法概览**：模型包含多模态异构图构建与跨模态异构图推理两大模块。

这个整体介绍非常重要。它让读者在进入复杂公式前，先知道后面所有模块的目的和衔接关系。

### 6.2 核心创新模块一：Multi-Modal Heterogeneous Graph Construction

这个模块回答：**如何把图像、语言描述、事实知识放到一个可推理的统一结构中？**

它包含三层图：

#### 视觉图 Visual Graph

目标：表示图像中对象及其空间关系。  
动机：FVQA 中许多问题 grounded in visual objects and relationships，因此需要 appearance-level evidence。  
实现：使用 Faster R-CNN 提取 object regions，每个节点表示检测对象，边表示对象之间的相对空间关系。

#### 语义图 Semantic Graph

目标：表示图像区域的自然语言抽象和对象关系。  
动机：自然语言抽象能桥接图像对象与问题/事实中的概念。  
实现：利用 dense captions 获取局部语义描述，再通过 semantic graph parsing 构建语义图，节点为对象名或属性，边为关系。

#### 事实图 Fact Graph

目标：表示候选外部事实及其实体关系。  
动机：答案来自事实知识库中的实体，需要显式组织候选事实并支持全局推理。  
实现：根据问题词与视觉概念检索候选 facts，再用关系类型分类器过滤，保留相关事实并构建 fact graph。

### 6.3 核心创新模块二：Cross-Modal Heterogeneous Graph Reasoning

这个模块回答：**已经有 visual、semantic、fact 三层图后，如何选择与问题相关、并且跨模态互补的证据？**

它分为两个过程。

#### 过程 1：Intra-Modal Knowledge Selection

目标：先在每一层图内部选择与问题相关的模态内证据。  
对应操作：

```text
Visual-to-Visual Convolution
Semantic-to-Semantic Convolution
Fact-to-Fact Convolution
```

具体又分为三个子步骤：

1. **Question-guided Node Attention**：在问题引导下给节点分配注意力权重，选择相关节点。
2. **Question-guided Edge Attention**：在问题引导下评价边的重要性，考虑邻居节点与关系。
3. **Intra-Modal Graph Convolution**：使用节点和边注意力进行消息传递，更新节点表示。

课堂重点：复杂小节必须继续分小标题。小标题让审稿人即使不看所有公式，也能看出算法流程。

#### 过程 2：Cross-Modal Knowledge Reasoning

目标：把视觉图和语义图中的互补信息汇聚到事实图，从而支持最终答案决策。  
对应操作：

```text
Visual-to-Fact Convolution
Semantic-to-Fact Convolution
Fact-to-Fact Aggregation
```

理由：答案来自 fact graph 的某个实体，因此跨模态信息最终需要服务于 fact graph 中实体表示的更新和选择。

### 6.4 Learning 写得少，不代表不重要

课件指出，MuCKO 中 Learning 部分相对较短，因为本文主要创新在“多模态异构图构建”和“跨模态异构图推理”。Learning 只是最终训练目标和预测方式，不应占据与核心创新无关的大量篇幅。

这对应课堂的写作原则：**篇幅分配要与创新重点一致**。不要把大量篇幅浪费在常规预处理、常规损失函数、标准训练细节上；除非它们本身就是贡献。

---

## 7. 本讲抽象出的 Related Work 写作模板

### 7.1 先确定 Related Work 的维度

```text
本论文主题：
- 任务维度：____
- 直接问题维度：____
- 方法/技术维度：____
- 数据/评价/应用维度（如必要）：____

Related Work 小节设计：
1. [较大任务背景]
2. [最相关问题]
3. [核心方法技术]
4. [可选：数据集/评测/应用]
```

### 7.2 每个 Related Work 小节的段落骨架

```text
[Topic sentence: 说明这一类工作的共同目标/问题]

Existing methods can be broadly grouped into [route A] and [route B].
[Route A] methods usually ... . Representative works ... . Their advantage is ... . However, when applied to [our target problem], they ... .
[Route B] methods address part of this issue by ... . Nevertheless, they still ... .

Different from these methods, our work ... .
```

### 7.3 Related Work 自检问题

- 这一小节为什么必须出现在本文中？
- 它帮助读者理解任务、问题还是方法？
- 同一类工作是否被归纳成技术路线，而不是按作者罗列？
- 是否指出每类路线在本文问题上的不足？
- 是否说明本文与这些工作的区别？
- 是否避免了和 Introduction 的大段重复？
- 引用的论文是否都真正读过，并且评价角度与本文问题相关？

---

## 8. 本讲抽象出的 Method 写作模板

### 8.1 Method 开头：Problem Formulation + Overview

```text
Given [input symbols], the task aims to [prediction objective].
Formally, [define variables, structures, candidate sets, objective].

As shown in Figure X, our framework consists of [module 1], [module 2], and [module 3].
[Module 1] aims to ... .
[Module 2] then ... .
Finally, [module 3] ... .
```

### 8.2 每个模块的小节模板

```text
### [Module Name]

Motivation / Goal:
[为什么需要这个模块？它解决整体问题中的哪一环？]

Input and output:
Given [input], this module produces [output].

Design:
To achieve this goal, we ... .
[公式或算法步骤]

Connection:
The resulting [representation/output] is then used by [next module] to ... .

Why this design:
Compared with [alternative], this design is more suitable because ... .
```

### 8.3 复杂小节的内部拆分模板

当一个模块超过半页或包含多个算法动作时，用加粗小标题或三级标题拆分：

```text
#### Step 1: Question-guided Node Attention
[目标 + 实现 + 公式]

#### Step 2: Question-guided Edge Attention
[目标 + 实现 + 公式]

#### Step 3: Intra-Modal Graph Convolution
[目标 + 实现 + 公式]
```

### 8.4 Method 自检问题

- 开头是否定义了任务、输入、输出、测试目标和符号？
- 是否先给整体框架，而不是直接进入公式？
- 每个模块是否有清晰边界？
- 每个模块是否说明动机、目标、输入、输出、实现、与前后模块关系？
- 小标题是否体现实现方式、逻辑关系和创新点？
- 图中模块名是否与正文小节标题一致？
- 公式是否服务于解释，而不是堆砌？
- 是否说明为什么不用其他实现方式？
- 实验设计是否能逐一验证方法模块和动机？

---

## 9. 本讲的“论文修改动作清单”

### 9.1 修改 Related Work

1. 列出本文所有主题：任务、问题、方法、数据/评价等。
2. 删除与本文问题无关的论文，即使你读过。
3. 将已有工作按路线归类，而不是按年份或作者堆叠。
4. 每一类路线后写一句“在本文问题上仍有什么不足”。
5. 每一节最后写一句“本文与这一类工作的区别”。
6. 检查 Related Work 与 Introduction 是否重复：重复则把 Introduction 保留动机，把 Related Work 改成系统分类与比较。
7. 检查每篇引用是否有真实阅读依据：问题、方法、优点、局限都能说清楚。

### 9.2 修改 Method

1. 先画框架图：模块、信息流、创新点、输入输出。
2. 将框架图中的模块转为正文小节标题。
3. Method 第一段补充 problem formulation 和 model overview。
4. 每个模块开头补一句动机与目标。
5. 每个模块写清输入、输出、关键操作。
6. 复杂过程内部加小标题。
7. 为每个设计补充“为什么这样做，而不是其他方式”。
8. 删减与创新无关的预处理细节。
9. 回到 Experiment，确认有消融或分析验证每个关键模块。

---

## 10. 本讲知识转化为 Agent Skill 的核心规则

本讲可被自动化为一个 Agent Skill，核心行为是：当用户写作或修改英文学术论文时，Agent 必须用本讲标准检查 Related Work 与 Method 是否建立了“主题—问题—方法—贡献”链条，并修复常见问题。

### 10.1 Agent 应强制检查 Related Work

```text
1. Identify the paper's task, exact research problem, and method family.
2. Build Related Work dimensions from those three layers.
3. Reject paper-listing paragraphs.
4. Rewrite work-by-work lists into route-based synthesis.
5. Make every paragraph end by connecting existing limitations to the current paper.
6. Ensure the final Related Work logic differentiates the current contribution from prior work.
```

### 10.2 Agent 应强制检查 Method

```text
1. Require problem formulation before module details.
2. Require a framework-level overview before formulas.
3. Map every figure module to a section heading.
4. Require each method module to state motivation, goal, input, output, design, and connection.
5. Split long procedures into subheadings.
6. Ask why this design is used instead of plausible alternatives.
7. Link method claims to experiments or analysis.
```

---

## 11. 课堂原始 transcript（保留原始转写，供追溯）

> 说明：下列 transcript 直接来自用户提供的原始 `.txt` 文件，作为追溯材料保留。本文前面的课堂重构已基于该 transcript 与 slides 做了结构化整理。

```text
各位同学，我们前面已经介绍完了论文的摘要和引言。那么下面我们来介绍一下论文相关工作怎么写。刚才我们也提到，有很多同学会把相关工作里描述现有方法的介绍的内容和引言里面介绍现有方法的内容重复写，也看不出来他们有大概哪方面的差别。所以这里面呢，我会重点讲相关工作需要突出哪些内容。那么我们先看看它相关工作，我们要基本涵盖哪几个维度的信息。首先你必须得理解你这篇文章想要做的工作到底你的方法到底包含了哪几个主题。那这个主题其实分几个维度，一个是你做的任务是什么？嗯，比如说我们上面介绍的那个工作是讲视觉问答的。那视觉问答相关的工作有哪些？基于知识的视觉问答又有哪些？ 这个就是和我们主题密切相关的相关工作。 那另外呢？ 就是我们这个主题相关的这个相关的方法。 也是我们主题相关的内容，比如说我们用了图神经网络。那图神经网络相关的方法有哪些？它的发展脉络有哪些？ 这也是我们可以去考虑的。 那第二个就是和我们问题所相关的工作。 比如说我们做的是这个知识型视觉问答。 那么在知识型视觉问答的这方面，大家解决这个问题上面都有哪些相关的工作？ 因为这个任务本身其实有很多维度不同的问题，比如说 他可能也有数据的问题，也有偏执的问题，对吧？也有做引入知识的问题。 那么有这么多的问题，你在introduction里面你重点。 最后介绍现在方法的挑战是什么？ 那你就要围绕这个方法。 的挑战，这个问题的挑战。 去介绍相关的相呃问题相关的工作，而不是把其他的。 比如说跟数据相关的呀，跟模型优化相关的呀，跟这个模型损失相关的呀，这些工作全都罗列在你的相关工作里。 只需要和你文章所要理解的主题相关，和你解决的问题相关就可以。 那么你在我们知道要写哪些内容的时候呢？ 你在写的时候，到底应该怎么去写这些相关工作？ 其中最主要的就是你要把相关工作划分不同的维度去介绍。 对。 后面我会举具体的例子。 那么同一个主题，刚才说了我们有这么多。 呃，比如说视觉问答、知识性视觉问答等等不同的主题。 那同一类主题也需要归纳。 它到底有哪几种技术路线和相应的问题？ 嗯。 那最后你在每一个主题下面的相关工作，你还是需要去总结。 这一类方法到底存在什么样？现在突出的问题。 以及你到底怎么样去解决这样的问题？ okay. 最后其实你是引出了这篇文章所研究的工作和现有方法工作的区别和创新性。 那么这里面，我觉得主要想给大家提示两点。 第一。 基本上你所引用的工作都是你看过的工作，而且是深入理解的。 否则你的relative work是很难写深入的，可能你只能从别人论文里去copy一下。 他们大概怎么样去介绍这个工作的，但是他们介绍的角度是出发于他到底要解决什么问题。 因为一篇文章，其实你从不同的角度去看它，你对它的评价是不一样的。 所以你需要真正的去理解这篇文章，以及这篇文章在解决你当前这个要解决的问题上面。 他所做的好的和不好的地方。 那第二个。 就是不要罗列你所有写的论文，就是不要说a做了什么，b做了什么，c做了什么，他们存在的问题是什么。 而是还是要以一个整体去介绍他们的思想。但是在研究工作相关工作这一块，你可以具体展开去讲一讲他们在解决的这个思路上面有什么样的区别。比如说有两三篇代表性的工作。 好，那我们还是沿着我们之前的这篇论文，我们来看看。 它包含了我们写了哪几个相关工作？ 首先，我们介绍了。 视觉问答相关的方法，因为本身不管是知识型的还是非知识型的，它本身都是要看图去回答问题。 那么这一类。 传统的任务上面的传统方法，它有什么样的？ 记住路线以及它存在什么样的方法，就是 为什么我们在解决知识型视觉问答的时候，不能够延续之前传统视觉问答的方法去做？ 所以这一块其实是系统梳理了。 V R language那呃不是V Q A这一个问题相关的方法，最后一定大家看到我标红线的这一部分就是落脚到 现在的这些方法。 在解决知识型视觉问答的任务上，它存在什么样的不足？ 也就是你一定要建立。 这一类方法和你所解决的问题之间的关系。 和你在解决问题上面相比，现有方法的一个进步在哪里？ 那么第二部分呢，其实就更聚焦在我们今天这个文章里在解决的一个问题，就是基于知识型的视觉文档。 那这一类可能方法就没有以前那么多，所以。 这两类方法你看到，其实它总结出来的体量是差不多的。 那也就是说，你总结问题的力度是不一样的。 以前传统的方法，你其实总结大概的思路，技术脉络就可以。 为的是你能够更全面地理解这个问题和相关方法。 而基于知识的试卷问答，就跟这个文章更相关的这个 related work 你要写的更详细。也许这个领域并没有特别多的相关的工作，那每一个工作其实都对你的工作很有关联，所以他们的做的好还是不好，你可以详细的把他们的缺陷指出来。那最后一句也是我 highlight 的这部分，也是一定要落脚到那现在的，最新的方法，它存在的局限性。我这篇论文针对这个局限性，我是怎么样去提出了一个什么方法解决的。所以你在总结现有的这些方法的时候，一定是有一个层层递进的关系，就是前面的方法，前面这一类方法，它是什么思路出现了什么问题，那后面这一类方法针对前面的问题是怎么样解决的？再往后最新的方法又是怎么解决的？那最新的方法依然存在什么样的局限，所以我们提出了一个什么样的方法。所以这一块。 其实你需要非常简洁，一两句话点出来他们的问题，以及我这篇的文章到底哪一个环节或者哪一个模块解决了这个问题。 OK，那第三部分其实是从另一个维度，就是从方法层面去讲了相关的工作。因为我们在任务层面是呃和上面这两部分是相关的，那么在方法技术实现层面，我们是和图神经网络这一块相关的。但是大家想到图神经网络其实发展了很长时间，那相关的工作也非常多，你不可能罗列所有的方法。所以这里面重点，你的工作用到的是图神经网络的哪方面的技术？我们这里用到的是异构图神经网络，那这里面其实异构图神经网络在其他领域，比如说呃自然语言理解，然后图像或者社交网络都有非常多的工作，那他们和你的这个工作的最大的区别。 方法上的区别是什么？为什么他们的方法不能够直接迁移过来？或者说他们方法在解决的问题上和你方法存在的最大的差异是什么？你要把这个一定要点出来，否则大家可能会觉得你用了一个一直图神经网络的方法，是不是就是迁移，直接用了现有的一些方法？那你的创新性在方法上的创新性到底是什么？你需要通过详细的去介绍现有方法在技术层面上和你在技术层面实现层面上的差别，而不能仅仅停留在我们做的任务不一样。它一定是在方法的细节和方法针对的数据，针对数据解决的问题上存在着很大的区别。 OK，好，我们这里面介绍方法的时候，写方法的时候，我建议大家，写相关工作的时候，建议大家可以写完你的论文的方法你就可以写了。因为你写完方法之后，你就可以非常清楚的了解我方法大概涉及到了哪些相关。 关技术以及哪些相关的呃任务，所以你这个时候就可以把它梳理成自己的方面去写相关工作。好，那下面就进入到我觉得论文里面其实最好写的一部分，就是我们自己去设计的模型和方法。那总的原则来说，大家写方法一定要从读者，不管是给你提意见的老师、同学还是审稿人，要从他们的角度、专业的角度去思考，怎么样把你的贡献亮点突出。并且让审稿人或者帮你提意见的同行在最短的时间内能够清晰的理解你的模型的思路，这个是总的原则。但是这个大家也是现在最难做到的。那么你在写的时候一定要用标准的数学的表达，规范的表达，确定好每一部分。 你到底想表达的目标是什么？不要把所有东西都混在一起，没有任何边界的界定的去写，笼统的写。那么在你模型介绍的时候，我待会会举一个具体的例子，讲第一步、第二步、第三步到底应该怎么去做。但是这里面我觉得会有一些总的原则，就是我一般习惯会让同学们先画我们的框架图，基于框架图的逻辑再去写你的论文的语言会特别的快捷，防止返工，而且逻辑非常的清晰自洽。那么在你写内容或者画图的时候，不管是怎样，你都要清晰的去界定你的方法，每一个具体过程的之间的边界。这个边界既是你实现过程的边界，也是你这个每每一个过程，它到底解决了整个问题的哪一个环节，也是要清晰把它界定出来的。OK，最后就是 是我们怎么样去解释我每一步到底它解决了什么问题，为什么能够解决这个问题。好，那我们再看一下，就是 CCFA 类的论文在这一块写的时候，它一定是针对问题，每一步都会讲清楚我是为什么能够这一步做的，解决了这个问题的其中一个环节。而且它图和表一定是相互呼应，能够印证的。就是其实论文大家可以看到画一个图会占特别大的篇幅，但是意图胜千言，就是你的图一定是辅助审稿人去理解你的文字的，而你的文字一定是更详细、更有说服力的去把你的方法能够阐明清楚的。所以在有限的篇幅之内，一定要提供尽量多的信息，让别人能够清晰理解你的方法，而不是浪费这些空间。但是呢，C类的论文基本上大部分的很。 很少，就是说能够把动机讲清楚。他一般都是在罗列一些方法，但是你从这个一步一步方法来看，你不能说理解它到底有什么样的通用性，为什么不用另一种实现方式。 OK，那我们就来具体的，还拿我们2020年埃及卡的这篇是基于知识的视觉问答的嗯那个论文来给大家讲。方法这一步到底怎么去做？ OK，好，我这里面把具体方法这一部分的内容和我们这个方法对应的框架图都罗列在这里面了。那我想跟大家说，我们第一步一定最好先要去把这个框架图画出来。那么后面我专门会有一讲，去讲怎么样去详细的画好一个框架图，以及怎么样基于这个框架图能够写好这个 methodology。但这一块我重点想跟大家说，这个写的整个的过程。 那么第一步一定是你要确立好你整个的逻辑，就是你的这几块大的标题，你的方法到底分哪几个比较呃明确的模块，他们之间的衔接度关系是什么？那么在这一块我想跟大家说的是，你不是说不一定是按照你做实验或者最初思考的过程去写你的方法。有可能你在最一开始信息表征这一块，或者其他的正常逻辑应该先去叙述的部分，它可能放在最后叙述。你需要尽量早的去把你的创新的东西，你核心的方法，在最多的篇幅，最主要的这个地方去写清楚，而不是大量的篇幅去写一些，比如说数据预处理呀，一些跟你创新性不太相关的内容，那些只需要非常精简的语言就可以把它表达清楚。所以这一块我想说一定 定先要确定你的创新要表达成哪几个模块，比如说我们这个工作两大创新，第一个就是我怎么样去。 表征用统一的框架去表征视觉语言和知识，那这是一块，也就是我们。 画的这一个标题多模态的意志图的构建。 所以我们用了一大笔。 篇幅不管是图还是文字，去讲这一个内容。 那第二块就是我有了这样统一的表征之后，我怎么样？ 在这个推理的过程中，去自适应的互补关联这样的信息。 那么我们就提出了第二个关键的模块，就是跨模态的一致图的推理，无论是在图上还是在文章里。 都会有对应的部分。 而且是很大的篇幅去重点讲这个东西。 而大家可以看到，最后learning的过程其实非常简单，写的非常少篇幅。 而甚至在这个看这个意志图推理的过程，其实也是。 比较复杂也是我们的创新点所在，所以我们又把它内部分成了两个小的过程。而且这两个小的过程在我们正文里又分了两个小的subsection，分别去讲。 所以。 大家要记得，就是我们第一一定要清晰的界定我们核心的一个创新。 第二个就是。 哪几个模块儿？ 分别解决了我创新点的哪几个环节？ 用不同的子的这个章节去介绍。 第三个就是你的标题一定。 要突出两点，第一，你怎么样实现的？ 第二，你的实现过程之间是什么样的逻辑关系，以及它的创新性。 所以你别看这个标题只有四五个单词，但其实也是经过反复的琢磨，还 一定是让整个的这个标题，其实你不用看正文的内容，你只看标题，你大概也了解我这个过程是怎么实现的，这就达到了你写这个标题。 它的作用和目的。 好，那另外就是你的标题，大家可以看到和你的图一定是对应的，也就是审稿人或者其他读者。 在看你的标题，看你的图的时候，就大概理解你的过程，但是不 当我想去详细了解这一部分的实现细节的时候，我直接通过标题就可以定位到你文章里介绍这个的公式和这个语言描述。 所以。 尽量最低的程度，让审稿人去花时间读懂你的文章。 Okay. 好，那第二个就是第二个大家要写的就是在你真正的写每一个模块内容的时候，一定要去先去介绍你这一个模块。 要达到的目标是什么？ 你为什么要通过这个达到？ 这个目标，这个方法能达到这个目标，以及我达到这个目标和前一步和后一步之间的关系是什么？ 所以大家可以看到，其实在每一个小节的最前面，我标绿色的这个框里的话，都是在写这一部分内容。 Okay. 好。 那么我们再往后写，比如说到一个具体的小节里面，我们发现其实这个过程也很复杂。 我们可能非花半页的这个篇幅才能把这个事情介绍清楚。 但是如果你 全部从头到尾这样罗列这个过程去。 会给审稿人非常大的这种阅读的。 障碍 就是他很难把握其中的逻辑关系。 所以这里很建议大家，如果你的过程会非常复杂，一节内容有点长，那你可以里面再细分这种，比如说加粗呀或者其他的小标题。 去把这个过程的步骤再给它highlight出来，让大家很清晰的。比如说我这篇文章，我完全不看内容的情况下，我只看这些小标题，我也大概知道你是怎么实现的，就达到目的了。 好。 那最后其实我想说的是，在所有的方法介绍之前，大家还需要在你的整个方法的第一段，也就是一进来的这一段里介绍清楚你的问题，就是对问题的定义。 比如说你这是一个什么样的任务，它的输入输出是什么，它的测试要怎么测，都需要用符号标准的语言去把它定义清楚。 另外第二部分要描述的就是你这个方法整个这么大一篇幅的，就 后面的细节大概他们。 有包含哪几个模块儿？ 这些模块之间的逻辑关系是什么？他们之间的支撑或者 这个衔接关系是怎样的？ 以及是不是有框架图可以去直接先去看一下整个的逻辑？ 所以这一块整体介绍，其实大家有的时候经常会忽略。 所以希望大家能够早早的去先写好这一部分。 那么在整个写方法的时候，我觉得大家需要注意的第一个就是第 一定要加入你的动机的说明，在每一部分方法，否则。 审稿人会非常不解，我这一部分到底对于解决整体问题是什么样的一个作用？ 那第二个其实就是要说明为什么我这一步。 要这样去实现，而不用其他的方法。 这个其实在审稿的过程中，大家看到很多的审稿意见都会给大家提这种问题。比如说你为什么不把这个融合的方式换成比如说双线性映射呀，或者拼接呀，或者怎样融合呀？为什么你只单单选择了这种方法？ 当然你可以在你后面的实验消融实验里面去试啊，我试别的方法是没有这个效果好，这只是一种解释。但我觉得更有力的解释是你从原理上。 从这个机理上，或者从数学推导上去分析，为什么这种方法是现在所有这么多方法里面最优的选择。

```

---

## 12. 一句话复盘

Related Work 的任务是把本文放进已有研究脉络中：**不是罗列论文，而是围绕主题、问题、方法归类比较，并引出本文区别**。Method 的任务是让审稿人快速理解你的创新模块：**不是罗列步骤，而是先定义问题，再用框架图、小标题、动机、公式和分析说明每一步为什么必要、如何实现、解决哪一环问题**。


---
---

# Version 2 — Independent Reconstruction (companion skill's author)

> This is the companion skill's own independent full reconstruction of this
> same lecture, produced separately from the original transcript and slide
> deck. Appended in full rather than cross-referenced: Version 1 above and
> Version 2 below are two independent passes over the same source material,
> kept side by side so a gap or slip in one is very likely caught by the
> other (see `references/provenance.md` for the specific corrections each
> pass independently made that the other missed). Read both when precision
> matters; either alone is already high-fidelity.

# 《科研与英文学术论文写作指南》

## 第四讲：英文学术论文之写作思路——相关工作和方法

### —— 课堂完整复盘（Markdown 版）

---

## 文档说明

体例与前三讲一致。本讲 PDF 同样为中文 CID 子集字体、文本层无法直接提取中文，中文部分以 OCR（chi_sim+eng）识别并与逐字稿交叉核对；论文原文（英文）可直接从 PDF 文本层可靠提取，本讲展示的方法段落原文引自 Mucko 论文（IJCAI 2020，于静老师本人工作，与第二、三讲共享同一示例，保持全系列讲解的连贯性）。

---

## 〇、本讲基本信息

| 项目 | 内容 |
| --- | --- |
| 讲次标题 | 第四讲：英文学术论文之写作思路——相关工作和方法 |
| 讲者 | 于静 副研究员，中国科学院信息工程研究所 |
| PPT 页数 | 8 页 |
| 示例论文 | Mucko: Multi-Layer Cross-Modal Knowledge Reasoning for Fact-based Visual Question Answering（IJCAI 2020，延续第二、三讲） |

### 课堂讲解：开场

> 各位同学，我们前面已经介绍完了论文的摘要和引言。那么下面我们来介绍一下论文相关工作怎么写。刚才我们也提到，有很多同学会把相关工作里描述现有方法的介绍的内容和引言里面介绍现有方法的内容重复写，也看不出来他们有大概哪方面的差别。所以这里面呢，我会重点讲相关工作需要突出哪些内容。

---

## 一、相关工作——基本要求（PPT 第 2 页）

### 幻灯片内容（原文精准转录，OCR 噪声较大处已结合课堂讲解逻辑复原）

标题：**一篇论文的组成——相关工作**

基本要求：
- 详细概括本文所有主题的相关工作
- 需要从不同维度划分主题
- 同一主题内的相关工作需要归类总结
- 总结出该类方法存在的问题
- 引出本研究与现有工作的区别和贡献

### 课堂讲解：相关工作要涵盖哪些维度

> 首先你必须得理解你这篇文章想要做的工作，你的方法到底包含了哪几个主题。

于静老师指出，"主题"需要从多个维度去思考，并非只有单一角度：

**维度一：任务维度（Task）。** 例如 Mucko 这篇论文做的是视觉问答，那"视觉问答相关的工作有哪些？基于知识的视觉问答又有哪些？"这些都是与主题密切相关的相关工作。

**维度二：方法/技术维度（Method）。** 例如本文用了图神经网络，那"图神经网络相关的方法有哪些？它的发展脉络是什么？"这也是需要考虑的相关工作范畴。

**维度三：与"问题"直接相关的工作。** 她进一步区分：知识型视觉问答这个任务本身可能牵涉多个不同维度的问题（数据的问题、偏置的问题、引入知识的问题等），但在 Introduction 里，你最终落脚的是"现在方法的挑战是什么"，那么相关工作就要**紧紧围绕这个挑战/问题**去介绍，而不能把和数据相关、模型优化相关、模型损失相关等其他不属于你所述核心挑战的工作，全都堆砌进相关工作里——**只写与你要理解的主题、要解决的问题相关的内容**。

### 课堂讲解：相关工作要怎么写

于静老师给出的核心写法原则：

1. **按维度划分介绍，而非按时间顺序罗列。** 同一主题下的相关工作需要归纳出"到底有哪几种技术路线和相应的问题"，而不是"A 做了什么、B 做了什么、C 做了什么，他们存在的问题是什么"这种简单堆砌。
2. **每一类方法下要总结出这一类方法目前存在的突出问题，以及你打算怎么解决。** 最终目的是引出本文工作与现有方法的区别和创新性。
3. **两个重要提醒：**
   - **必须是真正读过、深入理解的工作**，否则相关工作很难写深入，只能从别人论文里"抄"一下别人怎么介绍这个工作——但那种介绍的角度出发于别人要解决的问题，而同一篇论文从不同角度去看，评价是不一样的。你需要真正理解这篇被引用的文章，尤其是它在解决你当前问题上做得好与不好的地方。
   - **不要罗列所有引用的论文逐一点评**（不要"A 做了什么、B 做了什么、C 做了什么"式的记流水账），而要以整体视角介绍这一类方法的思想；但对于两三篇代表性工作，可以具体展开讲一讲它们在解决思路上的区别。

---

## 二、相关工作范文精讲：以 Mucko（IJCAI 2020）为例的三层维度（PPT 第 3 页）

### 幻灯片内容（原文精准转录，来自 PDF 文本层直接提取，可信度高）

页面展示了 Mucko 论文 Related Work 章节的三个子部分原文：

**"视觉问答方法"（Visual Question Answering，一般性/传统任务层面）：**
> *"Visual Question Answering. The typical solutions for VQA are based on the CNN-RNN architecture [Malinowski et al., 2015] and leverage global visual features to represent image, which may introduce noisy information. Various attention mechanisms [Yang et al., 2016; Lu et al., 2016; Anderson et al., 2018] have been exploited to highlight visual objects that are relevant to the question. However, they treat objects independently and ignore their informative relationships. [Battaglia et al., 2018] demonstrates that human's ability of combinatorial generalization highly depends on the mechanisms for reasoning over relationships. Consistent with such proposal, there is an emerging trend to represent the image by graph structure to depict objects and relationships in VQA and other vision-language tasks [Hu et al., 2019b; Wang et al., 2019a; Li et al., 2019b]. As an extension, [Jiang et al., 2020] exploits natural language to enrich the graph based visual representations. However, it solely captures semantics in natural language by LSTM, which lacks fine-grained correlations with the visual information."*

**"基于知识的视觉问答方法"（Fact-based / Knowledge-based VQA，任务细分层面）：**
> *"Fact-based Visual Question Answering. Human can easily combine visual observation with external knowledge for answering questions, which remains challenging for algorithms. [Wang et al., 2018] introduces a fact-based VQA task, which provides a knowledge base of facts and associates each question with a supporting-fact. Recent works based on FVQA generally select one entity from fact graph as the answer and fall into two categories: query-mapping based methods and learning based methods. [Wang et al., 2017] reduces the question to one of the available query templates and this limits the types of questions that can be asked. [Wang et al., 2018] automatically classifies and maps the question to a query which does not suffer the above constraint. Among both methods, however, visual information is used to extract facts but not introduced during the reasoning process. [Narasimhan et al., 2018] applies GCN on the fact graph where each node is represented by the fixed form of image-question-entity embedding. However, the visual information..."*（原文在此段末尾继续论述现有方法在视觉信息引入推理过程方面的不足，承接下方方法部分的创新点设计）

**"异构图神经网络方法"（Heterogeneous Graph Neural Networks，技术/方法层面）：**
> *"...common in the real world. [Schlichtkrull et al., 2018] generalizes graph convolutional network (GCN) to handle different relationships between entities in a knowledge base, where each edge with distinct relationships is encoded independently. [Wang et al., 2019; Hu et al., 2019] propose heterogeneous graph attention networks with dual-level attention mechanism. All these methods model different types of nodes and edges on a unified graph. In contrast, the heterogeneous graph in this work is across multiple modalities... For this specific constraint, we propose the intra-modal and cross-modal graph convolutions for reasoning over such multi-modal heterogeneous graphs."*

### 课堂讲解

于静老师带读这三段，逐一说明其对应的写作意图：

**第一段（视觉问答方法，传统/一般任务层面）：** 系统梳理"VQA"这一大类问题相关的方法——传统方法的技术路线是什么，存在什么样的不足。最后落脚（原 PPT 中以红线标出）到"这些方法在解决知识型视觉问答任务上存在什么样的不足"——即必须建立起"这一类方法"和"你所解决的问题"之间的关系：现有方法相比你要解决的问题，进步和差距分别在哪里。**这一部分的写作分量与下一部分（知识型 VQA）大致相当**，但着重点不同——传统方法只需要总结大概思路和技术脉络（目的是让读者更全面理解问题和相关方法），不需要逐篇精读点评。

**第二段（基于知识的视觉问答方法，任务细分/更贴近本文问题层面）：** 这一部分更聚焦本文实际解决的问题——基于知识的视觉问答。于静老师指出，这一领域相关工作数量通常没有传统 VQA 那么多，所以**每一篇被引用的工作都和本文工作关联更紧密，可以也应该写得更详细**——具体指出每个工作的缺陷。最后一句（她特别 highlight 的部分）一定要落脚到"最新的方法存在什么样的局限性，本文针对这个局限性提出了什么方法来解决"。她强调，总结现有方法一定要呈现出**层层递进的关系**：前一类方法是什么思路、出现了什么问题 → 后一类方法针对前面的问题怎么解决 → 最新的方法又是怎么解决的、依然存在什么局限 → 因此本文提出了什么方法。这一段要非常简洁，用一两句话点出问题所在，以及本文哪个模块解决了这个问题。

**第三段（异构图神经网络方法，技术/方法实现层面）：** 这是"从另一个维度"——方法/技术实现层面——来写相关工作，与前两段的任务层面维度并列。图神经网络本身发展历史很长、相关工作非常多，不可能全部罗列，因此要**聚焦本文实际用到的技术分支**（本例中是异构图神经网络）。关键是要讲清楚：这类技术在其他领域（自然语言理解、图像、社交网络等）已有大量工作，它们与本文工作在**方法层面**最大的区别是什么？为什么不能直接迁移过来？她特别强调这一点很重要：**否则读者可能会认为你只是把现有方法直接迁移过来用，看不出方法层面的创新性**——必须通过详细介绍现有方法在技术细节层面、以及所针对数据/问题层面与本文方法的差异，而不能仅仅停留在"我们做的任务不一样"这种表面区别上。

**关于写作时机：** 于静老师建议，相关工作可以在**写完方法部分之后**再写——因为写完方法后，会非常清楚地知道方法到底涉及了哪些相关技术和相关任务，这时候更容易把相关工作梳理成自己的维度。

---

## 三、一篇论文的组成——方法：写作总则与要素（PPT 第 4 页）

### 幻灯片内容（原文精准转录）

标题：**一篇论文的组成——方法**（最容易写的部分，可以先写这一部分内容）

- **总原则：** 换位思考，从读者角度出发
- 数学语言描述、问题建模、确定研究目标
- 方法：
  - 模型框架图，清晰定义模块，突出创新之处
  - 小标题确定，突出方法特色、用途、创新性，图文一致
  - 模型总体介绍，突出模块间关联
  - 分模块介绍，突出模块设计动机
  - 精简表达，善用公式，理论分析

### 课堂讲解

> 好，那下面就进入到我觉得论文里面其实最好写的一部分，就是我们自己去设计的模型和方法。

**总原则：** 写方法一定要**从读者的角度**（不管是给你提意见的老师、同学还是审稿人）去思考，怎么样把你的贡献亮点突出，并让审稿人或同行在最短时间内清晰理解你的模型思路——这是总的原则，但也是目前大家最难做到的。写作时要用**标准、规范的数学表达**，确定好每一部分到底想表达的目标是什么，不要把所有内容混在一起、没有边界地笼统去写。

**建议做法（先画图后写文字）：** 于静老师建议同学们先画好框架图，基于框架图的逻辑再去写论文的语言，这样会特别快捷、防止返工，逻辑也非常清晰自洽（她提到后续会有专门一讲详细介绍如何画好模型框架图）。不论是画图还是写文字，都要**清晰界定方法每一个具体过程之间的边界**——这个边界既是实现过程的边界，也是"这个过程到底解决了整个问题的哪一个环节"的边界，都需要清晰界定出来。最后要解释清楚每一步到底解决了什么问题、为什么能够解决这个问题。

**CCF-A vs 一般论文的差异（呼应下页表格）：** CCF-A 类论文针对每一步都会讲清楚"我为什么这样做，能够解决这个问题的哪一个环节"，而且图和表一定与文字相互呼应、能够印证——"意图胜千言"，图辅助审稿人理解文字，文字则更详细、更有说服力地把方法阐明清楚，在有限篇幅内提供尽量多的信息。C 类论文大多很少能把动机讲清楚，一般只是罗列方法步骤，读者难以理解其通用性、也看不出为什么不用另一种实现方式。

---

## 四、方法写作：CCF-A / CCF-C 对比（PPT 第 5 页）

### 幻灯片内容（原文精准转录）

| | CCF-A | CCF-C |
| --- | --- | --- |
| 总体 | 问题—方法—实验，相互呼应 | 问题—方法—实验，各自其说 |
| 动机 | 有理有据 | 大家都在研究，所以我研究 |
| 方法 | 针对问题设计，每一步设计目标明确；标题和图突出创新性和重点，相互呼应；每一步方法设计都有理可依 | step1 -> step2 -> step3 |
| 实验 | 针对方法逐一证明，针对动机逐一分析 | 只看结果，缺乏分析 |

（该表为第二、三讲中反复出现的 CCF-A/CCF-C 对比框架在"方法"维度上的具体化版本，新增"标题和图突出创新性和重点，相互呼应"以及"每一步方法设计都有理可依"两条，专门针对方法部分的写作提出要求。）

---

## 五、方法范文精讲：以 Mucko 为例逐步拆解（PPT 第 6–7 页）

### 幻灯片内容（原文精准转录）

**PPT 第 6 页** 展示 Mucko 论文 Figure 2（模型总体框架图），图中包含两大模块：**Multi-Modal Heterogeneous Graph Construction**（多模态异构图构建：Object Regions / Dense Captions / Candidate Facts 分别构建 Visual Graph / Semantic Graph / Fact Graph）与 **Cross-Modal Heterogeneous Graph Reasoning**（跨模态异构图推理：Intra-Modal Reasoning + Cross-Modal Reasoning），并通过"红色消防栓用途"示例问答贯穿始终，最终得出答案"Firefighting"。图注原文：*"Figure 2: An overview of our model. The model contains two modules: Multi-modal Heterogeneous Graph Construction aims to depict an image by multiple layers of graphs and Cross-modal Heterogeneous Graph Reasoning supports intra-modal and cross-modal evidence selection."*

**PPT 第 7 页** 展示该论文方法部分的正文原文片段（3.1 Multi-Modal Graph Construction 及 3.3 Cross-Modal Knowledge Reasoning 小节），并以中文批注叠加标出写作要点，包括：**"标题突出创新点和过程"**（标注在小节标题旁）、**"小标题"**（标注在子过程分段处）、**"每一个过程首先介绍背后的动机和目标"**（标注在小节开篇的目标陈述段落处）。

### 课堂讲解

> 我这里面把具体方法这一部分的内容和我们这个方法对应的框架图都罗列在这里面了。第一步一定最好先要去把这个框架图画出来。

**第一步：确立整体逻辑框架。** 先确定方法分哪几个明确的大模块，以及它们之间的衔接关系是什么。于静老师特别提醒：**写作顺序不必等于实验或最初思考的顺序**——某些按常规逻辑应该先叙述的内容（比如信息表征部分），完全可以放到最后叙述；而应该**尽早、用最多篇幅**把最核心、最具创新性的方法讲清楚，不要在数据预处理等与创新性关系不大的内容上花费大量篇幅（这些只需精简语言带过）。

以 Mucko 为例，两大核心创新分别对应两大模块：
1. **多模态异构图的构建：** 怎么样用统一的框架去表征视觉、语言和知识——这一块用了大篇幅的图和文字去讲；
2. **跨模态异构图的推理：** 有了统一表征之后，怎么样在推理过程中自适应地互补关联这些信息——这也是重点篇幅所在；由于这部分本身也比较复杂、也是创新点所在，于静老师团队进一步把它拆成两个子过程（Intra-Modal Reasoning 和 Cross-Modal Reasoning），并在正文中分成两个独立的 subsection 分别讲解。

而模型的 **Learning（训练/损失函数）部分则写得非常简单、篇幅很少**——因为这不是本文的核心创新。

**取写作经验提炼为三条：**
1. 清晰界定核心创新点是什么；
2. 明确哪几个模块分别解决了创新点的哪几个环节，用不同的子章节分别介绍；
3. 每个（子）标题一定要突出两点：怎么样实现的？实现过程之间的逻辑关系及创新性是什么？——"标题只有四五个单词，但也是经过反复琢磨"，好的标题应达到"不看正文，只看标题，也能大概了解整个过程是怎么实现的"这一效果，且**标题要与图对应**：审稿人看标题、看图就能大致理解流程，若想深入了解细节，可直接通过标题定位到对应的公式和文字描述——**尽量以最低的阅读成本，让审稿人读懂你的文章**。

**第二步：模块内部的写法——先讲动机，再讲实现。** 在写每一个模块的具体内容之前，一定要先介绍这个模块要达到的目标是什么、为什么要通过这个方法达到这个目标、这一步和前后步骤之间的关系是什么（对应 PPT 第 7 页中用绿色框标出的每小节开篇段落）。如果某个过程特别复杂（可能要花半页篇幅才能讲清楚），不要从头到尾线性罗列（会给审稿人造成很大的阅读障碍、难以把握逻辑关系），建议进一步用加粗小标题等方式把步骤 highlight 出来，让读者即使完全不看正文，只看这些小标题，也能大概知道你是怎么实现的。

**方法部分的"开篇第一段"不可或缺：** 于静老师强调，在所有具体方法介绍之前，方法部分的第一段必须讲清楚**问题定义**——这是一个什么样的任务，输入输出是什么，怎么测试，都要用标准的符号化语言定义清楚；随后要描述整个方法**包含哪几个模块、模块之间的逻辑关系和衔接支撑关系是什么**，并说明是否有框架图可供先行整体把握逻辑。她指出这部分"整体介绍"的内容常常被同学们忽略，因此建议尽早写好这一部分。

**写方法时两个必须注意的点（reviewer 最常问到的问题）：**
1. **每一部分方法都要加入动机说明**，否则审稿人会非常不解——这一部分到底对解决整体问题起到什么作用？
2. **要说明为什么这一步要这样实现，而不用其他方法。** 这是审稿意见中极为常见的问题类型（比如"为什么不把这种融合方式换成双线性映射、或者拼接、或者其他融合方式？为什么只单单选择了这种方法？"）。虽然可以在后面的消融实验里做对比说明（"我试了别的方法，效果没这个好"），但于静老师认为**更有力的解释是从原理、机理或数学推导层面**分析，为什么这种方法是所有可能方法里最优的选择——而不仅仅是实验层面"试出来的"经验性解释。

---

## 六、结语（PPT 第 8 页）

**幻灯片内容：** 与前几讲结尾页版式一致（欢迎在 B 站/知乎专栏/邮件交流 + 联系方式 + 三个二维码入口）。本讲 transcript 中未见到与前几讲相同的完整结语口播文字，推测录制时以相同套路收尾（详见课程结语通用文本，见第一至三讲文档）。

---

## 附录：本讲核心概念速查

1. **相关工作的三个维度：** 任务维度（一般任务 + 细分任务）、方法/技术维度、与核心挑战直接相关的工作——只写与本文所述核心问题相关的内容，不做无关堆砌。
2. **相关工作写法：** 按维度分类归纳（而非按时间顺序罗列）→ 每类总结技术脉络与现存问题 → 层层递进（前一类方法思路及问题 → 后一类方法如何解决 → 最新方法仍存在的局限）→ 落脚到本文方法针对该局限的解决方案。
3. **两个铁律：** 必须读过、深入理解被引用的工作（而非转述他人转述）；不逐篇罗列点评，以整体视角呈现，仅对 2–3 篇代表性工作展开细节对比。
4. **相关工作宜在方法部分写完之后再写**——此时最清楚方法涉及哪些相关技术和任务。
5. **方法部分总原则：** 换位思考，从读者角度出发；先画框架图，再据图写文字，防止返工。
6. **方法写作三步法：** 确立整体逻辑框架（不必按实验顺序，核心创新最先/最多笔墨）→ 分模块介绍（先讲动机目标，再讲实现，复杂步骤用小标题拆解）→ 精简表达（善用公式、图文呼应）。
7. **方法部分开篇必写：** 问题定义（任务/输入输出/测试方式的符号化定义）+ 模块总览（几个模块及其逻辑关系，可配框架图）。
8. **审稿人最常问的两类问题：** "这一步到底解决了整体问题的什么环节？"（需要动机说明）、"为什么这样做而不用其他方法？"（最有力的回答来自原理/数学推导，而非仅靠消融实验）。
