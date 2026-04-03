def check_user(name, arm):
    Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"

    if name == "Дмитрий" and arm == 1:
        return "Добро пожаловать!"
    elif name == "Ангелина" and arm == 2:
        return "Добро пожаловать!"
    elif name == "Василий" and arm == 3:
        return "Добро пожаловать!"
    elif name == "Екатерина" and arm == 4:
        return "Добро пожаловать!"
    elif name == "Дмитрий" and arm != 1:
        return Dmitriy_check
    else:
        return "Логин или пароль не верный, попробуйте еще раз"


user_name1 = "Дмитрий"
arm1 = 1
print(f"Проверка для {user_name1}, АРМ {arm1}: {check_user(user_name1, arm1)}")

user_name2 = "Дмитрий"
arm2 = 2
print(f"Проверка для {user_name2}, АРМ {arm2}: {check_user(user_name2, arm2)}")

user_name3 = "Ангелина"
arm3 = 2
print(f"Проверка для {user_name3}, АРМ {arm3}: {check_user(user_name3, arm3)}")

user_name4 = "Ангелина"
arm4 = 1
print(f"Проверка для {user_name4}, АРМ {arm4}: {check_user(user_name4, arm4)}")

user_name5 = "Василий"
arm5 = 3
print(f"Проверка для {user_name5}, АРМ {arm5}: {check_user(user_name5, arm5)}")

user_name6 = "Екатерина"
arm6 = 4
print(f"Проверка для {user_name6}, АРМ {arm6}: {check_user(user_name6, arm6)}")

user_name7 = "Петр"
arm7 = 5
print(f"Проверка для {user_name7}, АРМ {arm7}: {check_user(user_name7, arm7)}")