user_name = input("Введите имя пользователя: ")

Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
other_message = "Добро пожаловать"

if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(other_message)

print("\nПроверка для Дмитрий:")
user_name = "Дмитрий"
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(other_message)

print("\nПроверка для Ангелина:")
user_name = "Ангелина"
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(other_message)



enter_number = int(input("\nВведите количество попыток входа: "))

if enter_number < 3:
    print(f"Попробуйте еще раз. У вас осталось {3 - enter_number} попыток")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки")

print("\nПроверка для 2 попыток:")
enter_number = 2
if enter_number < 3:
    print(f"Попробуйте еще раз. У вас осталось {3 - enter_number} попыток")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки")

print("\nПроверка для 3 попыток:")
enter_number = 3
if enter_number < 3:
    print(f"Попробуйте еще раз. У вас осталось {3 - enter_number} попыток")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки")
