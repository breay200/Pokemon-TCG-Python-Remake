from classes.Card import *
from classes.Colours import *

class EnergyCard(Card):
    def __init__(self, name="", supertype=[], subtypes=[], rules=[], number=0, artist="", rarity="", images=[]):
        #self.id = id
        self.name = name
        self.supertype = supertype
        self.subtypes = subtypes
        self.rules = rules
        self.number = number
        self.artist = artist
        self.rarity = rarity
        self.images = images

    def __str__(self):
        return f"name: {self.name}\ntype: {self.supertype}\nsubtype: {self.subtypes}"

    def print_card(self):
        colour_list = ['Colorless', 'Fighting', 'Fire', 'Grass', 'Lightning', 'Psychic', 'Water']
        colour = ""
        for x in colour_list:
            if x in self.name:
                colour_obj = Colours()
                colour = getattr(colour_obj, x)
            else:
                pass
        print(f"\n{colour}{self.name}")