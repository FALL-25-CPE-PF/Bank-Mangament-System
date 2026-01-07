from student1_accounts_user import load_accounts, deposit, withdraw
from student2_user_security import user_login, transfer_money, check_balance, view_history
from admin import admin_login, admin_menu

def main():
    accounts = load_accounts()

    while True:
        print("\nBANK ACCOUNT MANAGEMENT SYSTEM")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_no = user_login(accounts)
            if acc_no:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer Money")
                    print("4. Check Balance")
                    print("5. View History")
                    print("6. Logout")

                    opt = input("Choose option: ")

                    if opt == "1":
                        deposit(accounts, acc_no)
                    elif opt == "2":
                        withdraw(accounts, acc_no)
                    elif opt == "3":
                        transfer_money(accounts, acc_no)
                    elif opt == "4":
                        check_balance(accounts, acc_no)
                    elif opt == "5":
                        view_history(accounts, acc_no)
                    elif opt == "6":
                        break
        elif choice == "2":
            if admin_login():
                admin_menu(accounts)
            else:
                print("Admin login failed.")

        elif choice == "3":
            print("Program closed.")
            break


if __name__ == "__main__":
    main()
