def insertion_sort(n: int, arr: list):
    for i in range(n):
        for j in range(n - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = insertion_sort(7, [9, 5, 234, 5, 124, 2354, 235])
answ = ', '.join(str(i) for i in arr)
print(answ)
print(insertion_sort(7, [9, 5, 234, 5, 124, 2354, 235]))
