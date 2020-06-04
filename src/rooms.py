import json
from room import Room

# Declare all the rooms



defaultrooms = {
     'outside':  {"name":"Outside Cave Entrance",
                     "description":"North of you, the cave mount beckons", 'id':'outside', 'discovered':True},
    'foyer':    {"name":"Foyer", "description":"""Dim light filters in from the south. Dusty
passages run north and east.""", 'id':'foyer', "item_ids": [0]},

    'overlook': {"name":"Grand Overlook", "description":"""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "id":'overlook'},

    'narrow':   {"name":"Narrow Passage", "description":"""The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'id':'narrow'},

    'treasure': {"name":"Treasure Chamber", "description":"""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "id":'treasure'},
}

def buildrooms(rooms):
    builtrooms = {}
    # Build rooms from room info dictionary
    # If there is a save file
    if rooms:
        for room in rooms:
            builtrooms[room['id']] = Room(**room)
    # If no save file use defaults
    else:
        for room in defaultrooms.values():
            builtrooms[room['id']] = Room(**room)
    # Link rooms together
    builtrooms['outside'].n_to = builtrooms['foyer']
    builtrooms['foyer'].s_to = builtrooms['outside']
    builtrooms['foyer'].n_to = builtrooms['overlook']
    builtrooms['foyer'].e_to = builtrooms['narrow']
    builtrooms['overlook'].s_to = builtrooms['foyer']
    builtrooms['narrow'].w_to = builtrooms['foyer']
    builtrooms['narrow'].n_to = builtrooms['treasure']
    builtrooms['treasure'].s_to = builtrooms['narrow']
    return builtrooms





