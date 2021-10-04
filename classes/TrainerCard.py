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

    def __str__(self):
        return f"name: {self.name}\ntype: {self.supertype}\nrules: {self.rules}"
    
    def print_card(self):
        return f"name: {self.name}\ntype: {self.supertype}\nrules: {self.rules}"


    
