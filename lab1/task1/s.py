def secretar_swap(list_length: int, arr: list, out):
    for j in range(list_length):
        for i in range(list_length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                out.write += f"Swap elements at indices {i} and {i + 1}.\n"
    out.write += "No more swaps needed."
    return arr

res = ""
arr = secretar_swap(7, [9, 5, 234, 5, 124, 2354, 235])
answ = ', '.join(str(i) for i in arr)
print(answ)
print(secretar_swap(7, [9, 5, 234, 5, 124, 2354, 235]))
