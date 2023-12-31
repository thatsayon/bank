from User import Admin, Client
from Account import UserAccount, bank


def client(aid):
    current_user = None
    for user in UserAccount.accounts:
        if user.acc_num == aid:
            current_user = user

    while True:
        print("1. Check available balance\n2. Deposit\n3. Withdraw\n4. Take loan\n5. Transfer money\n6. Transaction history")
        print("7. Exit Client Panel")
        uin = int(input("Choose Option: "))
        if uin == 1:
            for user in UserAccount.accounts:
                if user.acc_num == aid:
                    print("-" * 20)
                    print(f"Available Balance: {user.balance}")
                    print("-" * 20)
        elif uin == 2:
            deposit_amount = int(input("Enter the deposit amount: "))
            current_user.deposit(deposit_amount)
        elif uin == 3:
            withdraw_amount = int(input("Enter the withdraw amount: "))
            current_user.withdraw(withdraw_amount)
        elif uin == 4:
            loan_amount = int(input("Enter the loan amount: "))
            current_user.take_loan(loan_amount)
        elif uin == 5:
            ac_num = int(input("Enter transfer account number: "))
            t_amount = int(input("Enter transfer amount: "))
            current_user.transfer_money(ac_num, t_amount)
        elif uin == 6:
            current_user.show_history()
        elif uin == 7:
            break


def admin():
    while True:
        print("1. Create an admin account\n2. Delete an account\n3. See all user accounts list\n4. Total available balance\n5. Total loan amount\n6. Turn on or off loan feature")
        print("7. Exit admin panel")
        admin_in = int(input("Choose Option: "))
        if admin_in == 1:
            name = input("Enter admin username: ")
            email = input("Enter admin email address: ")
            password = input("Enter admin password: ")
            Admin(name, email, password)
        elif admin_in == 2:
            anum = int(input("Enter the account number you want to delete: "))
            bank.delete_user(anum)
            Admin.delete_user(anum)
        elif admin_in == 3:
            Admin.show_accounts()
        elif admin_in == 4:
            bank.total_balance()
        elif admin_in == 5:
            bank.total_loan()
        elif admin_in == 6:
            bank.loan_on_or_off()
        elif admin_in == 7:
            break


def main():
    while True:
        print("*" * 20)
        print("1. User Access\n2. Admin Access \n3. Close the application")
        print("*" * 20)
        user_input = int(input("Choose Option: "))

        # code to manage a user
        if user_input == 1:
            while True:
                print("*" * 20)
                print("1. Log in\n2. Create a new account\n3. Exit user panel")
                print("*" * 20)
                user_input = int(input("Choose Option: "))

                # log in into the account
                if user_input == 1:
                    email = input("Enter your email address: ")
                    password = input("Enter your password: ")
                    return_data = Client.log_in(email, password)
                    if return_data[0]:
                        print("*"*20)
                        print("Logged in sucessfully")
                        print("*"*20)
                        client(return_data[1])
                    else:
                        print("*"*20)
                        print("Wrong email or password")

                # create an account
                elif user_input == 2:
                    print("-" * 20)
                    username = input("Enter your name: ")
                    email = input("Enter your email address: ")
                    address = input("Enter your address: ")
                    password = input("Enter your password: ")
                    acc_type = None 
                    while True:
                        ac = input("Account Type: Savings or Current (S/C): ")
                        if ac.lower() == 's' or ac.lower() == 'c':
                            acc_type = ac 
                            break 
                        print("Type 's' or 'c'")
                    Client(username, email, address, password, acc_type)

                elif user_input == 3: break
        # code to manage an admin
        elif user_input == 2:
            print("*" * 20)
            admin_name = input("Enter admin username: ")
            admin_pass = input("Enter admin password: ")
            print("*" * 20)
            if admin_name == 'admin' and admin_pass == '123':
                print("Successfully Login")
                print("-" * 20)
                admin()
            elif Admin.log_in(admin_name, admin_pass):
                print("Successfully Login")
                print("-" * 20)
                admin()
            else:
                print("Wrong username or password")

        elif user_input == 3:
            break


if __name__ == '__main__':
    main()
