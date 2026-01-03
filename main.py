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
