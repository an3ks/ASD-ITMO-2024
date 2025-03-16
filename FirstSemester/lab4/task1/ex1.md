
# Задание: Реализация стека с командами добавления и удаления элементов  
Студент ИТМО, Авдиенко Данила, itmoId 464919

## Вариант 1

## Задание 1
Реализовать стек с командами добавления элемента в стек (`+`) и удаления элемента из стека (`-`). При удалении элемента из стека результат необходимо сохранить.

## Input / Output

### Формат входных данных:
- Первая строка содержит число `n` — количество операций.
- Последующие строки содержат команды:
  - `+ X` — добавить элемент `X` в стек.
  - `-` — удалить верхний элемент из стека.

### Формат выходных данных:
- Список элементов, удаленных из стека в порядке их удаления.

| Input                               | Output             |
|-------------------------------------|--------------------|
| 5                                   | ['2', '1']         |
| + 1                                 |                    |
| + 2                                 |                    |
| -                                   |                    |
| -                                   |                    |
| + 3                                 |                    |

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
   cd lab4/task1/src
   ```
3. Запустите программу:
   ```bash
   python ex1.py
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

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from FirstSemester.lab4.utils.utils import write_output, read_input_lines, time_memory_tracking


def stack(n, arr):
    stck = []
    callStck = []
    for i in arr:
        if i[0] == "+":
            stck.append(i[1])
        else:
            callStck.append(stck.pop(-1))
    return callStck


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    print(n)
    print(arr)
    arr1 = stack(n, arr)
    write_output(arr1, "../txtf/output.txt")
    time_memory_tracking(time_start)
```
