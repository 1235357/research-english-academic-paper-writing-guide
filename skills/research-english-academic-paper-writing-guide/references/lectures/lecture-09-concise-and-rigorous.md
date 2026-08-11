# 第九讲 英文学术论文之英文规范——如何做到简洁与严谨

**English title for Skill**: How to Be Concise and Rigorous  
**课程**：科研与英文学术论文写作  
**主讲**：于静 副研究员，中国科学院信息工程研究所  
**时间与平台**：2022.07 @ Bilibili  
**课程主页**：https://mmlab-iie.github.io/course/  
**本 Markdown 复现方式**：仅使用文字复现课件、课堂讲解、公式、表格、图示与视觉信息，不引用 PNG/JPEG 等图片。

---

## 0. 本讲一句话定位

本讲不是单纯讲“英文好不好”，而是讲英文科研论文中的**表达思维**与**叙述逻辑**：论文的目标不是把语言写得复杂、华丽或“像翻译腔的长句”，而是让同行和审稿人在有限时间内，用最小阅读成本准确理解你的科研发现、技术目标、创新点、公式定义、图表含义与实验结论。

本讲的总原则可以压缩成一句话：

> 用最简单的话表达最明白的意思；用最清晰的逻辑支撑最重要的结论。

---

## 1. 课堂开场：问题不只是“英文不是 native speaker”

于老师开场先回应很多学生的共同焦虑：自己不是英文 native speaker，怎样把英文学术论文写得既地道又专业？很多同学把论文难写归因于“英文不好”，但本讲强调，当前大部分问题并不主要出在语言词汇本身，而在于**英文论文中的逻辑思维方式**。

课堂提出两个目标：

1. 让学生理解怎样用英文思维写学术论文，而不是把中文长句机械翻译成英文。
2. 给出实操建议和工具意识，帮助检查专业术语、符号定义、拼写、图表、文献等规范问题。

---

## 2. 英语写作规范的八项注意

英语写作规范非常细碎，但本讲把常见问题归纳为八项：

1. 精简的表达方式
2. 严谨的叙述逻辑
3. 专业的学术用语
4. 规范的符号使用
5. 标准的学术术语
6. 客观的图表绘制
7. 正确的文献引用
8. 坚守的学术道德

其中第 1 项和第 2 项最难，因为它们涉及论文作者的思维方式：如何确定一句话的功能、如何安排信息层级、如何让审稿人快速建立理解。第 3 项到第 8 项更偏向规则与检查项，相对容易通过清单和工具改进。

本讲重点展开前两项：

- 精简的表达方式
- 严谨的叙述逻辑

---

## 3. 第一部分：精简的表达方式

### 3.1 论文是科研发现的载体，不是炫技文字

课堂引用施一公老师的话：论文只是一个载体，是为了向同行宣告科研发现，是科学领域交流的重要工具。因此写论文时必须记住：**用最简单的话表达最明白的意思**。

这句话的含义不是“写得短就好”，而是要求每一句话都承担清晰功能：命名方法、说明目标、交代创新、解释机制、支撑结论。没有功能的句子、重复的句子、塞满细节但没有中心的句子，都应当被拆解或删除。

### 3.2 反例：一句话里塞入方法名、任务、技术路线和目标

课件用一个学生论文的 introduction 修改过程说明问题。最初版本中，一句话包含三个从句，试图同时表达：

- 我提出了一个新框架。
- 这个框架用于 encrypted traffic classification。
- 这个框架叫 ET-BERT，基于 pre-training 来学习 datagram representation。
- 这个表示用于从 large-scale unlabeled encrypted traffic 中学习 generic features。

问题是，这些信息都重要，但不应该挤在一个英文句子里。这样写会造成：

- 方法和问题混在一起。
- 模型命名没有定义清楚。
- 目标、创新、任务之间没有层级。
- 语法上依赖多个逗号和从句，读者难以判断主干。
- 审稿人无法快速抓住“本文到底做了什么”。

### 3.3 改进：把一个长句拆成“命名—目标—创新—方法思路”

最终版本的组织方式更清晰。它先用一句话说明本文提出了一个用于 encrypted traffic classification 的 pre-training model，并明确模型名称：Encrypted Traffic Bidirectional Encoder Representations from Transformer (ET-BERT)。

然后再用一句话说明目标：它旨在从大规模无标注加密流量中学习 generic traffic representations。

再往后，才介绍核心方法思路：先提出 raw traffic representation，用 transmission-guided structure，即 BURST，作为输入；然后说明框架包含 pre-training 和 fine-tuning 两个阶段；最后说明 Transformer 结构如何通过 self-supervised learning 获得 datagram-level generic traffic representations。

这说明一个重要原则：**Introduction 中的方法概述不是 Method section 的细节搬运，而是读者理解创新逻辑的路线图。**

### 3.4 精简表达的三个 Tips

#### Tip 1：一句话只表达一个意思

每一句话应只服务一个核心功能。可以包含必要的修饰、缩写、数据或限定条件，但主干只能有一个。比如：

- 一句话命名方法及问题。
- 一句话突出方法目标。
- 一句话介绍方法创新。
- 一句话表达核心方法思路。

如果一句话中同时有“模型名字”“技术创新”“任务场景”“训练数据”“实验目标”“具体实现细节”，就应拆分。

#### Tip 2：减少中文翻译英文

不要先写中文长句，再交给翻译软件或自己逐句直译。中文论文表达中常见的多个逗号串联，在英文中往往会变成语法混乱、主从关系不清、信息重心模糊的长句。

更好的训练方式是：读英文论文时不要只看翻译，要琢磨作者为什么使用某个关键词、为什么把某个信息放在句首、为什么在这里使用 “aims to”“we first propose”“specifically”等表达。真正理解优秀论文的英文表达逻辑后，才能迁移到自己的论文中。

#### Tip 3：避免重复表达

很多初学者会在 Abstract、Introduction、Method 中反复说同一句“我能做到”。但真正有说服力的论文不是反复强调结论，而是在不同位置用不同证据支撑同一结论：

- 在 Introduction 中通过现有方法不足来引出结论。
- 在 Method 中通过机制和公式解释为什么能做到。
- 在 Experiment 中用结果和消融实验证明确实做到。
- 在 Analysis 中解释性能提升背后的原因。

如果不同章节只是重复口号，读者不会被说服。

---

## 4. 第二部分：严谨的叙述逻辑

### 4.1 站在审稿人的阅读场景中写作

课堂设置了一个典型场景：审稿人还有一个小时审稿 deadline，刚打开你的论文。如果此时读到一句没有定义的模型名、一个没有解释的公式、一个看不出核心逻辑的图，他不会像作者一样耐心揣摩。他只会认为：读不懂；读不懂就是作者没有表达清楚。

因此，一篇高水平论文要让审稿人在语言、公式、图表每个环节都能最快捷、最清晰、最准确地理解。

### 4.2 读不懂的三类入口

#### 入口 1：突然出现的术语或模型名

例如：

```text
Now, we could use CoTNet model to predict the result of that dataset.
```

如果前后没有定义 CoTNet model，审稿人会立刻产生疑问：这是已有模型，还是本文模型？为什么使用？它的全称是什么？与当前任务有什么关系？

#### 入口 2：没有解释符号的公式

例如：

```text
α_i = softmax(w_a^T tanh(W_1 v_i + W_2 q))
```

如果 `w_a`、`W_1`、`v_i`、`W_2`、`q` 没有定义，公式就只是符号堆叠。即使领域内某些符号有惯例，作者仍应在公式附近清晰说明。

#### 入口 3：没有明确输入、输出、关键过程和创新点的图

图是审稿人最先扫读的对象之一。方法图中如果没有明确输入、输出、关键过程、变量含义、模型命名、创新模块和它们之间的关系，审稿人不会因为图“看起来复杂”而认为论文专业，反而会浪费更多时间。

### 4.3 严谨叙述的四个 Tips

#### Tip 1：在术语使用前定义解释

第一次出现的术语、模型名、变量名、缩写都应在使用前或使用时定义。好的写法会同时给出全称、缩写和用途。例如：

```text
Next, a novel Transformer-style building block, named Contextual Transformer (CoT), is introduced for image representation learning.
```

这个句子完成了三件事：

1. 说明这是一个 Transformer-style building block。
2. 给出名称 Contextual Transformer 和缩写 CoT。
3. 说明用途：image representation learning。

后续出现 CoT、CoTNet、CoTNeXt 时，读者就有理解基础。

#### Tip 2：给出公式后集中解释定义及符号

公式之后要集中解释所有关键符号，尤其是：

- 参数是什么。
- 变量是什么。
- 表示来自哪里。
- 是否为 learned parameters。
- 是否为 embedding。
- 是否涉及拼接、邻接节点、上下文记忆等操作。

好的公式段落不是只写公式，而是写出“公式 + where 解释 + 下一步用途”。

#### Tip 3：有清晰段落结构，段落/章节之间有过渡

论文不能只是把事实堆在一起，而要写出完整 story。课堂给出的过渡链条如下：

```text
为了缓解上述问题，***提出
然而，他们方法只…
但事实上，需要…
本工作中，我们提出…
具体来说，我们首先…
在上面构建的表征基础上，我们进行…
然后，实现…
```

这些过渡词不仅帮助审稿人理解，也逼迫作者自己检查每句话与前后逻辑的关系：当前句子是在承接问题、反驳不足、提出需求、介绍方法，还是说明实现？

#### Tip 4：图表文字清晰直接表达内容，并与图注、表注、正文一致

图、图注、表注和正文必须使用一致的模型名、变量名、模块名、实验设置和指标名称。否则审稿人会质疑：图中结果和表中模型是否对应？正文分析的是否是同一个方法？

课件中的例子展示了 Figure 2、Table 1 和 Table 2 如何服务同一个模型 Mucko：图解释模型结构，Table 1 展示与 SOTA 的对比，Table 2 展示关键组件的消融。三者必须在命名与语义上保持一致。

---

## 5. 本讲形成的论文修改工作流

当你修改英文论文时，可以按如下顺序执行：

1. **句子级检查**：每句话是否只表达一个意思？是否存在一个句子三个从句、四十多个单词、多个目标混杂？
2. **段落级检查**：每段是否有明确功能？段落内部是否有“问题—不足—需求—本文方法—具体步骤”的推进？
3. **术语级检查**：所有模型名、缩写、任务名、变量名是否第一次出现时就定义？
4. **公式级检查**：每个公式后的符号是否集中解释？是否符合领域惯例？是否说明计算来源与后续用途？
5. **图表级检查**：图内文字、图注、表注、正文是否一致？图是否表达输入、输出、关键过程和创新点？
6. **重复性检查**：Abstract、Introduction、Method、Experiment 是否只是重复同一句话，还是从不同证据层面支撑同一结论？

---

## 6. 可直接复用的写作检查清单

### 6.1 精简表达检查清单

- [ ] 每句话是否只有一个中心意思？
- [ ] 是否把模型命名、方法目标、方法创新、实现细节塞进同一句？
- [ ] 是否存在“中文先写好再翻译成英文”的痕迹？
- [ ] 是否存在多个逗号串联、主句不清的长句？
- [ ] 是否把 Method section 的实现细节提前塞到 Introduction？
- [ ] 是否只是在不同章节重复“我能做到”，而没有给出机制、公式或实验支撑？

### 6.2 严谨逻辑检查清单

- [ ] 第一次出现的术语、缩写、模型名是否定义？
- [ ] 模型名字是否说明全称、缩写、任务和核心思想？
- [ ] 公式后的每个符号是否解释清楚？
- [ ] 符号是否遵守领域惯例，例如图像常用 `I`，文本常用 `T`？
- [ ] 段落之间是否有清晰过渡词？
- [ ] 论文是否有完整 story，而不是事实堆叠？
- [ ] 图内文字、图注、表注、正文是否完全一致？
- [ ] 审稿人只看图、表、公式和段首句，是否能快速理解本文核心贡献？

---

## 7. 本讲对 Agent 的可执行规则抽象

当 Agent 被要求润色、评审或重写英文学术论文时，应始终执行以下规则：

1. 不先追求“高级表达”，先追求“一句一个意思”。
2. 遇到长句，优先拆成：方法命名、问题/任务、目标、创新、核心思路。
3. 对任何缩写、模型名、任务名，检查第一次出现处是否完成定义。
4. 对任何公式，检查后文是否解释所有符号、参数、变量、操作和后续用途。
5. 对任何段落，检查是否有承接关系：问题、现有方法、不足、需求、本文方法、具体步骤、结果。
6. 对任何图表，检查图内文字、caption、正文、表格中的命名是否一致。
7. 避免中文翻译腔；优先模仿高水平英文论文中的逻辑表达方式。
8. 任何修改建议都应说明修改原因，而不是只给出更“像英文”的句子。

---


## 课件逐页纯文本重构

> 本节完全使用文字复现课件内容与视觉布局，不包含任何 PNG、JPEG 或其他图片引用。

## Slide 1：封面

**页面主标题**：科研与英文学术论文写作  
**讲次标题**：第九讲 英文学术论文之英文规范——如何做到简洁与严谨  
**主讲人**：于静 副研究员  
**单位**：中国科学院信息工程研究所  
**系列报告主页**：https://mmlab-iie.github.io/course/  
**时间与平台**：2022.07 @ Bilibili

**视觉布局文字化描述**：页面上半部分为蓝色横幅与白色大标题；下半部分居中列出主讲人、单位、课程主页和时间。页面底部左侧为“中国科学院 信息工程研究所”标识，右侧为“中国科学院大学”标识。

## Slide 2：英语写作规范——八项注意

**页眉**：于静 中科院信息工程研究所  
**页面主标题**：英语写作规范——八项注意

八项注意如下：

1. 精简的表达方式
2. 严谨的叙述逻辑
3. 专业的学术用语
4. 规范的符号使用
5. 标准的学术术语
6. 客观的图表绘制
7. 正确的文献引用
8. 坚守的学术道德

**视觉结构**：

- 第 1 项“精简的表达方式”和第 2 项“严谨的叙述逻辑”被一个红色括号归为“不太容易”。
- 第 3 项到第 8 项被一个绿色括号归为“很容易”。
- 这页的核心意思是：真正困难的不是一些细节规范，而是英文论文中的表达思维与叙述逻辑。

## Slide 3：英语写作规范（1）——精简的表达方式

**页眉**：于静 中科院信息工程研究所  
**页面主标题**：英语写作规范（1）——精简的表达方式

页面引用施一公老师的话：

> 论文只是一个载体，是为了向同行们宣告你的科研发现，是科学领域交流的重要工具。所以，在科研论文写作时，一定要谨记于心的就是：用最简单的话表达最明白的意思！
> ——施一公

**页面核心示例**：将同一篇论文 introduction 中“最初版本”和“最终版本”的英文表达进行对照。

### 最初版本的典型问题

左侧示例把多个意思压进同一个英文句子中。课件标注出的主要问题为：

- 表达：一句话 3 个从句
- 问题：混淆方法和问题
- 无重点！有语病！
- 表达：一句话 44 个单词
- 问题：加入太多细节
- 无重点！有语病！

**最初版本示例中的核心英文片段**：

```text
Motivated by the above idea, we propose a novel framework for classifying encrypted traffic in this paper, encrypted datagram representation by pre-training (ET-BERT), for learning generic features in large-scale unlabeled encrypted traffic (Figure 1(c)).

We define a special structure, BURST, to depict a traffic flow and represent it with the bi-gram language model for highlighting the structural features of the traffic transmission.

To learn application-specific generic features, the proposed framework consists of a two-part model: pre-training and fine-tuning. Specifically, the high-dimensional representations of dependencies that bridges the gap between different datagram bytes are provided by pre-training in large-scale unlabeled encrypted traffic, and the generic representations of specific encryption scenarios are supported in fine-tuning with small labeled traffic through reusing the pre-training results.
```

### 最终版本的组织方式

右侧最终版本把信息拆成更清楚的层次：

- 一句话命名方法及问题
- 一句话突出方法目标
- 一句话介绍方法创新
- 一句话表达核心方法思路

**最终版本示例中的核心英文片段**：

```text
In this paper, we propose a novel pre-training model for classifying encrypted traffic, called Encrypted Traffic Bidirectional Encoder Representations from Transformer (ET-BERT). It aims to learn generic traffic representations from large-scale unlabeled encrypted traffic (Figure 1(d)).

We first propose a raw traffic representation for pre-training. Each traffic flow is presented by a transmission-guided structure, denoted as BURST, which serves as the input. The proposed framework consists of two stages: pre-training and fine-tuning. Specifically, the pre-training network with Transformer structure obtains datagram-level generic traffic representations by self-supervised learning on large-scale unlabeled encrypted traffic.
```

**页面底部 Tips**：

1. 一句话只表达一个意思！
2. 减少中文翻译英文！
3. 避免重复表达！

**视觉布局文字化描述**：左上方为施一公老师照片；中间为引用框；下方左右两栏对比英文论文段落。最初版本使用红框、紫框、蓝色高亮标出冗长和无重点的问题；最终版本使用红框、紫框、蓝色高亮标出“命名—目标—创新—核心思路”的清晰层次，中间有一个黄色手形箭头从最初版本指向最终版本。

## Slide 4：英语写作规范（2）——严谨的叙述逻辑：审稿人读不懂的瞬间

**页眉**：于静 中科院信息工程研究所  
**页面主标题**：英语写作规范（2）——严谨的叙述逻辑

页面情境设定：

```text
假设审稿人还有一个小时审稿 deadline，刚打开你的论文，读到…
```

页面分为三类“读不懂”的对象：

### 这么一句话

```text
Now, we could use CoTNet model to predict the result of that dataset.
```

问题在于：CoTNet model 是什么？前文是否定义？为什么在这里突然出现？为什么可以用它预测这个 dataset 的 result？

### 这么一个公式

```text
α_i = softmax(w_a^T tanh(W_1 v_i + W_2 q))
```

页面用红框圈出 `w_a^T`、`W_1v_i`、`W_2q` 等符号，提示如果符号没有定义，公式无法被读者快速理解。

### 这么一个图

图示中包含若干模块与文字，如 question、object feature、weight summing、Cross Modal attention、Pretrain model、Classified object、relation、answer 等。页面用红框圈出“Cross Modal attention”“Pretrain model”“relation”等关键模块，强调如果图中的模块命名、变量、输入输出、核心创新没有被解释，审稿人同样会困惑。

**视觉布局文字化描述**：每一类对象右侧都放置一张“疑惑表情 + 问号”的梗图，表示审稿人的困惑。页面的整体信息是：语言、公式和图如果没有前置定义与逻辑铺垫，都会造成阅读中断。

## Slide 5：英语写作规范（2）——严谨的叙述逻辑：Tip 1

**页面 Tip**：

> Tips: （1）在术语使用前定义解释！

页面给出论文方法部分的一个好例子。

**章节标题**：3. Our Approach

高亮英文核心句：

```text
Next, a novel Transformer-style building block, named Contextual Transformer (CoT), is introduced for image representation learning.
```

另一处高亮英文核心句：

```text
two kinds of Contextual Transformer Networks, i.e., CoTNet and CoTNeXt deriving from ResNet [22] and ResNeXt [53], respectively, are further elaborated.
```

**页面意图**：先解释 Contextual Transformer，再给出缩写 CoT；然后说明 CoTNet 和 CoTNeXt 是从 ResNet 与 ResNeXt 派生出的两类 Contextual Transformer Networks。术语第一次出现时就完成定义，后续读者才不会被缩写和模型名阻断。

**视觉布局文字化描述**：左侧是论文截图，黄色高亮标出术语定义句；右侧是一张写有“Nice! 兄dei!”的猫图，表示这样的定义方式值得肯定。

## Slide 6：英语写作规范（2）——严谨的叙述逻辑：Tip 2

**页面 Tip**：

> Tips: （2）给出公式后集中对定义及公式中的符号进行解释

页面展示公式和符号解释的组织方式。

### 公式 (1)

```text
α_i = softmax(w_a^T tanh(W_1 v_i + W_2 q))                         (1)
```

紧随其后集中解释：

```text
where W_1, W_2 and w_a (as well as W_3,..., W_12, w_b, w_c mentioned below) are learned parameters. q is question embedding encoded by the last hidden state of LSTM.
```

### 公式 (2)

```text
β_ji = softmax(w_b^T tanh(W_3 v'_j + W_4 q'))                       (2)
```

紧随其后集中解释：

```text
where v'_j = W_5[v_j; r_ji], q' = W_6[v_i; q] and [.;.] denotes concatenation operation.
```

### 公式 (11) 和 (12)

```text
m_j^(t+1) = W_11[m_j^(t), c_j^nei, h^(t)]                          (11)

c_j^nei = Σ_{k∈N_j} W_12[m_k^(t), r_jk]                            (12)
```

紧随其后集中解释：

```text
where N_i represents a set of 1-hop neighboring nodes regarding the memory entity m_j and c_j^nei is the contextual memory representation. Then the updated memory is served as the new knowledge memory used in the next reasoning step.
```

**页面意图**：每个公式不是“放出来就完了”，而是要马上告诉读者每个符号是什么、来自哪里、如何得到、将被如何使用。

## Slide 7：英语写作规范（2）——严谨的叙述逻辑：Tip 3

**页面 Tip**：

> Tips: （3）有清晰的段落结构，段落/章节之间有过度！

页面用论文中的 Abstract、Introduction 和模型图作为例子，展示如何通过过渡句组织完整 story。

**页面右侧总结的过渡逻辑**：

- 为了缓解上述问题，***提出
- 然而，他们方法只…
- 但事实上，需要…
- 本工作中，我们提出…
- 具体来说，我们首先…
- 在上面构建的表征基础上，我们进行…
- 然后，实现…

**页面中的论文主题**：Fact-based Visual Question Answering (FVQA)。例子强调：如果任务需要外部知识，论文必须说明现有方法为什么不足、真正需要什么、本文如何提出新的图结构或推理机制来解决问题。

**图示文字化描述**：页面中部有一个模型动机示意图，包含输入图像、dense captions、question、object、fact graph、semantic graph、cross-modal knowledge reasoning 等元素。图中问题示例为：“What is the red cylinder object in the image is used for?” 答案示例为：“firefighting”。图意在说明：文章的段落结构不是孤立句子的堆砌，而是从任务需求、现有不足、本文方法，到具体步骤逐步推进。

## Slide 8：英语写作规范（2）——严谨的叙述逻辑：Tip 4

**页面 Tip**：

> Tips: （4）图表文字清晰直接表达内容，与图注、表注、正文一致！

### 图 2 文字化重构

图 2 的标题/图注：

```text
Figure 2: An overview of our model. The model contains two modules: Multi-modal Heterogeneous Graph Construction aims to depict an image by multiple layers of graphs and Cross-modal Heterogeneous Graph Reasoning supports intra-modal and cross-modal evidence selection.
```

图中流程文字化描述：

1. 输入图像和问题：问题为“What is the red cylinder object in the image is used for?”
2. 通过 DenseCap 得到候选描述，如 “Woman is wearing blue shorts.”、“Red fire hydrant on the sidewalk.”、“Woman is next to fire hydrant.”
3. 通过 knowledge base of facts 和 Fact Retrieval 得到候选事实，如：
   - `<Fire hydrant, UsedFor, Firefighting>`
   - `<Fire hydrant, AtLocation, Street>`
   - `<Fire hydrant, HasProperty, Red>`
   - `<Car, UsedFor, Transport>`
4. 构建 Multi-Modal Heterogeneous Graph Construction：包括 object regions、visual graph、fact graph、semantic graph。
5. 进入 Cross-Modal Heterogeneous Graph Reasoning：包括 intra-modal knowledge selection 与 cross-modal knowledge reasoning。
6. 输出答案相关的权重与 answer。

### 表 1：State-of-the-art comparison on FVQA dataset

| Method | Overall Accuracy top-1 | Overall Accuracy top-3 |
|---|---:|---:|
| LSTM-Question+Image+Pre-VQA | 24.98 | 40.40 |
| Hie-Question+Image+Pre-VQA | 43.14 | 59.44 |
| FVQA (top-3-QOmapping) | 56.91 | 64.65 |
| FVQA (Ensemble) | 58.76 | - |
| Straight to the Facts (STTF) | 62.20 | 75.60 |
| Reading Comprehension | 62.96 | 70.08 |
| Out of the Box (OB) | 69.35 | 80.25 |
| Human | 77.99 | - |
| Mucko | 73.06 | 85.94 |

### 表 2：Ablation study of key components of Mucko

| Method | Overall Accuracy top-1 | Overall Accuracy top-3 |
|---|---:|---:|
| Mucko (full model) | 73.06 | 85.94 |
| w/o Semantic Graph | 71.28 | 82.76 |
| w/o Visual Graph | 69.12 | 78.05 |
| w/o Semantic Graph & Visual Graph | 20.43 | 29.10 |
| S-to-F Concat. | 67.82 | 76.65 |
| V-to-F Concat. | 69.93 | 80.12 |
| V-to-F Concat. & S-to-F Concat. | 70.68 | 82.04 |
| w/o relationships | 72.10 | 83.75 |

**页面意图**：图内文字、图注、表注、正文必须指向同一个模型、同一套变量和同一层语义；如果正文中的名称、图中的名称和表中的名称不一致，审稿人会怀疑实验和方法是否对应。

## Slide 9：结束页

**页面大字**：欢迎大家在 B 站留言交流！

联系与主页信息：

- 于静
- 邮箱：yujing02@iie.ac.cn
- 课程主页：https://mmlab-iie.github.io/course/
- 研究组主页：https://mmlab-iie.github.io/
- 知乎专栏：https://www.zhihu.com/column/c_1284803871596797952

**视觉布局文字化描述**：页面右下方有三个二维码，分别对应课程主页、研究组主页、知乎专栏；底部包含中国科学院信息工程研究所和中国科学院大学标识。

---

## 原始 Transcript（逐字稿原文，未校订）

```text
﻿好，各位同学，大家晚上好。今天我们进入下一个讲解的内容——英文学术论文的英文规范问题。很多同学都给我提出很多问题：关于我不是英文的NATIVE SPEAKER，我怎么样把我的英文的学术论文写得既地道又专业？所以很多时候觉得自己英文写作不好是因为自己的英文不好。但今天我想通过跟大家去分享一些英文学术论文里面的英文规范，其实想告诉大家，现在大部分同学的问题并不是出现在表达语言的问题，而在于你英文的一些逻辑思维的问题。所以今天这一讲，我觉得对大家应该非常有帮助。一方面，我们怎样用英文的思维去写学术论文，给大家提出一些很实操的建议；另外呢，我还会给大家提供很多的工具，包括怎么样去把自己的英文的 专业的术语，英文的符号的定义，英文的一些。 检查、拼写等等这些，我觉得比较实操实用的一些小工具也分享给大家。 英文写作规范其实是一个非常繁琐，涉及到非常多细节，就是大家的问题都是五花八门的。 我大概把最核心，也就是。 大家常犯的一些问题，总结成了。 八项注意的这个方面。 那么这里面其实分成我标红和标绿的两大块儿。 我觉得最难的其实也是涉及到大家英文的思维方式的这样的内容，包括怎么样做精简的表达，然 怎么做严谨的叙述，这个我觉得是最难的。 但是大家可能常问的问题并不在于表达，反而在于下面的这些很细节的，包括我 我怎么去用专业的术语呀？然后怎么去把这个 符号定义的清楚，这下面的往往往是更容易一些的，所以我会花上下两讲。 去介绍这八项内容，那么前两讲。 前一讲我会重点去展开，拿具体的例子讲怎么样去表达更精简、更严谨。好，那 其实施一公老师曾经说的一个特别关键的，对于英文学术论文写作核心的一个目标，就是我们要用文字。 去论文去告诉你的同行，你发现了什么？ 这启示就是用大家有共识的这种学科领域的。 语言去做这个成果的交流。 而不在于你把这个东西描述的多高大上，多五花八门。 所以呢，最核心的是你怎么用最简单的语言。 把你最直接的、最明确的成果给它表达出来。 这就是我们做科研学术论文写作的目标。 那么我下面想 拿一个具体的我学生的例子给大家看看。 其实大家在第一版，或者说在最初写论文的时候，大家的思维方式到底和我们最后定稿的这一版，真正让同行能够理解的这种思维方式有多大的差距，对吧？ 那么OK，我们先看一下最左边的这个版本。我这里拿了标标出颜色的几句话，给大家作为典型的例子去展开讲一下。 那么我们来看第一句话，这段话出现在我们论文的introduction的。 呃，最后面就是我们大概发现了问题，然后再讲我这篇论文针对问题，我想提出一个什么方法，再写这一段。 那这一段其实大家的思路都比较类似。 那你前面提完问题之后，接着就开始说：哎，我提了一个大概什么样的思路？那这个思路重点解决了什么样的问题？ OK，那大家来看他第一句话一开始是怎么写的。 啊。 他说呃，基于上面的这个一些启发和想法，我们提出了一个新的框架。 用来做这种加密流量分类的。 然后逗号这个地方其实他没有写完一个完整的句子，他还想做一些。 更深入的表达。 就是说他想说他这篇工作做的是这种。 加密的 这个数据报文的表示用预训练的方法。 然后他把这个名字，也就是他的模型的名字，括号括起来叫E T Bert。 然后这句话他还没完，他还想再表达。 说这个方法。 用来干什么用的呢？是用来学习这种。 在大规模无标注的这种流量数据上，学习这种通用的特征。 但是这一句话，首先第一个。 非常长啊，大家可能。 一开始写英文的时候，习惯于把自己的英文完整的表达，因为大家写中文的逻辑可能相对是通畅的。 然后把中文的可能有若干个逗号这样的句子。 写清楚之后，习惯于放在比如说英文的翻译软件里面。 然后它自动的给它翻译成若干个从句。 也可能是大家就。 完全依据于大家中文的。 这个思路啊，这个表达逻辑去把它一句一句翻译成英文。 而觉得这样表达就应该放在一个句子里面去，所以中间加了很多逗号。但大家可以读的时候发现，首先你加了这么多逗号是不符合英文的语法的。 这个是最关键的。 第二，就是一旦你不符合语法。 你这个句子里其实包含了很多个想表达的意思，大家可以分析一下。 第一。 他想表达他提的模型的名字叫什么？ OK，这是第一个。 第二个就是他想表达他模型的技术上的创新是什么。 就用了他用了预训练去得到了一个什么样的表示。 第三。 他想表达。 他做了这个技术之后，他想实现的一个解决的问题或者实现的一个目的是什么？ 就是在这种无标注的数据上，它能够得到这种通用的表示。 对这种无标注的数据做分类。 就是说他一句话其实表达了三个意思。 OK，这个信息我们是希望在这一段里都表达清楚的。 但是当你把所有的信息量汇聚在用一句话去表达的时候，其实你每一个想突出表达的意思都没有表达清楚。 那么我们看一下。 最后面改的camera ready的版本。 怎么样去重新组织的这些表达的内容？ 那首先第一句话，它就很明确的只表达一个意思。 就是我这篇文章提出了一个预训练模型，OK，这肯定是它的一个contribution。 用来做流量分类的，先说清楚。 你做的技术的创新和你解决的问题。 这也其实就是我们当时题目说。 要怎么样去组织题目？ 接着他明确的说了我这个模型叫什么，这其实特别重要，如果说 大家在自己论文里给模型起了一个明确的名字。 那么这个名字，不管是你怎么命名的，其实你要给他一个明确的说法。 是你用一些名字的呃，单词的首字母。 还是你给他做了一个明确的。 含义的界定。 那你在这里面就说清楚，那后面其实所有用到这个名字的地方就不用再解释了。 所以这个地方。 看我们最初的这同学写的这个版本，其实他并没有把这个名字。 到底怎么由来的，说清楚。 这里面。 最后camera ready，他就会把这个名字的解释，名字的解释是用来做加密流量的双向编码表示。 从transformer这种架构里。 那就很清晰的，也就是他名字其实代表了他的。 创新性和解决的问题。 然后括号，它是叫什么缩写？ okay. 那么这一句话其实就说明了一件事情，就是我到底应 提出的这个模型叫什么？它解决了什么问题？ 那第二句话，也就是说一开始这句话其实把三个意思放在一句话里面了。 那后面的改进的版本，其实他把 最终这个模型能够达到的目标，给它单独用一句话给它表述清楚。也其实就大家回想一下我们之前讲abstract怎么写的时候。 其实你要一句话很清晰的，先把你做的这件事的思路讲清楚。 那么在这一块其实就是。 你提了这么一个。 为了达到这样的任务，那我提了一个这样的。 模型之后。 那他最后解决的问题是什么？ 那你看他这样写。 It aims to learn generative. ah generic traffic representations from large scale and labeled. 呃，in encrypted traffic，就是说 我就是为了。 学通用的表示。 那这个通用的表示就是从大规模的、无监督的。 没有标注的这样的数据你去学。 这其实就是它最核心的创新的地方。 也是咱们在。 motivation 整个上面画的那个motivation图里面，和现有方法最大的区别。 所以这一块在你真正的大家特别习惯于哈，在这一段就上来就讲我第一步怎么做，第二步怎么做，第三步怎么做。 那其实你这一句引领的话。 就会。 预告读者，我下面就要讲我怎么样去实现在无监督的数据里面去学习通用的表征。 我为了达到这个目标，我后面第一步、第二步、第三步怎么做的？ 所以大家其实。 在这这次报告，我特别想跟大家就是核心的一个点，就是 你的一篇论文里的任何一句话都是有目标的。 不是我想把所有我知道的东西表达出来。 而是任何一句话都不管是引领下面，还是引导读者。 一定要给他传输出。 你核心想让他有印象。 你最重要的这些信息。 而且这些信息一定是。 有。 结论。 有数据和。 分析支撑。 然后再有最后结果的。 所以这一段话其实也是一样的逻辑，那么我提出了一个东西。 之后。 我这个目，我这个模型是要达到这样的目标。 那下面其实蓝色的这些话，就是我这这个方法，我第一步怎么做？第二步怎么做？第三步怎么做？ 都是环环相扣，去告诉他我怎么解决的这个目标。 好，那下面其实就到了。 以前最初版本的时候。 与这个同学在讲自己方法。 那么他首先啊，这句话我为什么重点给大家标出来？ 就大家也很习惯。 一句话一逗到底，而这句话有44个单词，我数了一下。 为什么他有这么多单词？ 大家。 可以自己再去看一下这个。 呃。 暂暂停看一下他具体写的内容。 我这里面就给大家讲，它其实把很多它模型的细节，它 比如说他这个。 数据怎么样？一开始从原始的数据到最后模型中输入的数据中间，它做了哪些细详细的变换？ 以及中间这个数据怎么样流转？ 然后支撑。 到下游的这个任务等等，中间他加了很多的。 细节的描述。 反而冲淡了他整个大的流程的介绍。 也就是说，你一句话非常长的时候，别人是不知道你重点想表达什么的。 那这个时候。 你其实整个的逻辑就是想呼应刚才说绿色这一句话，我的目标的这句话不能够。 通过一个。 逻辑清晰的。 表述。 有层次的表述给它呈现出来。 所以在审稿人看来，那我这样做也可以，为什么我不那样做？ 他就会有这样的。 在大脑里就已经给你有这种鲜鲜艳的印象。 那您看。 这里面其实特别简单。 我们就用一句话，先把核心的方法总结出来。 就是他右左边这么长的四十四个单词，其实核心的方法。 就是他用了，提出了一个结构。 把这个结构应用在了。 原始的数据上，让它得到了一个能够给预训练模型的表示。 那这个具体这个结构到底怎么样去处理，怎么样得到？那我在方法里面还会详细的讲。 但是这个地方就是我在introduction里给大家讲的时候，重点要讲我的逻辑。 就是我先提了一个什么样的表示，这个是一个很重要的环节。 那么基于这个表示，大家可以看到下面的红色的这些部分，这 我接着又提了一个预训练和微调的框架，然后再讲我的预训练的框架是什么样的。 我微调的过程是什么样的？ 这里面就重点给大家讲清楚。 你的创新的地方就是你三块创新的地方，每一块核心的一个东西是什么，而不需要展开去讲你这核心的东西怎么是具体实现的。 好吧，嗯。 所以呢，我想给大家。 提大家只要记住这三个，我觉得tips。 就能很大程度上去避免。 句子特别的冗长，又没有重点。 那么第一个就是大家记住一句话，只表达一个意思。 就像我，大家可以看以前我做的PPT。 就是每一页PPT，我们其实只表达一个意思。不管是我有大量的结论，还是我有这个数据的支撑，还是我有建议，那么我这一页PPT就只表达一个意思。 大家的句子也是一样的，我一句话我可以。 用各种，比如说数据或者 呃，名字缩写等等各种方式去表达，但是我只表达一个核心的意思。 第二个就是。 大家尽量。 我觉得不管是从初期啊，到后面。 呃，熟悉之后都尽量避免直接写成英文之后，中文之后找翻译软件翻译成英文或者自己。 从中文直译成英文。 就是大家要习惯用这种英文的。 逻辑和他的 常用的表达去写。 英文的论文。 所以大家在看现在英文论文的时候，一定也记得不要去上来就把它拿到翻译软件里翻译，因 因为这个作者其实最核心的一些想法和细节的这些创新，他 就蕴含在它很精巧的。 那么有时候一两个关键词上的表达，而当你把这几这些关键词，比 在翻译软件里翻译出来之后，其实你是看不出来他们细微的差别的。 所以当你真的想去了解别 一个作者他核心的一些想法和创新的时候，大家一定要去真的。 体会哈。 仔细琢磨他为什么这么表达啊？ 而你真正理解之后，他的这种表达方式和思维方式，你就是可以借鉴过来，灵活再运用在你的这个论文表达里的。 Okay. 那么第三个。 就是我想说，避免重复表达。 其实大家现在一开始写作的时候，因为呃 你习惯于对你的工作。 只去重点突出它一个重要的地方，和一个从一个维度去突出它重要的地方。 所以大家不管是在introduction里。 还是abstract里，还是在你的呃方法里面。 总是翻过来调过去的，就讲这么一句话。 嗯 所以呢，我想说其实避免重复的一个很大的一个方法，就是大家更深入的去问自己。 这个方法到底对领域有什么样重要的作用？ 为什么有这样的作用？我可以通过什么样的？ 公式去证明它有能够达到这样的作用，以及我通过什么样的实验结果去证明它确实做到了。 那么你在其实一篇论文的不同地方。 你就会从不同的角度去同时印证相同的结论。 但是你表达的时候，并不是只去强调这个结论。 而是通过事实也好，通过你的理论或者公式的分析也好，还是通过对现有方法的分。 分析也好，去支撑你这个结论。所以你在不同地方一定说出的话是不一样的，并不是干巴巴的给大家就说我能做到。那这个很 基本上是不能说服别人你能做到的。 Okay. 好。 那么下面一个很很大的问题就是大家表达上面是给审稿人造成了很大的误区，对。 很难去充分的在短时间内理解你的论文。 那一般我们说审稿人很多时候都会在大家烂之前，可能把你的论文打开才去，在一两个小时之内。 快速的看一遍一遍之后，给你一个判断。 那这个时候，如果说你有一些呃 逻辑不清晰，或者是你定义完全没有。 呃，那个表达清楚的地方，那审稿人是没有耐心和时间去。 像你一样去思考它到底是什么样的逻辑，那它就是读不懂。 读不懂，就是你没有表达清楚。 那都不懂，有很多种方原因。 比如说。 你这里面突然间宣告人看见一句话，说我们能用什么cold night model去做一个什么呃事情。 而前后左右从来没见过这个model的名字出现在什么地方，它到底代表什么意思？ 那沈某人从这个时候开始往后，其实就很难再读懂你后面的东西，或者说他觉得这个是一个。 很关键的东西，但是。 完全不知道。 是什么意思？ Okay. 那另外还有一个，就是大家非常习惯于。 呃，定义各种自己。 呃。 写到哪里去啊？随时定义一个新的符号，而这个符号往往 一方面和现有的这个领域人共识的一些符号定义。 不一致。 第二就是。 即使说大家都默认为这个符号是什表达什么意思，但是在你这个符号定义出来之后，你依然没有给它一个明确的定义解释。 那审稿人依然是存疑的。 不管说这个符号代表什么。 还有这个符号到底是怎么样去，如果它是一个变量，它怎么样去计算得到的？ 那这里面都是让审稿人难以再往下去呃清晰的理解的一个原因。 Okay。 那其实最三个就是大家。 在论文里一目了然的就是你所有的图。 嗯。 不，这个图其实之前我们画的这个方法图。 这里面在方法图里面，什么样的关键的？ 信息以及定义的逻辑和你的创新性都没有表达清楚，所 那当审稿人在你的论文还没有细读的时候，先去关注你这几个。 关键的图的时候，他没法在图里面很快速的。 理解到你的核心的东西。 那他再去看论文，其实会浪费大量的时间。 所以。 不管是语言公式，还是文文那个图片。 其实你一篇A类的论文，在每一个环节上都需要让审稿人。 都最快捷、最清晰的、准确的理解。 好，所以我这里面给大家。 几个比较明确的第建议。 第一个就是在任何，不管是你模型名字。 还是你变量名字。 还是任何大家只要第一次出现的专业术语，一定要提前的定义清楚。 那么你这个定义方式一定要把它的，如果有缩写的话，把它的全称和缩写都同时出现在一个定义的位置。 那后面其实大家就不用再反复的提及了。 Okay. 那第二个其实就是。 我最近在给学生改论文的时候，非常头疼的就是。 改了很多版，他依然可能。 没法去把论文里所有的公式。 里面的符号定义清楚。 那么你给审稿人就完全是很凌乱，对。 很没有体系，很那个就是按一步一步的这种step by step的这种思思思思路。 所以我想给大家提三点建议，一 第一个就是大家平时其实有很多的，后面我会给大家讲很多的。 就是呃。 总结的好的文章哈，就是有规范的数学符号，到底在学术论文里怎么样去定义，比如说你标量，你 用什么样的符号？ 你变量、向量、矩阵到底哪些是斜体？ 对吧，哪些是正题，哪些加粗，哪些不加粗。 哪些是大写，哪些应该小写？ 这些其实都是有。 大家统一的规范的，如果你这个和大家的认知是违背的，那其实就给阅读造成了特别大的障碍。 那第二个我觉得就是。 大家可能。 写论文的时候，可能不是特别在意。 嗯 大家写的时候，哦，我知道了，大家规范的定义是什么样的。 但是忽视了。 在我的小领域里面，比如说我们做这个计算机视觉，对吧？图像、图 到底。 怎么样去用什么样的符号定义，对吧？比如说大家图像都用大写的I去定义。 因为image嘛，大家习惯大家都用i去定义，而你对于呃图像你可能用t。 对吧？ 大写的T去定义OK，这个没有任何的大家说逻辑上的问题。 但是大家默认t代表的是text，是文本。 所以你这个时候和大家认知是冲突的。 他在理解你文章的时候就有很大的歧义，因为你在最初提及这个符号的时候，你可能给他他明确的解释。 但是到后面。 公式里再出现，或者说反复在这个变量上面再去不断的去更新特征表示或者什么信息的时候，这 同样用T。 审稿人可能就不记得你最一开始这个t是什么意思了。 那么就会给他造成很大的误解。哎，文本为什么要这样像图像一样处理？ 所以当你。 用领域内后共同的这种约定俗成的共识的语言去表达的时候，其实你就省去了很多不必要的歧义。 啊 然后第三个就是。 你任何的，当你有统一的符号之后呢？ 你。 文章里只要出现的这种变量，你还是要给出明确的定义和解释。就像每一个公式后面我都会。 详细的展开啊，这些变量每一个都是什么样的含义？ ok，这三点我觉得是层层递进的，所以大家 每一个其实都要去做到啊。 那么。 下一个我觉得严谨的方式就是大家，哎。 其实经常写写文章的时候，为什么会出现我前言不搭后语？大家觉得哎，我这个文章确实你也写了很多东西，也提供了很多信息，但是别人看完之后大脑没有任何印象。 那就是你论文里没有写出一个完整的story。 所以呢，我觉得让大家最好能写出完整story的一个小trick，就是 你在写文章的时候，你一定要告诉自己。 我要用一些过渡词。 去 也是告诉自己，也是告诉审稿人，我的论文里的逻辑是什么？我当前说这句话，我为了跟前面是什么关系？ 跟后面一句话有什么关系？ 那你其实也自己在不断的。 问自己，让自己有意识的去把所有的信息。 有因果，有逻辑的表达出来。比如说我们在introduction里面对吧，我们说哎，上面现有方法有只有这个任务有这样的问题，那现有方法提出了哪些哪些解决的方案。 那这些解决方案呢？ 还是存在很多的问题，比如说他们只能做到某一些程度。 上的问题解决。 但实际上。 要解真正解决这个问题，还需要做到什么什么。 对，那所以说我们这篇工作提出了那个方法。 具体来说，我们先怎么样？然后在这个基础之上，我们又进行了什么样的操作？然后我们实现了什么什么。 就是当你把这些句子。 你当你把这些零散的东西先都排列出来之后，你在中间加上一些衔接的语言，那么你会重新改写你以前表达出来客观的这个事实，反而让它能够更好的去支撑。 你前面说的一些。 啊，提出的一些思路。 这个是我觉得是一个特别好的，就是大家在写的，不管是段落之间。 还是一段的句子之间要加上一些过渡词，去强化自己对逻辑的。 呃，思考方式。 也去让审稿人有逻辑的去读你的论文。 Okay。 好。 那第四个小tip就是给大家呃一定要，就是最后check论文的时候再去仔细检查。 你的图里面的。 符号的定义和对模型名字的定义，以及你正文里面甚至你的caption里面，对吧？对应的这些符号名字的定义，以及你正文里面和你所有的论文里面实验结果里面出现的图啊、表啊。 对应这样的呃，文字和名称都要保持一致。 因为其实我我我我的学生就很很在初期的时候。 不相信这些，不太相信，所以。 他比如说忽视了在检查实验结果分析的时候，以及实验结果正文分析的时候，名字和一开始的不对应。 导致审稿人之间就说，哦，那你这个图的结果和你这个表的这个表达东西都不是一个模型。 你用的是什么模型？ 然后你最后rebutt的时候，当然你可以说我写错了，对吧？但这个其实给寻找人就是一个特别不专业、特别不认真的。 这个科研态度，那其实他就会同样质疑你其他的东西。 啊，所以我先就是大家最后再把所有的图注啊、表注啊、正文呀、图片呀，所有的 只要表达相同的东西，一定要表达一致。 ok 好，那这一讲就简单给大家介绍到这儿。后面还有具体的很多的实操的小的工具，给大家提高效率哦。好，谢谢大家。

```


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

## 第九讲：英文学术论文之英文规范——如何做到简洁与严谨

### —— 课堂完整复盘（Markdown 版）

---

## 文档说明

体例与前几讲一致。本讲开启课程第四大板块——"学术论文之英文规范"。PDF 中文部分以 OCR（chi_sim+eng）识别并与逐字稿交叉核对；本讲展示的论文原文片段（ET-BERT 初稿/终稿对比、CoTNet 论文节选、Mucko 摘要引言全文、实验表格）均可从 PDF 文本层直接可靠提取，可信度高。

---

## 〇、本讲基本信息

| 项目 | 内容 |
| --- | --- |
| 讲次标题 | 第九讲：英文学术论文之英文规范——如何做到简洁与严谨 |
| 讲者 | 于静 副研究员，中国科学院信息工程研究所 |
| PPT 页数 | 9 页 |
| 示例论文 | ET-BERT（WWW 2022，初稿 vs camera-ready 对比）；CoTNet（Contextual Transformer Networks，术语定义示范）；Mucko（IJCAI 2020，段落逻辑与图表一致性示范） |

### 课堂讲解：开场

> 今天我们进入下一个讲解的内容——英文学术论文的英文规范问题。很多同学都给我提出很多问题：关于我不是英文的 native speaker，我怎么样把我的英文学术论文写得既地道又专业？

于静老师首先纠正一个普遍误区：大部分同学觉得自己"英文写作不好"，但真正的问题往往**不在于语言表达能力，而在于英文的逻辑思维方式**。本讲会给出很实操的建议（如何用英文思维写学术论文），也会提供实用小工具（术语规范、符号定义、拼写检查等）。

**核心引用（施一公老师的观点）：** 于静老师引用施一公老师的一句话，作为英文学术论文写作最核心的目标：

> 论文只是一个载体，是为了向同行们宣告你的科研发现，是学术界交流的重要工具。所以，在科研论文写作时，一定要谨记于心的就是：**用最简单的话表达最明白的意思！**

即：用大家有共识的学科领域语言去做成果交流，而不在于描述得多"高大上"、多五花八门。

---

## 一、英语写作规范——八项注意（PPT 第 2 页）

### 幻灯片内容（原文精准转录）

标题：**英语写作规范——八项注意**

页面用红/绿两色区分难度：

**红色（较难，涉及英文思维方式）：**
1. 精简的表达方式
2. 严谨的叙述逻辑

**绿色（相对容易，细节层面）：**
3. 专业的学术用语
4. 规范的符号使用
5. 标准的学术术语
6. 完整的图表绘制
7. 正确的文献引用
8. 诚实的学术道德

### 课堂讲解

> 英文写作规范其实是一个非常繁琐、涉及非常多细节的东西，大家的问题都是五花八门的。我大概把最核心、大家常犯的一些问题总结成了八项注意……我觉得最难的其实也是涉及大家英文思维方式的内容，包括怎么样做精简的表达、怎么做严谨的叙述；但大家常问的问题反而不在于这些表达层面，而在于下面这些很细节的（专业术语、符号定义等）——这些往往更容易一些。所以我会花上下两讲去介绍这八项内容，前一讲（本讲）重点展开怎么样表达更精简、更严谨。

---

## 二、精简的表达方式（PPT 第 3 页）

### 幻灯片内容（原文精准转录，来自 PDF 文本层直接提取）

标题：**规范(1)——精简的表达方式**

页面开篇提示：

> 论文只是一个载体，是为了向同行们宣告你的科研发现，是学术界交流的重要工具。所以，在科研论文写作时，一定要谨记于心的就是：用最简单的话表达最明白的意思！

**左侧（学生初稿版本）原文：**

> *"Motivated by the above idea, we propose a novel framework for classifying encrypted traffic in this paper, encrypted datagram representation by pretraining (ET-BERT), for learning generic features in large-scale unlabeled encrypted traffic (Figure 1(c))."*
> —— 标注：**表达：一句话 3 个从句 ｜ 问题：混淆方法和问题，无重点，有语病！**

> *"...more insightfully, we propose a relation-aware pre-training model for encrypted traffic to adaptively capture a generic representation of traffic in multiple encryption scenarios. It can be demonstrated by two procedures. First, the Masked Burst Model (MBM) procedure captures the correlation between different payload bytes from unmasked contexts. Then, the Same-origin Burst Prediction (SBP) procedure captures same-origin evidence between different classes of sub-BURST pairs."*
> —— 标注：**表达：一句话 44 个单词 ｜ 问题：加入太多细节，无重点！有语病！**

**右侧（camera-ready 终稿）原文：**

> *"In this paper, we propose a novel pre-training model for classifying encrypted traffic, named as Encrypted Traffic Bidirectional Encoder Representations from Transformer (ET-BERT), which aims to learn datagram contextual relationship features from large-scale unlabeled encrypted traffic (Figure 1(d))."*
> —— 标注：**一句话命名方法及问题 ｜ 一句话突出方法目标 ｜ 一句话介绍方法创新**

> *"We first propose a raw traffic representation, denoted as BURST, which serves as the input... Then, the pre-training network with Transformer... obtains datagram-level generic traffic representations by self-supervised learning on large-scale unlabeled data, and captures the traffic-specific patterns: the Masked BURST Model (MBM) task captures the correlated relationship between different datagram bytes in the same BURST and represent them by their context; the Same-origin BURST Prediction (SBP) task models the transmission relationships of preceding and subsequent BURST. Then, ET-BERT incorporates with the specific classification task and fine-tune the parameters with small number of task-specific labeled data."*
> —— 标注：**一句话表达核心方法思路**

页面底部三条 Tips（原文）：

> Tips: (1) 一句话只表达一个信息! (2) 减少中文翻译英文! (3) 减少重复表达!

### 课堂讲解

于静老师逐句对比初稿与终稿，拆解具体问题：

**初稿第一句话的问题：** 这句话（"基于上面这些启发和想法，我们提出了一个新的框架用来做加密流量分类的，[ET-BERT]，用来在大规模无标注的流量数据上学习通用的特征"）一次性塞进了**三层意思**：① 模型叫什么名字，② 模型技术上的创新是什么（用预训练得到表示），③ 做了这个技术之后要实现的目的是什么（在无标注数据上学到通用表示）。她指出：这种写法常见于同学们习惯于把中文里若干个逗号连接的完整句子，直接丢进翻译软件，或按中文思路逐句直译成英文——中间加了很多逗号，"首先，这不符合英文语法；第二，一旦不符合语法，句子里包含的这么多层意思，反而每一个都表达不清楚"。

**终稿的重新组织：** 
- 第一句：只表达一个意思——"这篇文章提出了一个预训练模型，用来做流量分类"，先说清楚技术创新和解决的问题（这其实也呼应了第二讲讲的"怎样组织题目"）。
- 明确说清模型叫什么名字：如果论文里给模型起了明确的名字，一定要说明这个名字的来源/含义（缩写全称是什么），"这里说清楚之后，后面所有用到这个名字的地方就不用再解释了"。ET-BERT 在终稿里被解释为"Encrypted Traffic Bidirectional Encoder Representations from Transformer"的缩写。
- 第二句单独表达模型要达到的**目标**："It aims to learn... generic traffic representations from large-scale and unlabeled encrypted traffic"——呼应此前讲摘要写作时提到的"先用一句话讲清楚大思路"的原则。于静老师特别指出：这句话其实**预告了读者**，下面就要讲怎么样在无监督数据里学习通用表征，为了达到这个目标，后面第一步第二步第三步怎么做——"这就是我特别想跟大家说的核心一点：你论文里的任何一句话都是有目标的，不是想把所有知道的东西都表达出来，而是任何一句话不管是引领下文还是引导读者，都一定要传输出你核心想让他有印象的信息——而且这些信息一定要有结论、有数据和分析支撑，然后再有最后结果。"

**第二处 44 词长句的问题（方法部分开篇）：** 于静老师提到自己数了一下这句话有 44 个单词。问题在于把很多模型细节（数据从原始形态到模型输入之间经历的详细变换、数据怎样流转支撑下游任务）都塞进这一句话里，"反而冲淡了整个大的流程介绍"——句子太长，读者根本不知道重点想表达什么，审稿人会想"我这样做也可以，为什么不那样做"，从而留下不好的第一印象。

**终稿改法：** 先用一句话把核心方法总结出来（提出了一个结构，应用在原始数据上，得到能给预训练模型的表示），具体这个结构怎么处理、怎么得到，留到 Method 部分详细讲；在 introduction 里，只需要按逻辑顺序依次点出三块创新（表示 → 预训练/微调框架 → 预训练框架具体是什么样 → 微调过程是什么样）各自的**核心点**，不需要展开讲这些核心点具体怎么实现。

### 避免冗长无重点的三个 Tips

1. **一句话只表达一个意思。** 于静老师以自己做 PPT 为例："每一页 PPT 我们其实只表达一个意思，不管我有大量的结论，还是有数据支撑，还是有建议，这一页 PPT 就只表达一个意思。" 句子也是一样——可以用各种数据、名字缩写等方式去支撑，但核心只表达一个意思。
2. **尽量避免直接把中文翻译成英文（无论是翻译软件还是自己直译）。** 要习惯用英文的逻辑和常用表达去写英文论文。她还补充：读别人论文时也不要习惯性地丢进翻译软件——作者最核心的想法和创新，往往蕴含在很精巧的一两个关键词表达上，翻译软件会抹平这些细微差别。真正想理解一个作者的核心想法和创新时，一定要读原文、仔细琢磨他为什么这样表达，理解之后才能真正借鉴、灵活运用到自己的论文表达中。
3. **避免重复表达。** 刚开始写作的同学习惯于只从一个维度反复强调工作的重要性——不管在 introduction、abstract 还是 method 里，翻来覆去讲同一句话。避免的方法：更深入地追问自己"这个方法对领域到底有什么样重要的作用？为什么有这样的作用？我可以通过什么样的公式证明？通过什么样的实验结果证明确实做到了？"——这样在论文不同地方，会从不同角度同时印证同一个结论，但表达的话是不一样的（通过事实、理论公式分析、或对现有方法的分析去支撑），而不是干巴巴地反复说"我能做到"。

---

## 三、严谨的叙述逻辑：审稿人视角的换位思考（PPT 第 4 页）

### 幻灯片内容（原文精准转录）

标题：**规范(2)——叙述逻辑**

页面设置了一个情境：**"假设审稿人只有一个小时审稿 deadline，刚打开你的论文，看到……"**

随后展示两个"审稿人读到就会打问号"的反例：

> 读了一句话："Now, we could use CoTNet model to predict the result of that dataset." → **？？**

> 读了一个图 → **？？**

### 课堂讲解

于静老师说明这一部分要解决的问题：论文表达上给审稿人造成很大的理解障碍，导致他们很难在短时间内充分理解你的论文。审稿人往往是在截止日期前，花一两个小时快速看一遍就要给出判断——如果存在逻辑不清晰或定义不清楚的地方，审稿人没有耐心和时间像作者一样去思考背后的逻辑，读不懂就是没有表达清楚。

**导致"读不懂"的几类典型原因：**

1. **突然出现一个从未定义过的模型/方法名字**（如例句中的"CoTNet model"）——审稿人完全不知道这代表什么意思，从这里开始，后面的内容都很难再读懂，或者即使觉得这是个关键的东西，也完全不知道具体含义。
2. **习惯于随时自己定义新符号**——一方面可能与领域内大家共识的符号定义不一致，另一方面即使符号含义"默认"大家能猜到，也没有给出明确的定义解释（这个符号如果是变量，怎样计算得到的？）——都会让审稿人难以继续清晰理解。
3. **图（比如此前几讲讲的方法框架图）里关键信息、定义逻辑和创新性没有表达清楚**——审稿人在细读论文之前，通常会先看这几个关键的图，如果图里不能快速理解核心内容，再去看正文就会浪费大量时间。

> 所以不管是语言、公式还是图片，一篇 A 类论文在每一个环节上都需要让审稿人最快捷、最清晰、准确地理解。

---

## 四、四条具体建议（PPT 第 5–8 页）

### Tip (1)：术语使用前先定义解释（PPT 第 5 页）

**幻灯片内容（原文精准转录，来自 PDF 文本层，解答了第 4 页 "CoTNet model" 的疑惑）：**

> **3. Our Approach**
> *"In this section, we first provide a brief review of the conventional self-attention widely adopted in vision backbones. Next, a novel Transformer-style building block, named Contextual Transformer (CoT), is introduced for image representation learning. This design goes beyond conventional self-attention mechanism by additionally exploiting the contextual information among input keys to facilitate self-attention learning, and finally improves the representational properties of deep networks. After replacing 3×3 convolutions with CoT block across the whole deep architecture, two kinds of Contextual Transformer Networks, i.e., CoTNet and CoTNeXt deriving from ResNet [2] and ResNeXt [3], respectively, are further elaborated."*

### 课堂讲解

这段文字正是"CoTNet"这个模型名字第一次被清晰定义的地方——先介绍 Contextual Transformer（CoT）这个新模块，解释它相对传统 self-attention 的改进之处，然后说明把 CoT block 替换 3×3 卷积后得到的架构分别叫 CoTNet 和 CoTNeXt。**任何模型名字、变量名字，或第一次出现的专业术语，一定要提前定义清楚；如果有缩写，全称和缩写要同时出现在定义的位置**，后面就不用再反复解释了。

### Tip (2)：公式后紧跟符号解释（PPT 第 6 页）

**幻灯片内容（原文精准转录）：**

> a_i = softmax(w_v^T tanh(W₁v_i + W₂q)) —— (1)
> *"where W₁, W₂ and w_v (as well as W₃..., W₁₂, w_u, mentioned below) are learned parameters. Q is question embedding encoded by the last hidden state of LSTM."*
>
> β_ij = softmax(w₂^T tanh(W₃v'_i + W₄q')) —— (2)
> *"where v'_i = W₅[e_i; c_ij], q' = W₆[u_i, q] and [·,·] denotes concatenation operation."*
>
> m_i^(t) = W₁₀[m_i, c_i, Δ] —— (11)
> c_i = Σ_{k∈N_i} W₁₁[m_k^(t), s_ik] —— (12)
> *"where N_i represents a set of 1-hop neighboring nodes regarding the memory entity m_i and c is the contextual memory representation. Then the updated memory is served as the new knowledge memory used in the next reasoning step."*

### 课堂讲解

于静老师这一页想具体示范的是：好的论文里，**每一个公式后面，都会紧跟着把公式里出现的每一个变量/符号详细解释清楚**——不是写完公式就默认读者能猜到符号含义，而要像范例这样逐一说明。这一点她提到自己在给学生改论文时"非常头疼"，因为改了很多版，学生依然没法把论文里所有公式的符号定义清楚，给审稿人的感觉就是很凌乱、没有体系。她给出三层递进的建议：

1. **遵循学术论文里规范的数学符号使用惯例**——标量、变量、向量、矩阵分别应该用斜体还是正体、加粗还是不加粗、大写还是小写，这些都有大家统一的规范，如果和大家的认知相违背，就会给阅读造成很大障碍。
2. **遵循自己小领域内约定俗成的符号使用习惯**——比如计算机视觉领域，图像大家习惯用大写 I（Image）表示；如果你偏偏用 T 表示图像，虽然逻辑上没有问题，但大家默认 T 代表 Text（文本），这就会和读者认知冲突，造成理解上的很大歧义（"文本为什么要这样像图像一样处理？"），即使你最初提及时给出了明确解释，但后面公式里反复出现时，审稿人可能已经忘记你最初的定义。
3. **即使符号统一、规范，论文里出现的每一个变量仍然要给出明确的定义和解释**——就像范例中每个公式后面都详细展开每个变量的含义。

> 这三点我觉得是层层递进的，所以每一个都要做到。

### Tip (3)：清晰的段落结构，善用过渡词（PPT 第 7 页）

**幻灯片内容（原文精准转录，来自 PDF 文本层，取自 Mucko 论文摘要与引言全文）：**

页面展示 Mucko 完整的 Abstract 与 Introduction 正文，并用中文批注在关键转折句旁标出逻辑关系：

- 在"...introduces noises for reasoning"附近标注：**"然而，他们方法只..."**
- 在描述现有方法局限性的句子附近标注：**"但事实上，需要..."**
- 在"In this paper, we depict an image by a multi-modal heterogeneous graph..."附近标注：**"本工作中，我们提出..."**
- 在方法具体展开处标注：**"具体来说，我们首先..."**
- 在后续步骤描述处标注：**"然后，实现..."**

### 课堂讲解

> 大家经常写文章的时候，为什么会出现"前言不搭后语"？大家觉得，哎，这个文章确实写了很多东西，也提供了很多信息，但别人看完之后大脑没有任何印象——那就是你论文里没有写出一个完整的 story。

于静老师给出一个写出完整 story 的小 trick：**写文章时一定要用过渡词，既是告诉自己、也是告诉审稿人，"我当前说的这句话，和前面是什么关系，跟后面一句话有什么关系"**——这个过程本身也是在强迫自己有逻辑地组织信息、把有因果关系的内容表达出来。她以 Introduction 的典型逻辑链条为例："现有方法只有这样的问题 → 现有方法提出了哪些解决方案 → 这些方案还存在什么问题（比如只能做到某种程度）→ 但实际上要真正解决问题还需要做到什么 → 所以我们这篇工作提出了这个方法 → 具体来说我们先怎么样 → 在此基础上又进行了什么操作 → 最终实现了什么"。

> 当你把这些零散的表达先都排列出来之后，中间加上一些衔接的语言，你会重新改写以前那些客观陈述的事实，反而让它们能够更好地支撑你前面提出的思路。这是大家在段落之间、句子之间，都要加上过渡词去强化自己逻辑思考方式、也让审稿人有逻辑地读懂论文的一个特别好的方法。

### Tip (4)：图表命名与正文表达前后一致（PPT 第 8 页）

**幻灯片内容（原文精准转录，来自 PDF 文本层，取自 Mucko 论文）：**

页面并列展示 **Table 1**（FVQA 数据集上的 SOTA 对比，含 LSTM-Question+Image+Pre-VQA、Hie-Question+Image+Pre-VQA、FVQA (top-3-QQmapping)、Straight to the Facts (STTF)、Reading Comprehension、Out of the Box (OB)、**Mucko 73.06 / 85.94**）、**Table 2**（Mucko 消融实验：full model / w/o Semantic Graph / w/o Visual Graph / w/o Semantic Graph & Visual Graph 等）、**Figure 2**（模型总览图，含 Multi-modal Heterogeneous Graph Construction 与 Cross-modal Heterogeneous Graph Reasoning 两大模块）。

### 课堂讲解

于静老师提醒大家在**论文定稿前的最后检查环节**要特别仔细核对：图里的符号定义、模型名字，以及正文里、甚至图/表 caption 里对应的这些符号名字，都要保持一致。她分享了一个真实的反面教训：

> 我的学生就很在初期的时候不太相信这些，忽视了在检查实验结果分析、以及实验结果正文分析时，名字和一开始的不对应，导致审稿人指出——"你这个图的结果和这个表表达的东西都不是一个模型，你用的是什么模型？"最后 rebuttal 的时候，当然可以说"我们写错了"，但这其实给审稿人一个特别不专业、不认真的科研态度印象，他就会同样质疑你其他的东西。

因此，最后检查阶段一定要把所有图注、表注、正文，只要表达相同的东西，都核对为完全一致的表达。

---

## 五、结语（PPT 第 9 页）

**幻灯片内容：** 标题"欢迎大家在 B 站留言交流！"（与第八讲结语页版式一致）。

**课堂讲解：**

> 好，这一讲就简单给大家介绍到这儿。后面还有具体的很多实操的小工具，给大家提高效率。好，谢谢大家。

---

## 附录：本讲核心概念速查

1. **英语写作规范八项注意：** 精简表达、严谨叙述逻辑（本讲，较难）+ 专业学术用语、规范符号使用、标准学术术语、完整图表绘制、正确文献引用、诚实学术道德（下一讲，相对容易）。
2. **写作核心目标（施一公语）：** 用最简单的话表达最明白的意思——论文是向同行宣告发现的载体，不在于描述多"高大上"。
3. **精简表达三 Tips：** 一句话只表达一个意思 → 避免直接中译英（无论翻译软件还是直译，也不要用翻译软件读别人论文）→ 避免重复表达（从不同角度/不同证据支撑同一结论，而非反复空喊同一句话）。
4. **审稿人视角换位思考：** 假设审稿人只有一小时，任何"从天而降"的未定义名字、随意自定义且未解释的符号、信息传达不清的图，都会让他从此处开始读不下去、留下负面印象。
5. **四条具体建议：** ① 术语/名字/缩写首次出现即完整定义；② 公式后紧跟逐一解释符号含义（三层递进：通用数学规范 → 子领域约定俗成 → 逐一显式定义）；③ 善用过渡词构建完整 story，把零散事实通过因果衔接语言组织成有逻辑支撑的论述；④ 全文图注/表注/正文/模型名字必须完全一致，检查阶段务必仔细核对，避免因粗心导致的专业性质疑。
6. **一句话有目标：** 论文里任何一句话都要么引领下文、要么引导读者，服务于让审稿人记住核心信息（结论+数据分析支撑+结果），而非堆砌所有已知信息。
