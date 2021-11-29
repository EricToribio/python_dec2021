from pet import Pet

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet_type, pet_name, tricks):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(pet_type, treats,pet_food, pet_name, tricks)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self








# class Pet:
#     def __init__(self, pet_type, treats, pet_food, pet_name, tricks):
#         self.pet_type = pet_type
#         self.pet_name = pet_name
#         self.treats = treats
#         self.pet_food = pet_food
#         self.tricks = tricks
#         self.health = 50
#         self.energy = 100

#     def play(self):
#         self.energy -= 5
#         if self.health < 100:
#             self.health += 5

#     def eat(self):
#         if self.health < 100:
#             self.health += 10
#         if self.energy < 100:
#             self.energy += 5

#     def sleep(self):
#         if self.health < 75:
#             self.health += 25
#         elif self.health > 75:
#             self.health = 100

#     def noise(self):
#         if self.pet_type == "dog":
#             print("Woof woof")
#         elif self.pet_type == "cat":
#             print("Meow meow")






eric = Ninja("Eric", "Toribio", "biscuits", "dry", "dog", "Trixie", "Fetch")
print(eric.pet.health)
print(eric.pet.energy)
eric.walk().feed().bathe().feed()
print(eric.pet.health)
print(eric.pet.energy)
