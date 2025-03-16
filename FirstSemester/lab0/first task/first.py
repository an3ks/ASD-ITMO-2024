bl = 10 ** (-9)
br = 10 ** 9
# Задача 1
a1, b1 = map(int, input().split())
if (bl <= a1 <= br) and (bl <= b1 <= br):
    print(a1 + b1)
else:
    print("Введенные данные не соответсвуют условию")

# Задача 2
a2, b2 = map(int, input().split())
if (bl <= a2 <= br) and (bl <= b2 <= br):
    print(a2 + (b2 ** 2))
else:
    print("Введенные данные не соответсвуют условию")

# Задача 3
f = open("input.txt")
line = f.readline()
a, b = map(int, line.split())
if (bl <= a <= br) and (bl <= b <= br):
    answ = str(a + b)
    fo = open("output.txt", "w")
    fo.write((answ))
else:
    print("Введенные данные не соответсвуют условию")
    
