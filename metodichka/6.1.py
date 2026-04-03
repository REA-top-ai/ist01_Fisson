def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)
print("Нижний предел" + str(low_limit) + "Верхний предел" + str(high_limit))