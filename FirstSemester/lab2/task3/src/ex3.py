import os
from FirstSemester.lab2.utils.utils import *


def merge_sort(arr: list):
    number_of_inversions = 0
    if len(arr) > 1:  # проверяем, не является ли длина массива единицей
        l = arr[:len(arr) // 2]  # делим текущий массив на две части
        r = arr[len(arr) // 2:]
        # рекурсивно вызываем функцию на каждую из частей, пока она внутри не дойдет до условия, что длина == 1 и не начнет выполнять код ниже
        number_of_inversions += merge_sort(l)
        number_of_inversions += merge_sort(r)
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
                number_of_inversions += len(l) - i
        if len(l) == i:  # если мы подошли к концу списка л, то добавляем все элементы списка р и наоборот в елсе
            templist.extend(r[j:])
        else:
            templist.extend(l[i:])
        for i in range(len(templist)):  # обновляем исходный лист
            arr[i] = templist[i]
    return number_of_inversions


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input("../txtf/input.txt")
    number_of_inversions = str(merge_sort(arr))
    write_output(number_of_inversions, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(number_of_inversions, file_name)
    time_memory_tracking(time_start)
