import time
import resource
from lab2.utils import write_output, read_input_for_binary_search


# Function to print memory usage in MB
def print_memory_usage():
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Memory usage: {usage / 1024:.2f} MB")  # Convert to MB


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
    n_sorted, sorted_arr, n, arr = read_input_for_binary_search("input.txt")
    answer = []
    for i in arr:
        g = str(binary_search(sorted_arr, i))
        answer.append(g)
    write_output(answer, "output.txt")
    time_elapsed = (time.perf_counter() - time_start)
    mmry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("Время:", time_elapsed)
    print("Память:%5.1f МБ" % (mmry))
