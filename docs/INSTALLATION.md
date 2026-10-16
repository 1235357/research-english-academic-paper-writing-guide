# 4.7.8 通用二合一包：离线使用与验收边界
本说明适用于唯一对外交付的 web-plugin 通用 ZIP。发布状态以对应 GitHub Release 为准；ChatGPT 网页导入与 Windows 实机安装仍需单独验证。
该通用 ZIP 仅有academic-research/外层文件夹，其中包含plugin.json、LICENSE、NOTICE及skills/。作为通用Skill时复制完整skills/research-english-academic-paper-writing-guide目录；不能只复制SKILL.md。作为Plugin时保留整个根目录，并使用宿主实际支持的导入方式。复制或选择ZIP不等于已加载。
所有现有课程Markdown、完整重建、两个历史版本和19个playbook均在共同核心中，正常文字阅读不需要旧Release、联网下载、GitHub连接或Python。可选脚本保持原样，没有新增依赖。
先读SKILL.md、references/current-source-erratum.md及references/course-review-notes.md；再依照references/lecture-index.md读取完整相关讲次。历史来源链接只作引用线索，不是核心使用的材料获取前置条件。
未来含原始材料包必须复制这一共同核心的全部字节，再添加已核验原件及其清单。当前用户历史原ZIP/独立transcript尚未找回，所以没有把当前官网PDF冒充历史原件加入本包，也没有交付一个假的全原件版。
当前来源错配及文字/视觉保真边界以current-source-erratum.md为准。历史package-history/安装说明与清单保留作追溯，不是当前安装步骤或当前文件哈希。
release-manifest.json列本包实际文件与摘要；source_commit以实际构建清单为准；它必须绑定构建来源提交，未提交候选不能冒充正式提交。它不证明发行者身份、版权、完整视觉转录或客户端已启用。旧版文件和插件均未覆盖。

Windows与Linux均需复制完整技能目录；正常离线带读无需获取旧版附件。当前取得的仓库、发布包及工作目录没有可交付的用户历史原始PDF/transcript文件，所以尚不能据此认定完成全原件交付；不以联网链接或转写替代原件。

开发者的 --kind all 回归构建还会生成独立 Skill 和完整 Plugin 测试产物；它们不是本次通用交付附件，不能套用本页的外层目录说明。
