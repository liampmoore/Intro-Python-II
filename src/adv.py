from room import Room
from rooms import rooms
from items import items

#
# Main
#



import json
import os
from player import Player

# Try to load player with specified name
# If no file is found create a new player with specified name that is currently in the 'outside' room.


## Load function
def load():
    while True:
        name = input("What is thy name adventurer? ")
        name = name.replace(" ", "_")
        if os.path.exists("./saves/" + name + ".json"):
            savefile = open("./saves/" + name + ".json", "r")
            player_json = savefile.read()
            player_dict = json.loads(player_json)
            player = Player(name = player_dict['name'], location = rooms[player_dict["location"]], items = [items[item_id] for item_id in player_dict["items"]])
            print(f"Game loaded. Welcome back, {player.name}.")
            return player
        else:
            player = Player(name, rooms['outside'])
            print(f"New game. Welcome, {player.name}")
            return player
            

## Save function
def save(player):
    if not os.path.exists('saves'):
        os.makedirs('saves')
    filename = "./saves/{}.json".format(player.name)
    savefile = open(filename, "w")
    savefile.write(player.jsonformat())
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

while True:
    print(player.location.name)
    print(player.location.description)
    player_input = input("Which way wilst though go next? Enter a cardinal direction or enter 'quit': ")
    player_input = player_input.lower().split(' ')

    if (player_input[0] == 'north') or (player_input[0] == 'n') or (player_input[0] == 'south') or (player_input[0] == 's') or (player_input[0] == 'west') or (player_input[0] == 'w') or (player_input[0] == 'east') or (player_input[0] == 'e') or (player_input[0] == 'back'):
        player.move(player_input[0])
    elif ((player_input[0] == 'move') or (player_input[0] == 'go') or (player_input[0] == 'walk')) and ( (player_input[1] == 'north') or (player_input[1] == 'n') or (player_input[1] == 'south') or (player_input[1] == 's') or (player_input[1] == 'west') or (player_input[1] == 'w') or (player_input[1] == 'east') or (player_input[1] == 'e') or (player_input[1] == 'back')):
        player.move(player_input[1])
    elif (player_input[0] == 'inventory'):
        player.inventory()
    elif (player_input[0] == 'search'):
        player.location.search()
    elif (player_input[0] == 'q') or (player_input[0] == 'quit'):
        while True:
            should_save = input("Would you like to save before quitting? Y/n")
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
    else:
        print("Didn't recognize that input, try again.")