"""Failure-case and integrity tests; no claims about writing quality."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_skill as validator
import build_release as builder


class SkillPackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "meaning-first-writing"
        for path in builder.source_files(ROOT):
            target = self.root / path.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)

    def write(self, rel, text):
        (self.root / rel).write_text(text, encoding="utf-8")

    def test_valid_package(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_reference(self):
        (self.root / "references/bilingual-writing.md").unlink()
        self.assertTrue(any("bilingual-writing.md" in e for e in validator.validate(self.root)))

    def test_nested_broken_link(self):
        self.write("references/bilingual-writing.md", "[Missing](missing.md)")
        self.assertTrue(any("Broken local" in e for e in validator.validate(self.root)))

    def test_link_cannot_escape_root(self):
        (self.root.parent / "outside.md").write_text("exists", encoding="utf-8")
        self.write("references/bilingual-writing.md", "[Outside](../../outside.md)")
        self.assertTrue(any("Broken local" in e for e in validator.validate(self.root)))

    def test_percent_encoded_local_path(self):
        self.write("references/space name.md", "A real local document.")
        self.write("references/bilingual-writing.md", "[Space](space%20name.md)")
        self.assertEqual(validator.validate(self.root), [])

    def test_version_mismatch(self):
        self.write("VERSION", "9.0.0")
        self.assertTrue(any("CHANGELOG" in e for e in validator.validate(self.root)))

    def test_missing_required_file(self):
        (self.root / "agents/openai.yaml").unlink()
        self.assertTrue(any("agents/openai.yaml" in e for e in validator.validate(self.root)))

    def test_duplicate_frontmatter_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            validator.parse_frontmatter("---\nname: a\nname: b\n---\ntext")

    def test_missing_frontmatter_end(self):
        with self.assertRaisesRegex(ValueError, "closing"):
            validator.parse_frontmatter("---\nname: a\ntext")

    def test_block_description(self):
        result = validator.parse_frontmatter("---\nname: a\ndescription: >-\n  One.\n  Two.\n---\ntext")
        self.assertEqual(result["description"], "One. Two.")

    def test_unresolved_repo_placeholder(self):
        self.write("README.md", "YOUR_GITHUB_USERNAME/meaning-first-writing")
        self.assertTrue(any("placeholder" in e for e in validator.validate(self.root)))

    def test_ui_prompt_mentions_skill(self):
        p = self.root / "agents/openai.yaml"
        self.write("agents/openai.yaml", p.read_text(encoding="utf-8").replace("$meaning-first-writing", "a skill"))
        self.assertTrue(any("default_prompt" in e for e in validator.validate(self.root)))

    def test_invalid_package_cannot_build(self):
        (self.root / "SKILL.md").unlink()
        with self.assertRaises(ValueError):
            builder.build(self.root)
        self.assertFalse((self.root / "dist").exists())

    def test_archive_integrity_and_exclusions(self):
        self.write(".env", "DUMMY_TEST_SECRET=not-real")
        self.write("private.md", "Not a maintained root file.")
        result = builder.build(self.root)
        manifest = json.loads(Path(result["manifest"]).read_text(encoding="utf-8"))
        with zipfile.ZipFile(result["archive"]) as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(len(z.namelist()), len(manifest["files"]))
            self.assertFalse(any(".env" in n or "private.md" in n or "/dist/" in n for n in z.namelist()))
            for rel, item in manifest["files"].items():
                data = z.read("meaning-first-writing/" + rel)
                self.assertEqual(len(data), item["bytes"])
                self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"])
            extracted = Path(self.temp.name) / "extracted"
            z.extractall(extracted)
            self.assertEqual(validator.validate(extracted / "meaning-first-writing"), [])

    def test_build_is_reproducible(self):
        first = builder.build(self.root)
        data = Path(first["archive"]).read_bytes()
        second = builder.build(self.root)
        self.assertEqual(data, Path(second["archive"]).read_bytes())
        self.assertEqual(first["checksum"], second["checksum"])

    def test_symlink_source_rejected(self):
        target = self.root / "references/link.md"
        try:
            target.symlink_to(self.root / "README.md")
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks not permitted on this host")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            builder.build(self.root)


if __name__ == "__main__":
    unittest.main()
