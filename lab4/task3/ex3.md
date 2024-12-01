# Задание: Проверка правильной скобочной последовательности  
Студент ИТМО, Авдиенко Данила, itmoId 464919

## Вариант 1

## Задание 3
Реализовать проверку правильной скобочной последовательности, состоящей из символов `(`, `)`, `[`, `]`. Последовательность считается правильной, если:
- Пустая последовательность является правильной.
- Если последовательность начинается с открывающей скобки, то для каждой открывающей скобки должна быть соответствующая закрывающая.
- Скобки закрываются в правильном порядке (например, `([)]` — некорректно, а `([])` — корректно).

## Input / Output

### Формат входных данных:
- Первая строка содержит число `n` — количество строк.
- Следующие `n` строк содержат последовательности, состоящие из символов `(`, `)`, `[`, `]`.

### Формат выходных данных:
- Для каждой строки вывести `YES`, если последовательность правильная, иначе `NO`.

| Input                               | Output             |
|-------------------------------------|--------------------|
| 3                                   | YES                |
| ()                                  | YES                |
| ([])                                | YES                |
| ([)]                                | NO                 |

## Ограничения по времени и памяти

- Ограничение по времени: 2 сек.
- Ограничение по памяти: 256 Мб.

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/an3ks/ASD-ITMO-2024
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd lab4/task3/src
   ```
3. Запустите программу:
   ```bash
   python ex3.py
   ```

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover test/
```

## Код для ex1.py
```python
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab4.utils.utils import write_output, read_input_lines, time_memory_tracking

def is_valid_parentheses(sequence):
    stack = []
    pairs = {')': '(', ']': '['}
    for char in sequence:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != pairs[char]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    results = [is_valid_parentheses(''.join(line)) for line in arr]
    write_output(results, "../txtf/output.txt")
    time_memory_tracking(time_start)
```