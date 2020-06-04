# Implement a class to hold room information. This should have name and
# description attributes.

import json
from items import items

class Room:
    def __init__(self, name, description, id, item_ids = [], discovered = False):
        self.name = name
        self.description = description
        self.items = [items[item_id] for item_id in item_ids]
        self.id = id
        self.discovered = discovered
    def search(self):
            if len(self.items) > 0:
                print("You search the area and find:")
                for item in self.items:
                    print(item.name)
            else:
                print("You search the area but you don't find anything.")
    def takeitem(self, itemname):
        if next(item for item in self.items if item.name.lower() == itemname):
            item = next(item for item in self.items if item.name.lower() == itemname)
            self.items.remove(item)
            return item
        else:
            return False
    def recieveitem(self, item):
        self.items.append(item)
        print(f"You put down the {item.name}.")
    def save(self):
        return {
            "name": self.name,
            "description": self.description,
            "item_ids": [item.id for item in self.items],
            "id": self.id,
            "discovered" : self.discovered
        }
        