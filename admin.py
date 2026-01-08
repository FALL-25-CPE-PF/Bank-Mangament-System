from student1_accounts_user import save_accounts, generate_account_number

ADMIN_USER = "admin"
ADMIN_PASS = "1234"


def admin_login():
    user = input("Admin Username: ")
    pwd = input("Admin Password: ")
    return user == ADMIN_USER and pwd == ADMIN_PASS


def admin_create_account(accounts):
    name = input("Enter customer name: ")
    pin = input("Set 4-digit PIN: ")

    if not (pin.isdigit() and len(pin) == 4):
        print("Invalid PIN.")
        return

    acc_no = generate_account_number(accounts)
    accounts[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": 0.0,
        "history": [],
        "blocked": False
    }

    save_accounts(accounts)
    print("Account created successfully. Account Number:", acc_no)


def admin_menu(accounts):
    while True:
        print("\nADMIN MENU")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Unblock Account")
        print("4. Reset PIN")
        print("5. Delete Account")
        print("6. Total Bank Balance")
        print("7. Logout")
        print("8. Block Account")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_create_account(accounts)

        elif choice == "2":
            for acc_no, data in accounts.items():
                status = "BLOCKED" if data["blocked"] else "ACTIVE"
                print(acc_no, data["name"], data["balance"], status)

        elif choice == "3":
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                accounts[acc_no]["blocked"] = False
                save_accounts(accounts)
                print("Account unblocked.")

        elif choice == "4":
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                new_pin = input("Enter new 4-digit PIN: ")
                if new_pin.isdigit() and len(new_pin) == 4:
                    accounts[acc_no]["pin"] = new_pin
                    save_accounts(accounts)
                    print("PIN reset successful.")

        elif choice == "5":
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                del accounts[acc_no]
                save_accounts(accounts)
                print("Account deleted.")

        elif choice == "6":
            total = sum(a["balance"] for a in accounts.values())
            print("Total Bank Balance:", total)

        elif choice == "7":
            break

        elif choice == "8":
            acc_no = input("Enter account number to block: ")
            if acc_no in accounts:
                accounts[acc_no]["blocked"] = True
                save_accounts(accounts)
                print("Account blocked successfully.")
