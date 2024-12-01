import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab4.utils.utils import write_output, read_input, time_memory_tracking


def max_in_window(n, arr, m):
    dq = []
    res = []
    for i in range(0, n):
        if dq and dq[0] < i - m + 1:
            dq.pop(0)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop(-1)
        dq.append(i)
        if i >= m-1:
            res.append(arr[dq[0]])
    return res


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr, m = read_input("../txtf/input.txt")
    print(n, arr, m)
    arr = max_in_window(n, arr, m)
    write_output(arr, "../txtf/output.txt")
    time_memory_tracking(time_start)
