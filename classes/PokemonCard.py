from classes.Card import Card

class PokemonCard(Card):
    def __init__(self, name, supertype, subtypes, level, hp, types, attacks, weaknesses, retreatCost, convertedRetreatCost,number, artist, rarity, flavorText, nationalPokedexNumbers, images):
        self.name = name
        self.supertype = supertype
        self.subtypes = subtypes
        self.level = level
        self.hp = hp
        self.types = types
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