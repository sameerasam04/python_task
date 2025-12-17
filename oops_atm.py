class Account:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(("Deposit", amount))
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("Withdraw", amount))
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount"

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def get_transactions(self):
        return self.transactions

# *******************************************************************
class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner, balance=0.0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, owner, balance)
            return f"Account created for {owner} with balance {balance}"
        return "Account already exists"

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

#   *****************************************************************************************************

class BalanceView:
    def show(self, account):
        return account.get_balance()


class DepositView:
    def execute(self, account, amount):
        return account.deposit(amount)


class WithdrawView:
    def execute(self, account, amount):
        return account.withdraw(amount)


class TransactionHistoryView:
    def show(self, account):
        return account.get_transactions()

#   *************************************************************

# Initialize ATM
atm = ATM()

# Create account
print(atm.create_account("1234567890", "sameera",1400))

# Get account
account = atm.get_account("1234567890")

# Views
balance_view = BalanceView()
deposit_view = DepositView()
withdraw_view = WithdrawView()
history_view = TransactionHistoryView()

# Actions
print(balance_view.show(account))
print(deposit_view.execute(account,1400))
print(withdraw_view.execute(account,1800))
print(balance_view.show(account))
print(history_view.show(account))