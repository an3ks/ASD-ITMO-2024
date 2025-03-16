import time
import resource


def read_input(file_path="input.txt"):
    """Чтение данных из файла"""
    with open(file_path, "r") as inp:
        n = int(inp.readline())  # Количество строк
        arr = [line.strip() for line in inp.readlines()]  # Считываем строки как команды
    print("==========Входные данные========== ")
    print(f"Входные данные n = {n}; arr = {arr}")
    return n, arr


def read_input_lines(file_path="input.txt"):
    """Чтение данных из файла"""
    with open(file_path, "r") as inp:
        arr = [line.strip() for line in inp.readlines()]  # Считываем строки как команды
    print("==========Входные данные========== ")
    print(f"arr = {arr}")
    return arr


def write_output(data, file_path="output.txt", index_log=None):
    """Запись данных в файл с логом индексов (если передан) и основными данными"""
    with open(file_path, "w") as out:
        if index_log:
            for el in index_log:
                out.write(f"{el[0]} {el[1]} {el[2]} {el[3]}\n")  # Запись индексов и значений
        out.write(' '.join(map(str, data)) + '\n')  # Запись основного массива или данных


def read_input_for_lottery(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        s, p = map(int, lines[0].split())
        segments = [tuple(map(int, line.split())) for line in lines[1:s + 1]]
        points = list(map(int, lines[s + 1].split()))
        return [(s, p)] + segments + [points]


def time_memory_tracking(time_start: float):
    time_elapsed = (time.perf_counter() - time_start)
    mmry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("Время:", time_elapsed)
    print(f"Память:%5.1f МБ\n" % (mmry))


def time_memory_tracking1(time_start: float):
    time_elapsed = (time.perf_counter() - time_start)
    mmry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    return time_elapsed, mmry


def printResult(answer, filename):
    print(f"=======Результат для {filename}=======")
    print(answer)
    print("==========Измерения==========")
