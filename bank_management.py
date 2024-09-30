class BankAccount:
    def __init__(self,account_holder,balance=0.0):
        self.account_holder = account_holder 
        self.balance = balance
    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be Positive.")
        self.balance += amount
        print(f"${amount:.2f} has been deposited. Your new balance is ${self.balance:.2f}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be Positive.")
        if amount > self.balance:
            raise ValueError("Insufficient Balance.")
        self.balance-=amount
        print(f"${amount:.2f} has been withdrawn. Your new balance is ${self.balance:.2f}")
    
    def check_balance(self):
        print(f"{self.account_holder}'s balance is ${self.balance:.2f}")
    