import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import time_memory_tracking, printResult


def has_negative_cycle(n, m, edges):
    dist = [0] * (n + 1)

    for i in range(n):
        upd = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                upd = True
        if not upd:
            break
    for u, v, w in edges:
        if dist[v] > dist[u] + w:
            return 1
    return 0


def read_input_lines(file_path="../txtf/input.txt"):
    with open(file_path, "r") as inp:
        n, m = map(int, inp.readline().strip().split())
        edges = []
        for line in inp:
            line = line.strip()
            if line:
                u, v, w = map(int, line.split())
                edges.append((u, v, w))

        print("==========Входные данные==========")
        print(f"n = {n}, m = {m}; edges = {edges}")
        return n, m, edges


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, m, edges = read_input_lines("../txtf/input.txt")
    result = has_negative_cycle(n, m, edges)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)
