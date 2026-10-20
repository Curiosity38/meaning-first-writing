# Worked examples / 对照示例

These examples are **illustrations only**, not claims about published datasets or actual experiments. For 18 detailed examples see [`references/before-after.md`](../references/before-after.md).

## Example 1 — The claim is empty / 平凡真命题

**Input**

> 科研很重要，竞赛也很重要。本科生应该结合自身情况，综合提升能力。

**Improved**

> 如果目标是学习如何提出未知问题、设计验证方案并处理失败数据，应优先考虑能让学生独立承担这些环节的项目。科研和竞赛都可能提供这样的机会；决定训练价值的是具体任务，而不是活动名称。

**Why it improves the argument**: The second version supplies the *decision criterion* missing from the first. It does not invent comparative statistics or replace the user's question with an inspirational message.

## Example 2 — Scientific evidence boundary / 科研证据范围

**Input**

> 我们的新模型具有颠覆性，证明了统一描述符可以解释全部纳米结构的光学规律。

**Improved, given only a cross-structure prediction comparison**

> 在本文测试的纳米结构及参数范围内，统一描述符支持在相同输入表征下进行跨结构光谱预测。该比较证明了这种表征对预测任务的有效性，但不能仅由预测精度推导出唯一的电磁机制。

**Why**: Predictive evidence supports a bounded performance claim; a mechanism claim requires additional tests. This example does *not* assert a real performance result.

## Example 3 — Context-aware tone / 按身份确定语体

**Known facts**: A university student helped design posters for a campus event. No specific achievement metrics were provided.

**Bad**

> 本人聚焦校园品牌全链路传播，以用户触点优化为抓手，构建视觉资源资产化闭环。

**Improved**

> 在校园活动中，我参与了海报设计与排版。这个过程让我需要考虑怎样安排活动信息，使观众能更快找到时间、地点和参与方式。

**Why**: Keeps a credible student voice, uses only the known activity, and describes the *type* of design decision without inventing results or feedback.

## Suggested evaluation

Ask the agent to revise the same prompt **with and without** this skill. Judge whether the edited version (1) answers the asked question, (2) adds concrete and defensible information, (3) preserves factual boundaries and the user's stance, and (4) fits the audience. Do not reduce the assessment to banned-phrase counts.
