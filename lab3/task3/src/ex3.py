import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab3.utils.utils import write_output, read_input_for_lottery, time_memory_tracking, printResult


def pugalo_sort(n, k, sizes):
    buckets = [[] for _ in range(k)]
    for i in range(n):
        buckets[i % k].append(sizes[i])

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for i in range(n):
        sorted_array.append(buckets[i % k][i // k])

    for i in range(1, n):
        if sorted_array[i] < sorted_array[i - 1]:
            return "НЕТ"

    return "ДА"


if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("../txtf/input.txt", "r") as file:
        n, k = map(int, file.readline().strip().split())
        sizes = list(map(int, file.readline().strip().split()))
    print(f"==========Входные данные========== \nn = {n}; k = {k} \nsizes = {sizes}")
    result = pugalo_sort(n, k, sizes)
    write_output(result, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)
