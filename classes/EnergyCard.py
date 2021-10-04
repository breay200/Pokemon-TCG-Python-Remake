from classes.Card import *

class EnergyCard(Card):
    def __init__(self, name="", supertype=[], subtypes=[], rules=[], number=0, artist="", rarity="", images=[]):
        #self.id = id
        self.name = name
        self.supertype = supertype
        self.subtypes = subtypes #array
        self.rules = rules
        self.number = number
        self.artist = artist
        self.rarity = rarity
        self.images = images #object

    def __str__(self):
        return f"name: {self.name}\ntype: {self.supertype}\nsubtype: {self.subtypes}"

    def print_card(self):
        return f"name: {self.name}\ntype: {self.supertype}\nsubtype: {self.subtypes}"
