# Web 插件发行包与入口选择

此文档描述待审阅的分发改进；尚未发布新 GitHub Release。已核验的正式源版本仍是 4.7.3，提交为 `6ca9f5d386fab598c97e967844678a3ee95d4b00`。新分发版本须在审阅后确定，不把已有云端 bridge 的 4.7.4 当作本仓库正式版本。

## 选择正确附件

- `*-skill-full.zip`：独立 Agent Skills 包，入口是 `SKILL.md`，不能当作 New Plugin 包。
- `*-plugin.zip`：完整仓库式插件分发，包括 marketplace、开发工具和安装器；用于相应仓库／本地客户端工作流。
- `academic-research-v<version>-web-plugin.zip`：专用精简插件包，一个 `academic-research/` 根目录，包含原始 `plugin.json`、全部 `skills/` 文件、LICENSE、NOTICE 和自动生成的逐文件发行清单。不含 marketplace、开发工具、npm 安装器或额外 MCP 配置。

精简包保留所有 43 个技能源文件的字节，包括 13 讲、19 个 playbook、完整重建文本和辅助脚本；并不提供完整开发仓库。技能中既有的开发／安装说明可能提到仓库专用文件，运行那些操作应使用仓库分发。现有课程、技能、安装说明和历史版本文本均不为此打包改动而重写。

正式插件身份是 `academic-research`；技能身份不变，组合名称长 63 字符。已有云端 `english-academic-research-github-bridge` 是不同的历史宿主身份；本构建模式不会更新、改名或删除它，也不改变用户已有权限。

## 构建和验证

```bash
python3 tools/build_release.py --output /absolute/path/outside-repository --kind web-plugin
python3 tools/build_release.py --verify /absolute/path/outside-repository/academic-research-v4.7.3-web-plugin.zip
python3 tools/test_web_distribution.py
```

`--kind all` 也生成专用 web 包，其他发行包保持原有选择逻辑。只收录 Git 已跟踪的技能和必需根文件；新增发布文件须先纳入 Git。构建器重新读取 ZIP 以验证 CRC、SHA-256、路径、合法身份和源字节；带 `--root` 的验证还检查全部已跟踪技能文件没有遗漏。发行清单里的 `source_commit` 标识构建基线，文件哈希标识实际输入；未提交工作树构建不等于正式 Release。

## 已观察结果与限制

2026-10-15，相同原始身份的精简 4.7.3 包在网页 New Plugin 入口报通用错误，但通过已授权 Plugin Creator 成功保存为个人私有插件，随后读回确认所有技能字节不变。平台补充兼容清单并规范化作者／开发者账户信息。此事实仅证明两个入口结果不同；底层原因仍未知，不能宣称本打包改动修复网页上传、平台全面故障或已通过公开目录审核。

[官方打包说明](https://developers.openai.com/plugins/build/plugins)和[提交错误参考](https://developers.openai.com/plugins/deploy/submission-errors)区分插件结构和更严格的公开目录规则。构建器采用保守的公开提交大小／路径上限，不把这些检查当作特定账户入口成功的保证。上传、实际安装、技能可见性和运行结果需分别核验；重复失败时保留具体错误及文件哈希，不通过创建占位插件、改名或删除既有插件来试错。
