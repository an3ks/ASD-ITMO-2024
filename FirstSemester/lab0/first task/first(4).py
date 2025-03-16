bl = 10 ** (-9)
br = 10 ** 9
# Задача 4
fi = open("input.txt")
line = fi.readline()
a, b = map(int, line.split())
if (bl <= a <= br) and (bl <= b <= br):
    answ = str(a + b ** 2)
    fo = open("output.txt", "w")
    fo.write((answ))
else:
    print("Введенные данные не соответсвуют условию")
