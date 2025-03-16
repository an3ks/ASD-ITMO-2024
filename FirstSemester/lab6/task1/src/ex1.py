import time
import sys
import os
from lab6.utils.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))


def process_set_operations(queries):
    my_set = set()
    results = []

    for query in queries:
        command, value = query.split()
        value = int(value)

        if command == "A":
            my_set.add(value)
        elif command == "D":
            my_set.discard(value)
        elif command == "?":
            results.append("Y" if value in my_set else "N")

    return results


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, queries = read_input("../txtf/input.txt")
    answ = process_set_operations(queries)
    write_output(answ, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(answ, file_name)
    time_memory_tracking(time_start)