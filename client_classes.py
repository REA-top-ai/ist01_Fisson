from abc import ABC, abstractmethod


class BankAccount:

    @abstractmethod
    def add_money(self, name):
        pass


    class DepositBankAccount(ABC):
    def __init__(self, client_name):
        self.client_name = client_name
        self_balance = 0

    def add_money(self, amount):
        self.__balance += amount
        print(f'{self.__client_name} added {amount}. Balance is {self.__client_balance}')

    def payments(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'{self.__client_name} pay {amount}. Balance is {self.___balance}')
        else:
            print(f'Not enough money. Balance is {self.__balance}')

    def get_balance(self):
        return self.__balance

class Client:
    def __init__(self, name):
        self.name = name
        self.account = []

    def create_bank_account(self):
        new_account = BankAccount(self.name)
        self.account.append(new_account)
