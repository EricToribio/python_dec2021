from modules.player import Player
class Pirate ( Player):

    def __init__(self, name, strength=25, speed=3, health=100):
        super().__init__(name, strength=strength, speed=speed, health=health)

    def grunt(self):
        print(f"{self.name}: ARRRRRRGGhhhh!")
        return self

    def shout(self):
        print(f"{self.name}: ARRRRRGGhhh FREE RUM!!!")
        return self

    def victory(self):
        print(f'{self.name} is Victorious!!' )
        print( f'{self.name}: Where is my Rum!!')

class Sword_Pirate ( Pirate ):
    def __init__(self, name, strength=26, speed=8, health=110):
        super().__init__(name, strength=strength, speed=speed, health=health)
        
class Blunderbuss_Pirate ( Pirate ):
    def __init__(self, name , strength=20, speed=13, health=150):
        super().__init__(name, strength=strength, speed=speed, health=health)

class Axe_Pirate ( Pirate ):
    def __init__(self, name, strength=16, speed=10, health=200):
        super().__init__(name, strength=strength, speed=speed, health=health)