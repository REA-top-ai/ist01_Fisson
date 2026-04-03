# 1. Создаем переменную clothes
clothes = "домашняя одежда"
print("У меня большой гардероб")

times_of_day = ["Утром", "Днем", "Вечером", "Ночью"]

for time in times_of_day:
    print(f"{time} лучше всего подходит {clothes}")


def meal_p(meal_type, meal):
    print(f"На {meal_type} лучше всего подходит {meal}")
meal = "овсяная каша"

print("Мои предпочтения в еде")
meal_p("завтрак", meal)

lunch = "суп и салат"
dinner = "курица с овощами"
meal_p("обед", lunch)
meal_p("ужин", dinner)