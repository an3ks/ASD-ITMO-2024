import time
import resource
from lab2.utils import write_output, read_input, time_memory_tracking


def merge_sort(arr: list):
    if len(arr) > 1:  # проверяем, не является ли длина массива единицей
        l = arr[:len(arr) // 2]  # делим текущий массив на две части
        r = arr[len(arr) // 2:]
        # рекурсивно вызываем функцию на каждую из частей, пока она внутри не дойдет до условия, что длина == 1 и не начнет выполнять код ниже
        merge_sort(l)
        merge_sort(r)
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
        for i in range(len(templist)):  # обновляем исходный лист
            arr[i] = templist[i]


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input("input.txt")
    merge_sort(arr)
    write_output(arr, "output.txt")
    time_memory_tracking(time_start)

    # time_elapsed = (time.perf_counter() - time_start)
    # mmry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    # print("Время:", time_elapsed)
    # print("Память:%5.1f МБ" % (mmry))
# usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# print(f"Memory usage: {usage / 1024:.2f} MB")  # Convert to MB