import os
from FirstSemester.lab2.utils.utils import *


def merge_sort(arr: list, index_log: list, start_idx=0):
    if len(arr) > 1:  # проверяем, не является ли длина массива единицей
        l = arr[:len(arr) // 2]  # делим текущий массив на две части
        r = arr[len(arr) // 2:]
        # рекурсивно вызываем функцию на каждую из частей, пока она внутри не дойдет до условия, что длина == 1 и не начнет выполнять код ниже
        merge_sort(l, index_log, start_idx)
        merge_sort(r, index_log, start_idx + len(l))
        templist = []  # временный список для слияния двух частей
        i = j = 0  # задаем индексы для работы с массивами
        while len(l) > i and len(
                r) > j:  # условие для прекращения (пока индекс сравниваемого элемента не станет равным длине списка)
            if l[i] <= r[j]:  # сравнение
                templist.append(l[i])
                i += 1
            else:
                templist.append(r[j])
                j += 1
        if len(l) == i:  # если мы подошли к концу списка л, то добавляем все элементы списка р и наоборот в елсе
            templist.extend(r[j:])
        else:
            templist.extend(l[i:])

        # out.write(f"{arr.index(templist[0]) + 1} {arr.index(templist[-1]) + 1} {templist[0]} {templist[-1]}\n")
        # Записываем индексы начала и конца объединенного списка и значения
        first_idx = start_idx
        last_idx = start_idx + len(templist) - 1
        index_log.append((first_idx + 1, last_idx + 1, templist[0], templist[-1]))  # +1 для человеческого индекса

        for i in range(len(templist)):  # обновляем исходный лист
            arr[i] = templist[i]


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input("../txtf/input.txt")
    index_log = []  # Хранение индексов и значений для каждой итерации слияния
    merge_sort(arr, index_log)
    write_output(arr, "../txtf/output.txt", index_log)
    file_name = os.path.basename(__file__)
    printResult(arr, file_name)
    time_memory_tracking(time_start)
