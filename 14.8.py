import random
import string
length = int(input("Введите длину пароля: "))
characters = string.ascii_letters
password = ""
for i in range(length):
    password += random.choice(characters)
print(password)