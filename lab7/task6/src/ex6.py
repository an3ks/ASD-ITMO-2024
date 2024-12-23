import time
import sys
import os
from lab7.utils.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


def process_lis(n, sequence):
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Длина LIS
    lis_length = max(dp)
    # Восстановление LIS
    lis_index = dp.index(lis_length)
    lis = []
    while lis_index != -1:
        lis.append(sequence[lis_index])
        lis_index = prev[lis_index]
    lis.reverse()

    return lis_length, lis


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, sequence = read_input1("../txtf/input.txt")
    lis_length, lis = process_lis(n, sequence)
    answ = f"{lis_length}\n{' '.join(map(str, lis))}"
    write_output(answ, "../txtf/output.txt")
    printResult(answ, "ex6.py")
    time_memory_tracking(time_start)