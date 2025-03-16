import os
import sys
import time
from FirstSemester.lab5 import read_input, write_output, time_memory_tracking, printResult

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))


def calculate_tree_height(n, parents):
    # Шаг 1: Найти корневой узел и построить список дочерних узлов
    tree = [[] for _ in range(n)]
    root = -1

    for i in range(n):
        if parents[i] == -1:
            root = i  # Узел без родителя - корневой
        else:
            tree[parents[i]].append(i)  # Добавляем дочерний узел

    # Шаг 2: Обход в глубину для подсчета высоты дерева
    def dfs(node):
        if not tree[node]:  # Лист дерева
            return 1
        return 1 + max(dfs(child) for child in tree[node])

    # Шаг 3: Запуск DFS от корня
    return dfs(root)


if __name__ == "__main__":
    time_start = time.perf_counter()

    # Читаем данные из файла
    n, parents = read_input("../txtf/input.txt")  # parents уже является списком чисел

    # Подсчитываем высоту дерева
    result = calculate_tree_height(n, parents)

    # Записываем результат в файл
    write_output([result], "../txtf/output.txt")

    # Печать и мониторинг времени/памяти
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)