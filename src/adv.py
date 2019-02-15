from room import Room, Store
from player import Player
from item import Item, LightSource
import textwrap

# Declare game-wide "constants"
char_line_limit = 70

# Declare global functions

wrapper = textwrap.TextWrapper(width=char_line_limit, replace_whitespace=False)
def print_wrap(foo):
    if not isinstance(foo, str):
        bar = str(foo)
    else:
        bar = foo
    split = bar.split("\n")
    for paragraph in split:
        print(wrapper.fill( text=paragraph ))

# Declare all the rooms

rooms = {
    'store':   Store("General Store", "A jolly fat bearded man sits behind the counter. \"Yessir, commerce happens here!\" he says.", True),
    'town':     Room("Town Gate", "Here is the gate to a small village south of the mountain. To the west is the general store. To the east is the tavern.", True),
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons.", True),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", True),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", False),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", False),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", False)
}

# Link rooms together

rooms['store'].e_to = rooms['town']
rooms['town'].w_to = rooms['store']
rooms['town'].n_to = rooms['outside']
rooms['outside'].s_to = rooms['town']
rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

# Populate rooms with items
rooms['foyer'].add_item(Item("Potion", "You can drink this to boost your health.", 12))
rooms['foyer'].add_item(Item("Coins", "These can be used to buy stuff.", 10))
rooms['foyer'].add_item(LightSource("Lamp", "This burns oil for light.", 3))
rooms['outside'].add_item(Item("Stick", "A very crude weapon.", 0))
rooms['narrow'].add_item(Item("Coin", "This can be used to buy stuff.", 1))
rooms['narrow'].add_item(Item("Coin", "This can be used to buy stuff.", 1))
rooms['narrow'].add_item(Item("Stick", "A very crude weapon.", 0))
rooms['narrow'].add_item(Item("Coin", "This can be used to buy stuff.", 1))
rooms['treasure'].add_item(Item("Rope", "Good for lots of things.", 5))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
pc = Player( rooms['outside'] )

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
move_error = "You can't move in that direction!\n"
command = None

print('')
while command != "q":

    # Move the player if they just entered a movement direction, or tell them they can't.
    if command == "north" or command == "n":
        if pc.room.n_to:
            pc.room = pc.room.n_to
        else:
            print(move_error)
    elif command == "south" or command == "s":
        if pc.room.s_to:
            pc.room = pc.room.s_to
        else:
            print(move_error)
    elif command == "east" or command == "e":
        if pc.room.e_to:
            pc.room = pc.room.e_to
        else:
            print(move_error)
    elif command == "west" or command == "w":
        if pc.room.w_to:
            pc.room = pc.room.w_to
        else:
            print(move_error)

    # View inventory
    elif command == "i" or command == "inv" or command == "inventory":
        print_wrap( pc.display_items() )
        print("")

    # Parse more complex commands as multiple words
    elif command:
        complex_command = command.split(' ', 1)

        if len(complex_command) == 2:
            verb = complex_command[0]
            noun = complex_command[1]

            if verb == "take" or verb == "get":
                print(pc.try_take_item( noun.capitalize() ))
            elif verb == "drop":
                print(pc.try_drop_item( noun.capitalize() ))
            elif verb == "sell":
                print(pc.try_sell_item( noun.capitalize() ))
            elif verb == "buy":
                print(pc.try_buy_item( noun.capitalize() ))

        else:
            print("Command not understood.\n")
        
    if pc.can_see():
        print_wrap( pc.room )
        print_wrap( pc.room.display_items() )
    else:
        print("It's pitch black!")

    command = input("What do you want to do? ")
    print('')