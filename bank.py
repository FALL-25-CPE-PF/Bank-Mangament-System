ADMIN_USER = "admin"
ADMIN_PASS = "1234"

class BankAdmin:
    def __init__(self, accounts):
        self.accounts = accounts

    def admin_login(self):
        return (
            input("Admin Username: ") == ADMIN_USER and
            input("Admin Password: ") == ADMIN_PASS
        )