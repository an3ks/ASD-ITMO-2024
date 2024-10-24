import sys
import time
import resource


def bubble_sort(list_length, arr):
    for i in range(list_length):
        for j in range(list_length - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("input.txt", "r") as inp:
        list_length = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        inp.close()
    answ = ', '.join(str(i) for i in bubble_sort(list_length, arr))
    with open("output.txt", "w+") as out:
        out.write(answ)
        out.close()
    time_elapsed = (time.perf_counter() - time_start)
    mmry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("Время:", time_elapsed)
    print("Память:%5.1f МБ" % (mmry))
