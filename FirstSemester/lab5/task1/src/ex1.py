import time
import sys
import os
from FirstSemester import lab5

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))


def is_heap(arr, n):
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            return "NO"
        if right < n and arr[i] > arr[right]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = lab5.utils.utils.read_input("../txtf/input.txt")
    answ = is_heap(arr, n)
    lab5.utils.utils.write_output(answ, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    lab5.utils.utils.printResult(answ, file_name)
    lab5.utils.utils.time_memory_tracking(time_start)
