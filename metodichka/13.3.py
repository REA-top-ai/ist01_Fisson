caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["match"] = 30
try:
    print(caffeine_level['match'])
except KeyError:
    print("Неизвестный уровень кофеина")