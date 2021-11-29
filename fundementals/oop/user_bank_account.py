class User:		# here's what we have so far
    def __init__(self, name, email, account_type):
        self.name = name
        self.email = email
        self.account = BankAccount(0.5, 250 , account_type)#required deposit to open account is 250
    # adding the deposit method
    def make_deposit(self, amount,account_type):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount,account_type)
        self.display_user_balance(account_type)	
        # the specific user's account increases by the amount of the value received
        print
        return self

    def open_new_account(self, int_rate ,amount , account_type):
        if account_type == "checking":
            self.account.open_checking(int_rate, amount)
        elif account_type == "savings":
            self.account.open_savings(int_rate, amount)
    
    def make_withdrawal(self, amount,account_type):
        self.account.withdraw(amount, account_type)
        self .display_user_balance(account_type)
        return self
    
    def display_user_balance(self, account_type):
        if account_type == "checking":
            print(f"{self.name}'s Checking Balance: {self.account.checking} ")
        elif account_type =="savings":
            print(f"{self.name}'s Savings Balance: {self.account.savings} ")
        
        return self
    
    def transfer_money(self, account,other_user,  account_type, amount):
            self.account.withdraw(amount, account)
            other_user.account.deposit(amount,account_type)
            self.display_user_balance(account)
            other_user.display_user_balance(account_type)




class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate , balance , account_type ): 
        if account_type == "checking":
            self.open_checking(int_rate, balance)
        elif account_type == "savings":
            self.open_savings(int_rate, balance)
    
    def open_checking(self, int_rate, balance):
        self.checking = balance
        self.checking_interest = int_rate

    def open_savings(self, int_rate, balance):
        self.savings = balance
        self.savings_interest = int_rate
        
        # self.balance = balance
        # self.int_rate = int_rate
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount, account_type):
        if account_type == 'checking':
            self.checking += amount
        elif account_type == "savings":
            self.savings += amount
        
        return self

    # your code here
    def withdraw(self, amount ,account_type):
        if account_type == 'checking' :
            account = self.checking
        elif account_type == "savings" :
            account = self.savings
        
        if account - amount >= 0:
            account -= amount
        else:
                print("Insufficient funds: Charging a $5 fee")
                account -= 5
        return self
    # your code here
    # def display_account_info(self, account_type):
    #     if account_type == "checking":
    #         print(f"{self} Checking Balance: {self.checking} ")
    #     elif account_type == "savings":
    #         print(f"Savings Balance: {self.savings}")
        
        
        
    # your code here
    def yield_interest(self, account_type):
        if account_type == "checking" and self.checking > 0:
            self.checking += self.checking * self.checking_interest
        elif account_type == "savings" and self.savings > 0:
            self.savings += self.savings* self.savings_interest
        else:
            print("Insufficient funds no intrest applied!")
    # your code here
    



eric = User("Eric", "et@et.com","savings")
eric.open_new_account(.02, 300, "checking")
eric.display_user_balance("savings").display_user_balance("checking")

eric.make_deposit(100, "checking").make_deposit(75,"savings")
bob = User ('Bob', "Bob@bobross.com", "checking")
bob.display_user_balance('checking')
bob.open_new_account(.06, 500, "savings")
bob.display_user_balance("savings")

eric.transfer_money("savings", bob, "checking", 100)
bob.account.yield_interest("savings")
bob.display_user_balance("savings")





