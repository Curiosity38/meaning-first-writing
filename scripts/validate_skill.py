#!/usr/bin/env python3
"""Validate Agent Skills structure without third-party dependencies.

This is a structural check, not a claim that the skill improves writing quality.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED = (
    "SKILL.md", "README.md", "README.en.md", "DEPENDENCIES.md", "PUBLISHING.md",
    "LICENSE", "requirements.txt", "VERSION", "CHANGELOG.md", "SOURCE_INPUTS.json",
    "agents/openai.yaml", "tests/regression-prompts.md", "tests/EVALUATION.md",
    "scripts/validate_skill.py", "scripts/build_release.py",
    ".github/workflows/validate.yml",
)


def parse_frontmatter(contents: str) -> dict[str, str]:
    """Read the small set of standard fields we require from YAML frontmatter.

    This minimal parser deliberately supports only top-level scalars and indented
    multiline text; it is not a general-purpose YAML parser.
    """
    lines = contents.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter ('---').")
    try:
        stop = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter must have a closing '---'.") from exc
    front = lines[1:stop]
    out: dict[str, str] = {}
    i = 0
    while i < len(front):
        line = front[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line[:1].isspace():
            raise ValueError(f"Unexpected frontmatter indentation at line {i + 2}")
        match = re.fullmatch(r"([a-z][a-z0-9-]*):(?:\s*(.*))?", line)
        if not match:
            raise ValueError(f"Malformed frontmatter key at line {i + 2}: {line!r}")
        key, value = match.group(1), (match.group(2) or "")
        if key in out:
            raise ValueError(f"Duplicate field: {key}")
        if value in (">-", ">", "|-", "|"):
            i += 1
            block = []
            while i < len(front) and (front[i][:1].isspace() or not front[i].strip()):
                block.append(front[i].strip())
                i += 1
            out[key] = " ".join(s for s in block if s)
            continue
        out[key] = value.strip().strip('"\'')
        i += 1
    return out


def validate(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    errors = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        return ["Required SKILL.md is missing."]
    try:
        data = skill.read_text(encoding="utf-8")
    except UnicodeError:
        return ["SKILL.md must be UTF-8."]
    try:
        fm = parse_frontmatter(data)
    except ValueError as exc:
        return [str(exc)]
    name = fm.get("name", "")
    description = fm.get("description", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append("name must use lowercase ASCII letters, digits, hyphens, <=64 chars, no repeated/edge hyphens.")
    if name != root.name:
        errors.append(f"name {name!r} must match parent folder name {root.name!r}.")
    if not description.strip() or len(description) > 1024:
        errors.append(f"description must be 1..1024 characters (found {len(description)}).")
    if data.count("\n---\n") < 1:
        errors.append("Closing frontmatter delimiter missing.")
    if not data.split("\n---\n", 1)[-1].strip():
        errors.append("SKILL.md has no body after frontmatter.")
    referenced = sorted(set(re.findall(r"\b(?:references|tests)/[A-Za-z0-9_-]+\.md", data)))
    for rel in referenced:
        if not (root / rel).is_file():
            errors.append(f"SKILL.md references missing file: {rel}")
    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"Missing repository documentation: {rel}")
    # Verify local Markdown links in reader-facing docs; external URLs are not fetched.
    docs = sorted(root.glob("*.md"))
    for directory in ("references", "examples", "tests"):
        docs.extend(sorted((root / directory).rglob("*.md")))
    for doc in docs:
        rel = doc.relative_to(root).as_posix()
        if not doc.resolve().is_relative_to(root):
            errors.append(f"Document escapes repository: {rel}")
            continue
        try:
            content = doc.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"Document must be UTF-8: {rel}")
            continue
        if "YOUR_GITHUB_USERNAME" in content:
            errors.append(f"Unresolved repository placeholder in {rel}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme in ("http", "https", "mailto") or target.startswith("#"):
                continue
            local_path = (doc.parent / unquote(parsed.path)).resolve()
            if parsed.scheme or not local_path.is_relative_to(root) or not local_path.is_file():
                errors.append(f"Broken local Markdown link in {rel}: {target}")
    tests = root / "tests" / "regression-prompts.md"
    if not tests.is_file():
        errors.append("Missing manual regression test file.")
    else:
        ids = re.findall(r"^## Test (\d+)", tests.read_text(encoding="utf-8"), flags=re.M)
        if len(ids) < 20 or len(set(ids)) != len(ids):
            errors.append("Expected at least 20 unique semantic regression tasks.")
    version_file = root / "VERSION"
    if version_file.is_file():
        version = version_file.read_text(encoding="utf-8").strip()
        if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version):
            errors.append("VERSION must be a three-part release version.")
        changelog = root / "CHANGELOG.md"
        if changelog.is_file() and f"## [{version}]" not in changelog.read_text(encoding="utf-8"):
            errors.append("VERSION has no matching CHANGELOG entry.")
    ui = root / "agents/openai.yaml"
    if ui.is_file():
        text = ui.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            match = re.search(rf'^  {field}: "([^"\n]+)"$', text, flags=re.M)
            if not match:
                errors.append(f"UI metadata requires quoted {field}.")
            elif field == "short_description" and not 25 <= len(match[1]) <= 64:
                errors.append("UI short_description must contain 25..64 characters.")
            elif field == "default_prompt" and f"${name}" not in match[1]:
                errors.append("UI default_prompt must mention the skill explicitly.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Root skill directory")
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        print("FAIL: skill structure validation", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1
    print("PASS: skill frontmatter, naming, references, and package structure")
    print("NOTE: writing quality requires human review of tests/regression-prompts.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
