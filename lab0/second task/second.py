import time

t_start = time.perf_counter()
fi = open("input.txt")
l = fi.readline()
a = int(l)
sum = 0
if not (0 <= a <= 45):
    print("Число не удовлетворяет границам")
    exit()


def calc_fibonacci(a):
    l = [0, 1]
    i = 2
    while i <= a:
        l.append(l[i - 1] + l[i - 2])
        i+=1
    return l[a]


answ = str(calc_fibonacci(a))
fo = open("output.txt", "w")
fo.write(answ)

print("Время работы алгоритма:", (time.perf_counter() - t_start))
