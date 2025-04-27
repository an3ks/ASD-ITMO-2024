import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab2.utils.utils import time_memory_tracking, printResult


def substr_search(p, t):
    n = len(p)
    m = len(t)
    res = []
    for i in range(m - n + 1):
        if t[i:i+n] == p:
            res.append(i + 1)
    return len(res), res


def read_input(file_path="../txtf/input.txt"):
    with open(file_path, "r") as inp:
        substr = inp.readline().strip()
        string = inp.readline().strip()

    return substr, string


if __name__ == "__main__":
    time_start = time.perf_counter()
    substr, string = read_input("../txtf/input.txt")
    n, idx = substr_search(substr, string)
    file_name = os.path.basename(__file__)
    printResult((n, idx), file_name)
    time_memory_tracking(time_start)