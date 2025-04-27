import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab2.utils.utils import time_memory_tracking, printResult


def pref_func(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def read_input(file_path="../txtf/input.txt"):
    with open(file_path, "r") as inp:
        s = inp.readline().strip()
    return s


if __name__ == "__main__":
    time_start = time.perf_counter()
    s = read_input("../txtf/input.txt")
    result = pref_func(s)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)