from Account import UserAccount


class User:
    accounts = []

    def __init__(self, name, email, address, password, acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.acc_type = acc_type
        self.account_num = len(User.accounts) + 1234
        User.accounts.append(self)


class Client(User):
    def __init__(self, name, email, address, password, acc_type):
        super().__init__(name, email, address, password, acc_type)
        UserAccount(self.account_num)
        print("*"*20)
        print("\nAccount Created Successfully!!!\nPlease log in to use our facilities\n")

    @staticmethod
    def log_in(email, password):
        for users in User.accounts:
            if email == users.email and password == users.password:
                return [True, users.account_num]
        return [False]


class Admin(User):
    accounts = []
    def __init__(self, name, email, password):
        self.name = name 
        self.email = email 
        self.password = password
        Admin.accounts.append(self)
        print("*"*20)
        print("Admin account created successfully!")
        print("*"*20)
        
    @staticmethod
    def show_accounts():
        print("-"*20)
        print("Accounts list: ")
        for users in User.accounts:
            print(f"Name: {users.name} | Email: {users.email} | Account Number: {users.account_num}")
        print("-"*20)

    @staticmethod
    def delete_user(ac_num):
        for users in User.accounts:
            if users.account_num == ac_num:
                User.accounts.remove(users)
                print(f"Account {ac_num} deleted successfully")
                print("-"*20)
                return
        print("-"*20)
        print(f"Account {ac_num} doesn't exist")
        print("-"*20)


    @staticmethod
    def log_in(username, password):
        for users in Admin.accounts:
            if username == users.name and password == users.password:
                return True
        return False