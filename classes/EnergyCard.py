from classes.Card import *

class EnergyCard(Card):
    def __init__(self, name, supertype, subtypes, number, artist, rarity, images):
        #self.id = id
        self.name = name
        self.supertype = supertype
        self.subtypes = subtypes #array
        self.number = number
        self.artist = artist
        self.rarity = rarity
        self.images = images #object