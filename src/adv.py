import textwrap
from item import Item
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Items

item = {
    'sword':  Item("sword",
                     "A sharp sword you can use to protect yourself"),

    'stone':  Item("stone", """A large stone you can use to 
protect yourself against your enemies."""),

    'book': Item("book", """A book with all the maps and
information you need to get around in the forest and find your way
to the enchanted castle."""),

    'coin':  Item("coin", """A coin you can use to buy your
way into the next village."""),

    'mirror': Item("mirror", """Ask for guidance using
the mirror with magical powers."""),

    'backpack':  Item("backpack",
                     "A red backpack for carrying all your items"),

    'water':  Item("water", """A pint of water to get you
through your journey."""),

    'knife': Item("knife", """A handy pocket knife to help you
through the forest."""),

    'chain':  Item("chain", """A chain for anything you see 
fit along your journey."""),

    'pen': Item("pen", """A pen for writing or scribbling notes
for sending messages."""),
}

# Assigning items to rooms

room['outside'].items = [item['sword'], item['stone']]
room['foyer'].items = [item['book'], item['coin']]
room['overlook'].items = [item['mirror'], item['backpack']]
room['narrow'].items = [item['water'], item['knife']]
room['treasure'].items = [item['chain'], item['pen']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

my_player = Player("Nayomi", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
dir = ""
while dir != "q":
    print(my_player.current_room)
    # print(textwrap.fill(my_player.current_room.description, 50))
    print("\n[n] Enter n to go north.")
    print("[s] Enter s to go south.")
    print("[w] Enter w to go west.")
    print("[e] Enter e to go east.")
    print("[get item] Enter 'get' followed by an item name.")
    print("[drop item] Enter 'drop' followed by an item name.")
    print("[i] Enter i to see your list of items.")
    print("[q] Enter q to quit.")

    dir = input("\nWhat would you like to do? ").lower()
    if len(dir.split()) == 1:
        if dir == "n":
            if my_player.current_room.n_to is not None:
                my_player.current_room = my_player.current_room.n_to
            else:
                print("You can't move north. Choose another direction.")
        elif dir == "s":
            if my_player.current_room.s_to is not None:
                my_player.current_room = my_player.current_room.s_to
            else:
                print("You can't move south. Choose another direction.")
        elif dir == "e":
            if my_player.current_room.e_to is not None:
                my_player.current_room = my_player.current_room.e_to
            else:
                print("You can't move east. Choose another direction.")
        elif dir == "w":
            if my_player.current_room.w_to is not None:
                my_player.current_room = my_player.current_room.w_to
            else:
                print("You can't move west. Choose another direction.")
        elif dir == "i":
            print(my_player)
        elif dir == "q":
            print("\nThanks for playing. See you later.\n")
            exit()
        else:
            print("Please type 'n', 's', 'w', 'e', 'get item' or 'drop item'.")
    elif len(dir.split()) == 2:
        room_items = [i.name for i in my_player.current_room.items]
        player_items = [i.name for i in my_player.items]
        if dir.split()[0] == 'get':
            if dir.split()[1] in room_items:
                my_player.items.append(item[dir.split()[1]])
                my_player.current_room.items.remove(item[dir.split()[1]])
                item[dir.split()[1]].on_take()
            else:
                print("Sorry, this item is not in the room.")
        else:
            if dir.split()[1] in player_items:
                my_player.items.remove(item[dir.split()[1]])
                my_player.current_room.items.append(item[dir.split()[1]])
                item[dir.split()[1]].on_drop()
            else:
                print("Sorry, you do not have this item.")
    else:
        print("Please type 'n', 's', 'w', 'e', 'get item' or 'drop item'.")
