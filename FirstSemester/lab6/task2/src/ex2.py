import time
import sys
import os
from lab6.utils.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))


def phone_book(queries):
    book = {}
    results = []
    for query in queries:
        query = query.split()
        command = query[0]
        if command == "add":
            number, name = query[1], query[2]
            book[number] = name
        elif command == "del":
            number = query[1]
            if number in book:
                del book[number]
        elif command == "find":
            number = query[1]
            if number in book:
                results.append(book[number])
            else:
                results.append("not found")

    return results


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, queries = read_input("../txtf/input.txt")
    answ = phone_book(queries)
    write_output(answ, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(answ, file_name)
    time_memory_tracking(time_start)
