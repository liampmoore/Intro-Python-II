from item import Item
from item import Key

# Declare all the rooms

items = [
    Item("Torch","A wooden torch. It provides light.", 0),
    Item("Rope","A long coil of sturdy rope.", 1),
    Key("Iron Key","A polished iron key.", 2, 452)
]

def getitemsbyids(ids):
    return [items[id] for id in ids]