import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import time_memory_tracking, printResult


def read_input_lines(file_path="../txtf/input.txt"):
    """Чтение данных"""
    with open(file_path, "r") as inp:
        d = int(inp.readline())  # общее расстояние
        m = int(inp.readline())  # максимальная дальность
        n = int(inp.readline())  # количество заправок
        stops = list(map(int, inp.readline().split()))
        print("==========Входные данные========== ")
        print(f"d = {d}, m = {m}, n = {n}; stops = {stops}")
        return d, m, n, stops


def gas_stations(d, m, n, stops):
    """Задача о заправках"""
    stop_count = 0
    current_fuel = m
    for i in range(n):
        dist = stops[i] - stops[i - 1] if i > 0 else stops[i]  # учитываем расстояния между остановками и
        # едем дальше, пока топлива хватает до следующей остановки, иначе заправляемся и cnt+=1
        current_fuel -= dist
        if m < dist:
            return -1
        if current_fuel < dist:
            current_fuel = m
            stop_count += 1
    return stop_count


if __name__ == "__main__":
    time_start = time.perf_counter()
    d, m, n, stops = read_input_lines("../txtf/input.txt")
    result = gas_stations(d, m, n, stops)
    file_name = os.path.basename(__file__)
    printResult(result, file_name)
    time_memory_tracking(time_start)
