inventory = [
    "двухспальная кровать", "двухспальная кровать", "изголовье", "двухспальная кровать",
    "двуспальная кровать", "комод", "комод", "стол", "стол", "тумбочка", "тумбочка",
    "королевская кровать", "двуспальная кровать", "две односпальные кровати",
    "две односпальные кровати", "простыни", "простыни", "подушка", "подушка"
]

inventory_len = len(inventory)
print(inventory_len)
first = inventory[0]
print(first)

last = inventory[-1]
print(last)
inventory_2_6 = inventory[2:6]
print(inventory_2_6)
first_3 = inventory[:3]
print(first_3)
twin_beds = inventory.count("две односпальные кровати")
print(twin_beds)
inventory.sort()
print(inventory)