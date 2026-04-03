import random
random_list = [random.randint(1, 100) for i in range(101)]
random_number = random.choice(random_list)
print(random_number)