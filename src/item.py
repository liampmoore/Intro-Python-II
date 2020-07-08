class Item:
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id

class Key(Item):
    def __init__(self, name, description, id, locked_passage_id):
        super().__init__(name, description, id)
        self.locked_passage_id = locked_passage_id