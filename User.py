class User:
    accounts = []

    def __init__(self, name, email, address, password, acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.acc_type = acc_type
        User.accounts.append(self)


class Client(User):
    def __init__(self, name, email, address, password, acc_type):
        super().__init__(name, email, address, password, acc_type)
        print("\nAccount Created Successfully!!!\nPlease log in now to use our facilities\n")

    @staticmethod
    def log_in(email, password):
        for users in User.accounts:
            if email == users.email and password == users.password:
                return True
        return False


class Admin(User):
    @staticmethod
    def show_accounts():
        for users in User.accounts:
            print(f"Name: {users.name} Email: {users.email}")


