# Implement a class to hold room information. This should have name and
# description attributes.

from items import items

class Room:
    def __init__(self, name, description, id, item_ids):
        self.name = name
        self.description = description
        self.items = [items[item_id] for item_id in item_ids]
        self.id = id
    def search(self):
        print("You take a look around the room and find:")
        for item in self.items:
            print(item.name)