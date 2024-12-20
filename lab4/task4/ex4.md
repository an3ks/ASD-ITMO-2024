# Отчет по заданию

## Задание: Проверка скобочной последовательности  
Студент ИТМО, Авдиенко Данила, itmoId 464919

## Вариант 1

---

## Задание 4

Реализовать функцию для проверки правильности скобочной последовательности, состоящей из символов `()`, `[]`, `{}`, с дополнительными требованиями:
1. Если последовательность неправильная, вывести индекс первой ошибки.
2. Если последовательность правильная, вывести "Success".

---

## Input / Output

### Формат входных данных:
- Первая строка содержит число `n` — количество строк.
- Последующие строки содержат последовательности, состоящие из:
  - Латинских букв (a-z, A-Z)
  - Цифр (0-9)
  - Скобок `()`, `[]`, `{}`.

### Формат выходных данных:
- Если последовательность корректна, вывести `Success`.
- Если последовательность некорректна, вывести индекс первой ошибки (индексация начинается с 1).

| Input                   | Output  |
|-------------------------|---------|
| ()()                   | Success |
| ([])                   | Success |
| ([)]                   | 3       |
| ((]]                   | 3       |
| )(                     | 1       |

---

## Ограничения по времени и памяти

- Ограничение по времени: 5 сек.
- Ограничение по памяти: 256 Мб.

---

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/an3ks/ASD-ITMO-2024
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd lab4/task4/src
   ```
3. Запустите программу:
   ```bash
   python ex4.py
   ```

---

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover test/
```