Студент ИТМО, Авдиенко Данила, itmoId 464919  

## Вариант 1  

## Задание 5  
Реализовать проверку, является ли массив неубывающей пирамидой (кучей). Для выполнения задачи необходимо проверить, что для каждого элемента массива с индексом `i` выполняются следующие условия:  
1. Если левый потомок существует, то `arr[i] <= arr[2*i + 1]`.  
2. Если правый потомок существует, то `arr[i] <= arr[2*i + 2]`.  

## Input / Output  

### Формат входных данных:  
- Первая строка содержит число `n` — количество элементов в массиве.  
- Вторая строка содержит `n` целых чисел — элементы массива.  

### Формат выходных данных:  
- Вывести `YES`, если массив является неубывающей пирамидой.  
- В противном случае вывести `NO`.  

| Input                               | Output             |
|-------------------------------------|--------------------|
| 5                                   | YES                |
| 1 3 2 5 4                           |                    |
| 5                                   | NO                 |
| 1 0 2 5 4                           |                    |

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
   cd lab5/task2/src  
   ```  
3. Запустите программу:  
   ```bash  
   python ex2.py  
   ```  

## Тестирование  
Для запуска тестов выполните:  
```bash  
python -m unittest discover test/  
```  

## Код для ex2.py  
```python  
import time  
import sys  
import os  
import lab5.utils.utils  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))  

def is_heap(arr, n):  
    for i in range(n // 2):  # Проверка всех родительских узлов  
        left = 2 * i + 1  # Левый потомок  
        right = 2 * i + 2  # Правый потомок  

        if left < n and arr[i] > arr[left]:  
            return "NO"  
        if right < n and arr[i] > arr[right]:  
            return "NO"  
    return "YES"  

if __name__ == "__main__":  
    time_start = time.perf_counter()  
    n, arr = lab5.utils.utils.read_input("../txtf/input.txt")  
    answ = is_heap(arr, n)  
    lab5.utils.utils.write_output(answ, "../txtf/output.txt")  
    file_name = os.path.basename(__file__)  
    lab5.utils.utils.printResult(answ, file_name)  
    lab5.utils.utils.time_memory_tracking(time_start)  
```