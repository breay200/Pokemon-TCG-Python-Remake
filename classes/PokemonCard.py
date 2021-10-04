from classes.Card import Card

class PokemonCard(Card):
    def __init__(self, name="", supertype=[], subtypes=[], level=0, hp=0, types=[], evolvesFrom="", abilities=[], attacks=[], weaknesses=[], retreatCost=[], convertedRetreatCost=0, number=0, artist="", rarity="", flavorText="", nationalPokedexNumbers=[], images=[]):
        self.name = name
        self.supertype = supertype
        self.subtypes = subtypes
        self.level = level
        self.hp = hp
        self.types = types
        self.evolvesFrom = evolvesFrom
        self.abilities = abilities
        self.attacks = attacks
        self.weaknesses = weaknesses
        self.retreatCost = retreatCost
        self.convertedRetreatCost = convertedRetreatCost
        self.number = number
        self.artist = artist
        self.rarity = rarity
        self.flavorText = flavorText
        self.nationalPokedexNumbers = nationalPokedexNumbers
        self.images = images

    def __str__(self):
            return f"name: {self.name}\ntype: {self.supertype}\nstage: {self.subtypes}\nlevel: {self.level}\nhp: {self.hp}\ntype(s): {self.types}\nevolves from: {self.evolvesFrom}\nabilities: {self.abilities}\nattack(s): {self.attacks}\nweaknesses: {self.weaknesses}\nretreat cost: {self.retreatCost} / {self.convertedRetreatCost}\nflavour text: {self.flavorText}"
        
    def print_card(self):
        return f"name: {self.name}\ntype: {self.supertype}\nstage: {self.subtypes}\nlevel: {self.level}\nhp: {self.hp}\ntype(s): {self.types}\nevolves from: {self.evolvesFrom}\nabilities: {self.abilities}\nattack(s): {self.attacks}\nweaknesses: {self.weaknesses}\nretreat cost: {self.retreatCost} / {self.convertedRetreatCost}\nflavour text: {self.flavorText}"