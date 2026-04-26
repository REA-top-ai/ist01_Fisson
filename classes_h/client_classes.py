from abc import ABC, abstractmethod

class AbstractBankAccount(ABC):
    new_id = 1

    def __init__(self, client_name):
        self.id = AbstractBankAccount.new_id
        AbstractBankAccount.new_id += 1
        self.client_name = client_name
        self._balance = 0  # защищенный атрибут

    @abstractmethod
    def add_money(self, amount):
        pass

    @abstractmethod
    def payments(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


class BankAccount(AbstractBankAccount):
    def add_money(self, amount):
        self._balance += amount
        print(f'{self.client_name} added {amount}. Balance is {self._balance}')

    def payments(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f'{self.client_name} pay {amount}. Balance is {self._balance}')
        else:
            print(f'Not enough money. Balance is {self._balance}')

    def get_balance(self):
        return self._balance



class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = []  # список счетов клиента

    def create_bank_account(self):
        new_account = BankAccount(self.name)
        self.accounts.append(new_account)
        print(f'Account {new_account.id} created for {self.name}')
        return new_account

    def get_total_balance(self):
        total = sum(acc.get_balance() for acc in self.accounts)
        print(f'Total balance for {self.name}: {total}')
        return total



client1 = Client('Alice')
acc1 = client1.create_bank_account()
acc1.add_money(1000)
acc1.payments(300)

client2 = Client('Bob')
acc2 = client2.create_bank_account()
acc2.add_money(500)

accounts_list = [acc1, acc2]
for acc in accounts_list:
    print(f'Account {acc.id} balance: {acc.get_balance()}')

class BankSystem:
    def __init__(self):
        self.accounts = []

    def __len__(self):
        return len(self.accounts)

    def __add__(self, account):
        self.accounts.append(account)
        print(f'Account {account.id} added to bank system')
        return self


system = BankSystem()
system + acc1
system + acc2
print(f'Total accounts in system: {len(system)}')