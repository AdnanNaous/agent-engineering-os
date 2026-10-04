from pathlib import Path
import tempfile
import unittest

from tools.validate_skill import check_links, load_frontmatter


class ValidationTests(unittest.TestCase):
    def test_missing_and_external_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / "reference.md"
            doc.write_text("[source](https://example.com/x)\n[missing](gone.md)\n")
            findings = check_links(doc, root)
            self.assertEqual(len(findings), 1)
            self.assertIn("missing link target", findings[0])

    def test_relative_link_and_fenced_example(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "assets").mkdir()
            (root / "assets/state.md").write_text("state")
            (root / "references").mkdir()
            doc = root / "references/work.md"
            doc.write_text("[state](../assets/state.md)\n```text\n[example](absent.md)\n```\n")
            self.assertEqual(check_links(doc, root), [])

    def test_repository_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / "reference.md"
            doc.write_text("[outside](../outside.md)\n")
            self.assertIn("escapes repository", check_links(doc, root)[0])

    def test_invalid_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            doc = Path(directory) / "metadata.md"
            for content in ("no frontmatter", "---\n- unexpected-list\n---\nbody"):
                doc.write_text(content)
                with self.assertRaises(ValueError):
                    load_frontmatter(doc)


if __name__ == "__main__":
    unittest.main()
