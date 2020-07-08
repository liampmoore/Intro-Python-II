class Passage:
    def __init__(self, id, is_open, open_description, closed_description ):
        self.id = id
        self.is_open = is_open
        self.open_description = open_description
        self.closed_description = closed_description

class Door(Passage):
    def __init__(self, id, is_open, open_description = 'wooden door', closed_description = 'locked wooden door'):
        super().__init__(id, is_open, open_description, closed_description)