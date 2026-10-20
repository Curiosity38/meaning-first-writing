# Meaning-First Writing

**Fix the reasoning before polishing the wording. Help the text answer the actual question.**

A writing skill for Chinese and English, covering planning, drafting, substantive editing, and final polishing. It examines what the reader learns, how evidence supports a judgment, and whether the prose fits its audience. A dedicated **Scientific Writing module** supports research manuscripts and proposals.

[简体中文](README.md) · [Install and use](#install-and-use) · [Full skill](SKILL.md) · [Scientific Writing](references/scientific-writing.md) · [Worked examples](examples/README.md)

## AI wrote 3,000 words. What did it actually answer?

Ask an AI: “Should an undergraduate invest more time in research or academic competitions?”

A familiar answer might be:

> Research and competitions each have advantages. Students should consider their interests, future plans, and available time, as both can develop a broad range of abilities.

The prose is fluent and difficult to dispute. Yet replace “research and competitions” with “graduate study and employment,” and most of it still works. The reader has not learned what to compare, how to choose, or which conditions would change the answer.

The same problem appears in longer texts. An Introduction spends several paragraphs praising a field before stating its scientific problem. Results repeatedly claim “significant improvements” while barely explaining relationships in the data. Commentary lists every position and possibility without reaching an evidence-based judgment.

**Fluent prose and a complete structure can still leave the reader's main question unanswered.**

Meaning-First Writing starts by asking what the text needs to answer, what each paragraph adds, and which facts and reasoning support its conclusions.

## Give the reader a basis for comparison

For the research-versus-competitions question, a useful response could begin:

> If the goal is research training, compare the opportunities to formulate questions independently, design experiments, analyze failures, and revise a research plan. A project that involves students throughout this process will generally provide deeper research training than one limited to repetitive operations. The choice depends on the work students actually undertake and the feedback they receive.

This illustrative rewrite keeps the original question and gives the reader criteria for evaluating specific opportunities.

The same approach applies to reports, commentary, and applications. “I learned a lot” needs an account of what was learned. “The proposal is better” needs a comparison and a criterion. “The result is important” needs an explanation of what it changes.

## How the skill revises a text

First establish the task, audience, and available material; then examine the argument and edit the language. The requested scope determines the depth of revision: proofreading preserves the structure, while a substantive rewrite can reorganize paragraphs and reasoning.

1. **Answer the original question.** Identify the judgment or explanation the text should deliver, and avoid replacing a specific problem with a broad statement of values.
2. **Examine content and evidence.** Merge repeated points and explain how facts support conclusions. Check existing material for support omitted from the draft; identify genuinely missing evidence or narrow the claim when the material is insufficient.
3. **Repair logic and audience fit.** Distinguish causation, conditions, contrasts, and parallel ideas; weigh positions by their evidence; choose a voice suited to the author, reader, and purpose, reducing misplaced judgment and lecturing.
4. **Remove repetitive self-justification.** Once claims and evidence are clear, remove irrelevant audit commentary, imagined rebuttals, and self-criticism. State the object, finding, and conditions directly; place methodological and internal process details where readers need them; describe data and code resources that actually exist.
5. **Edit the prose.** Reduce mechanical transitions, repetitive patterns, empty introductions, and vague abstractions while retaining useful rhetoric, technical terms, and the author's voice.

Words such as “may,” “perhaps,” and “cannot rule out” need to be judged by their function. Remove repetitive caveats that do not affect the conclusion. Retain qualifications that express real uncertainty, experimental conditions, or the limits of an inference.

The skill supports drafting, substantive editing, compression, argument review, and bilingual revision. It preserves facts, the relative weight of the author's claims, numbers, citations, and necessary conditions without inventing experience, data, or references. Apply the rules by genre: retain installation commands in READMEs, concrete plans in proposals, and responses to actual objections in reviewer replies. See the [failure guide](references/writing-failures.md) and [review checks](references/review-gates.md) for details.

## Scientific Writing: connect the question, data, and conclusion

The scientific module covers papers, research plans, grant proposals, and methods reports. It distinguishes **observation, interpretation, mechanism, and implications**, then examines the connections between them. Writing choices follow the discipline, venue, and available evidence.

Preserve numbers, confidence intervals, independent sample counts, null and contradictory results, prespecified criteria, and required disclosures. Explain design and reproducibility in Methods and report findings in Results. For example, when the supplied material confirms that the test set was held out from model selection, state that design fact directly without appending verification assurances to every result. Retain conditions that affect a particular finding where that finding is interpreted.

### Introduction: state the specific problem

Explain what previous work has resolved, what difficulty remains, and where the present study begins. Replace repeated statements about a field's importance with a concrete research object, methodological limitation, or unanswered question.

For example, an introduction about optical prediction across spheres, shells, and rods can begin with their different geometric parameter definitions, then explain the motivation for shared electromagnetic response variables. This identifies the modeling problem more directly than a broad claim about the potential of nanomaterials.

### Results: report findings against the data

“Model performance improved significantly” needs a comparator, evaluation conditions, the size of the change, and supporting results. A claim of statistical significance also needs an appropriate statistical basis.

For **illustrative data** in which MAE falls from 0.13 to 0.09 on a fixed test set, a concrete statement is:

> On this test set, MAE decreased from 0.13 to 0.09, an absolute reduction of 0.04 and a relative reduction of approximately 30.8%.

This reports what the supplied numbers support. A mechanistic explanation needs further reasoning about which observations support it and whether alternative explanations can be distinguished. Better predictive performance alone does not establish a mechanism.

### Discussion: explain what has been learned

Discuss how the findings address the original problem, which explanations gained support, and which conditions remain untested. Further research should focus on specific tests that distinguish explanations or extend the evaluated scope. Avoid merely repeating numerical results or ending with a generic claim of broad impact.

### Other scientific writing tasks

| Section or task | Main check |
| --- | --- |
| Abstract | Does it convey the problem, approach, key result, and supported conclusion within the word limit? |
| Methods | Are the objects, parameters, data splits, replicates, and statistical methods sufficient for understanding and reproduction? |
| Figure captions | Are panels, comparison conditions, metrics, colors, uncertainty, and sample counts clear? |
| Grants and research plans | Are the question, methodological difference, rationale, and milestones specific and testable? |
| Chinese and English prose | Do terminology, numbers, negation, conditions, and claim strength agree? |
| Whole-manuscript revision | Do the abstract, body, captions, and citations refer to consistent facts and evidence? |

See [Scientific Writing](references/scientific-writing.md) and [bilingual revision guidance](references/bilingual-writing.md). The reference guides are primarily Chinese, with English examples.

## Relationship to Humanizer skills

Humanizer projects offer useful approaches to recurring AI vocabulary, fixed sentence patterns, repetitive wording, and mechanical language. Some also address structure, factual fidelity, and individual voice.

Meaning-First Writing draws on these ideas and on the essays *应试智能* and *应试智能（下）*, particularly their discussion of defensive writing, uninformative truths, context, and arguments that go nowhere. Its emphasis is on content and reasoning: establish a clear question, traceable evidence, and paragraphs that advance understanding, then refine the prose.

It can complement other writing tools. The aim is better writing; AI-detector scores are not its evaluation criterion.

## Install and use

### Codex / Claude Code

Install with the [Skills CLI](https://github.com/vercel-labs/skills). Node.js, npx, and Git are needed; consult the upstream documentation for version requirements.

```bash
# Global installation for Codex
npx skills add Curiosity38/meaning-first-writing -g -a codex

# Global installation for Claude Code
npx skills add Curiosity38/meaning-first-writing -g -a claude-code

# Discover available skills without installing
npx skills add Curiosity38/meaning-first-writing --list

# From a downloaded checkout: install into the current project
npx skills add . -a codex
```

Alternatively, copy the complete `meaning-first-writing` directory into your client's supported skills location, preserving relative paths between the entrypoint and its resources. Follow the client's instructions for discovery and reloading. See [dependencies](DEPENDENCIES.md).

### Use the files as writing guidance in a chat tool

In tools such as ChatGPT or Doubao, provide [SKILL.md](SKILL.md) as the current mode's file-reading capabilities permit. For research writing, also provide [scientific-writing.md](references/scientific-writing.md), and explicitly ask the model to apply the guidance to your text. Supply any additional references needed for the task, or paste the relevant material.

Providing files as writing guidance differs from a client's automatic discovery and loading of an installed skill. The available workflow depends on the product version and mode.

### Example prompts

**Revise a draft**

```text
Use meaning-first-writing to revise the text below.
Preserve the facts, claims, and author's voice. Check whether it answers
its original question, merge repetition, and repair reasoning and phrasing.
Deliver the complete revised text.

[draft]
```

**Edit scientific Results**

```text
Apply the scientific writing guidance in meaning-first-writing to these Results.
Use the supplied text, tables, and captions to explain comparisons, findings,
and conclusions. Distinguish observations from mechanistic inferences.
Identify evidence gaps without inventing data or citations.

[draft, tables, and captions]
```

**Revise and translate an abstract**

```text
Use meaning-first-writing to polish this English abstract and provide
its Chinese translation. Preserve terms, numbers, citations, and claim strength.
Do not turn suggest or consistent with into prove.

[abstract]
```

**Draft from source material**

```text
Use meaning-first-writing to draft a report for my project team from the
material below. Identify the question the report must answer, then organize
the evidence and analysis. Use only the available facts and identify any
missing information that would change the conclusion.

[material, purpose, and length]
```

See [16 worked examples for common writing tasks](examples/README.md).

## Repository contents and maintenance

[SKILL.md](SKILL.md) routes to task-specific references: [editing](references/editing-protocol.md), [scientific writing](references/scientific-writing.md), [bilingual consistency](references/bilingual-writing.md), [failure diagnosis](references/writing-failures.md), [pragmatics](references/pragmatics.md), and [review checks](references/review-gates.md).

The skill has zero runtime package dependencies. Maintainers can validate and build it with Python 3.9+ and its standard library:

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/build_release.py
```

The build writes a ZIP, file manifest, and SHA-256 checksum to `dist/`. GitHub Actions runs structural checks and packaging. Writing behavior is evaluated separately through [28 semantic regression tasks](tests/regression-prompts.md) and the [evaluation protocol](tests/EVALUATION.md). Passing structural tests does not establish writing quality.

[Contributing](CONTRIBUTING.md) · [Publishing](PUBLISHING.md) · [Changelog](CHANGELOG.md)

## Sources and license

The writing approach was inspired by the Xiaohongshu essays [应试智能](https://xhslink.cn/o/34k4yIQD5U4) and [应试智能（下）](https://xhslink.cn/o/5VmTsODLAwB). Organizational and writing references include [blader/humanizer](https://github.com/blader/humanizer), [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit), and [ai-zixun/humanizer-zh](https://github.com/ai-zixun/humanizer-zh). Some guidance is adapted from a user-supplied local expansion of Anti-Defensive Writing identifying [Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) as its upstream; the MIT copyright notice is retained. Packaging follows the [Agent Skills specification](https://agentskills.io/specification).

Third-party source articles and screenshots are not distributed. Input provenance is recorded in [SOURCE_INPUTS.json](SOURCE_INPUTS.json).

Original project content is distributed under the [MIT License](LICENSE). Rights to third-party articles and external resources remain with their respective owners.
