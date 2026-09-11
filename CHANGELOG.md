# Журнал изменений

Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/),
нумерация версий — [Semantic Versioning](https://semver.org/lang/ru/).

## [1.0.0] — 2026-09-11

### Добавлено
- Модуль `lexico.analyzer`: разбиение текста на слова, подсчёт символов
  (с пробелами и без), слов, строк и средней длины слова.
- Консольная команда `python -m lexico stats FILE`.
- Тесты `unittest` для модуля анализа и CLI.
