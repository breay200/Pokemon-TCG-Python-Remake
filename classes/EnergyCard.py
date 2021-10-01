from classes.Card import *

class EnergyCard(Card):
    def __init__(self, id, name, supertype, subtypes, number, artist, rarity, legalities, images):
        self.id = id
        self.name = name
        self.supertype = supertype
        self.subtypes = subtypes #array
        self.number = number
        self.artist = artist
        self.rarity = rarity
        self.legalities = legalities #object
        self.images = images #object