# Meaning-First Writing

**Fix the reasoning before polishing the wording.** A Chinese and English writing skill that preserves evidence, authorial intent, and voice.

[简体中文](README.md) · [Skill](SKILL.md) · [Examples](examples/README.md) · [Changelog](CHANGELOG.md)

## What it does

Work from task to evidence, reasoning, reader, and language. Repair empty claims, false contrasts, irrelevant caveats, and mismatched tone. Preserve facts, numbers, citations, uncertainty, and the author's priorities. Copyediting stays within its requested scope; substantive editing may reorganize arguments without inventing evidence. This skill makes no AI-detector claims.

Scientific writing guidance separates observation, interpretation, mechanism, and implications. Bilingual guidance preserves negation, scope, quantities, and epistemic strength. The operational guides are primarily Chinese and include English examples; both output languages are supported.

## Install

This repository exposes one skill, `meaning-first-writing`. A private repository requires authenticated access; the commands do not grant repository permissions. See the [Skills CLI documentation](https://github.com/vercel-labs/skills) for current Node.js and Git requirements.

```bash
npx skills add Curiosity38/meaning-first-writing --list
npx skills add Curiosity38/meaning-first-writing -a codex
npx skills add Curiosity38/meaning-first-writing -g -a codex -a claude-code
# From a local checkout:
npx skills add . -a codex
```

Alternatively, copy the entire directory into your client's discovered skills location. Preserve the relative paths of `SKILL.md`, `references/`, `tests/regression-prompts.md`, and `agents/`. Codex configurations may use `~/.codex/skills/` or `.agents/skills/`; use the path supported by your installation. Claude Code commonly uses `~/.claude/skills/`. Reload the session and confirm discovery. Do not copy only the entrypoint.

## Use

```text
Use $meaning-first-writing to revise the passage below.
Preserve all facts, claims, citations, and necessary uncertainty.
Fix reasoning and audience fit, then deliver the complete revised text.
[paste passage]
```

```text
Use $meaning-first-writing to edit my Results and provide a Chinese translation.
Use only the supplied tables and captions; do not rerun analyses.
Separate measured results from mechanisms and flag conflicting values.
[paste draft and source material]
```

For language-only editing, explicitly request that paragraph order and claims remain unchanged. The skill should flag substantive problems separately.

## Contents

The concise [entrypoint](SKILL.md) routes to [editing](references/editing-protocol.md), [scientific writing](references/scientific-writing.md), [bilingual consistency](references/bilingual-writing.md), [failure diagnosis](references/writing-failures.md), [pragmatics](references/pragmatics.md), and [review checks](references/review-gates.md). [Before/after examples](references/before-after.md) are demonstrations, not verified research or personal experience.

`agents/openai.yaml` supplies Codex UI metadata. [Regression prompts](tests/regression-prompts.md) and an [evaluation protocol](tests/EVALUATION.md) support behavioral review.

## Validate and package

The writing skill has zero runtime dependencies. Maintenance scripts require Python 3.9+ and use only its standard library.

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/build_release.py
```

The build writes a reproducible ZIP, per-file SHA-256 manifest, and ZIP checksum to `dist/`. It does not install, invoke a model, or publish anything. CI runs structural checks and packaging on Linux and Windows. These checks enforce this repository's conventions, not arbitrary YAML or the entire Agent Skills specification. They do not certify writing quality.

See [dependencies](DEPENDENCIES.md), [publishing](PUBLISHING.md), and [contribution guidance](CONTRIBUTING.md).

## Provenance and license

Version 1.1.0 builds on the user-supplied v1.0.0 repository and companion files recorded in [SOURCE_INPUTS.json](SOURCE_INPUTS.json). The existing [MIT license](LICENSE) and contributor attribution are retained.

The inherited source critique credits [应试智能](https://xhslink.cn/o/34k4yIQD5U4) and [应试智能（下）](https://xhslink.cn/o/5VmTsODLAwB). The underlying PDF was not available during this revision. Page references and attribution remain historical notes, not independently verified citations. Third-party articles and screenshots are not distributed or relicensed.

Packaging follows the [Agent Skills specification](https://agentskills.io/specification). The original package also credited [blader/humanizer](https://github.com/blader/humanizer), [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit), and [ai-zixun/humanizer-zh](https://github.com/ai-zixun/humanizer-zh) as organizational inspirations, not runtime dependencies.
