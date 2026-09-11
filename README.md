# Lexico — консольный анализатор текста

**Марков Арсений Алексеевич, группа 221141, вариант 10, лабораторная №1**

Учебный Python-проект для лабораторной работы № 1 по дисциплине
«Методы и технологии программирования» — «Система контроля версий. Работа с ней».
Репозиторий на GitHub: https://github.com/deiinferno/mtp-lab1-git

## Содержание

1. [О проекте](#1-о-проекте)
2. [Задания варианта 10](#2-задания-варианта-10)
3. [Задание 1 (средн. № 2): локальный репозиторий Python-проекта](#3-задание-1-средн--2-локальный-репозиторий-python-проекта)
4. [Задание 2 (средн. № 8): репозиторий на GitHub и связь с локальным](#4-задание-2-средн--8-репозиторий-на-github-и-связь-с-локальным)
5. [Задание 3 (средн. № 10): клонирование чужого репозитория и изучение истории](#5-задание-3-средн--10-клонирование-чужого-репозитория-и-изучение-истории)
6. [Задание 4 (повыш. № 10): Git flow для проекта](#6-задание-4-повыш--10-git-flow-для-проекта)
7. [Задание 5 (повыш. № 3): Pull Request](#7-задание-5-повыш--3-pull-request)
8. [Проверка работоспособности](#8-проверка-работоспособности)

## 1. О проекте

Lexico — небольшая утилита командной строки на Python (только стандартная
библиотека), которая считает статистику текстового файла и находит самые
частые слова. Проект написан специально для этой лабораторной, чтобы на нём
показать работу с Git: коммиты, ветки, слияния, теги, Git flow и Pull Request.

```text
mtp-lab1-git/
├── lexico/              # пакет приложения
│   ├── __init__.py      # версия пакета (__version__)
│   ├── __main__.py      # запуск: python -m lexico
│   ├── analyzer.py      # подсчёт символов/слов/строк, частотный словарь
│   └── cli.py           # argparse-интерфейс: команды stats и top
├── tests/               # тесты unittest (python -m unittest)
├── samples/example.txt  # пример входного текста
├── CHANGELOG.md         # журнал изменений по версиям
├── pyproject.toml       # метаданные проекта
├── .gitignore           # игнорируемые файлы Python-проекта
└── README.md            # этот отчёт
```

Запуск (Python ≥ 3.10):

```text
$ python -m lexico stats samples/example.txt
Символов              : 412
Символов без пробелов : 357
Слов                  : 55
Строк                 : 6
Средняя длина слова   : 6.31

$ python -m lexico top samples/example.txt -n 3
1. историю: 2
2. и: 2
3. веток: 2

$ python -m lexico --version
lexico 1.1.0
```

## 2. Задания варианта 10

По таблице индивидуальных вариантов методички (вариант 10 → Средн. 10, 2, 8;
Повыш. 10, 3):

| № | Сложность | № в общем списке | Задание | Где выполнено |
|---|---|---|---|---|
| 1 | средняя | 2 | Создать локальный репозиторий Python-проекта | [раздел 3](#3-задание-1-средн--2-локальный-репозиторий-python-проекта) |
| 2 | средняя | 8 | Создать репозиторий на GitHub и связать его с локальным | [раздел 4](#4-задание-2-средн--8-репозиторий-на-github-и-связь-с-локальным) |
| 3 | средняя | 10 | Склонировать чужой репозиторий и изучить историю | [раздел 5](#5-задание-3-средн--10-клонирование-чужого-репозитория-и-изучение-истории) |
| 4 | повышенная | 10 | Реализовать Git flow для своего проекта | [раздел 6](#6-задание-4-повыш--10-git-flow-для-проекта) |
| 5 | повышенная | 3 | Создать Pull Request | [раздел 7](#7-задание-5-повыш--3-pull-request) |

Все коммиты — атомарные, в стиле Conventional Commits (`feat:`, `fix:`,
`docs:`, `chore(release):`), все слияния — через `git merge --no-ff`
(в истории есть merge-коммиты), все ветки и теги отправлены на GitHub
(`git push --all && git push --tags`).

## 3. Задание 1 (средн. № 2): локальный репозиторий Python-проекта

Создан каркас Python-проекта (пакет `lexico`, `pyproject.toml`, `.gitignore`
для Python, `README.md`) и инициализирован локальный репозиторий с основной
веткой `main`. Имя и почта автора заданы для репозитория:

```bash
mkdir mtp-lab1-git && cd mtp-lab1-git
git init -b main
git config user.name "Arseniy Markov"
git config user.email "inferno8274@gmail.com"
git add -A
git commit -m "feat: create lexico project skeleton"
```

Первый коммит — `6995f27 feat: create lexico project skeleton`. Дальнейшая
разработка (модуль `analyzer.py`, CLI, тесты) велась в ветках по модели
Git flow, см. раздел 6.

`.gitignore` исключает `__pycache__/`, `*.pyc`, виртуальные окружения,
`.env`, кэши тестов, артефакты сборки и настройки IDE.

## 4. Задание 2 (средн. № 8): репозиторий на GitHub и связь с локальным

Репозиторий создан на GitHub из локального с помощью GitHub CLI, привязан как
удалённый `origin` и заполнен из локального репозитория:

```bash
gh auth login                  # вход под аккаунтом deiinferno
gh repo create mtp-lab1-git --public --source=. --remote=origin \
   --description "Лабораторная работа №1 (Git): Lexico — консольный анализатор текста"
git remote -v
git push -u origin main
git push --all origin          # все ветки: main, develop, feature/*, release/*, hotfix/*
git push --tags origin         # теги v1.0.0, v1.0.1, v1.1.0
```

Вывод `git remote -v`:

```text
origin	https://github.com/deiinferno/mtp-lab1-git.git (fetch)
origin	https://github.com/deiinferno/mtp-lab1-git.git (push)
```

Адрес репозитория: https://github.com/deiinferno/mtp-lab1-git

## 5. Задание 3 (средн. № 10): клонирование чужого репозитория и изучение истории

Клонирован официальный образцовый проект Python Packaging Authority —
**https://github.com/pypa/sampleproject** (в отдельную папку, вне этого
репозитория; чужой код в мой репозиторий не добавлялся):

```bash
git clone https://github.com/pypa/sampleproject.git
cd sampleproject
```

Изучение истории — команды и их вывод:

```text
$ git remote -v
origin	https://github.com/pypa/sampleproject.git (fetch)
origin	https://github.com/pypa/sampleproject.git (push)

$ git rev-list --count HEAD
197

$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main

$ git log --oneline -n 10
621e497 pyproject: prep 4.0.0 (#219)
8603eaf Update workflow actions to remove warning messages (#214)
a1f0005 Switch to `nox` for automated testing (#212)
5d27795 Update pyproject.toml (#204)
b1dfa48 Fixes inconsistencies in pyproject.toml documentation. (#197)
9944026 update python versions (#207)
3fb1461 Update `release.yml` with release branch for `gh-action-pypi-publish` (#195)
bae8ff4 Add token permissions to release workflow. (#192)
fc8d83e Update `release.yml` to use Trusted Publishing (#191)
fa13f7d Remove workflow warnings (#190)

$ git log -3 --format="%h | %ad | %an | %s" --date=short
621e497 | 2024-11-06 | William Woodruff | pyproject: prep 4.0.0 (#219)
8603eaf | 2024-11-06 | Guy Hoozdis | Update workflow actions to remove warning messages (#214)
a1f0005 | 2024-06-01 | chrysle | Switch to `nox` for automated testing (#212)

$ git log --reverse --format="%h | %ad | %an | %s" --date=short | head -3
215d8d6 | 2013-12-03 | Paul Moore | Initial commit
6979a8d | 2013-12-03 | Paul Moore | Tidy up setup.py and add the mandatory url parameter
ec93951 | 2013-12-03 | Paul Moore | Read the __init__.py file directly to get the package version

$ git shortlog -sn --no-merges HEAD | head -10
    26	Marcus Smith
    25	Dustin Ingram
     9	Paul Moore
     6	Ryan Long
     4	Marcel Martin
     3	Dan Søndergaard
     3	Matt Iversen
     3	Philip James
     3	Rebecca Turner
     2	David Tucker

$ git log --merges --oneline | wc -l
58

$ git log --stat -1
commit 621e4974ca25ce531773def586ba3ed8e736b3fc
Author: William Woodruff <william@yossarian.net>
Date:   Wed Nov 6 17:36:40 2024 -0500

    pyproject: prep 4.0.0 (#219)
    
    * pyproject: prep 4.0.0
    
    Signed-off-by: William Woodruff <william@trailofbits.com>
    
    * remove 3.8, add 3.13
    
    Signed-off-by: William Woodruff <william@trailofbits.com>
    
    * noxfile: remove 3.8, add 3.13
    
    Signed-off-by: William Woodruff <william@trailofbits.com>
    
    ---------
    
    Signed-off-by: William Woodruff <william@trailofbits.com>

 .github/workflows/test.yml |  2 +-
 noxfile.py                 |  5 +++--
 pyproject.toml             | 28 ++++++++++++----------------
 3 files changed, 16 insertions(+), 19 deletions(-)
```

Что видно из истории:

- 197 коммитов с 3 декабря 2013 г. (первый коммит Paul Moore) по 6 ноября
  2024 г.; 58 из них — merge-коммиты.
- Единственная ветка — `main`; тегов в репозитории нет, версии фиксируются
  коммитами вида `pyproject: prep 4.0.0`.
- Самые активные авторы — Marcus Smith (26 коммитов) и Dustin Ingram (25).
- Изменения попадают в проект через Pull Request: в заголовках коммитов
  стоят номера PR (`(#219)`, `(#214)` …), а последний коммит — squash
  нескольких правок из PR #219.
- `git log --stat` показывает, какие файлы затронул коммит: обновление
  `pyproject.toml`, `noxfile.py` и workflow GitHub Actions.

## 6. Задание 4 (повыш. № 10): Git flow для проекта

Проект ведётся по модели Git flow (Vincent Driessen):

| Ветка | Назначение | Откуда | Куда сливается |
|---|---|---|---|
| `main` | только выпущенные версии, каждая помечена тегом `vX.Y.Z` | — | — |
| `develop` | интеграционная ветка следующего выпуска | `main` | — |
| `feature/*` | разработка одной возможности | `develop` | `develop` |
| `release/*` | подготовка выпуска: версия, CHANGELOG | `develop` | `main` **и** `develop` |
| `hotfix/*` | срочное исправление выпущенной версии | `main` | `main` **и** `develop` |

Все слияния выполнены с `--no-ff`, поэтому каждое слияние — отдельный
merge-коммит и ветки видны в графе истории. Ветки после слияния намеренно
**не удалены**, чтобы их можно было проверить на GitHub.

Последовательность шагов и команды:

```bash
# 1. интеграционная ветка
git checkout -b develop main

# 2. feature/text-stats: модуль статистики и команда stats
git checkout -b feature/text-stats develop
git commit -m "feat: add text statistics functions"
git commit -m "feat: add stats command to CLI"
git checkout develop
git merge --no-ff feature/text-stats

# 3. release/1.0.0: версия и CHANGELOG, выпуск в main с тегом, обратное слияние в develop
git checkout -b release/1.0.0 develop
git commit -m "chore(release): prepare version 1.0.0"
git checkout main
git merge --no-ff release/1.0.0
git tag -a v1.0.0 -m "Release 1.0.0: статистика текста, команда stats"
git checkout develop
git merge --no-ff release/1.0.0

# 4. hotfix/1.0.1: ошибка ZeroDivisionError на пустом файле
git checkout -b hotfix/1.0.1 main
git commit -m "fix: return zero average word length for empty text"
git commit -m "chore(release): bump version to 1.0.1"
git checkout main
git merge --no-ff hotfix/1.0.1
git tag -a v1.0.1 -m "Hotfix 1.0.1: stats не падает на пустом файле"
git checkout develop
git merge --no-ff hotfix/1.0.1

# 5. feature/top-words: частотный словарь и команда top — влита через Pull Request (раздел 7)
git checkout -b feature/top-words develop
git commit -m "feat: add top-N frequent words analysis"
git commit -m "feat: add top command to CLI"
git push -u origin feature/top-words
gh pr create --base develop --head feature/top-words ...
gh pr merge 1 --merge          # merge-коммит, без fast-forward

# 6. release/1.1.0: выпуск с командой top
git checkout -b release/1.1.0 develop
git commit -m "chore(release): prepare version 1.1.0"
git commit -m "docs: add lab report to README"
git checkout main
git merge --no-ff release/1.1.0
git tag -a v1.1.0 -m "Release 1.1.0: команда top"
git checkout develop
git merge --no-ff release/1.1.0

# 7. публикация всего
git push --all origin
git push --tags origin
```

Граф истории (`git log --graph --oneline --all --decorate`) на момент
подготовки выпуска 1.1.0:

```text
* 703c20f (HEAD -> release/1.1.0) chore(release): prepare version 1.1.0
*   fd82bd8 (origin/develop, develop) Merge pull request #1 from deiinferno/feature/top-words
|\  
| * 22dfd2d (origin/feature/top-words, feature/top-words) feat: add top command to CLI
| * c55ac4f feat: add top-N frequent words analysis
|/  
*   0326b72 Merge branch 'hotfix/1.0.1' into develop
|\  
* \   35e0872 Merge branch 'release/1.0.0' into develop
|\ \  
| | | *   5aa1274 (tag: v1.0.1, origin/main, main) Merge branch 'hotfix/1.0.1'
| | | |\  
| | | |/  
| | |/|   
| | * | 6d5c62e (origin/hotfix/1.0.1, hotfix/1.0.1) chore(release): bump version to 1.0.1
| | * | 8c5d8f9 fix: return zero average word length for empty text
| | |/  
| | *   e6b6a99 (tag: v1.0.0) Merge branch 'release/1.0.0'
| | |\  
| | |/  
| |/|   
| * | 64b41b3 (origin/release/1.0.0, release/1.0.0) chore(release): prepare version 1.0.0
|/ /  
* |   2d80a48 Merge branch 'feature/text-stats' into develop
|\ \  
| |/  
|/|   
| * eab68fc (origin/feature/text-stats, feature/text-stats) feat: add stats command to CLI
| * a0b1606 feat: add text statistics functions
|/  
* 6995f27 feat: create lexico project skeleton
```

Теги: `v1.0.0`, `v1.0.1`, `v1.1.0` (аннотированные, `git tag -n1`).

## 7. Задание 5 (повыш. № 3): Pull Request

Ветка `feature/top-words` (функция `top_words` и команда `top`) отправлена
на GitHub и влита в `develop` через Pull Request:

- **Pull Request:** https://github.com/deiinferno/mtp-lab1-git/pull/1
- база: `develop`, сравнение: `feature/top-words`
- создан командой `gh pr create --base develop --head feature/top-words`
- влит кнопкой «Merge pull request» / `gh pr merge --merge` — с merge-коммитом
  `fd82bd8` в `develop` (без fast-forward), ветка сохранена.

После слияния PR из `develop` подготовлен выпуск `release/1.1.0`, влитый в
`main` с тегом `v1.1.0` (раздел 6).

## 8. Проверка работоспособности

```text
$ python -m unittest -v
test_average_word_length (tests.test_analyzer.CountTests.test_average_word_length) ... ok
test_average_word_length_of_empty_text_is_zero (tests.test_analyzer.CountTests.test_average_word_length_of_empty_text_is_zero) ... ok
test_count_chars (tests.test_analyzer.CountTests.test_count_chars) ... ok
test_count_lines (tests.test_analyzer.CountTests.test_count_lines) ... ok
test_count_words (tests.test_analyzer.CountTests.test_count_words) ... ok
test_keys_and_values (tests.test_analyzer.TextStatsTests.test_keys_and_values) ... ok
test_punctuation_is_ignored (tests.test_analyzer.TokenizeTests.test_punctuation_is_ignored) ... ok
test_words_are_lowercased (tests.test_analyzer.TokenizeTests.test_words_are_lowercased) ... ok
test_counting_is_case_insensitive (tests.test_analyzer.TopWordsTests.test_counting_is_case_insensitive) ... ok
test_most_frequent_words_come_first (tests.test_analyzer.TopWordsTests.test_most_frequent_words_come_first) ... ok
test_non_positive_n_gives_empty_list (tests.test_analyzer.TopWordsTests.test_non_positive_n_gives_empty_list) ... ok
test_missing_file_returns_error_code (tests.test_cli.StatsCommandTests.test_missing_file_returns_error_code) ... ok
test_stats_prints_word_count (tests.test_cli.StatsCommandTests.test_stats_prints_word_count) ... ok
test_top_lists_most_frequent_words (tests.test_cli.TopCommandTests.test_top_lists_most_frequent_words) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.007s

OK
```

Проверить локально:

```bash
git clone https://github.com/deiinferno/mtp-lab1-git.git
cd mtp-lab1-git
python -m unittest -v
python -m lexico stats samples/example.txt
python -m lexico top samples/example.txt -n 5
```
