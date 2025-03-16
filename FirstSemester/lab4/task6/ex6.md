# Задание: Реализация очереди с запросом минимума  
Студент ИТМО, Авдиенко Данила, itmoId 464919  

## Вариант 1  

## Задание 6  
Реализовать очередь, поддерживающую следующие операции:  
- Добавление элемента в очередь: `+ N`, где `N` — добавляемый элемент.  
- Удаление элемента из начала очереди: `-`.  
- Запрос минимального элемента: `?`.  

Очередь должна быть реализована таким образом, чтобы запросы `?` выполнялись максимально эффективно.  

## Input / Output  

### Формат входных данных:  
- Первая строка содержит число `n` — количество команд.  
- Следующие `n` строк содержат команды `+ N`, `-`, или `?`.  

### Формат выходных данных:  
- Для каждой команды `?` вывести минимальный элемент текущей очереди.  

| Input                               | Output |
|-------------------------------------|--------|
| 6                                   | 1      |
| + 3                                 | 1      |
| + 1                                 |        |
| ?                                   |        |
| -                                   |        |
| ?                                   |        |
| + 2                                 |        |

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
   cd lab4/task6/src
   ```
3. Запустите программу:  
   ```bash
   python ex6.py
   ```

## Тестирование  
Для запуска тестов выполните:  
```bash
python -m unittest discover test/
```

## Код для ex6.py

```python
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from FirstSemester.lab4.utils.utils import write_output, read_input_lines, time_memory_tracking


def queue_min(n, arr):
    res = []
    queue = []
    for cm in arr:
        if cm[0] == "+":
            queue.append(int(cm[1]))
        elif cm[0] == "-":
            queue.pop(0)
        elif cm[0] == "?":
            mn = 10 ** 10
            for i in queue:
                if i < mn:
                    mn = i
            res.append(mn)
    return res


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    res = queue_min(n, arr)
    write_output(res, "../txtf/output.txt")
    time_memory_tracking(time_start)
```