class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"₹{amount} deposited successfully"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
       
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"₹{amount} withdrawn successfully"

    def check_balance(self):
        return f"Current balance: ₹{self.balance}"
