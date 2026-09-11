"""Функции подсчёта статистики текста."""

import re

# Слово: буквы или цифры; внутри слова допускаются дефис и апостроф.
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё0-9]+(?:[-\x27][A-Za-zА-Яа-яЁё0-9]+)*")


def tokenize(text: str) -> list[str]:
    """Разбить текст на слова, приведя их к нижнему регистру."""
    return [word.lower() for word in WORD_RE.findall(text)]


def count_chars(text: str, *, ignore_spaces: bool = False) -> int:
    """Число символов в тексте (при ignore_spaces=True пробельные не считаются)."""
    if ignore_spaces:
        return sum(1 for ch in text if not ch.isspace())
    return len(text)


def count_words(text: str) -> int:
    """Число слов в тексте."""
    return len(tokenize(text))


def count_lines(text: str) -> int:
    """Число строк в тексте (последняя строка без перевода тоже считается)."""
    if not text:
        return 0
    return text.count("\n") + (0 if text.endswith("\n") else 1)


def average_word_length(text: str) -> float:
    """Средняя длина слова в символах."""
    words = tokenize(text)
    return sum(len(word) for word in words) / len(words)


def text_stats(text: str) -> dict[str, int | float]:
    """Сводная статистика текста."""
    return {
        "chars": count_chars(text),
        "chars_no_spaces": count_chars(text, ignore_spaces=True),
        "words": count_words(text),
        "lines": count_lines(text),
        "avg_word_length": round(average_word_length(text), 2),
    }
