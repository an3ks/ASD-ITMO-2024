import sys
import time
import resource
import os
from lab1.utils.utils import *


def linear_search(v: int, arr: list):
    cnt = 0
    idx = []
    for i, char in enumerate(arr):
        if char == v:
            cnt += 1
            idx.append(i)
    if cnt == 1:
        return idx[0]
    elif cnt == 0:
        return -1
    else:
        return idx, cnt


if __name__ == "__main__":
    time_start = time.perf_counter()
    list_length, arr = read_input("../txtf/input.txt")
    answ = linear_search(list_length, arr)
    write_output(answ, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(answ, file_name)
    time_memory_tracking(time_start)
