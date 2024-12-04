import sys
import time
import resource
import os
from lab1.utils.utils import *


def secretar_swap(list_length: int, arr: list, out):
    for j in range(list_length):
        for i in range(list_length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                out.write(f"Swap elements at indices {i + 1} and {i + 2}.\n")
    out.write("No more swaps needed.\n")
    return arr


if __name__ == "__main__":
    time_start = time.perf_counter()
    list_length, arr = read_input("../txtf/input.txt")
    with open("../txtf/output.txt", "w") as out:
        answ = ', '.join(str(i) for i in secretar_swap(list_length, arr, out))
        out.write(answ)
    file_name = os.path.basename(__file__)
    printResult(answ, file_name)
    time_memory_tracking(time_start)
