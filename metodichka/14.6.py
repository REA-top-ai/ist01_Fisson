import random
n = int(input("Введите количество попыток: "))
for i in range(n):
    result = random.randint(0, 1)
    if result == 0:
        print("Орел")
    else:
        print("Решка")