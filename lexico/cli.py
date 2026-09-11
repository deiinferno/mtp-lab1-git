"""Интерфейс командной строки Lexico."""

import argparse
import sys
from pathlib import Path

from lexico import __version__
from lexico.analyzer import text_stats

LABELS = {
    "chars": "Символов",
    "chars_no_spaces": "Символов без пробелов",
    "words": "Слов",
    "lines": "Строк",
    "avg_word_length": "Средняя длина слова",
}


def read_text(path: str) -> str:
    """Прочитать текстовый файл в кодировке UTF-8."""
    return Path(path).read_text(encoding="utf-8")


def cmd_stats(args: argparse.Namespace) -> int:
    """Команда stats: вывести сводную статистику файла."""
    stats = text_stats(read_text(args.file))
    width = max(len(label) for label in LABELS.values())
    for key, value in stats.items():
        print(f"{LABELS[key]:<{width}} : {value}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Собрать разбор аргументов командной строки."""
    parser = argparse.ArgumentParser(
        prog="lexico", description="Lexico — консольный анализатор текста"
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    stats = subparsers.add_parser("stats", help="сводная статистика текста")
    stats.add_argument("file", help="путь к текстовому файлу (UTF-8)")
    stats.set_defaults(func=cmd_stats)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Точка входа CLI; возвращает код завершения."""
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except FileNotFoundError as exc:
        print(f"Ошибка: файл не найден: {exc.filename}", file=sys.stderr)
        return 1
