import time
import sys
import os
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab2.utils.utils import time_memory_tracking, printResult


def z_func(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z[1:]


def read_input(file_path="../txtf/input.txt"):
    with open(file_path, "r") as inp:
        s = inp.readline().strip()
    return s


if __name__ == "__main__":
    time_start = time.perf_counter()
    s = read_input("../txtf/input.txt")
    result = z_func(s)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)