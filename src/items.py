from item import Item

# Declare all the rooms

items = [
    Item("Torch",
                     "A wooden torch. It provides light.", 0),
]

def getitemsbyids(ids):
    return [items[id] for id in ids]