import os
from FirstSemester.lab2.utils.utils import *


def binary_search(sorted_arr: list, number: int):
    l, r = 0, len(sorted_arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if sorted_arr[mid] == number:
            return mid
        elif sorted_arr[mid] < number:
            l = mid + 1
        else:
            r = mid - 1
    return -1


if __name__ == "__main__":
    time_start = time.perf_counter()
    n_sorted, sorted_arr, n, arr = read_input_for_binary_search("../txtf/input.txt")
    answer = []
    for i in arr:
        g = str(binary_search(sorted_arr, i))
        answer.append(g)
    write_output(answer, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(answer, file_name)
    time_memory_tracking(time_start)
