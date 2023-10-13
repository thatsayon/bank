class User:
    accounts = []

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        User.accounts.append(self)


class Client(User):
    def __init__(self, name, email):
        super().__init__(name, email)


class Admin(User):
    @staticmethod
    def show_accounts():
        for users in User.accounts:
            print(f"Name: {users.name} Email: {users.email}")


us1 = Client("Ayon", "hi")
us2 = Client("Saba", "li")
us3 = Client("Sara", "ali")
