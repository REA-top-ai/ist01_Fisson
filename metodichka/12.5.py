drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drink: caffeine for drink, caffeine in zipped_drinks}
print("Словарь напитков и содержания кофеина:")
for drink, mg in drinks_to_caffeine.items():
    print(f"{drink}: {mg} мг")