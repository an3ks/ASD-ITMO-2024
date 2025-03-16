import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from FirstSemester.lab4.utils.utils import write_output, read_input_lines, time_memory_tracking, printResult


def is_valid_brackets(sequence):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for i, char in enumerate(sequence.strip()):
        if char in "([{":
            stack.append((char, i + 1))
        elif char in ")]}":
            if not stack or stack[-1][0] != pairs[char]:
                return i + 1
            stack.pop()
    if stack:
        return stack[0][1]
    return "Success"


if __name__ == "__main__":
    time_start = time.perf_counter()
    file_name = os.path.basename(__file__)
    n, arr = read_input_lines("../txtf/input.txt")
    result = [is_valid_brackets(line[0]) for line in arr]
    write_output(result, "../txtf/output.txt")
    printResult(result, file_name)
    time_memory_tracking(time_start)