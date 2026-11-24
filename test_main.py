"""Local checks for the entry writer (not part of the graded program)."""

import tempfile
import unittest
from pathlib import Path

from main import ENTRY, OUTPUT_PATH, write_entry


class EntryWriterTests(unittest.TestCase):
    def test_choice_is_one_scalar(self):
        self.assertEqual(len(ENTRY), 1)
        self.assertEqual(ENTRY, "\U0001F601")
        self.assertEqual(ENTRY.encode("utf-8"), b"\xf0\x9f\x98\x81")

    def test_output_path(self):
        self.assertEqual(str(OUTPUT_PATH).replace("\\", "/"), "/output/entry.txt")

    def test_writes_no_trailing_newline(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "nested" / "entry.txt"
            write_entry(target, ENTRY)
            self.assertEqual(target.read_bytes(), b"\xf0\x9f\x98\x81")

    def test_rejects_invalid_text(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "entry.txt"
            for bad in ("", "   ", "123456789"):
                with self.subTest(bad=bad):
                    with self.assertRaises(ValueError):
                        write_entry(target, bad)


if __name__ == "__main__":
    unittest.main()
