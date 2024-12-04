import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab4.utils.utils import write_output, read_input_lines, time_memory_tracking, printResult


def queue_min(n, arr):
    res = []
    queue = []
    for cm in arr:
        if cm[0] == "+":
            queue.append(int(cm[1]))
        elif cm[0] == "-":
            queue.pop(0)
        elif cm[0] == "?":
            mn = 10 ** 10
            for i in queue:
                if i < mn:
                    mn = i
            res.append(mn)
    return res


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    res = queue_min(n, arr)
    write_output(res, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(res, file_name)
    time_memory_tracking(time_start)
