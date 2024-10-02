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
    
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        if self.balance <= 0:
            raise ValueError("Interest must be applied to an Account.")
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"With interest, your new balance is ${self.balance:.2f}.")

    def __str__(self):
        return f"Savings Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate * 100:.2f}%"

        
def main():
    accounts = {}
    while True:
        print('''\nBank Account Management System
        1. Create a Savings Account
        2. Deposit Money
        3. Withdraw Money
        4. Apply Interest (Savings Account Only)
        5. Check Balance")
        6. Exit''')
        choice = input("Choose an option:")
        name = input("Enter account holder name: ")
        if choice == "1":
            accounts[name] = SavingsAccount(name)
            print(f"Savings account created for {name} with balance: ${accounts[name].balance:.2f}")

        elif choice == "2":
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                try:
                    accounts[name].deposit(amount)
                except ValueError:
                    print("Deposit amount must be positive.")
            else:
                print(f"No account found for {name}.")
        elif choice == "3":
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                try:
                    accounts[name].withdraw(amount)
                except ValueError:
                    print("Withdrawal amount is invalid.")
            else:
                print(f"No account found for {name}.")

        elif choice == "4":
            if name in accounts and isinstance(accounts[name], SavingsAccount):
                try:
                    accounts[name].apply_interest()
                except ValueError:
                    print("Interest must be applied to an account.")
            else:
                print(f"No savings account found for {name}.")
        elif choice == "5":
            if name in accounts:
                accounts[name].check_balance()
            else:
                print(f"No account found for {name}.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()