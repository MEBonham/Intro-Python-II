from room import Room
from player import Player
from item import Item

char_line_limit = 70

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", char_line_limit),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", char_line_limit),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", char_line_limit),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", char_line_limit),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", char_line_limit)
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

# Populate rooms with items
rooms['foyer'].add_item(Item("Potion", "You can drink this to boost your health."))
rooms['foyer'].add_item(Item("Coins", "These can be used to buy stuff."))
rooms['outside'].add_item(Item("Stick", "A very crude weapon."))
rooms['narrow'].add_item(Item("Coin", "This can be used to buy stuff."))
rooms['narrow'].add_item(Item("Coin", "This can be used to buy stuff."))
rooms['narrow'].add_item(Item("Stick", "A very crude weapon."))
rooms['narrow'].add_item(Item("Coin", "This can be used to buy stuff."))
rooms['treasure'].add_item(Item("Rope", "Good for lots of things."))

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
    elif command == "take":
        print(pc.take_item("Coin"))
        
    print(pc.room)
    print(pc.room.display_items())

    command = input("What do you want to do? ")
    print('')