#!/usr/bin/env python3
"""Configure additive, dependency-free Skill and plugin distribution surfaces."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parents[1]
SPECS = {
    "xuexiguan-agent-skill": {
        "version": "2.0.0", "skill": "read-xuexiguan", "bin": "xuexiguan-skill-install",
        "display": "学习观完整原书与 Agent 带读", "marketplace": "szsdt-xuexiguan",
        "description": "完整保存《学习观》350页原文与扫描、83原图、原交付包、作者官网来源及独立标识的逐段带读；按来源证据阅读、应用和复核。",
        "short": "完整原书、来源定位与逐段带读", "private": True,
        "base": "eb4f3d83b27868bd5ae86554e18ff583aeababd5",
    },
    "research-english-academic-paper-writing-guide": {
        "version": "4.7.0", "skill": "research-english-academic-paper-writing-guide", "bin": "research-writing-skill-install",
        "display": "Research and English Academic Paper Writing Guide", "marketplace": "szsdt-research-writing",
        "description": "Full 13-lecture research and academic-writing reconstruction, both complete independent versions, 19 execution playbooks and evidence-integrity workflows.",
        "short": "Research planning and academic paper writing", "private": False,
        "base": "036777d921b528f922df5fb74a6bdb07ec8aafbd",
    },
}

def dump(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def baseline(root: Path, spec: dict) -> None:
    target = root / "docs/distribution-baseline.json"
    if target.exists():
        return
    paths = subprocess.check_output(["git", "ls-tree", "-rz", "--name-only", spec["base"]], cwd=root).split(b"\0")
    rows = []
    for raw in paths:
        if not raw:
            continue
        name = raw.decode("utf-8")
        data = subprocess.check_output(["git", "show", f"{spec['base']}:{name}"], cwd=root)
        rows.append({"path": name, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    dump(target, {"schema": "incremental-distribution-baseline/1", "base_commit": spec["base"], "files": rows})

def installation(spec: dict, repo: str) -> str:
    skill, version, executable = spec["skill"], spec["version"], spec["bin"]
    book = spec["private"]
    sizes = ("《学习观》提供完整版 Skill ZIP、完整插件 ZIP 和37份 Cloud Skill ZIP。完整版保留全部225 MB PDF原始字节分片、原始交付ZIP分片、350原扫描、83原图、Obsidian插件、字体及所有文字。Cloud每包保留全书350页文字、37单元正文和旧批注、本轮全部逐段带读与证据、官网来源、56份原始Markdown笔记和4场景；只附该单元扫描和原图。37包合起来覆盖全部350扫描和83原图。PDF、原ZIP及阅读器二进制资源继续完整保存在完整版，Cloud不是原始交付包的替代品。\n\nCloud不重压缩原PNG；大结构JSON仅做可逆gzip，脚本可直接读取，`platform_package.py expand-json` 可还原精确原字节。每包解压文件总量严格小于29,000,000字节，为Claude API的30 MB上限留出余量。当前API每请求最多20个Skill，代码容器无网络、不能临时安装软件包；按当前单元选择包，不能依赖运行时下载补齐缺图。\n" if book else "论文写作Skill ZIP保留原54文件基线对应的课程内容和全部双版本正文，13讲与19个playbook不删减。单Skill包及插件包的实测字节、文件清单与SHA-256见Release校验清单。\n")
    auth = ("《学习观》仓库保持私有。下载Release、Git克隆和社区安装器需要已有的GitHub账户访问权及Git凭证。不要把令牌写进命令行、ZIP或仓库。\n\n" if book else "")
    return f"""# {spec['display']}：安装与发布

当前发布层版本：{version}。原有课程、书籍和说明原字节完整保留；旧文档中的历史版本号表示相应内容的历史版本。

## 选择下载文件

下载 [GitHub Release](https://github.com/1235357/{repo}/releases/tag/v{version}) 的显式附件，而非GitHub自动生成的 Source code ZIP。

| 文件类型 | 解压后入口 | 用途 |
| --- | --- | --- |
| `*-skill-full.zip` | `{skill}/SKILL.md` | 支持Agent Skills的上传入口，或本地技能目录 |
| `*-plugin.zip` | `{repo}/plugin.json` 与 `.claude-plugin/plugin.json` | Agent Plugins / Claude Code 插件入口 |
| `read-xuexiguan-<unit>-cloud-skill.zip`（仅学习观） | 同名单根目录里的 `SKILL.md` | 有容量限制的云端技能导入入口 |

ZIP包含一个顶层文件夹；文件夹名与Skill YAML `name`相同。普通聊天附件可供读取，但不会因此自动注册为系统Skill；在ChatGPT支持Skill／插件的环境及Claude Custom Skills中使用相应导入入口。格式兼容、目录审核、账户功能和实际客户端导入是不同条件。本仓库离线验证包结构，不能据此宣称已经通过所有平台的商店审核或登录后上传。

{sizes}
{auth}## 本地完整安装

Node.js 18+，Python辅助阅读脚本需要3.9+；安装器不依赖第三方npm模块，也不联网或执行书内Obsidian插件。

```bash
git clone https://github.com/1235357/{repo}.git
cd {repo}
git checkout v{version}
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

`--target /path/to/skills`指定技能父目录；`--skill {skill}`选择技能；`--list`列出技能；`--dry-run`只预览；`--verify`核验安装目录的全部文件SHA-256、字节数及额外文件。完整复制包括原资产、隐藏文件和中文路径，安装回执另放在技能父目录的`.skill-installation`。

重复安装相同内容保持幂等。只有未被修改的受管理安装可以用`--upgrade`升级，升级前把全部旧文件与回执保存在`.skill-backups`。未管理的同名目录、本地新增／删改文件以及符号链接路径都拒绝覆盖；先保存并处理个人改动。

## npm／npx和社区目录

仓库含标准`package.json`和`bin`，可从Git来源运行；尚未在npm公共registry发布，也不需要把书籍二进制发布成npm依赖。

```bash
npx --yes --package=github:1235357/{repo}#v{version} {executable} --agent codex --project /absolute/path/to/project
```

完整大书在Git/npm缓存及最终目录各占空间；也可直接使用上一节的本地安装器。社区`skills` CLI支持多个Agent及已认证私有Git来源：

```bash
DISABLE_TELEMETRY=1 npx --yes skills@1.7.2 add 1235357/{repo} --skill {skill} --agent codex --agent claude-code --copy -y
```

社区CLI有自己的更新行为；上面的命令宜用于新的安装目录。要保留已有本地改动并取得完整备份，用本仓库安装器。直接URL下载在社区CLI有独立下载／解压／文件数预算，完整大书用Git来源。当前支持路径以版本1.7.2的维护方文档为据；其他Agent可由该CLI选择，无需修改原语料。

## 插件市场入口

可移植入口为根`plugin.json`（Agent Plugins 1.0.0）；`skills/`在插件根。Claude叠加入口位于`.claude-plugin/plugin.json`。仓库同时提供`.agents/plugins/marketplace.json`和`.claude-plugin/marketplace.json`，两者本地来源`./`均指仓库／插件根。

在支持的Claude Code客户端：

```text
/plugin marketplace add 1235357/{repo}
/plugin install {repo}@{spec['marketplace']}
```

ChatGPT／Codex支持的本地客户端可读取仓库市场清单；重启或刷新客户端后选择插件。公开Plugins Directory或组织工作区发布仍需相应账号、审核与权限，GitHub Release不等于已进入官方目录。本项目不添加无用途的MCP服务器、自动联网钩子或凭证接收工具。

Claude CLI在线`plugin validate`在本次环境被自动批准审核拒绝：该进程尝试向`api.anthropic.com`发送私有资料。因此没有重试或绕过，验证报告记录为blocked；已改做官方schema和本地包内容验证。

## 构建与核验

```bash
python tools/validate_distribution.py
node --test tools/test_installer.mjs
python tools/build_release.py --output /absolute/path/outside-repository --kind all
```

构建器仅取Git已跟踪文件，构建前必须提交或暂存新增发布文件。每份ZIP附逐文件大小、源路径和SHA-256；构建完成后流式重新读取每个ZIP条目并对比原字节。输出保存在仓库外，不将ZIP反复嵌入Skill。{(' `python tools/build_cloud_skills.py --output /absolute/path/outside-repository` 要求37单元、1055段本轮带读全部实际编译完成，再验证350/83的图像集合覆盖。' if book else '')}

来源与限制记录见仓库`docs/ecosystem/sources.json`；原始内容保留基线见`docs/distribution-baseline.json`。所有引用、阅读活动、视觉校对、结构验证和理解验收分别记录，发布机制不会替代实际理解。
"""

def configure(root: Path) -> None:
    repo = root.name
    if repo not in SPECS:
        raise ValueError(f"Unsupported repository: {repo}")
    spec = SPECS[repo]
    baseline(root, spec)
    url = f"https://github.com/1235357/{repo}"
    portable = {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "name": repo, "version": spec["version"], "description": spec["description"], "author": {"name": "1235357", "url": "https://github.com/1235357"}, "homepage": url, "repository": url, "keywords": ["agent-skills", "education", "source-preservation"], "extensions": {"com.openai": {"interface": {"displayName": spec["display"], "shortDescription": spec["short"], "longDescription": spec["description"], "developerName": "1235357", "category": "Productivity", "capabilities": ["Read", "Write"], "websiteURL": url, "defaultPrompt": [f"Use ${spec['skill']} to read the complete source before applying its reasoning."]}}}}
    if not spec["private"]:
        portable["license"] = "MIT"
    dump(root / "plugin.json", portable)
    claude = {key: value for key, value in portable.items() if key not in ("$schema", "extensions")}
    dump(root / ".claude-plugin/plugin.json", claude)
    dump(root / ".agents/plugins/marketplace.json", {"name": spec["marketplace"], "interface": {"displayName": spec["display"]}, "plugins": [{"name": repo, "source": {"source": "local", "path": "./"}, "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Productivity"}]})
    dump(root / ".claude-plugin/marketplace.json", {"name": spec["marketplace"], "owner": {"name": "1235357"}, "plugins": [{"name": repo, "source": "./", "description": spec["description"]}]})
    package = {"name": repo, "version": spec["version"], "description": spec["description"], "type": "module", "private": spec["private"], "bin": {spec["bin"]: "bin/install.mjs"}, "engines": {"node": ">=18"}, "files": ["skills", "bin", "tools", "docs", "plugin.json", ".claude-plugin", ".agents", "README.md", "CHANGELOG.md", "LICENSE", "NOTICE"], "repository": {"type": "git", "url": f"git+{url}.git"}, "homepage": url, "license": "UNLICENSED" if spec["private"] else "MIT", "scripts": {"test:installer": "node --test tools/test_installer.mjs", "validate:distribution": "python tools/validate_distribution.py"}}
    dump(root / "package.json", package)
    text = installation(spec, repo)
    (root / "docs/INSTALLATION.md").write_text(text, encoding="utf-8")
    (root / "skills" / spec["skill"] / "references/installation.md").write_text(text, encoding="utf-8")
    marker = f"## {spec['version']}：Skill／插件发布与完整安装"
    readme = root / "README.md"
    current = readme.read_bytes()
    if marker.encode() not in current:
        readme.write_bytes(current + f"\n\n{marker}\n\n原有内容完整保留。本次新增[安装和平台兼容说明](docs/INSTALLATION.md)、[正式发布附件](https://github.com/1235357/{repo}/releases/tag/v{spec['version']})、标准Skill ZIP、Agent Plugins／Claude插件清单、社区npx与离线字节校验安装器。发布层版本与旧正文里的历史版本号分别记录。\n".encode())
    changelog = root / "CHANGELOG.md"
    old = changelog.read_bytes() if changelog.exists() else b"# Changelog\n"
    note = f"## {spec['version']} — 2026-10-10"
    if note.encode() not in old:
        changelog.write_bytes(old + f"\n\n{note}\n\n- 增量新增单根Skill／插件ZIP构建与逐文件SHA-256验证，原有内容不删改。\n- 增加Agent Plugins 1.0.0、Claude叠加清单、两市场入口和Git来源npx安装。\n- 完整离线复制、幂等安装、保护个人修改、干净升级及全部旧文件备份。\n- 明确云端容量、网络、官方目录审核和实际客户端导入的适用范围。\n".encode())
    print(json.dumps({"repository": repo, "version": spec["version"], "skill": spec["skill"], "original_baseline": len(json.loads((root / 'docs/distribution-baseline.json').read_text())["files"])}, ensure_ascii=False))

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repositories", nargs="*", type=Path)
    args = parser.parse_args()
    for root in args.repositories or [HERE]:
        configure(root.resolve())

if __name__ == "__main__":
    main()
