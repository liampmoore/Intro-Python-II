import json
from rooms import buildrooms
from items import getitemsbyids

# Write a class to hold player information, e.g. what room they are in
# currently.




class Player:
    def __init__(self, name = 'Adventurer', location = 'outside', items = [], rooms = None):
        self.name = name
        self.items = getitemsbyids(items)
        self.rooms = buildrooms(rooms)
        self.location = self.rooms[location]
        self.path = []

    def move(self, direction):
        deadend = "Nowhere to go in that direction. Try a different direction."
        if direction == ('north' or 'n'):
            if hasattr(self.location, 'n_to'):
                if self.location.n_passage:
                  if self.location.n_passage.is_open:
                    self.location = self.location.n_to
                    self.path.append('south')
                  else:
                      print("There is a " + self.location.n_passage.closed_description + " to the north.")
                      print("You'll need to figure out a way through.")
                else:
                    self.location = self.location.n_to
                    self.path.append('south')
            else:
                print(deadend)
        elif direction == ('south' or 's'):
            if hasattr(self.location, 's_to'):
                if self.location.s_passage:
                  if self.location.s_passage.is_open:
                    self.location = self.location.s_to
                    self.path.append('north')
                  else:
                      print("There is a " + self.location.s_passage.closed_description + " to the south.")
                      print("You'll need to figure out a way through.")
                else:
                    self.location = self.location.s_to
                    self.path.append('north')
            else:
                print(deadend)
        elif direction == ('west' or 'w'):
            if hasattr(self.location, 'w_to'):
                if self.location.w_passage:
                  if self.location.w_passage.is_open:
                    self.location = self.location.w_to
                    self.path.append('east')
                  else:
                      print("There is a " + self.location.w_passage.closed_description + " to the west.")
                      print("You'll need to figure out a way through.")
                else:
                    self.location = self.location.w_to
                    self.path.append('east')
            else:
                print(deadend)
        elif direction == ('east' or 'e'):
            if hasattr(self.location, 'e_to'):
                if self.location.e_passage:
                  if self.location.e_passage.is_open:
                    self.location = self.location.e_to
                    self.path.append('west')
                  else:
                      print("There is a " + self.location.e_passage.closed_description + " to the east.")
                      print("You'll need to figure out a way through.")
                else:
                    self.location = self.location.e_to
                    self.path.append('west')
            else:
                print(deadend)
        elif direction == ('back'):
            if len(self.path) > 0:
                if self.path[-1] == 'north':
                    self.location = self.location.n_to
                    self.path.pop()
                elif self.path[-1] == 'south':
                    self.location = self.location.s_to
                    self.path.pop()
                elif self.path[-1] == 'west':
                    self.location = self.location.w_to
                    self.path.pop()
                elif self.path[-1] == 'east':
                    self.location = self.location.e_to
                    self.path.pop()
            else:
                print("You've only just started, there is nowhere to go back to.")
        self.location.discovered = True
    def inventory(self):
        if len(self.items) > 0:
            print("You look over your inventory:")
            for item in self.items:
                print(item.name)
        else:
            print("You don't have anything with you.")
    def recieveitem(self, item):
        self.items.append(item)
        print(f"You put {item.name} in your inventory.")
    def dropitem(self, itemname):
        if next(item for item in self.items if item.name.lower() == itemname):
            item = next(item for item in self.items if item.name.lower() == itemname)
            self.items.remove(item)
            return item
        else:
            return False
    def save(self):
        return {
            "name": self.name,
            "location": self.location.id,
            "items": [item.id for item in self.items],
            "rooms": [room.save() for room in self.rooms.values()]
        }
