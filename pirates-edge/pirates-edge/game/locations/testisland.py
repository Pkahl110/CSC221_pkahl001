
from game import location
import game.config as config
from game.display import announce
from game.events import *
from game.combat import Monster
import game.combat as combat
from game.combat import Combat
import random
from game.event import Event
from game import event
from game.items import Item
from game.display import menu


class TestIsland (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "island"
        self.symbol = 'L'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["cave"] = Cave(self)
        self.locations["puzzle room"] = Puzzle_Game(self)
        self.locations['forked path'] = Forked_Path(self)
        self.locations['west path'] = West_Path(self)
        self.locations['east path'] = East_Path(self)
        self.locations['death room'] = Death_Room(self)
        self.locations['battle room'] = Battle_Room(self)
        self.locations['treasure room'] = Treasure_Room(self)

    def enter (self, ship):
        announce ("\narrived at an island")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Beach_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 0
        self.events.append (seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("arrive at the beach. Your ship is at anchor in a small bay to the south.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            announce ("\nYou arrive at a cave")
            config.the_player.next_loc = self.main_location.locations["cave"]
        elif (verb == "east" or verb == "west"):
            announce ("You walk all the way around the island on the beach. It's not very interesting.")


class Cave(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "cave"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

    def enter(self):
        description = "\nYou walk into an open cave on the island."
        announce(description)

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "south": 
            config.the_player.next_loc = self.main_location.locations["beach"]
        elif verb == "north":
            announce("\nYou walk further into the cave.")
            config.the_player.next_loc = self.main_location.locations["puzzle room"]

class Puzzle_Game(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "puzzle room"
        self.solved_puzzles = 0
        self.max_puzzles = 3
        self.verbs['solve'] = self

    def enter(self):
        description = "\nYou enter a mysterious room with strange symbols etched on the walls. In order to proceed, you must solve three different puzzles."
        announce(description)

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "solve":
            if self.solved_puzzles < self.max_puzzles:
                self.solve_puzzle()
            else:
                announce("\nCongratulations! You've solved all the puzzles and unlocked the passage to the next room.")
                self.main_location.puzzles_solved = True
        elif verb == "north" and self.main_location.puzzles_solved:
            announce("\nYou proceed north to the forked path.")
            config.the_player.next_loc = self.main_location.locations["forked path"]
        else:
            announce("\nThere's nothing to do here except solve puzzles!")

    def solve_puzzle(self):
        if self.solved_puzzles == 0:
            announce("\nSolve this equation to proceed: 2 * 3 = ?")
            answer = input("Your answer: ")
            if answer.strip() == "6":
                self.solved_puzzles += 1
                announce("\nCorrect! You hear a mechanism unlocking somewhere in the room.")
            else:
                announce("\nIncorrect! The walls seem to rumble in disappointment.")
        elif self.solved_puzzles == 1:
            announce("\nSolve this equation to proceed: 10 - 4 = ?")
            answer = input("Your answer: ")
            if answer.strip() == "6":
                self.solved_puzzles += 1
                announce("\nCorrect! You hear a mechanism unlocking somewhere in the room.")
            else:
                announce("\nIncorrect! The walls seem to rumble in disappointment.")
        elif self.solved_puzzles == 2:
            announce("\nSolve this equation to proceed: 8 / 2 = ?")
            answer = input("Your answer: ")
            if answer.strip() == "4":
                self.solved_puzzles += 1
                announce("\nCorrect! You hear a mechanism unlocking somewhere in the room.")
            else:
                announce("\nIncorrect! The walls seem to rumble in disappointment.")

class Forked_Path(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "forked path"
        self.verbs['east'] = self
        self.verbs['west'] = self

    def enter(self):
        
        description = ("\nYou enter into a forked path, your options are to go east or to go west to go further in the cave." +
                 "\nThere is a riddle on the wall, it says..." +
                 "\nI'm a path, both wild and free," +
                 "\nTo the land where the sun dips in glee." +
                 "\nFollow me where the wild winds blow," +
                 "\nBut beware, eastward's not where you go.")
        announce(description)
       

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "west":
            announce("\nYou go down the west path")
            config.the_player.next_loc = self.main_location.locations["west path"]
        elif verb == "east":
            announce("\nYou go down the east path")
            config.the_player.next_loc = self.main_location.locations["east path"]
        else:
            announce("\nI'm sorry, I didn't understand that command.")

class West_Path(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "west path"
        self.verbs['enter'] = self

    def enter(self):
        description = "\nYou get to a door down the West path would you like to enter?"
        announce(description)

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "enter":
            announce("\nYou enter through the door down the west path")
            config.the_player.next_loc = self.main_location.locations["battle room"]
           
class East_Path(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "east path"
        self.verbs['enter'] = self

    def enter(self):
        description = "\nYou get to a door down the East path would you like to enter?"
        announce(description)

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "enter":
            announce("\nYou enter through the door down the east path")
            config.the_player.next_loc = self.main_location.locations["death room"]


class Skeletons(Monster):
    def __init__(self, name):
        attacks = {}
        attacks["slash"] = ["slashes", random.randrange(35,51), (5,15)]
        attacks["punch 1"] = ["punches",random.randrange(35,51), (1,10)]
        attacks["punch 2"] = ["punches",random.randrange(35,51), (1,10)]
        super().__init__(name, random.randrange(40,60), attacks, 180 + random.randrange(-20,21))

class Skeleton_Attack(event.Event):
    def __init__(self):
        self.name = "skeleton attack"

    def process(self, world):
        result = {}
        result["message"] = "The skeletons have been defeated!"
        monsters = []
        min_appearing = 4
        max_appearing = 4
        n_appearing = random.randint(min_appearing, max_appearing)
        for i in range(n_appearing):
            monsters.append(combat.Skeleton("Skeleton " + str(i + 1)))
        announce("You are attacked by a group of skeletons!")
        combat.Combat(monsters).combat()
        result["newevents"] = [self]
        return result

class Battle_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "battle room"
        self.verbs['north'] = self  # Adding 'north' verb
        
    def enter(self):
        announce("\nYou enter into the room and the door slams closed behind you!")
        announce("\nYou and your crew get attacked by a group of skeletons")
        self.process_verb("north", [], [])  # Automatically start the battle event
    
    def process_verb(self, verb, cmd_list, nouns):
        if verb == 'north':
            # Trigger the battle event here
            monsters = [Skeletons(Monster) for _ in range(4)]  # Assuming Skeletons is a class that creates skeleton enemies
            Combat(monsters).combat()  # Start combat with the skeletons
        else:
            announce("\nThere's nothing of interest in that direction.")

class Death_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "death room"
        self.verbs['north'] = self
    
    def enter(self):
        description = ("\nYou enter into the room and the door slams closed behind you!")
        announce(description)

class Battle_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "battle room"
        self.verbs['north'] = self  # Adding 'north' verb
        
    def enter(self):
        announce("\nYou enter into the room and the door slams closed behind you!")
        announce("\nYou and your crew get attacked by a group of skeletons")
        self.process_verb("north", [], [])  # Automatically start the battle event
    
    def process_verb(self, verb, cmd_list, nouns):
        if verb == 'north':
            # Trigger the battle event here
            monsters = [Skeletons(Monster) for _ in range(4)]  # Assuming Skeletons is a class that creates skeleton enemies
            combat_result = Combat(monsters).combat()  # Start combat with the skeletons
            if combat_result == "win":
                announce("\nThe skeletons have been defeated!")
                # Transition to the treasure room
                config.the_player.next_loc = self.main_location.locations["treasure room"]
            else:
                announce("\nThe skeletons overpower you! You'll need to try again.")
        else:
            announce("\nThere's nothing of interest in that direction.")

class Treasure_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "treasure room"
        self.verbs['search'] = self

    def enter(self):
        description = "\nYou walk into the next room and find it filled with glittering treasures!"
        announce(description)
        announce("\nCongratulations! You've found the treasure and won the game!")
        # End the game
        config.the_player.gameInProgress = False

    def process_verb(self, verb, cmd_list, nouns):
        if verb == 'search':
            announce("\nYou search the room but find no more treasures. It's time to leave.")
            # End the game
            config.the_player.gameInProgress = False
        else:
            announce("\nThere's nothing of interest to do here.")


            


