import os
from FirstSemester.lab1.utils.utils import *


def bubble_sort(list_length, arr):
    for i in range(list_length):
        for j in range(list_length - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    time_start = time.perf_counter()
    list_length, arr = read_input("../txtf/input.txt")
    answ = bubble_sort(list_length, arr)
    write_output(answ, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(arr, file_name)
    time_memory_tracking(time_start)

