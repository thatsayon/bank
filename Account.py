from abc import ABC, abstractmethod


class Account(ABC):
    accounts = []

    def __init__(self, acc_num=None):
        self.acc_num = acc_num
        self.balance = 0
        self.loan = 0
        Account.accounts.append(self)


class UserAccount(Account):
    def __init__(self, acc_num):
        self.loan_time = 0
        super().__init__(acc_num)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            bank.balance += amount
            print("-" * 20)
            print(f"Deposited ${amount}. New balance is ${self.balance}")
            print("-" * 20)
        else:
            print("-" * 20)
            print("Invalid deposit amount")
            print("-" * 20)

    def withdraw(self, amount):
        if amount > bank.balance:
            print("-" * 20)
            print("Bank is bankrupt")
            print("-" * 20)
            return
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            bank.balance -= amount
            print("-" * 20)
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
            print("-" * 20)
        else:
            print("-" * 20)
            print("Invalid withdraw amount")
            print("-" * 20)

    def take_loan(self, amount):
        if self.loan_time >= 2:
            print("-" * 20)
            print(f"Can't take loan more then 2 times")
            print("-" * 20)
            return
        if not bank.loan_enable:
            print("-" * 20)
            print("Loan feature is turned off by the bank.")
            print("-" * 20)
            return
        if bank.balance < amount:
            print("-" * 20)
            print("Bank doesn't have the money to give loan.")
            print("-" * 20)
            return

        self.balance += amount
        self.loan += amount
        self.loan_time += 1
        bank.loan += amount
        bank.balance -= amount
        print("-" * 20)
        print(f"${amount} loan has been added to your account. New balance ${self.balance} and total loan ${self.loan}")
        print("-" * 20)

    def transfer_money(self, ac_num, amount):
        for users in Account.accounts:
            if users.acc_num == ac_num:
                if self.balance >= amount:
                    users.balance += amount
                    self.balance -= amount
                    print("-" * 20)
                    print(f"${amount} has been successfully transferred. New balance ${self.balance}")
                    print("-" * 20)
                else:
                    print("-" * 20)
                    print("You don't have enough money to transfer")
                    print("-" * 20)
            else:
                print("-" * 20)
                print("Account does not exist")
                print("-" * 20)


class BankAccount(Account):
    def __init__(self):
        self.loan_enable = True
        super().__init__()

    def total_balance(self):
        print("-" * 20)
        print(f"Total available bank balance is: {self.balance}")
        print("-" * 20)

    def total_loan(self):
        print("-" * 20)
        print(f"Total loan amount is: {self.loan}")
        print("-" * 20)

    def loan_on_or_off(self):
        if self.loan_enable:
            uin = input("Loan feature is turned on. Do you want to turned it off?(Y/N): ")
            self.loan_enable = not self.loan_enable if uin.lower() == 'y' else None
        else:
            uin = input("Loan feature is turned off. Do you want to turned it onn?(Y/N): ")
            self.loan_enable = not self.loan_enable if uin.lower() == 'y' else None


    def delete_user(self, acc_num):
        for users in Account.accounts:
            if users.acc_num == acc_num:
                print("-" * 20)
                confirm = input(f"Do you want to delete account {acc_num}?(Y/N): ")
                if confirm.lower() == 'y':
                    Account.accounts.remove(users)
                    print(f"Account deleted successfully!")
                    print("-" * 20)


bank = BankAccount()
