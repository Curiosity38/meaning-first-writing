# Meaning-First Writing

**先修论证，再修措辞。让文章回答真正的问题。**

一个面向中文和英文的写作 Skill，覆盖初稿构思、文章撰写、改稿与后期润色。它关注文章有没有提供有用的信息、证据能否支撑判断，以及表达是否适合读者，并提供专门的 **Scientific Writing 科研写作模块**。

[English](README.en.md) · [安装与使用](#安装与使用) · [完整 Skill](SKILL.md) · [科研写作模块](references/scientific-writing.md) · [改写示例](examples/README.md)

## AI 写了 3000 字，到底回答了什么？

问 AI：“本科生做科研和参加竞赛，哪个更值得投入？”

一种常见的回答是：

> 科研和竞赛各有优势，应该根据个人兴趣、未来规划和时间安排综合考虑，两者都有助于提升综合能力。

这段话读起来很顺，也很难挑出明显错误。但把“科研和竞赛”换成“考研和就业”，几乎还能原封不动地用。读者仍然不知道该比较什么、依据什么选择，以及哪些条件会改变结论。

长文也会出现同样的问题：Introduction 花几百字强调研究方向重要，科学问题却迟迟没有出现；Results 反复说“显著提高”“具有优越性能”，对数据关系的解释很少；评论列出各种立场和可能性，最后没有形成有依据的判断。

**语言流畅、结构完整的文章，也可能没有回答读者最关心的问题。**

Meaning-First Writing 从这里开始检查文本：这篇文章要回答什么？每一段让读者多知道了什么？结论由哪些事实和推理支持？

## 有了比较标准，分析才有依据

仍以前面的科研与竞赛为例，如果目标是训练科研能力，可以这样展开：

> 先看学生有没有机会独立提出问题、设计实验、分析失败原因，并持续修改研究方案。能够完整参与这些过程的项目，通常比只负责重复操作的项目提供更深入的科研训练。选择科研还是竞赛，要看实际承担的工作，以及能得到什么反馈。

这段示范保留了原来的比较问题，同时给出了读者可以用来判断具体项目的标准。

同样的检查也适用于报告、评论和申请材料。说“收获很大”时，需要交代学到了什么；说“方案更好”时，需要说明比较对象和标准；说“结果很重要”时，需要解释它改变了什么认识。

## 它怎样修改一篇文章

写作时先明确任务、读者和可用材料，再检查论证，最后处理语言。修改深度服从你的要求：只改语病就保留原有结构，需要重写时再调整段落和论证顺序。

1. **先回答原问题。** 找到文章需要交付的判断或解释，避免把具体问题换成宽泛的价值宣言。
2. **检查内容和证据。** 合并反复表达同一观点的段落，说明事实与结论之间的联系。缺少证据时指出需要补充什么，或缩小主张的范围。
3. **处理逻辑与语境。** 分清并列、因果、条件和对立关系；按证据判断各方说法；根据作者身份、读者和用途选择合适的语气。
4. **修整语言。** 减少机械转折、重复排比、空泛引入和抽象词汇，保留有作用的修辞、专业术语与作者声音。

对于“可能”“也许”“不能排除”等表达，要看它们承担什么作用。与结论无关的反复免责可以删掉；表达真实不确定性、实验条件和推断范围的限定应当保留。让判断更清楚，也包括说清楚判断成立的条件。

这套规则适用于从零起草、实质改稿、压缩、论证审阅和中英双语修订。写作过程中保留原有事实、观点权重、数字、引文与必要条件，不补造经历、数据或文献。

## Scientific Writing：让科学问题、数据和结论接得上

科研模块面向论文、研究计划、基金申请和方法学报告。它要求把 **观察、解释、机制与意义** 分开，再说明它们之间的联系。写作方式随学科、期刊和实际证据调整。

### Introduction：把具体问题提出来

先讲清已有研究解决了什么、目前还面临什么困难，以及本工作准备从哪里入手。反复强调“研究意义重大”的段落，应当落实为具体对象、方法局限和未解决的问题。

例如，讨论球、壳和棒的跨结构光学预测时，可以从不同结构的几何参数定义不同这一困难切入，再说明为何考虑使用共通的电磁响应变量。这比铺陈“纳米材料具有广泛应用前景”更接近研究要解决的任务。

### Results：对照数据写出发现

一句“模型性能显著提升”，至少需要交代和什么方法比较、在哪些条件下比较、指标变化了多少，以及哪些结果支持这个结论。涉及统计显著性时，还需要相应的检验依据。

例如，在一组**演示数据**中，固定测试集上的 MAE 从 0.13 降到 0.09，可以写成：

> 在该测试集上，MAE 由 0.13 降至 0.09，绝对下降 0.04，相对下降约 30.8%。

这一句报告了已给数字支持的变化。进一步讨论机制时，还需说明哪些观察支持该解释、能否区分其他解释；性能改善本身不足以完成机制归因。

### Discussion：说明结果增加了什么认识

讨论这些结果如何回应最初的问题、哪些解释得到支持，以及哪些条件仍未被检验。下一步研究应围绕可以区分解释或拓展适用范围的具体问题展开，避免重复结果数字，或只用“具有重要理论意义和广阔应用前景”收尾。

### 其他科研写作任务

| 部分 | 重点检查 |
| --- | --- |
| Abstract | 是否用有限篇幅交代问题、方法、关键结果和可支持的结论 |
| Methods | 对象、参数、数据划分、重复次数和统计方法是否足以理解与复现 |
| Figure captions | 面板、比较条件、指标、颜色、误差与样本数是否说明清楚 |
| 基金与研究计划 | 科学问题、方法差异、研究依据和阶段目标是否具体、可检验 |
| 中英文表达 | 术语、数字、否定关系、条件与结论强度是否一致 |
| 全文修订 | 摘要、正文、图注和引用是否对应同一组事实与证据 |

完整规则见 [Scientific Writing](references/scientific-writing.md)，双语修订细节见 [中英双语写作](references/bilingual-writing.md)。

## 与 Humanizer 的关系

Humanizer 类项目在识别 AI 高频词、固定句式、重复表达和机械化语言方面提供了很多思路，有些也关注内容结构、事实保真和个人文风。

Meaning-First Writing 借鉴了这些思路，并结合《应试智能》中关于防御性写作、平凡真命题、语境理解和论证空转的分析，把重点放在内容与论证上：先让文章有明确的问题、可追溯的证据和能推进理解的段落，再调整表达。

它与其他写作工具的使用方式可以互补。目标是改善文章本身，不以 AI 检测分数作为评价标准。

## 安装与使用

### Codex / Claude Code

使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装，需要 Node.js、npx 和 Git；具体版本要求见官方说明。

```bash
# 全局安装到 Codex
npx skills add Curiosity38/meaning-first-writing -g -a codex

# 全局安装到 Claude Code
npx skills add Curiosity38/meaning-first-writing -g -a claude-code

# 仅查看仓库中的技能
npx skills add Curiosity38/meaning-first-writing --list

# 已下载仓库：在仓库根目录安装到当前项目
npx skills add . -a codex
```

也可以将整个 `meaning-first-writing` 目录复制到客户端的技能目录，保留入口、参考文件和其他资源之间的相对路径。安装位置及重新加载方式以所用客户端为准。依赖说明见 [DEPENDENCIES.md](DEPENDENCIES.md)。

### 在对话工具中作为写作参考

在 ChatGPT、豆包等对话工具中使用时，可按当前模式的文件读取能力提供 [SKILL.md](SKILL.md)，科研任务再提供 [scientific-writing.md](references/scientific-writing.md)，并明确要求依据这些规则处理原文。若涉及其他参考文件，也需要一并提供或粘贴相关内容。

提供文件作为写作参考，与客户端自动发现、加载完整 Skill 的安装机制不同；具体可用方式取决于产品版本和当前模式。

### 直接可用的提示词

**改稿与润色**

```text
使用 meaning-first-writing 修改下面的文章。
保留事实、观点和作者语气，检查是否回答原问题，
合并重复内容，修复论证与不自然表达，直接输出完整修改稿。

[原文]
```

**科研论文**

```text
按 meaning-first-writing 的科研写作规则修改下面的 Results。
以我提供的表格、图注和原文为依据，讲清比较对象、实际发现和结论。
区分直接观察与机制推断；缺少证据时指出具体缺口，不编造数据或引用。

[原文、表格和图注]
```

**中英双语修订**

```text
使用 meaning-first-writing 润色英文摘要，并提供中文译文。
保留术语、数字、引用和结论强度，不把 suggest 或 consistent with 改成 prove。

[英文摘要]
```

**从材料起草**

```text
使用 meaning-first-writing，根据下面的材料写一份面向项目组的报告。
先明确报告需要回答的问题，再组织证据与分析。
只使用已有事实；信息不足时说明哪项缺口会影响结论。

[材料、用途与篇幅要求]
```

更多示例见 [12 个常用场景对照示例](examples/README.md)。

## 仓库内容与维护

[SKILL.md](SKILL.md) 是入口，按任务读取参考资料。主要资源包括 [编辑协议](references/editing-protocol.md)、[科研写作](references/scientific-writing.md)、[双语写作](references/bilingual-writing.md)、[故障修复](references/writing-failures.md)、[语用与读者](references/pragmatics.md) 及 [交付检查](references/review-gates.md)。

技能本身没有运行时软件包依赖。维护者可使用 Python 3.9+ 标准库校验和打包：

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/build_release.py
```

打包输出位于 `dist/`，包括 ZIP、文件清单与 SHA-256 校验和。GitHub Actions 运行结构检查和打包；实际写作效果通过 [20 组语义回归任务](tests/regression-prompts.md) 与 [评估方法](tests/EVALUATION.md) 单独评阅。结构测试通过不代表已验证写作效果。

[贡献指南](CONTRIBUTING.md) · [发布说明](PUBLISHING.md) · [更新记录](CHANGELOG.md)

## 来源与许可

写作思路受到小红书文章 [《应试智能》](https://xhslink.cn/o/34k4yIQD5U4) 和 [《应试智能（下）》](https://xhslink.cn/o/5VmTsODLAwB) 的启发，并参考了 [blader/humanizer](https://github.com/blader/humanizer)、[softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit)、[ai-zixun/humanizer-zh](https://github.com/ai-zixun/humanizer-zh) 等项目的组织与写作思路。包结构参照 [Agent Skills specification](https://agentskills.io/specification)。

第三方文章原文与截图不随包分发。版本输入记录见 [SOURCE_INPUTS.json](SOURCE_INPUTS.json)。

本项目原创内容采用 [MIT License](LICENSE)。第三方文章和外部资源的权利归各自权利人所有。
