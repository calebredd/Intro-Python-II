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

room['outside'].items= ['gold','silver','murr'] 
#
# Main
#

decisions = ('n','s','e','w','q', 'i', 'take')
# Make a new player object that is currently in the 'outside' room.
player = Player("Player1", room["outside"])
# Write a loop that:
decision = ''
while decision != 'q':
# * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
# * Waits for user input and decides what to do.
    if( len(player.current_room.items) ):
        print(f'Items in room: {", ".join(player.current_room.items)}\n')
    decision = input("\nHow would you like to proceed?\n\n[n] North [s] South [e] East [w] West \n[take <item-name1> <item-name2> ....] Take Item(s) [take all] Take All Items \n[i] Open Inventory \n[q] Quit Game\n\n")
    while decision.split(' ')[0] not in decisions:
        print("\nPlease make a valid selection to proceed!")
        decision = input("\n\n[n] North [s] South [e] East [w] West \n[take <item-name1> <item-name2> ...] Take Item(s) [take all] Take All Items\n[i] Open Inventory \n[q] Quit Game\n\n")
# for e in room:
        # print("'{}' is the '{}' and is '{}'\n".format(e, room[e].name, room[e].description))
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    print("\n")
    if(decision == 'q'):
        print("Goodbye!")
    elif(decision[:4] == 'take'):
        grabList = decision.split(' ')
        grabList.remove('take')
        if( len(grabList) == 1 and grabList[0] == 'all'):
            for x in player.current_room.items:
                player.inventory.append(x)
            player.current_room.items = []
        elif( len(grabList) ):
            i=0
            while i < len(grabList):
                if( grabList[i] in player.current_room.items ):
                    player.inventory.append(grabList[i])
                    player.current_room.items.remove(grabList[i])
                else:
                    print("This room does not have that item.")
                i+=1
            print("You now have:",', '.join(player.inventory), 'in your inventory\n')
        else:
            print("The room is empty!\n")
    elif(decision == 'i'):
        if( len(player.inventory) ):
            print('You have:', ', '.join(player.inventory), '\n' )
            while decision != 'c':
                decision = input("[drop <item-name1> <item-name2>....] Drop Item(s),  [c] Close Inventory [q] Quit Game\n")
                if( decision == 'c' ):
                    break
                if( decision == 'q' ):
                    print("Goodbye!")
                    exit()
                if( decision[:4] == 'drop' ):
                    dropList = decision.split(' ')
                    dropList.remove('drop') 
                    if( len(dropList) == 1 and dropList[0] == 'all'):
                        for x in player.inventory:
                            player.current_room.items.append(x)
                        player.inventory=[]
                    else:
                        i=0
                        while i < len(dropList):
                            if( dropList[i] in player.inventory ):
                                player.current_room.items.append(dropList[i])
                                player.inventory.remove(dropList[i])
                            else:
                                print("You do not have that item.")
                            i+=1
                    if( len(player.inventory) ):
                        print(f"You now have: {', '.join(player.inventory)} in your inventory\n")
                    else:
                        print(f"You now have no items in your inventory\n")
                        decision = 'c'
        else:
            print("You are not carrying anything in your satchel of treasures.\n")
    else:
        move = decision+"_to"
        if hasattr(player.current_room, move):
            player.current_room=getattr(player.current_room, move)
            print("\n\n")
        else:
            print("{} does not have a path in that direction.\n".format(player.current_room.name))
exit()
