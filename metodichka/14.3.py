import matplotlib.pyplot as plt
import random

number_a = range(1, 13)
number_b = [random.randint(0, 1000) for i in range(12)]

plt.plot(number_a, number_b)
plt.show()