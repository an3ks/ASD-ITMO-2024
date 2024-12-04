import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab3.utils.utils import write_output, read_input_for_lottery, time_memory_tracking, printResult


def lottery(data):
    # Распаковка входных данных
    s, p = data[0]  # количество отрезков и точек
    array = data[1:s + 1]  # список всех списков
    dot_list = data[s + 1]  # список всех точек

    events = []

    for ul in array:
        events.append((ul[0], -1))
        events.append((ul[-1], 1))  # добавили конец и начало каждого отрезка, пометив их индексами -1 и 1

    for idx, dot in enumerate(dot_list):
        events.append((dot, 0, idx))

    events = sorted(events, key=lambda x: (x[0], x[1]))
    cntr = 0
    list_peresecheniy = []
    for event in events:
        if event[1] == -1:
            cntr += 1
        elif event[1] == 1:
            cntr -= 1
        elif event[1] == 0:
            list_peresecheniy.append((cntr, event[2]))
    list_peresecheniy = sorted(list_peresecheniy, key=lambda x: x[1])
    result = [count for count, _ in list_peresecheniy]
    return result


if __name__ == "__main__":
    time_start = time.perf_counter()
    data = read_input_for_lottery("../txtf/input.txt")
    answer = lottery(data)
    write_output(answer, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(answer, file_name)
    time_memory_tracking(time_start)
