import time
import sys
import os
import resource

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab3.utils.utils import write_output, time_memory_tracking, printResult


def anti_quick_sort(n):
    result = []

    def build(left, right):
        if left > right:
            return
        mid = (left + right) // 2
        result.append(mid + 1)
        build(left, mid - 1)
        build(mid + 1, right)

    build(0, n - 1)
    return result


if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("../txtf/input.txt", "r") as inp:
        n = int(inp.readline())
    print(f"==========Входные данные========== \nn = {n}")
    result = anti_quick_sort(n)
    write_output(result, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)
