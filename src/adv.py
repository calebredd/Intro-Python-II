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

#
# Main
#

decisions = ('n','s','e','w','q')
# Make a new player object that is currently in the 'outside' room.
player = Player("Player1", "outside")
# Write a loop that:
#
currentRoom = player.room
# print(dir(room[player.room]))
    # currentDict = room[currentRoom].__dict__
    # print(currentDict)
# * Prints the current room name
print(room[currentRoom].name)
# * Prints the current description (the textwrap module might be useful here).
print(room[currentRoom].description)
# * Waits for user input and decides what to do.
while player:

    decision = input("\nHow would you like to proceed?\n\n[n] North [s] South [e] East [w] West [q] Quit\n\n")
    while decision not in decisions:
        print("\nPlease make a valid selection to proceed!")
        decision = input("\n\n[n] North [s] South [e] East [w] West [q] Quit\n\n")
# for e in room:
        # print("'{}' is the '{}' and is '{}'\n".format(e, room[e].name, room[e].description))
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    print("\n")
    if(decision == 'q'):
        exit()
    else:
        move = decision+"_to"
        if hasattr(room[currentRoom], move):
            player.move(room[currentRoom][move].name)
            newRoom = currentRoom
            for j in room:
                if(room[j].name == room[currentRoom][move].name):
                    newRoom = j
            currentRoom = newRoom
            print(room[currentRoom].name)
            print(room[currentRoom].description)
            print("\n")
        else:
            print("{} does not have a path in that direction.".format(room[currentRoom].name))
exit()
