class Pet:
    def __init__(self, pet_type, treats, pet_food, pet_name, tricks):
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.treats = treats
        self.pet_food = pet_food
        self.tricks = tricks
        self.health = 50
        self.energy = 100

    def play(self):
        self.energy -= 5
        if self.health < 100:
            self.health += 5

    def eat(self):
        if self.health < 100:
            self.health += 10
        if self.energy < 100:
            self.energy += 5

    def sleep(self):
        if self.health < 75:
            self.health += 25
        elif self.health > 75:
            self.health = 100

    def noise(self):
        if self.pet_type == "dog":
            print("Woof woof")
        elif self.pet_type == "cat":
            print("Meow meow")
