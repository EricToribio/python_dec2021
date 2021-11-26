class User:
    # ! Class Atribute
    population = 0
    # ! constructor function!!!  creates the instance of an object
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.population += 1
    
    def greeting(self):
        print(f"Hello my name is { self.first_name} !")
    
    @classmethod
    def user_population(cls):
        print(f"{cls.population} users in the program.")
    
    @staticmethod
    def validate_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
        return is_valid


adrien = User("Adrien", "Dion", 39)
bob = User("Bob", "Ross", 55)
eric = User("Eric", "Toribio", 29)
patricia = User("Patricia", "Toribio", 6)
adrien.greeting()

# TODO  Calling a class method
User.user_population()









    

# # declare a class and give it name User
# class User:		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# User()
# guido = User()
# monty = User()
# # Accessing the instance's attributes
# print(guido.name)	# output: Michael
# print(monty.name)	# output: Michael

# guido.name = "Guido"
# print(guido.name) # output: Guido
# monty.name = "Monty"
# print(monty.name) # output: Monty

# class User:
#     # declaring a class attribute
#     bank_name = "First National Dojo"		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# guido = User()
# monty = User()
# User.bank_name = "Dojo Credit Union"
# print(guido.bank_name) # output: Dojo Credit Union 
# print(monty.bank_name) # output: First National Dojo

# User.bank_name = "Bank of Dojo"


# print(guido.bank_name) # output: Bank of Dojo 
# print(monty.bank_name) # output: Bank of Dojo

# class User:
#     # class attributes get defined in the class 
#     bank_name = "First National Dojo"
#     def __init__(self , name, email_address):
#     	# we assign them accordingly
#         self.name = name
#         self.email = email_address
#     	# the account balance is set to $0
#         self.account_balance = 0
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python



# class User:		# here's what we have so far
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
#     # adding the deposit method
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#         self.account_balance += amount	# the specific user's account increases by the amount of the value received

# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50

