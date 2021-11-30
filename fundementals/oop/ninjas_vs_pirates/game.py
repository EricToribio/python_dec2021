from classes.ninja import Ninja
from classes.pirate import Pirate
from random import randint

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")



while michelangelo.health > 0 and jack_sparrow.health > 0:
    who_attacks = randint(1, 1000)
    if who_attacks % 2 == 0:
        print(f'{michelangelo.name} Attacked')
        michelangelo.attack(jack_sparrow)
        jack_sparrow.show_stats()
    else:
        print(f'{jack_sparrow.name} Attacked')
        jack_sparrow.attack(michelangelo)
        michelangelo.show_stats()



# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# jack_sparrow.attack(michelangelo)
# michelangelo.show_stats()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# jack_sparrow.attack(michelangelo)
# michelangelo.show_stats()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# jack_sparrow.attack(michelangelo)
# michelangelo.show_stats()
