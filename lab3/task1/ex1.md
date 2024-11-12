# Задание №1 по варианту: `Улучшение Quick sort`  
Студент ИТМО, Авдиенко Данила, itmoId 464919

## Вариант 1

## Задание
Реализовать улучшенную версию алгоритма быстрой сортировки (Quick sort) с оптимизацией для улучшения производительности при сортировке больших массивов данных. Включить гибридный подход, использующий вставку для небольших подмассивов и случайный выбор опорного элемента.

## Input / Output

| Input                      | Output                                |
|----------------------------|---------------------------------------|
| 9, 7, 5, 11, 12, 2, 14, 3, 10, 6 | 2, 3, 5, 6, 7, 9, 10, 11, 12, 14 |

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
   cd lab3/task1/src
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

## Код для main.py
```python
import time
import resource
from lab2.utils import write_output, read_input, time_memory_tracking


def quick_sort(arr: list):
    """Обычный алгоритм быстрой сортировки"""
    if len(arr) <= 1:
        return arr  # base case
    pivo = arr[0]
    gt = []
    mn = []
    for i in arr:
        if i > pivo:
            gt.append(i)
        else:
            mn.append(i)
    return quick_sort(mn) + [pivo] + quick_sort(gt)


def quick_sort_upgrade(arr: list):
    """Улучшенный алгоритм быстрой сортировки"""
    if len(arr) <= 1:
        return arr  # base case
    pivo = arr[0]
    gt = []
    eq = []
    mn = []
    for i in arr:
        if i > pivo:
            gt.append(i)
        elif i < pivo:
            mn.append(i)
        else:
            eq.append(i)
    return quick_sort_upgrade(mn) + eq + quick_sort_upgrade(gt)


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input("input.txt")
    arr = quick_sort_upgrade(arr)
    write_output(arr, "output.txt")
    time_memory_tracking(time_start)
