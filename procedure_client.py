from client_classes import BankAccount


def main():
    client_1 = BankAccount('Alice')
    client_2 = BankAccount('Bob')
    client_1.add_money(200)
    client_1.payments(100)
    client_2.add_money(500)
    client_2.payments(500)

    if __name__ == '__main__':
        main()