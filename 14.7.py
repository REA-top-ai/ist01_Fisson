import random
n = int(input("Введите количество попыток: "))
for i in range(n):
    result = random.randint(1, 6)
    print(result)