# Задание по реализации алгоритма сортировки слиянием

Студент ИТМО, Авдиенко Данила, itmoId 464919

## Описание задания
Реализовать алгоритм сортировки слиянием (Merge Sort) для сортировки массива данных. Алгоритм рекурсивно делит массив на две части, пока длина каждого подмассива не станет равна единице, а затем выполняет слияние с упорядочиванием.

## Реализация алгоритма
Алгоритм сортировки слиянием был реализован с использованием Python. Основная идея заключается в следующем:
- Рекурсивное деление массива на левую и правую части до тех пор, пока каждая часть не станет содержать по одному элементу.
- Слияние и сортировка двух частей в один отсортированный массив.

### Input / Output

| Input                      | Output                                |
|----------------------------|---------------------------------------|
| [9, 7, 5, 11, 12, 2, 14, 3, 10, 6] | [2, 3, 5, 6, 7, 9, 10, 11, 12, 14] |

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
   cd lab2/task1/src
   ```
3. Запустите программу:
   ```bash
   python first.py
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


def merge_sort(arr: list):
    if len(arr) > 1:
        l = arr[:len(arr) // 2]
        r = arr[len(arr) // 2:]
        merge_sort(l)
        merge_sort(r)
        templist = []
        i = j = 0
        while len(l) > i and len(r) > j:
            if l[i] <= r[j]:
                templist.append(l[i])
                i += 1
            else:
                templist.append(r[j])
                j += 1
        if len(l) == i:
            templist.extend(r[j:])
        else:
            templist.extend(l[i:])
        for i in range(len(templist)):
            arr[i] = templist[i]


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input("../txtf/input.txt")
    merge_sort(arr)
    write_output(arr, "../txtf/output.txt")
    time_memory_tracking(time_start)
```

## Результаты

- **Время выполнения:** Время выполнения программы измерялось с помощью модуля `time` и составляет менее 2 секунд для тестовых данных.
- **Использование памяти:** Пиковое потребление памяти не превышает 256 Мб.
