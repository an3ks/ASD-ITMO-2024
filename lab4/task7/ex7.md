# Задание: Нахождение максимума в скользящем окне  
Студент ИТМО, Авдиенко Данила, itmoId 464919  

## Вариант 1  

## Задание 7  
Реализовать алгоритм для нахождения максимального элемента в каждом окне размера `m` массива `arr`.  

**Скользящее окно** — это подмассив размера `m`, который последовательно перемещается по массиву.  

## Input / Output  

### Формат входных данных:  
- Первая строка содержит число `n` — длина массива `arr`.  
- Вторая строка содержит элементы массива `arr` (целые числа).  
- Третья строка содержит число `m` — размер окна.  

### Формат выходных данных:  
- Список максимальных элементов для каждого окна.  

| Input                                | Output          |
|--------------------------------------|-----------------|
| 8                                    | 5 6 6 6 6 7     |
| 1 3 -1 -3 5 3 6 7                    |                 |
| 3                                    |                 |

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
   cd lab4/task7/src
   ```
3. Запустите программу:  
   ```bash
   python ex7.py
   ```

## Тестирование  
Для запуска тестов выполните:  
```bash
python -m unittest discover test/
```

## Код для ex7.py  
```python
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab4.utils.utils import write_output, read_input, time_memory_tracking


def max_in_window(n, arr, m):
    dq = []
    res = []
    for i in range(0, n):
        if dq and dq[0] < i - m + 1:
            dq.pop(0)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop(-1)
        dq.append(i)
        if i >= m-1:
            res.append(arr[dq[0]])
    return res


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr, m = read_input("../txtf/input.txt")
    print(n, arr, m)
    arr = max_in_window(n, arr, m)
    write_output(arr, "../txtf/output.txt")
    time_memory_tracking(time_start)
```
