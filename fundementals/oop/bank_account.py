
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
        
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    # your code here
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    # your code here
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    # your code here
    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        return self
    # your code here




bob = BankAccount(0.05, 100)
eric = BankAccount(0.10, 150)
eric.deposit(50).deposit(75).deposit(80).withdraw(50).yield_interest().display_account_info()
bob.deposit(50).deposit(75).withdraw(25).withdraw(50).withdraw(75).withdraw(150).yield_interest().display_account_info()
