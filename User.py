class User:
    accounts = []

    def __init__(self, name, email, address, acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        User.accounts.append(self)


class Client(User):
    def __init__(self, name, email, address, acc_type):
        super().__init__(name, email, address, acc_type)
        print("Created")


class Admin(User):
    @staticmethod
    def show_accounts():
        for users in User.accounts:
            print(f"Name: {users.name} Email: {users.email}")


