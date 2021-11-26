
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bob = User("Bob Ross", "bobross@bobross.com")
guido.make_deposit(75).make_deposit(40).make_deposit(100).make_withdrawal(50).display_user_balance()

monty.make_deposit(25).make_deposit(30).make_withdrawal(20).make_withdrawal(10).display_user_balance()

bob.make_deposit(300).make_withdrawal(50).make_withdrawal(30).make_withdrawal(100).display_user_balance()

guido.transfer_money(bob, 50)