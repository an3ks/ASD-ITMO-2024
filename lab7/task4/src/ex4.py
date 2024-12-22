import time
import sys
import os
from lab7.utils.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


def process_lcs(n, seq1, m, seq2):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, seq1, m, seq2 = read_input("../txtf/input.txt")
    answ = str(process_lcs(n, seq1, m, seq2))
    write_output(answ, "../txtf/output.txt")
    printResult(answ, "ex4.py")
    time_memory_tracking(time_start)