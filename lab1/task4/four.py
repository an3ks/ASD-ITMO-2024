def linear_search(v: int, arr: list):
    cnt = 0
    idx = []
    for i in arr:
        if i == v:
            cnt += 1
            idx.append(arr.index(i))
            arr[arr.index(i)] = v+1
    if cnt == 1:
        return idx[0]
    elif cnt == 0:
        return -1
    else:
        return idx, cnt


if __name__ == "__main__":
    with open("input.txt", "r") as inp:
        arr = list(map(int, inp.readline().split()))
        v = int(inp.readline())
        inp.close()

    with open("output.txt", "w") as out:
        answ = str(linear_search(v, arr))
        out.write(answ)
