import sys
import time
import resource
import os
from lab1.utils.utils import *


def reversed_insertion_sort(list_length, arr):
    for i in range(1, list_length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    time_start = time.perf_counter()
    list_length, arr = read_input("../txtf/input.txt")
    answ = reversed_insertion_sort(list_length, arr)
    write_output(answ, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(answ, file_name)
    time_memory_tracking(time_start)
