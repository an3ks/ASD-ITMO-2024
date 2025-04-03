import time
import sys
import os
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import time_memory_tracking, printResult


def min_transfers(n, m, edges, u, v):
    graph = [[] for i in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    vs = [False] * (n + 1)
    dist = [-1] * (n + 1)

    queue = deque()
    queue.append(u)
    vs[u] = True
    dist[u] = 0

    while queue:
        curr = queue.popleft()
        if curr == v:
            return dist[v]
        for nei in graph[curr]:
            if not vs[nei]:
                vs[nei] = True
                dist[nei] = dist[curr] + 1
                queue.append(nei)

    return -1


def read_input_lines(file_path="../txtf/input.txt"):
    with open(file_path, "r") as inp:
        n, m = inp.readline().strip().split()
        n = int(n)
        m = int(m)
        arr = []
        for line in inp:
            line = line.strip()
            if line:
                nums = list(map(int, line.split()))
                if len(nums) == 2:
                    arr.append((nums[0], nums[1]))
        print("==========Входные данные==========")
        print(f"n = {n}, m = {m}; arr = {arr}")
        return n, m, arr


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, m, arr = read_input_lines("../txtf/input.txt")
    u, v = arr[-1]
    result = min_transfers(n, m, arr[:-1], u, v)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)