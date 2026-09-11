"""Тесты интерфейса командной строки."""

import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from lexico.cli import main


class CliTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "text.txt"

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with redirect_stdout(out), redirect_stderr(io.StringIO()):
            code = main(list(argv))
        return code, out.getvalue()


class StatsCommandTests(CliTestCase):
    def test_stats_prints_word_count(self):
        self.path.write_text("раз два три\n", encoding="utf-8")
        code, output = self.run_cli("stats", str(self.path))
        self.assertEqual(code, 0)
        self.assertIn("Слов", output)
        self.assertIn(": 3", output)

    def test_missing_file_returns_error_code(self):
        code, _ = self.run_cli("stats", str(self.path.with_name("missing.txt")))
        self.assertEqual(code, 1)
