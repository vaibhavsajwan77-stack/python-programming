# Base Class
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance")


# Savings Account
class Saving(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: ₹{interest}. New balance: ₹{self.balance}")


# Current Account
class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Overdraft limit exceeded")


# Loan Account
class LoanAccount(Account):
    def __init__(self, account_number, loan_amount):
        super().__init__(account_number, 0)
        self.loan_amount = loan_amount

    def payloan(self, amount):
        if amount > 0:
            self.loan_amount -= amount
            print(f"Loan paid: ₹{amount}. Remaining loan: ₹{self.loan_amount}")
        else:
            print("Invalid payment")

    def get_loan_balance(self):
        return self.loan_amount


# Testing
s = Saving("CE4500", 40000, 12)
s.deposit(20000)
s.add_interest()

c = CurrentAccount("CERT234R", 150000, 20000)
c.withdraw(10000)

l = LoanAccount("RE3453TE", 10000)
l.payloan(25000)
