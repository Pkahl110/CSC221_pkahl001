import game.event as event
import random
import game.combat as combat
import game.superclasses as superclasses
from game.display import announce

class Skeletons (event.Event):

    def __init__ (self):
        self.name = "skeleton attack"

    def process (self, world):
        result = {}
        result["message"] = "the skeletons have been defeated!"
        monsters = []
        min = 4
        uplim = 4
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(combat.Drowned("Pirate captain"))
            monsters[0].speed = 1.2*monsters[0].speed
            monsters[0].health = 2*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            monsters.append(combat.Drowned("Drowned pirate "+str(n)))
            n += 1
        announce ("You are attacked by a group of skeletons!")
        combat.Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result