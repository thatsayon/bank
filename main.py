from User import Admin
def main():
    while True:
        print("*"*20)
        print("For User Access Type 1\nFor Admin Access Type 2")
        print("*"*20)
        user_input = int(input("Input 1 or 2: "))

        if user_input == 1:
            print("*" * 20)
            print("To log in type 1\nTo create a new account type 2")
            print("*" * 20)
            user_input = int(input("Input 1 or 2:"))
            break
        elif user_input == 2:
            print("*" * 20)
            admin_name = input("Enter admin username: ")
            admin_pass = input("Enter admin password: ")
            print("*" * 20)
            if admin_name == 'admin' and admin_pass == '123':
                print("Successfully Login")
                print("-"*20)
                print("3. See all user accounts list")
                admin_in = int(input("What you want to do?: "))
                if admin_in == 3:
                    Admin.show_accounts()


if __name__ == '__main__':
    main()