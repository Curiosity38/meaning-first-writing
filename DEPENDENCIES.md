# Dependencies and compatibility

The Markdown writing skill has **zero runtime dependencies**. It requires a host that reads Agent Skills instructions and local references. No API key, Python package, Node service, or other skill is required for basic editing. Source verification may need network tools when the user requests research.

| Operation | Requirement |
| --- | --- |
| Manual installation | Copy the whole skill directory to the host's supported location |
| Optional Skills CLI | Node.js, npx, Git, and any authentication required for the source repository |
| Validation, unit tests, ZIP build | Python 3.9+ standard library |
| GitHub publication | Authorized repository access |

The empty `requirements.txt` records that no pip dependencies are needed. Follow the [Skills CLI upstream requirements](https://github.com/vercel-labs/skills/blob/main/package.json) for its current release rather than assuming a fixed Node version.

The validator intentionally supports this package's top-level scalar and block-text frontmatter; it is not a general YAML parser. It checks files, links, frontmatter, version consistency, UI metadata conventions, and unresolved release placeholders. The tests exercise failures and deterministic packaging. They do not validate the truth of source articles, generated writing quality, or all clients' installation behavior. See [the evaluation protocol](tests/EVALUATION.md) for semantic assessment.
