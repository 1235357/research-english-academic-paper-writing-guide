# Research and English Academic Paper Writing Guide：安装与发布

## 当前分发：4.7.4（课程来源 4.7.3）

截至2026-10-15，已发布正式附件见 [v4.7.4 Release](https://github.com/1235357/research-english-academic-paper-writing-guide/releases/tag/v4.7.4)。已发布4.7.4修复分发；该版本43个技能源文件中，仅 SKILL.md 的当前包版本标识变化，其余42文件保持4.7.3来源字节。已发布4.7.4附件内 references/installation.md 中的4.7.3为保留的历史安装说明，不是当时的分发版本。上述字节不变结论仅描述已发布4.7.4，不适用于后续开发候选。

- 网页 New Plugin 选择 `academic-research-v4.7.4-web-plugin.zip`，入口为 `academic-research/plugin.json`，技能在 `academic-research/skills/research-english-academic-paper-writing-guide/SKILL.md`。
- 独立 Skill 入口选择 `research-english-academic-paper-writing-guide-v4.7.4-skill-full.zip`；不能把它当作 Plugin 包。
- 仓库／本地插件工作流选择 `research-english-academic-paper-writing-guide-v4.7.4-plugin.zip`；开发工具和安装器不在精简网页包内。

保存与选择上传文件时保留完整的 `.zip` 后缀。2026-10-15 本账户检查中，扩展名缺失的文件未通过选择；带 `.zip` 的对应文件通过了文件选择阶段。未点击最终 Add，避免创建重复插件；这不证明网页端到端安装成功，也不证明所有账户有相同限制。已有托管插件的更新与读回属于另一条验证路径；New Plugin 新建不能代替已有插件更新。

本开发候选同步更新仓库与技能内的安装说明，不改写课程原文或历史来源清单。已发布4.7.4附件保持不变；如后续发布包含本说明的新包，必须使用新的发行版本并独立验证，不能覆盖同版本附件。本候选尚未据此发布或更新托管插件，也不表示 npm 已发布4.7.4。完整打包范围与限制见 [WEB-PLUGIN.md](https://github.com/1235357/research-english-academic-paper-writing-guide/blob/main/docs/WEB-PLUGIN.md)。下方保留4.7.3历史操作说明；其中带版本号的命令明确针对旧版，不应当作4.7.4安装命令。

## 历史4.7.3安装说明

本节历史发布层版本：4.7.3。13讲与两份完整课程重建共15份课程原文保持逐字节一致；派生指南的语义修订与新增复核层单独记录。旧文档中的版本号保留历史身份。

## 选择下载文件

下载 [GitHub Release](https://github.com/1235357/research-english-academic-paper-writing-guide/releases/tag/v4.7.3) 的显式附件，而非GitHub自动生成的 Source code ZIP。

| 文件类型 | 解压后入口 | 用途 |
| --- | --- | --- |
| `*-skill-full.zip` | `research-english-academic-paper-writing-guide/SKILL.md` | 支持Agent Skills的上传入口，或本地技能目录 |
| `*-plugin.zip` | `research-english-academic-paper-writing-guide/plugin.json` 与 `.claude-plugin/plugin.json` | Agent Plugins / Claude Code 插件入口 |
| `read-xuexiguan-<unit>-cloud-skill.zip`（仅学习观） | 同名单根目录里的 `SKILL.md` | 有容量限制的云端技能导入入口 |

ZIP包含一个顶层文件夹；文件夹名与Skill YAML `name`相同。普通聊天附件可供读取，但不会因此自动注册为系统Skill；在ChatGPT支持Skill／插件的环境及Claude Custom Skills中使用相应导入入口。格式兼容、目录审核、账户功能和实际客户端导入是不同条件。本仓库离线验证包结构，不能据此宣称已经通过所有平台的商店审核或登录后上传。

论文写作Skill ZIP保留原54文件基线对应的课程内容和全部双版本正文，13讲与19个playbook不删减。单Skill包及插件包的实测字节、文件清单与SHA-256见Release校验清单。

## 本地完整安装

Node.js 18+，Python辅助阅读脚本需要3.9+；安装器不依赖第三方npm模块，也不联网或执行书内Obsidian插件。

```bash
git clone https://github.com/1235357/research-english-academic-paper-writing-guide.git
cd research-english-academic-paper-writing-guide
git checkout v4.7.3
node bin/install.mjs --agent codex --project /absolute/path/to/project
node bin/install.mjs --agent claude-code --project /absolute/path/to/project
```

| `--agent` | 项目目录 | `--global`目录 |
| --- | --- | --- |
| `codex` | `.agents/skills` | `~/.agents/skills` |
| `claude-code` | `.claude/skills` | `~/.claude/skills` |
| `gemini-cli` | `.agents/skills` | `~/.gemini/skills` |
| `github-copilot` | `.agents/skills` | `~/.copilot/skills` |
| `cursor` | `.cursor/skills` | `~/.cursor/skills` |
| `generic` | `.agents/skills` | `~/.agents/skills` |

`--target /path/to/skills`指定技能父目录；`--skill research-english-academic-paper-writing-guide`选择技能；`--list`列出技能；`--dry-run`只预览；`--verify`核验安装目录的全部文件SHA-256、字节数及额外文件。完整复制包括原资产、隐藏文件和中文路径，安装回执另放在技能父目录的`.skill-installation`。

重复安装相同内容保持幂等。只有未被修改的受管理安装可以用`--upgrade`升级，升级前把全部旧文件与回执保存在`.skill-backups`。未管理的同名目录、本地新增／删改文件以及符号链接路径都拒绝覆盖；先保存并处理个人改动。

## npm／npx和社区目录

公共 npm 安装命令（仅在该版本已成功发布到 npm 后可用）：

```bash
npx --yes --package=research-english-academic-paper-writing-guide@4.7.3 research-writing-skill-install --agent codex --project /absolute/path/to/project
```

`npm install -g research-english-academic-paper-writing-guide@4.7.3` 只安装命令行程序；仍需运行 `research-writing-skill-install --agent codex --global` 才会复制并注册本地技能目录。npm 不运行自动安装钩子，也不修改客户端设置。安装完成后，在同一项目打开新会话或刷新技能列表，显式调用 `$research-english-academic-paper-writing-guide`，并要求读取 `references/course-full-reconstruction.md` 的相关段落。

版本是否已发布应以 `npm view research-english-academic-paper-writing-guide@4.7.3 version` 实际返回为准。若 registry 返回 E404，则不能把 GitHub Release 当作 npm 发布成功。以下 Git 来源后备路径与 npm registry 发布相互独立：

```bash
npx --yes --package=github:1235357/research-english-academic-paper-writing-guide#v4.7.3 research-writing-skill-install --agent codex --project /absolute/path/to/project
```

完整技能在Git/npm缓存及最终目录各占空间；也可直接使用上一节的本地安装器。社区`skills` CLI支持多个Agent及已认证私有Git来源：

```bash
DISABLE_TELEMETRY=1 npx --yes skills@1.7.2 add 1235357/research-english-academic-paper-writing-guide --skill research-english-academic-paper-writing-guide --agent codex --agent claude-code --copy -y
```

社区CLI有自己的更新行为；上面的命令宜用于新的安装目录。要保留已有本地改动并取得完整备份，用本仓库安装器。直接URL下载在社区CLI有独立下载／解压／文件数预算，完整大书用Git来源。当前支持路径以版本1.7.2的维护方文档为据；其他Agent可由该CLI选择，无需修改原语料。

## 插件市场入口

可移植入口为根`plugin.json`（Agent Plugins 1.0.0）；`skills/`在插件根。Claude叠加入口位于`.claude-plugin/plugin.json`。仓库同时提供`.agents/plugins/marketplace.json`和`.claude-plugin/marketplace.json`，两者本地来源`./`均指仓库／插件根。

在支持的Claude Code客户端：

```text
/plugin marketplace add 1235357/research-english-academic-paper-writing-guide
/plugin install academic-research@szsdt-research-writing
```

ChatGPT／Codex支持的本地客户端可读取仓库市场清单；重启或刷新客户端后选择插件。公开Plugins Directory或组织工作区发布仍需相应账号、审核与权限，GitHub Release不等于已进入官方目录。本项目不添加无用途的MCP服务器、自动联网钩子或凭证接收工具。

Claude CLI在线`plugin validate`在本次环境被自动批准审核拒绝：该进程尝试向`api.anthropic.com`发送私有资料。因此没有重试或绕过，验证报告记录为blocked；已改做官方schema和本地包内容验证。

## 构建与核验

```bash
python tools/validate_distribution.py
node --test tools/test_installer.mjs tools/test_npm_package.mjs
python tools/build_release.py --output /absolute/path/outside-repository --kind all
```

构建器仅取Git已跟踪文件，构建前必须提交或暂存新增发布文件。每份ZIP附逐文件大小、源路径和SHA-256；构建完成后流式重新读取每个ZIP条目并对比原字节。输出保存在仓库外，不将ZIP反复嵌入Skill。

来源与限制记录见仓库`docs/ecosystem/sources.json`；原始内容保留基线见`docs/distribution-baseline.json`。所有引用、阅读活动、视觉校对、结构验证和理解验收分别记录，发布机制不会替代实际理解。


## 排查“安装成功但没有生效”

1. 确认使用的是目标客户端的技能安装入口或本地技能目录。GitHub、npm、普通聊天附件不会自动创建 ChatGPT 的云端 Skill。
2. 用相同参数运行安装器的 `--verify`，核对磁盘中的完整文件；这只证明文件一致，不证明客户端已加载。
3. 在客户端技能列表查找完整名称，并在新会话中显式调用。对 Codex，项目安装必须在该项目或其子目录启动。
4. 请客户端实际读取完整课程重建及一个任务相关 playbook，报告读取路径与课程论点。如果只能看到简介、读取资源报错或客户端未列出该技能，记录具体客户端、安装入口和错误，不推断“全文已经加载”。
5. 一个客户端的本地安装不会同步到另一个客户端、浏览器聊天或其他电脑；已有云端插件/桥接器也有独立版本，需要分别核验。

本次离线实测覆盖 npm tarball 的安装命令入口、完整复制、幂等重装、SHA-256 核验与 ZIP 内容；不把这些结果等同于任何登录后客户端的真实导入验收。


### 插件身份与 Skill 身份

插件名为 `academic-research`；独立 Skill 与 npm 包名继续为 `research-english-academic-paper-writing-guide`。插件安装命令使用短插件名，独立技能调用和 npm 命令保持原名。根据 [OpenAI 插件提交错误说明](https://developers.openai.com/plugins/deploy/submission-errors)，插件与 Skill 的组合身份最长 64 字符；当前 `academic-research:research-english-academic-paper-writing-guide` 为 63 字符，旧同名组合为 91 字符。此项修复面向插件导入校验，不代表已通过目录审核或所有客户端实际安装。
