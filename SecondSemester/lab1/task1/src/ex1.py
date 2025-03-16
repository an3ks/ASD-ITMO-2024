import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import read_input_lines, time_memory_tracking, printResult


def max_reward(W, arr):
    """Задача о дробном рюкзаке"""
    arr.sort(key=lambda i: i[0] / i[1], reverse=True)
    total_value = 0
    for value, weight in arr:
        if weight <= W:
            W -= weight
            total_value += value
        else:
            total_value += value * (W / weight)
    return f"{total_value:.4f}"


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, W, arr = read_input_lines("../txtf/input.txt")
    result = max_reward(W, arr)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)
