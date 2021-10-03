from classes.Card import *

class TrainerCard(Card):
    def __init__(self, name, supertype, rules, number, artist, rarity, images):
        self.name = name
        self.supertype = supertype
        self.rules = rules
        self.number = number
        self.artist = artist
        self.rarity = rarity
        self.images = images

    
