def get_tariff(brand, age, experience, reputation, traffic):
    tariffs = {
        ('Volkswagen Polo', '20-27', '2-9', '1-2', '1-3'): 8,
        ('Volkswagen Polo', '20-27', '2-9', '1-2', '4-7'): 8.5,
        ('Volkswagen Polo', '20-27', '2-9', '3-5', '1-3'): 7.5,
        ('Volkswagen Polo', '20-27', '2-9', '3-5', '4-7'): 7.4,
        ('Volkswagen Polo', '27-34', '2-9', '1-2', '1-3'): 7.2,
        ('Volkswagen Polo', '27-34', '2-9', '3-5', '1-3'): 7,
        ('Volkswagen Polo', '27-34', '2-9', '3', '4-7'): 7.2,
        ('Volkswagen Polo', '27-34', '10-15', '1-2', '1-3'): 6.9,
        ('Volkswagen Polo', '27-34', '10-15', '3-5', '4-7'): 6.6,
        ('Volkswagen Polo', '27-34', '10-15', '1-2', '4-7'): 6.7,

        # BMW X1
        ('BMW X1', '20-27', '2-9', '1-2', '1-3'): 12,
        ('BMW X1', '20-27', '2-9', '1-2', '4-7'): 12.5,
        ('BMW X1', '20-27', '2-9', '3-5', '1-3'): 11.6,
        ('BMW X1', '20-27', '2-9', '3-5', '4-7'): 11.3,
        ('BMW X1', '27-34', '2-9', '1-2', '1-3'): 11.4,
        ('BMW X1', '27-34', '2-9', '3-5', '1-3'): 11.7,
        ('BMW X1', '27-34', '2-9', '3-5', '4-7'): 11,
        ('BMW X1', '27-34', '10-15', '1-2', '1-3'): 10.8,
        ('BMW X1', '27-34', '10-15', '3-5', '4-7'): 10.9,
        ('BMW X1', '27-34', '10-15', '1-2', '4-7'): 11,
    }

    k = (brand, age, experience, reputation, traffic)
    return tariffs.get(k)

brand = input("Марка")
age = input("Возраст водителя")
experience = input("Стаж")
reputation = input("Репутация водителя")
traffic = input("Уровень пробок")
duration = float(input("Длительность поездки (минуты)"))

tariff = get_tariff(brand, age, experience, reputation, traffic)

if tariff is None:
    print("Тариф не найден")
else:
    cost = duration * tariff
    print("Стоимость вашей поездки составит " + str(round(cost, 2)) + " руб.")

