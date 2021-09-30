class Player:
    def __init__(self, name, deck, hand):
        self.name = name
        self.deck = deck
        self.hand = hand

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    #does this really need to be in the Player class?
    def change_deck():
        pass