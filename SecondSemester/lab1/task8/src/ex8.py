import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import read_input, time_memory_tracking, printResult


def time_table(n, arr):
    arr.sort(key=lambda x: x[1])

    cnt = 0
    end_time = 0

    for start, end in arr:
        if start >= end_time:
            cnt += 1
            end_time = end
    return cnt


if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("../txtf/input.txt", "r") as f:
        n = int(f.readline().strip())
        arr = [tuple(map(int, f.readline().split())) for _ in range(n)]
    result = time_table(n, arr)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)