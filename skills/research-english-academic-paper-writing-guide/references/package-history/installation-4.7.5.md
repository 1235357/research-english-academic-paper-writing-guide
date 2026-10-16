# 4.7.5 安装与离线使用

本说明随4.7.5包完整提供。手中没有该版本ZIP时停止安装并取得正确附件；不要用旧版、网页链接、GitHub克隆或npm缓存补齐本包。是否正式发布由发行记录单独确认，构建或源码合并不等于发布或账户安装。

## 两种使用方式与三个附件

1. **Windows／Linux本地手动复制**：`research-english-academic-paper-writing-guide-v4.7.5-skill-full.zip`含单个`research-english-academic-paper-writing-guide/`技能目录；`research-english-academic-paper-writing-guide-v4.7.5-plugin.zip`含同名插件根目录、plugin.json、.claude-plugin/plugin.json、skills/、本地安装器与开发工具。复制整个所选目录，不要只复制SKILL.md。无需git、npm、联网安装依赖或运行书内程序。
2. **网页插件文字包**：`academic-research-v4.7.5-web-plugin.zip`含单个`academic-research/`插件根，根内plugin.json、skills/、LICENSE、NOTICE与逐文件release-manifest.json。完整保留现有43个技能文件，包括完整课程转写／重建、历史层和19个playbook；不包含原始PDF、原始独立transcript.txt、视频、截图、图片、仓库开发工具或npm安装器。使用网页支持的Plugin ZIP入口；独立Skill入口只使用前一种skill-full包。各包不能互换。

**原始格式的真实边界：** 当前可核验的本仓库和上述三个附件均有全部已纳入来源基线的课程Markdown：13讲的双版本正文与完整课程重建。来源基线计15份课程Markdown，其中仓库docs/副本与技能references/副本内容相同；独立Skill／网页包保留一份完整正文，不丢失独有课程内容。当前取得的仓库、发布包及工作目录没有可交付的独立原始PDF／transcript.txt文件。历史正文记载曾使用上传原件，并不证明那些原始文件已在本包。用户要求的“本地包同时附全部原始格式”尚不能据此认定完成；缺少的原件需另行找回和核验，不以联网链接或转写替代原件，也不能擅自公开补传私人文件。

正常离线带读以本包完整Markdown为依据，不要求获取外部原件。只有需要原始文件逐字／逐页或视觉核验时，明确报告原始格式缺失并暂停该核验；不要声称已看过原图。历史正文中“随skill打包的.transcript.txt”及“sources文件夹”属于旧来源记录，在当前包中不成立。本段纠正交付边界，不改写或删减保存的课程正文。

## 本地手动复制步骤

先解压到新的空目录并保留原ZIP。目标目录由你正在使用的客户端设置确定；复制路径不是客户端加载或执行的证明。不要覆盖已有同名技能、个人修改或正在使用的插件。

- 独立Skill：复制整个`research-english-academic-paper-writing-guide`目录到客户端的skills父目录。目录中必须直接包含SKILL.md、references/、scripts/和agents/。
- 完整Plugin：复制整个解压后的插件根目录到客户端支持的plugins父目录，或者在该客户端的本地插件入口选中该根目录。根下直接有plugin.json和skills/；若客户端只支持技能目录，则改用skills/内的完整技能目录。
- Windows文件资源管理器与Linux文件管理器都可完成上述复制，不需要终端。目录选择使用绝对路径，避免误复制外层下载目录。
- 如果客户端使用Codex约定的项目技能目录，将技能目录放到项目的`.agents/skills/`下；Claude Code项目技能目录为`.claude/skills/`。其他客户端以其实际配置为准，不猜测插件注册路径。
- 重新打开或刷新客户端技能列表，在目标项目的新会话中显式调用`research-english-academic-paper-writing-guide`。实际读取下列包内文件，再检查是否识别为已加载；仅复制成功不代表客户端已启用。

## 网页入口步骤与已有插件更新

保留文件完整`.zip`扩展名，直接选择web-plugin附件，不重新压缩、更换技能名称或添加额外MCP。2026-10-15对4.7.4的检查只观察到带.zip文件通过选择阶段；未点击最终Add以避免重复插件。这不证明4.7.5网页安装成功。

New Plugin通常是新建，不能当作已有插件更新。已有插件应通过其受支持更新流程并保留原插件身份、分享范围与权限，再独立读回内容；若没有该更新入口，停止并说明，不用新建副本替代。仓库分发版本与托管插件版本独立，不能仅凭名称或版本推定已同步。

## 包内完整阅读入口

以下路径全部以包含SKILL.md的技能目录为基准；从完整Plugin或网页Plugin根目录先进入`skills/research-english-academic-paper-writing-guide/`。

1. `SKILL.md`：当前使用协议及完整保留的第二来源整体综合。
2. `references/course-review-notes.md`：当前适用范围与证据纠偏。
3. `references/course-full-reconstruction.md`：全课程完整重建正文。
4. `references/lecture-index.md`与`references/lectures/`：13讲全部双版本正文，按讲定位；历史外部链接只作来源线索，不是正常阅读前置步骤。
5. `references/playbooks/`：19份执行指南；与相关讲次一起读，不以摘要代替全文。
6. `references/provenance.md`：保留的来源、校验值与不确定性；记录中的原始文件名不等于本包存在该格式。
7. `references/quick-reference.md`：辅助检查表，不能取代完整正文。

三个文字辅助脚本都在`scripts/`内；不安装第三方依赖。可选在已安装Python3.9+的本地机器、技能目录下执行：

```text
python scripts/check_title.py "A Study of Visual Question Answering"
python scripts/new_research_point_canvas.py
python scripts/measure_prose_rhythm.py --help
```

网页宿主没有Python时，直接读取完整Markdown即可；这些脚本不是阅读前置条件。开发构建、npm发布、其他版本安装及外部WEB-PLUGIN.md均不是使用本包的必需步骤。

## 完整性、范围与验收

每个ZIP都有release-manifest.json，列出本包实际文件、字节数和SHA-256。它证明文件清单与完整性，不证明版权授权、原始格式齐备、模型已读完或客户端已生效。正常阅读不需要外部仓库、原始PDF、独立transcript.txt或旧Release补齐。

相较正式4.7.4，43个技能源文件中只更新SKILL.md的当前版本／交付范围说明及本安装说明，其余41文件保持字节一致；全部15份基线课程Markdown保留。两个版本均不得宣称已交付当前缺失的原始PDF／transcript.txt。

发布与安装验证分开：先核验ZIP和全部正文；再在目标客户端验证导入、技能可见、完整文件读取和实际调用。记录未通过的阶段，不把格式检查或CI成功写成端到端安装成功。不覆盖已发布4.7.4附件；本说明不宣称npm已发布或任何账户已更新。外部官方网站、论文和历史发行链接仅作可选出处，不承担本包正文、安装说明或运行所需文件。
