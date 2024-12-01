import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab4.utils.utils import write_output, read_input_lines, time_memory_tracking


def stack(n, arr):
    stck = []
    callStck = []
    for i in arr:
        if i[0] == "+":
            stck.append(i[1])
        else:
            callStck.append(stck.pop(-1))
    return callStck


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    print(n)
    print(arr)
    arr1 = stack(n, arr)
    write_output(arr1, "../txtf/output.txt")
    time_memory_tracking(time_start)
