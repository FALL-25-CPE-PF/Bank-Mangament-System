def transfer_money(accounts, sender):
    receiver_no = input("Enter receiver account number: ")

    if receiver_no not in accounts or receiver_no == sender.acc_no:
        print("Invalid receiver.")
        return

    amount = float(input("Enter transfer amount: "))
    if amount <= 0 or amount > sender.balance:
        print("Invalid amount.")
        return

    receiver = accounts[receiver_no]
    sender.balance -= amount
    receiver.balance += amount

    sender.add_history(f"Transferred {amount} to {receiver_no}")
    receiver.add_history(f"Received {amount} from {sender.acc_no}")

    Account.save_accounts(accounts)
    print("Transfer successful.")



def admin_menu(admin):
    while True:
        print("\nADMIN MENU")
        print("1.Create 2.View 3.Block 4.Unblock 5.Reset PIN 6.Delete 7.Total 8.Logout")
        ch = input("Choice: ")

        if ch == "1":
            admin.create_account()
        elif ch == "2":
            admin.view_accounts()
        elif ch == "3":
            admin.block_account()
        elif ch == "4":
            admin.unblock_account()
        elif ch == "5":
            admin.reset_pin()
        elif ch == "6":
            admin.delete_account()
        elif ch == "7":
            admin.total_balance()
        elif ch == "8":
            break

def main():
    accounts = Account.load_accounts()
    admin = BankAdmin(accounts)

    while True:
        print("\nBANK ACCOUNT MANAGEMENT SYSTEM")
        print("1.User Login")
        print("2.Admin Login")
        print("3.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc = Account.user_login(accounts)
            if acc:
                while True:
                    print("\n1.Deposit 2.Withdraw 3.Transfer 4.Balance 5.History 6.Logout")
                    op = input("Option: ")

                    if op == "1":
                        acc.deposit(float(input("Amount: ")))
                        Account.save_accounts(accounts)
                    elif op == "2":
                        acc.withdraw(float(input("Amount: ")))
                        Account.save_accounts(accounts)
                    elif op == "3":
                        transfer_money(accounts, acc)
                    elif op == "4":
                        print("Balance:", acc.balance)
                    elif op == "5":
                        acc.show_history()
                    elif op == "6":
                        break

        elif choice == "2":
            if admin.admin_login():
                admin_menu(admin)
            else:
                print("Admin login failed.")

        elif choice == "3":
            print("Program closed.")
            break


if __name__ == "__main__":
    main()