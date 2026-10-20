#!/usr/bin/env python3
"""Build a deterministic source ZIP and SHA-256 manifests; never publish."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import zipfile

from validate_skill import ROOT, validate

ROOT_FILES = {
    "SKILL.md", "README.md", "README.en.md", "DEPENDENCIES.md", "PUBLISHING.md",
    "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE", "VERSION", "requirements.txt",
    "SOURCE_INPUTS.json", ".gitignore", ".gitattributes",
}
DIRECTORY_SUFFIXES = {
    "references": {".md"}, "examples": {".md"}, "tests": {".md", ".py"},
    "scripts": {".py"}, "agents": {".yaml"}, ".github/workflows": {".yml", ".yaml"},
}


def source_files(root: Path) -> list[Path]:
    """Include maintained text sources only; reject symlinks and path escapes."""
    root = root.resolve()
    files = [root / name for name in ROOT_FILES if (root / name).is_file()]
    for dirname, suffixes in DIRECTORY_SUFFIXES.items():
        folder = root / dirname
        for part in (folder, *folder.parents):
            if part == root:
                break
            if part.is_symlink():
                raise ValueError(f"Symlink source directory: {part}")
        if folder.exists():
            for path in folder.rglob("*"):
                if path.is_symlink():
                    raise ValueError(f"Symlink in sources: {path}")
                if path.is_file() and path.suffix in suffixes and "__pycache__" not in path.parts:
                    files.append(path)
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"Source escapes repository: {path}")
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def build(root: Path = ROOT, output: Path = None) -> dict:
    root = root.resolve()
    files = source_files(root)
    errors = validate(root)
    if errors:
        raise ValueError("\n".join(errors))
    output = (output or root / "dist").resolve()
    output.mkdir(parents=True, exist_ok=True)
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    stem = f"meaning-first-writing-v{version}"
    archive = output / f"{stem}.zip"
    manifest_path = output / f"{stem}.manifest.json"
    checksum_path = output / f"{stem}.sha256"
    payload = {p.relative_to(root).as_posix(): p.read_bytes() for p in files}
    if any(p.resolve() in (archive, manifest_path, checksum_path) for p in files):
        raise ValueError("Output would overwrite a source file.")
    manifest = {
        "version": version,
        "files": {
            rel: {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            for rel, data in payload.items()
        },
    }
    # Stored ZIP avoids compressor-version drift; fixed metadata avoids clock/OS drift.
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_STORED) as z:
        for rel, data in payload.items():
            info = zipfile.ZipInfo(f"meaning-first-writing/{rel}", (2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum_path.write_text(f"{checksum}  {archive.name}\n", encoding="utf-8")
    return {"archive": str(archive), "manifest": str(manifest_path),
            "checksum": checksum, "file_count": len(files)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.root, args.output), indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Build failed: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
