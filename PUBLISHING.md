# Publishing

Target repository: `Curiosity38/meaning-first-writing`. Version is read from `VERSION`; keep the corresponding entry in `CHANGELOG.md`.

## Prepare

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/build_release.py
```

Review the exact files being uploaded. The release builder includes maintained text sources and excludes `.git`, caches, `dist`, original attachments, credentials, and local environment files. A structural pass is not evidence of improved prose; record actual behavioral evaluations separately using [tests/EVALUATION.md](tests/EVALUATION.md).

## Upload

Use an authenticated account authorized for the target repository. When using a connector, confirm its account before writing; local Git credentials may belong to another account. If the repository already contains work, fetch its current head and preserve existing content. Do not force-push or silently replace a populated repository.

The repository should be created only once. Default to private unless its owner requests public visibility. Upload the validated source as a commit, then verify remote file contents and the workflow outcome. If local source and remote commit histories differ because a connector created the commit, do not claim they are synchronized until reconciled.

## Optional release

Tag the verified commit as `v1.2.0` and attach the ZIP, manifest and checksum from `dist/` when preparing a GitHub release. Do not claim a tag or release exists without checking it remotely. No publication automation runs merely because the skill is installed.

## Discovery

With repository access configured:

```bash
npx skills add Curiosity38/meaning-first-writing --list
```

Expected discovery: one skill named `meaning-first-writing`. Private repository access and client installation still require the user's own authorization. Test installation into an isolated temporary location rather than overwriting an existing user skill.
