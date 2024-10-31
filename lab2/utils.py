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


