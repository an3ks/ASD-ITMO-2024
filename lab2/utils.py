import time
import resource


def read_input(file_path="input.txt"):
    """Чтение данных из файла"""
    with open(file_path, "r") as inp:
        n = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
    return n, arr


def write_output(data, file_path="output.txt", index_log=None):
    """Запись данных в файл с логом индексов (если передан) и основными данными"""
    with open(file_path, "w") as out:
        if index_log:
            for el in index_log:
                out.write(f"{el[0]} {el[1]} {el[2]} {el[3]}\n")  # Запись индексов и значений
        out.write(' '.join(map(str, data)) + '\n')  # Запись основного массива или данных


def read_input_for_binary_search(file_path="input.txt"):
    """Чтение данных из файла для задачи бинарного поиска"""
    n, arr_a = read_input(file_path)

    with open(file_path, "r") as inp:
        lines = inp.readlines()
        k = int(lines[2].strip())
        arr_b = list(map(int, lines[3].strip().split()))
    return n, arr_a, k, arr_b


def time_memory_tracking(time_start: float):
    time_elapsed = (time.perf_counter() - time_start)
    mmry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("Время:", time_elapsed)
    print("Память:%5.1f МБ" % (mmry))
