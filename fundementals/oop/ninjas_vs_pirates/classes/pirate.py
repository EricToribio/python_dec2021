from random import randint
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if ninja.dodge(self.speed, self.strength) == True:
            damage = randint(self.speed, self.strength)
            ninja.health -= damage
            print(f'{self.name} did {damage} health damage!')
        else:
            print(f"{ninja.name} Dodged your attack!")
        return self

    def dodge(self, speed, strength):
        hit_chance = randint(speed, strength)
        dodge_chance = randint(self.speed, self. strength)
        if hit_chance < dodge_chance: 
            return False
        else:
            return True