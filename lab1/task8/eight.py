def secretar_swap(list_length: int, arr: list, out):
    for j in range(list_length):
        for i in range(list_length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                out.write(f"Swap elements at indices {i+1} and {i + 2}.\n")
    out.write("No more swaps needed.\n")
    return arr


if __name__ == "__main__":
    with open("input.txt", "r") as inp:
        list_length = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        inp.close()

    with open("output.txt", "w") as out:
        answ = ', '.join(str(i) for i in secretar_swap(list_length, arr, out))
        out.write(answ)
