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
        print("\nAccount Created Successfully!!!\nPlease log in now to use our facilities\n")

    @staticmethod
    def log_in(email, password):
        for users in User.accounts:
            if email == users.email and password == users.password:
                return [True, users.account_num]
        return [False]


class Admin(User):
    @staticmethod
    def show_accounts():
        for users in User.accounts:
            print(f"Name: {users.name} Email: {users.email} Account Number: {users.account_num}")

    @staticmethod
    def delete_user(ac_num):
        for users in User.accounts:
            if users.account_num == ac_num:
                User.accounts.remove(users)
