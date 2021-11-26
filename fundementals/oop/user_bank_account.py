class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(0.5, 250)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.deposit(amount)	# the specific user's account increases by the amount of the value received
        return self
    
    def make_withdrawal(self, amount):
        self.balance.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.display_account_info())
    
    def transfer_money(self, other_user, amount):
        if self.balance - amount > 0:
            self.balance - amount
            other_user.balance + amount
            self.display_user_balance()
            other_user.display_user_balance()
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5



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

eric = User("Eric", "et@et.com")
eric.make_deposit(100)