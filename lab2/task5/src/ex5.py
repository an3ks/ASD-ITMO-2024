import time
import resource
from lab2.utils import write_output, read_input_for_binary_search, read_input, time_memory_tracking


def majority_element(A, left, right):
    if left == right:
        return A[left]

    # массив пополам
    mid = (left + right) // 2
    # ищем элемент большинства в левой и правой половинах
    left_majority = majority_element(A, left, mid)
    right_majority = majority_element(A, mid + 1, right)

    # если оба подмассива возвращают одинаковый элемент
    if left_majority == right_majority:
        return left_majority

    # количество вхождений каждой цифры в текущем подмассиве
    left_count = sum(1 for i in range(left, right + 1) if A[i] == left_majority)
    right_count = sum(1 for i in range(left, right + 1) if A[i] == right_majority)

    # возвращаем элемент
    if left_count > (right - left + 1) // 2:
        return left_majority
    if right_count > (right - left + 1) // 2:
        return right_majority

    # нет подходящего элемента
    return 0


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input("input.txt")
    res = majority_element(arr, 0, n - 1)
    if res != 0:
        res = 1
    write_output(str(res))
    time_memory_tracking(time_start)