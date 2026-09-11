"""Тесты модуля lexico.analyzer."""

import unittest

from lexico.analyzer import (
    average_word_length,
    count_chars,
    count_lines,
    count_words,
    text_stats,
    tokenize,
)

SAMPLE = "Git хранит историю.\nGit — распределённая система!\n"


class TokenizeTests(unittest.TestCase):
    def test_words_are_lowercased(self):
        self.assertEqual(tokenize("Git git GIT"), ["git", "git", "git"])

    def test_punctuation_is_ignored(self):
        self.assertEqual(tokenize("Привет, мир!"), ["привет", "мир"])


class CountTests(unittest.TestCase):
    def test_count_chars(self):
        self.assertEqual(count_chars("a b"), 3)
        self.assertEqual(count_chars("a b", ignore_spaces=True), 2)

    def test_count_words(self):
        self.assertEqual(count_words(SAMPLE), 6)

    def test_count_lines(self):
        self.assertEqual(count_lines(SAMPLE), 2)
        self.assertEqual(count_lines("одна строка без перевода"), 1)
        self.assertEqual(count_lines(""), 0)

    def test_average_word_length(self):
        self.assertAlmostEqual(average_word_length("ab abcd"), 3.0)


class TextStatsTests(unittest.TestCase):
    def test_keys_and_values(self):
        stats = text_stats(SAMPLE)
        self.assertEqual(
            set(stats),
            {"chars", "chars_no_spaces", "words", "lines", "avg_word_length"},
        )
        self.assertEqual(stats["words"], 6)
        self.assertEqual(stats["lines"], 2)


if __name__ == "__main__":
    unittest.main()
