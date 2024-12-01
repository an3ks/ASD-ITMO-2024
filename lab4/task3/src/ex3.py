import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab4.utils.utils import write_output, read_input_lines, time_memory_tracking


def is_valid_parentheses(sequence):
    stack = []
    pairs = {')': '(', ']': '['}
    for char in sequence:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != pairs[char]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    results = [is_valid_parentheses(''.join(line)) for line in arr]
    write_output(results, "../txtf/output.txt")
    time_memory_tracking(time_start)