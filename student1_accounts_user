import os

DATA_FILE = "accounts.txt"

def load_accounts():
    accounts = {}
    if not os.path.exists(DATA_FILE):
        return accounts
    with open(DATA_FILE, "r") as file:
        for line in file:
            acc_no, name, pin, balance, history, blocked = line.strip().split("|")
            accounts[acc_no] = {
                "name": name,
                "pin": pin,
                "balance": float(balance),
                "history": history.split(";") if history else [],
                "blocked": blocked == "True"
            }
    return accounts
    
def save_accounts(accounts):
    with open(DATA_FILE, "w") as file:
        for acc_no, data in accounts.items():
            history = ";".join(data["history"])
            file.write(
                f"{acc_no}|{data['name']}|{data['pin']}|{data['balance']}|{history}|{data['blocked']}\n"
            )

def generate_account_number(accounts):
    base = 10000
    return str(base + len(accounts) + 1)

# User operations – Deposit & Withdraw
def deposit(accounts, acc_no):
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid amount.")
        return
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["history"].append(f"Deposited {amount}")
    save_accounts(accounts)
    print("Deposit successful.")

def withdraw(accounts, acc_no):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount.")
        return
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance.")
        return
    accounts[acc_no]["balance"] -= amount
    accounts[acc_no]["history"].append(f"Withdrew {amount}")
    save_accounts(accounts)
    print("Withdrawal successful.")
