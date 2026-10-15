# Web 插件发行包与入口选择

## 4.7.5 安装说明同步

4.7.5同步修复仓库与技能内的离线安装说明，并更新入口的版本与交付范围说明。相较正式4.7.4，43个技能源文件中仅SKILL.md与references/installation.md变化，其余41文件和全部15份课程Markdown保持逐字节一致。原始独立PDF/transcript.txt在已检查材料中不可交付，不能认定本地原始格式包已齐备。三个附件都有完整现有课程Markdown；网页包省略仓库开发工具，本地插件包支持手动复制。制品入口及精确文件名见[安装说明](INSTALLATION.md)。是否正式发布以[v4.7.5 Release](https://github.com/1235357/research-english-academic-paper-writing-guide/releases/tag/v4.7.5)为准；构建候选不等于已发布、已更新托管插件或网页导入成功。旧4.7.4附件不覆盖；托管插件版本与仓库分发版本独立。

以下为4.7.4历史分发记录；其中当前、本次及不变文件计数均只适用于该历史版本。

## 4.7.4 历史记录

本次 4.7.4 是分发修复版本，基于已合并的打包修复 `821da6326ffabe96199ad410baf9829f83d2ed0f`；语料来自正式 4.7.3（`6ca9f5d386fab598c97e967844678a3ee95d4b00`）。43 个技能源文件中，仅 SKILL.md 的当前包版本标识从 4.7.3 改为 4.7.4；其余 42 个文件及课程正文逐字节不变。实际是否发布以 GitHub Release 为准。已有云端 bridge 的同名版本号 4.7.4 属于不同宿主，不能据此认定内容同步或自动升级。

## 选择正确附件

- `*-skill-full.zip`：独立 Agent Skills 包，入口是 `SKILL.md`，不能当作 New Plugin 包。
- `*-plugin.zip`：完整仓库式插件分发，包括 marketplace、开发工具和安装器；用于相应仓库／本地客户端工作流。
- `academic-research-v<version>-web-plugin.zip`：专用精简插件包，一个 `academic-research/` 根目录，包含原始 `plugin.json`、全部 `skills/` 文件、LICENSE、NOTICE 和自动生成的逐文件发行清单。不含 marketplace、开发工具、npm 安装器或额外 MCP 配置。

精简包保留本次版本全部 43 个技能源文件的字节，包括 13 讲、19 个 playbook、完整重建文本和辅助脚本；并不提供完整开发仓库。技能中既有的开发／安装说明可能提到仓库专用文件，运行那些操作应使用仓库分发。现有课程、技能、安装说明和历史版本文本均不为此打包改动而重写。

正式插件身份是 `academic-research`；技能身份不变，组合名称长 63 字符。已有云端 `english-academic-research-github-bridge` 是不同的历史宿主身份；本构建模式不会更新、改名或删除它，也不改变用户已有权限。

## 构建和验证

```bash
python3 tools/build_release.py --output /absolute/path/outside-repository --kind web-plugin
python3 tools/build_release.py --verify /absolute/path/outside-repository/academic-research-v4.7.4-web-plugin.zip
python3 tools/test_web_distribution.py
```

`--kind all` 也生成专用 web 包，其他发行包保持原有选择逻辑。只收录 Git 已跟踪的技能和必需根文件；新增发布文件须先纳入 Git。构建器重新读取 ZIP 以验证 CRC、SHA-256、路径、合法身份和源字节；带 `--root` 的验证还检查全部已跟踪技能文件没有遗漏。发行清单里的 `source_commit` 标识构建基线，文件哈希标识实际输入；未提交工作树构建不等于正式 Release。

## 已观察结果与限制

2026-10-15，相同原始身份的精简 4.7.3 包在网页 New Plugin 入口报通用错误，但通过已授权 Plugin Creator 成功保存为个人私有插件，随后读回确认所有技能字节不变。平台补充兼容清单并规范化作者／开发者账户信息。此事实仅证明两个入口结果不同；底层原因仍未知，不能宣称本打包改动修复网页上传、平台全面故障或已通过公开目录审核。

[官方打包说明](https://developers.openai.com/plugins/build/plugins)和[提交错误参考](https://developers.openai.com/plugins/deploy/submission-errors)区分插件结构和更严格的公开目录规则。构建器采用保守的公开提交大小／路径上限，不把这些检查当作特定账户入口成功的保证。上传、实际安装、技能可见性和运行结果需分别核验；重复失败时保留具体错误及文件哈希，不通过创建占位插件、改名或删除既有插件来试错。

## 4.7.4 分发范围

此版本增加独立 web-plugin 附件和完整性回归，不改变课程、playbook 或运行权限。历史安装说明中的 4.7.3 命令继续指向旧版，保留其原始字节；本次插件使用上列 4.7.4 附件。GitHub Release 不代表 npm 已发布，也不代表 New Plugin 网页错误已修复。
