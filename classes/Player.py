class Player:
    def __init__(self, name="", hand=[]):
        self.name = name
        self.hand = hand

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
