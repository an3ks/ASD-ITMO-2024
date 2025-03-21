import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from lab3.utils.utils import write_output, read_input, time_memory_tracking, printResult


def quick_sort(arr: list):
    """Обычный алгоритм быстрой сортировки"""
    if len(arr) <= 1:
        return arr  # base case
    pivot = arr[0]
    gt = []
    mn = []
    for i in arr:
        if i > pivot:
            gt.append(i)
        else:
            mn.append(i)
    return quick_sort(mn) + [pivot] + quick_sort(gt)


def quick_sort_upgrade(arr: list):
    """Улучшенный алгоритм быстрой сортировки"""
    if len(arr) <= 1:
        return arr  # base case
    pivot = arr[0]
    gt = []
    eq = []
    mn = []
    for i in arr:
        if i > pivot:
            gt.append(i)
        elif i < pivot:
            mn.append(i)
        else:
            eq.append(i)
    return quick_sort_upgrade(mn) + eq + quick_sort_upgrade(gt)


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input("../txtf/input.txt")
    arr = quick_sort_upgrade(arr)
    write_output(arr, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(arr, file_name)
    time_memory_tracking(time_start)
