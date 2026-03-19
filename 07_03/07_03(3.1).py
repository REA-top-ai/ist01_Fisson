tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}

def assign_table(table_number, name, vip_status=False):
    tables[table_number] = [name, vip_status]

assign_table(6, 'Yoni', False)

assign_table(4, 'Carla')
print(tables)


def print_order(*order_items):
    print(order_items)
print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')