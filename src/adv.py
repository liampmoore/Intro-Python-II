

#
# Main
#



import json
import os
from player import Player
from items import items

# Try to load player with specified name
# If no file is found create a new player with specified name that is currently in the 'outside' room.

## Load function
def load():
    while True:
        inputname = input("What is thy name adventurer? ")
        inputname = inputname.replace(" ", "_")
        if os.path.exists("./saves/" + inputname + ".json"):
            savefile = open("./saves/" + inputname + ".json", "r")
            player_json = savefile.read()
            player_dict = json.loads(player_json)
            player = Player(**player_dict)
            print(f"Game loaded. Welcome back, {player.name}.")
            return player
        else:
            player = Player(name = inputname, location = 'outside')
            print(f"New game. Welcome, {player.name}")
            return player
            

## Save function
def save(player):
    if not os.path.exists('saves'):
        os.makedirs('saves')
    filename = "./saves/{}.json".format(player.name)
    savefile = open(filename, "w")
    savefile.write(json.dumps(player.save()))
    savefile.close()
    print("Game saved!")



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# If the user enters 'back' go back one room.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = load()
print(player.location.name)
print(player.location.description)

while True:
    player_input = input("What will you do next? Enter 'help' to see some options: ")
    player_input = player_input.lower().split(' ')

    if (player_input[0] == 'north') or (player_input[0] == 'n') or (player_input[0] == 'south') or (player_input[0] == 's') or (player_input[0] == 'west') or (player_input[0] == 'w') or (player_input[0] == 'east') or (player_input[0] == 'e') or (player_input[0] == 'back'):
        player.move(player_input[0])
        print(player.location.name)
        print(player.location.description)
    elif ((player_input[0] == 'move') or (player_input[0] == 'go') or (player_input[0] == 'walk')) and ( (player_input[1] == 'north') or (player_input[1] == 'n') or (player_input[1] == 'south') or (player_input[1] == 's') or (player_input[1] == 'west') or (player_input[1] == 'w') or (player_input[1] == 'east') or (player_input[1] == 'e') or (player_input[1] == 'back')):
        player.move(player_input[1])
        print(player.location.name)
        print(player.location.description)
    elif (player_input[0] == 'look') or (player_input[0] == 'room') or (player_input[0] == 'location') or (player_input[0] == 'where') or (player_input[0] == 'explore'):
        print(player.location.name)
        print(player.location.description)
    elif (player_input[0] == 'inventory'):
        player.inventory()
    elif (player_input[0] == 'search'):
        player.location.search()
    elif (player_input[0] == 'get') or (player_input[0] == 'take'):
        if player_input[1]:
            item = player.location.takeitem(player_input[1])
            if item:
                player.recieveitem(item)
            else:
                print("That item isn't here.")
        else:
            print("Specify what you'd like to take.")
    elif (player_input[0] == 'drop') or (player_input[0] == 'leave'):
        if player_input[1]:
            item = player.dropitem(player_input[1])
            if item:
                player.location.recieveitem(item)
            else:
                print("You don't have that item.")
        else:
            print("Specify what you'd like to take.")
    elif (player_input[0] == 'q') or (player_input[0] == 'quit'):
        while True:
            should_save = input("Would you like to save before quitting? Y/n ")
            should_save = should_save.lower()
            if (should_save == 'yes') or (should_save == 'y'):
                save(player)
                break
            elif (should_save == 'no') or (should_save == 'n'):
                break
            elif (should_save == ''):
                save(player)
                break
            else:
                print("Didn't recognize that input. Try again.")
        print("See you next time!")
        break
    elif (player_input[0] == 'help') or (player_input[0] == 'commands') or (player_input[0] == 'h'):
        print("You can 'go north' or any other cardinal direction.")
        print("You can 'look' to see the description of the room you are in.")
        print("You can 'search' to try to find any items.")
        print("You can 'take [item]' to put an item you find in your inventory, or 'drop [item]'.")
        print("Type 'quit' to save and quit.")
    elif (player_input[0] == 'clear'):
        os.system('clear')
    else:
        print("Didn't recognize that input, try again. Type 'help' to view the list of commands.")
    for room in player.rooms.values():
        print(f"{room.name} {room.discovered}")