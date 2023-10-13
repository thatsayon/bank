from User import Admin, Client


def main():
    while True:
        print("*" * 20)
        print("For User Access Type 1\nFor Admin Access Type 2\nTo close the application type 3")
        print("*" * 20)
        user_input = int(input("Input 1, 2 or 3: "))

        # code to manage a user
        if user_input == 1:
            print("*" * 20)
            print("To log in type 1\nTo create a new account type 2")
            print("*" * 20)
            user_input = int(input("Input 1 or 2:"))

            # log in into the account
            if user_input == 1:
                email = input("Enter your email address: ")
                password = input("Enter your password: ")
                if Client.log_in(email, password):
                    pass
                else:
                    print("Wrong email or password")


            # create an account
            elif user_input == 2:
                username = input("Enter your name: ")
                email = input("Enter your email address: ")
                address = input("Enter your address: ")
                password = input("Enter your password: ")
                acc_type = input("Account Type: Savings or Current (S/C): ")
                Client(username, email, address, password, acc_type)

        # code to manage an admin
        elif user_input == 2:
            print("*" * 20)
            admin_name = input("Enter admin username: ")
            admin_pass = input("Enter admin password: ")
            print("*" * 20)
            if admin_name == 'admin' and admin_pass == '123':
                print("Successfully Login")
                print("-" * 20)
                while True:
                    print("3. See all user accounts list")
                    print("7. Exit from admin panel")
                    admin_in = int(input("What you want to do?: "))
                    if admin_in == 3:
                        Admin.show_accounts()
                    elif admin_in == 7:
                        break
            else:
                print("Wrong username or password")

        elif user_input == 3:
            break


if __name__ == '__main__':
    main()
