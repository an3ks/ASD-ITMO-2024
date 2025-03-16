import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import time_memory_tracking, printResult


def deleting_par(seq):
    pairs = {")":"(", "]":"[", "}":"{"}
    stack = []
    invalid_set = set()
    for i, char in enumerate(seq):
        if char in "([{":
            stack.append(i)
        elif char in ")]}":
            if stack and seq[stack[-1]] == pairs[char]:
                stack.pop()
            else:
                invalid_set.add(i)

    invalid_set.update(stack)

    res = "".join(seq[i] for i in range(len(seq)) if i not in invalid_set)
    return res


def read_input(file_path="input.txt"):
    """Чтение данных из файла"""
    with open(file_path, "r") as inp:
        n = inp.readline()
    print("==========Входные данные========== ")
    print(f"n = {n}")
    return n

if __name__ == "__main__":
    time_start = time.perf_counter()
    seq = read_input("../txtf/input.txt")
    result = deleting_par(seq)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)