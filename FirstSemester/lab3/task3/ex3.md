## Задание 6  
Реализовать алгоритм сортировки с использованием корзин (пугало-сортировка).

## **Описание задачи**  
Дана последовательность размеров `sizes` длины `n`.  
Алгоритм использует **k корзин** для распределения элементов и сортировки.  
Необходимо ответить на вопрос: можно ли отсортировать последовательность таким образом, чтобы после объединения корзин результат был **неубывающим**.  

## **Input / Output**  

### Формат входных данных:  
- Первая строка содержит два числа `n` и `k` — количество элементов и количество корзин.  
- Вторая строка содержит `n` чисел — размеры элементов последовательности.  

### Формат выходных данных:  
- Вывести **ДА**, если возможно получить неубывающую последовательность, иначе **НЕТ**.  

### Пример:  

| Input             | Output |
|-------------------|--------|
| 6 2              | ДА     |
| 1 6 3 4 5 2      |        |  

| Input             | Output |
|-------------------|--------|
| 6 2              | НЕТ    |
| 4 3 1 6 5 2      |        |  

---

## **Код программы**  

### Файл: `ex3.py`

```python
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from lab3.utils.utils import write_output, read_input_for_lottery, time_memory_tracking, printResult


def pugalo_sort(n, k, sizes):
    buckets = [[] for _ in range(k)]
    for i in range(n):
        buckets[i % k].append(sizes[i])

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for i in range(n):
        sorted_array.append(buckets[i % k][i // k])

    for i in range(1, n):
        if sorted_array[i] < sorted_array[i - 1]:
            return "НЕТ"

    return "ДА"


if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("../txtf/input.txt", "r") as file:
        n, k = map(int, file.readline().strip().split())
        sizes = list(map(int, file.readline().strip().split()))
    print(f"==========Входные данные========== \\nn = {n}; k = {k} \\nsizes = {sizes}")
    result = pugalo_sort(n, k, sizes)
    write_output(result, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)
```

---

## **Описание работы программы**  

### **1. Входные данные:**  
- Читаются из файла `../txtf/input.txt`.  
- Первая строка содержит два числа `n` и `k`.  
- Вторая строка — массив `sizes` из `n` элементов.

### **2. Алгоритм работы:**  
1. **Распределение по корзинам:**  
   - Создаётся `k` корзин (списков).  
   - Элементы массива распределяются по корзинам в зависимости от индекса:  
     `buckets[i % k].append(sizes[i])`.  

2. **Сортировка корзин:**  
   - Каждая корзина сортируется по возрастанию.  

3. **Объединение корзин:**  
   - Элементы собираются в новый список `sorted_array`, используя принцип:  
     `buckets[i % k][i // k]`.  

4. **Проверка на неубывание:**  
   - Выполняется линейный проход по массиву `sorted_array`.  
   - Если нарушается порядок `sorted_array[i] < sorted_array[i - 1]`, программа возвращает **"НЕТ"**.  
   - Иначе — **"ДА"**.

### **3. Выходные данные:**  
- Результат проверки записывается в файл `../txtf/output.txt`.  
- На экран выводится результат и входные данные.  

---

## **Пример запуска**  

### Входные данные:
```plaintext
6 2
1 6 3 4 5 2
```

### Выходные данные:
```plaintext
ДА
```

### Команда запуска:
```bash
python ex3.py
```

---

## **Замеры времени и памяти:**  
Время выполнения и использование памяти отслеживаются с помощью функции **`time_memory_tracking`**.

---

## **Запуск тестов**  
Для запуска тестов выполните:  
```bash
python -m unittest discover test/