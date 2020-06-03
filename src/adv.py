from room import Room

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

# Make a new player object that is currently in the 'outside' room.

from player import Player

player = Player(room['outside'])

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


while True:
    print(player.location.name)
    print(player.location.description)
    player_input = input("Which way wilst though go next? Enter a cardinal direction or enter 'quit': ")
    player_input = player_input.lower().split(' ')

    print(player.path)
    print(player_input[0])


    if (player_input[0] == 'north') or (player_input[0] == 'n') or (player_input[0] == 'south') or (player_input[0] == 's') or (player_input[0] == 'west') or (player_input[0] == 'w') or (player_input[0] == 'east') or (player_input[0] == 'e') or (player_input[0] == 'back'):
        player.move(player_input[0])
        print(player.path)
    elif ((player_input[0] == 'move') or (player_input[0] == 'go') or (player_input[0] == 'walk')) and ( (player_input[1] == 'north') or (player_input[1] == 'n') or (player_input[1] == 'south') or (player_input[1] == 's') or (player_input[1] == 'west') or (player_input[1] == 'w') or (player_input[1] == 'east') or (player_input[1] == 'e') or (player_input[1] == 'back')):
        player.move(player_input[1])
        print(player.path)
    elif player_input[0] == ('q' or 'quit'):
        print("You take a rest. See you next time!")
        break
    else:
        print("Didn't recognize that input, try again.")