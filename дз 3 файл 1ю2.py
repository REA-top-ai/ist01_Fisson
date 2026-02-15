maximum = float(input("максимум"))
average = float(input("среднее"))
minimum = float(input("минимум"))
std_deviation = float(input("стандартное отклонение"))


diff_max = (maximum - average) / std_deviation
diff_min = (average - minimum) / std_deviation

if diff_max > 5 or diff_min > 5:
    print("В ваших данных имеются экстремальные значения и требуют предобработки")
elif diff_max > 3 or diff_min > 3:
    print("В ваших данных имеются выбросы и требуют предобработки")
else:
    print("Ваши данные пригодны для анализа")
