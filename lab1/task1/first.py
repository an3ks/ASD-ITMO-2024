def insertion_sort(list_lentgh, arr):
    for i in range(list_lentgh):
        for j in range(list_lentgh - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    with open("input.txt", "r") as inp:
        list_length = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        inp.close()
    answ = ', '.join(str(i) for i in insertion_sort(list_length, arr))
    with open("output.txt", "w+") as out:
        out.write(answ)
        out.close()
