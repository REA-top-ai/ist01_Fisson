client_1 = 'Alice'
client_1_balance = 1000
client_2 = 'Bob'
client_2_balance = 500

amount = 200

def add_money(amount, client_name, client_balance ):
    client_balance += amount
    print(f'{client_name} added {amount}. Balance is {client_balance}')
    return client_balance

def payments(amount, client_name, client_balance):
    if client_balance > amount:
        client_balance -= amount
        print(f'{client_name} pay {amount}. Balance is {client_balance}')
    else:
        print(f'Not enough money. Balance is {client_balance}')


if __name__ == '__main__':
    client_1 = 'Alice'
    client_1_balance = 1000

    client_2 = 'Bob'
    client_2_balance = 500
    client_1_balance = add_money(200, client_1, client_1_balance)
    client_2_balance = add_money(400, client_2, client_2_balance)
    client_2_balance = payments(500, client_2, client_2_balance)