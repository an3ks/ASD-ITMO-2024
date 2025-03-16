import time
import sys
import os
from lab7.utils.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))


def process_lcs_3(n, seq1, m, seq2, l, seq3):
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if seq1[i - 1] == seq2[j - 1] == seq3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]


if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("../txtf/input.txt", "r") as inp:
        n = int(inp.readline().strip())
        seq1 = list(map(int, inp.readline().strip().split()))
        m = int(inp.readline().strip())
        seq2 = list(map(int, inp.readline().strip().split()))
        l = int(inp.readline().strip())
        seq3 = list(map(int, inp.readline().strip().split()))
    print("==========Входные данные========== ")
    print(f"n = {n} seq1 = {seq1}; m = {m} seq2 = {seq2}; l = {l} seq3 = {seq3}")
    answ = str(process_lcs_3(n, seq1, m, seq2, l, seq3))
    write_output(answ, "../txtf/output.txt")
    printResult(answ, "ex5.py")
    time_memory_tracking(time_start)