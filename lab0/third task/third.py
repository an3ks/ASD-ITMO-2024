import time

t_start = time.perf_counter()
fi = open("input.txt")
l = fi.readline()
a = int(l)
if not (0 <= a <= 10 ** 7):
    print("Число не удовлетворяет границам")
    exit()


def lastD_fib(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(n - 1):
        c = (a + b) % 10
        a, b = b, c
    return b


answ = str(lastD_fib(a))
fo = open("output.txt", "w")
fo.write(answ)

print("Время работы алгоритма:", (time.perf_counter() - t_start))
