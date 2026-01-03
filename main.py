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
