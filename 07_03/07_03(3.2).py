tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': 'Orange Juice, Apple Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {}
}

def assign_table(table_number, name, vip_status=False):
    tables[table_number] = {
        'name': name,
        'vip_status': vip_status,
        'order': ''
    }

def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    print(f"Заказ для стола {table_number}:")
    for item in order_items:
        print(f"- {item}")
assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Стейк', 'Морской окунь', 'Бутылка вина')

print("\nИтоговая информация о столах:")
print(tables)