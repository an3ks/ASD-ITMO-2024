import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab4.utils.utils import write_output, read_input_lines, time_memory_tracking, printResult


def stack(n, commands):
    stack = []
    max_stack = []
    results = []

    for command in commands:
        if command[0] == "push":
            value = int(command[1])
            stack.append(value)
            if not max_stack or value >= max_stack[-1]:
                max_stack.append(value)
        elif command[0] == "pop":
            if stack:
                value = stack.pop()
                if max_stack and value == max_stack[-1]:
                    max_stack.pop()
        elif command[0] == "max":
            if max_stack:
                results.append(max_stack[-1])

    return results


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, commands = read_input_lines("../txtf/input.txt")
    arr1 = stack(n, commands)
    write_output(arr1, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(arr1, file_name)
    time_memory_tracking(time_start)
