import time
import sys
import os
import resource

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab3.utils.utils import write_output, read_input, time_memory_tracking, printResult


def digital_sorting(n: int, m: int, k: int, matrix: list):
    # Инициализация индексов
    indices = [i for i in range(1, n + 1)]

    # Выполнение k фаз сортировки
    for phase in range(1, k + 1):
        # Определяем строку для сортировки
        row_to_sort_by = m - phase

        # Сортируем индексы на основе символа в строке `row_to_sort_by`
        indices.sort(key=lambda i: matrix[row_to_sort_by][i - 1])  # `i - 1` из-за индексации с 1

    # Возвращаем итоговый порядок индексов
    return indices




if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("../txtf/input.txt", "r") as inp:
        n, m, k = map(int, inp.readline().split())
        matrix = [inp.readline().strip() for i in range(m)]
    result_indices = digital_sorting(n, m, k, matrix)
    write_output(result_indices, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(result_indices, file_name)
    time_memory_tracking(time_start)