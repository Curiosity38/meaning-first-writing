# Contributing / 贡献指南

Thanks for helping improve Meaning-First Writing. The primary contribution is a **better decision rule or example**, not a longer list of forbidden words.

## Good contributions

- An example where a generated draft answered a different question from the one asked.
- A before/after rewrite that preserves all facts but improves evidence, reasoning, or voice.
- A new task-specific test with success and failure signals (not a rigid model-answer template).
- A concrete correction to reference guidance about academic writing, uncertainty, or pragmatics.
- Documentation improvements and compatible install instructions.

## Contribution expectations

1. Explain what writing failure the change fixes.
2. Include a short input, a failing behavior, an improved behavior, and *why* the improvement matters.
3. Preserve evidence, author intent, terminology, quotes, numbers, citations, and necessary uncertainty.
4. Do not add fabricated case details or claim to have tested model behavior that was not tested.
5. Do not reproduce entire third-party essays or copyrighted screenshots. Cite source links and create your own paraphrases/examples.
6. Keep `SKILL.md` readable and place lengthy examples in `references/` or `tests/`.

## Check before opening a PR

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

These are **structural tests only**. When changing writing behavior, manually exercise relevant cases in [`tests/regression-prompts.md`](tests/regression-prompts.md) and document both good and bad examples from a real run.

## License and attribution

By contributing, you agree that your original contribution may be distributed under this repository's MIT license. Clearly identify external sources. Avoid adding private text, third-party PDFs, user data, or unsupported factual claims.
