from bank_module import BankAccount

account = BankAccount(101, "Shane", 1000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance Check")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter amount: "))
        print(account.deposit(amt))

    elif choice == "2":
        amt = float(input("Enter amount: "))
        print(account.withdraw(amt))

    elif choice == "3":
        print(account.check_balance())

    elif choice == "4":
        break

    else:
        print("Invalid choice")
