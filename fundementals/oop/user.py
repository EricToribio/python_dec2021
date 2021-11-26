
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
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
guido.make_deposit(75)
guido.make_deposit(40)
guido.make_deposit(100)
guido.make_withdrawal(50)
guido.display_user_balance()

monty.make_deposit(25)
monty.make_deposit(30)
monty.make_withdrawal(20)
monty.make_withdrawal(10)
monty.display_user_balance()

bob.make_deposit(300)
bob.make_withdrawal(50)
bob.make_withdrawal(30)
bob.make_withdrawal(100)
bob.display_user_balance()

guido.transfer_money(bob, 50)
