import sys
import time
import resource


def linear_search(v: int, arr: list):
    cnt = 0
    idx = []
    for i, char in enumerate(arr):
        if char == v:
            cnt += 1
            idx.append(i)
    if cnt == 1:
        return idx[0]
    elif cnt == 0:
        return -1
    else:
        return idx, cnt


if __name__ == "__main__":
    time_start = time.perf_counter()
    with open("input.txt", "r") as inp:
        arr = list(map(int, inp.readline().split()))
        v = int(inp.readline())
        inp.close()

    with open("output.txt", "w") as out:
        answ = str(linear_search(v, arr))
        out.write(answ)
    time_elapsed = (time.perf_counter() - time_start)
    mmry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("Время:", time_elapsed)
    print("Память:%5.1f МБ" % (mmry))
