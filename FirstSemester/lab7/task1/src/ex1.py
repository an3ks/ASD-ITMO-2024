import time
import sys
import os
from lab7.utils.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))


def process_min_coins(money, coins):
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1


if __name__ == "__main__":
    time_start = time.perf_counter()
    money, coins = read_input_lines("../txtf/input.txt")
    answ = str(process_min_coins(money, coins))
    write_output(answ, "../txtf/output.txt")
    printResult(answ, "ex5.py")
    time_memory_tracking(time_start)
