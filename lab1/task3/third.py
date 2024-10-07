def reversed_insertion_sort(list_length, arr):
    for i in range(1, list_length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    with open("input.txt", "r") as inp:
        list_length = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        inp.close()
    answ = ', '.join(str(i) for i in reversed_insertion_sort(list_length, arr))
    with open("output.txt", "w+") as out:
        out.write(answ)
        out.close()
