# Meaning-First Writing

**先修论证，再修措辞。** 面向中英文改稿、起草和科研写作的 Agent Skill。

[English](README.en.md) · [技能入口](SKILL.md) · [使用示例](examples/README.md) · [更新记录](CHANGELOG.md)

## 它具体改善什么

把写作顺序放在 **任务 → 证据 → 论证 → 读者 → 语言**。处理没有判断的正确话、虚假对立、反复免责、无依据的强结论和不合身份的表达。保留作者观点、真实经历、数字、术语及必要的不确定性；不靠编造细节制造“人味”，也不承诺规避 AI 检测。

| 场景 | 工作方式 |
| --- | --- |
| 只改语病 | 保留结构与立场，不擅自重写论证 |
| 实质改稿 | 修正段落作用和推理关系，说明重要论点变化 |
| 科研写作 | 分开观察、解释、机制和意义；对齐图表、数据与结论 |
| 双语修订 | 保留否定、数量、条件、术语及证据强度 |
| 压缩或日常文本 | 保留关键意思，按读者关系调整语气 |

## 安装

此仓库包含一个技能：`meaning-first-writing`。私有仓库仅对有权限且已认证的用户可用，安装命令不会自动授予访问权限。

### Skills CLI

安装前按 [Skills CLI 官方说明](https://github.com/vercel-labs/skills)准备 Node.js 和 Git。版本要求以所用 CLI 版本为准。

```bash
# 先查看可发现的技能
npx skills add Curiosity38/meaning-first-writing --list

# 当前项目安装
npx skills add Curiosity38/meaning-first-writing -a codex

# 全局安装到指定客户端
npx skills add Curiosity38/meaning-first-writing -g -a codex -a claude-code

# 已下载本仓库：在根目录安装
npx skills add . -a codex
```

### 手动复制

将整个 `meaning-first-writing` 目录放到客户端的技能目录，保留 `SKILL.md`、`references/`、`tests/regression-prompts.md` 与 `agents/` 的相对位置。Codex 本地配置可能使用 `~/.codex/skills/` 或 `.agents/skills/` 等目录，以当前客户端实际发现位置为准；Claude Code 常用 `~/.claude/skills/`。重新加载会话后确认技能出现。不要只复制入口文件。

## 调用示例

```text
使用 $meaning-first-writing 修改下面的中文报告。
保留事实和观点，只删冗余、修复逻辑与不自然表达；直接输出成稿。
[原文]
```

```text
使用 $meaning-first-writing 重写 Results 并给中文译文。
以提供的表格和图注为依据，不重算，不增添文献；
区分测试集性能与机制推断，数值有冲突时明确指出。
[原文、表格、图注]
```

```text
只做英文语言润色，保留段序、引文、数字和结论强度。
发现科学判断有问题时单独指出，不悄悄改立场。
[原文]
```

原有 [18 组改写示范](references/before-after.md) 仅演示文字与逻辑，不是可移植到用户文本中的真实经历或研究数据。

## 内容组织

- [SKILL.md](SKILL.md)：精简入口、任务边界和按需阅读路由。
- [编辑协议](references/editing-protocol.md)：轻改/重写、材料矛盾、压缩与交付。
- [科研写作](references/scientific-writing.md)：论文各节、图注、基金申请、统计和来源约束。
- [双语写作](references/bilingual-writing.md)：术语、否定、数量与证据强度对齐。
- [故障修复](references/writing-failures.md)、[语用](references/pragmatics.md)、[交付检查](references/review-gates.md)：按问题读取。
- [来源分析](references/diagnosis-from-pdf.md)：继承的来源整理；原 PDF 未随包提供，页码未独立核验。
- [语义回归任务](tests/regression-prompts.md) 与 [评估方法](tests/EVALUATION.md)：人工/模型评阅，不能以结构测试代替。
- `agents/openai.yaml`：Codex 展示信息；`scripts/`：校验与可复现打包。

## 验证与打包

写作本身没有软件包依赖；维护脚本使用 Python 3.9+ 标准库，zero runtime dependencies。它们只验证本仓库约定，不是通用 YAML 或完整 Agent Skills 规范验证器。

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/build_release.py
```

最后一条命令在 `dist/` 生成带顶层技能目录的 ZIP、逐文件 SHA-256 清单和 ZIP 校验和。它不会安装技能、调用模型或上传内容。GitHub Actions 在 Linux / Windows 上执行结构测试与打包；语义质量需实际输出和评阅记录。

发布步骤见 [PUBLISHING.md](PUBLISHING.md)，依赖与支持范围见 [DEPENDENCIES.md](DEPENDENCIES.md)。

## 来源与许可

以用户提供的 v1.0.0 GitHub 包为基线，合并检查独立入口、科研扩展及早期技能包；文件摘要见 [SOURCE_INPUTS.json](SOURCE_INPUTS.json)。本次保留原有 MIT 许可与贡献者署名。

旧包将最初灵感归于 [《应试智能》](https://xhslink.cn/o/34k4yIQD5U4) 和 [《应试智能（下）》](https://xhslink.cn/o/5VmTsODLAwB)。本版本没有取得原 PDF；相关页码和归属作为继承记录保留，不声称独立核验。原 PDF、截图与第三方文章不随仓库分发，也不包含在 MIT 授权范围内。

包结构参照 [Agent Skills specification](https://agentskills.io/specification)。旧版还列出 [blader/humanizer](https://github.com/blader/humanizer)、[softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit)、[ai-zixun/humanizer-zh](https://github.com/ai-zixun/humanizer-zh) 为组织与写法参考；这些不是运行依赖。本项目不将其他技能概括成统一的能力边界。

贡献请见 [CONTRIBUTING.md](CONTRIBUTING.md)。
