#Bank Account System

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: $"))
        if amount <= self.balance:
            self.balance -= amount
            print (f"The withdrawal of amount ${amount} is successful. Your current balance is ${self.balance}")
        else:
            print("Insufficient Balance")

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: $"))
        self.balance += amount
        print (f"The amount of ${amount} is deposited in your account")

    def check_balance(self):
        print(f"Your account has a balance of ${self.balance}")

acc= BankAccount("Andrew", 1200)
acc.withdraw()
acc.deposit()
acc.check_balance()
