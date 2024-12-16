Студент ИТМО, Авдиенко Данила, itmoId 464919  

## Вариант 1  

## Задание 2  
Реализовать вычисление высоты дерева по его описанию. Дерево задаётся списком родителей для каждого узла, где:  
- Корневой узел имеет значение `-1` в массиве родителей.  
- Высота дерева — это максимальная глубина от корневого узла до любого листа.  

## Input / Output  

### Формат входных данных:  
- Первая строка содержит число `n` — количество узлов в дереве.  
- Вторая строка содержит `n` чисел — список родителей узлов (индексы от `0` до `n-1`).  

### Формат выходных данных:  
- Одно число — высота данного дерева.  

| Input                               | Output             |
|-------------------------------------|--------------------|
| 5                                   | 3                 |
| 4 -1 4 1 1                          |                    |

**Пояснение**:  
- Дерево имеет 5 узлов. Узел с индексом `1` — корневой (`-1`). Узлы `4` и `1` имеют дочерние узлы. Максимальная глубина равна `3`.  

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

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))  
from lab5.utils.utils import write_output, read_input_lines, time_memory_tracking  

def calculate_tree_height(n, parents):  
    # Строим дерево из списка родителей
    tree = [[] for _ in range(n)]  
    root = -1  
    for i in range(n):  
        if parents[i] == -1:  
            root = i  
        else:  
            tree[parents[i]].append(i)  

    # DFS для подсчёта высоты дерева
    def dfs(node):  
        if not tree[node]:  
            return 1  
        return 1 + max(dfs(child) for child in tree[node])  

    return dfs(root)  

if __name__ == "__main__":  
    time_start = time.perf_counter()  
    n, parents = read_input_lines("../txtf/input.txt")  
    result = calculate_tree_height(n, parents)  
    write_output([result], "../txtf/output.txt")  
    time_memory_tracking(time_start)  
```