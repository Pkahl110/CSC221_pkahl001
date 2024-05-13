from game import event
import random
import game.config as config

class Falling(event.Event):

    def __init__ (self):
        self.name = "Falling trap"

    def process (self, world):
        c = random.choice(config.the_player.get_pirates())
        result = {}
        deathcause = "died from falling"
        died = c.inflict_damage(c.health, deathcause)
        if died == True:
            result["message"] = c.get_name() + " fell and perished instantly"
            result["newevents"] = []
        return result
