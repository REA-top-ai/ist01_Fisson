sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location_data in sales_data:
    for scoops in location_data:
        scoops_sold += scoops
print(scoops_sold)