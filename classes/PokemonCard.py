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
        print(f"name: {self.name}")
        print(f"card type: {self.supertype}")
        print("== stage ==")

        for stage in self.subtypes:
            print(stage)

        print(f"level: {self.level}")
        print(f"hp: {self.hp}")
        print("== types ==")

        for type in self.types:
            print(type)

        if self.evolvesFrom:
            print(f"evolves from: {self.evolvesFrom}")
        else:
            pass
        
        if self.abilities:
            print("== abilities ==")
            for ability in self.abilities:
                print(ability)
        else:
            pass
        
        if self.attacks:
            count = 0
            for attack in self.attacks:
                count += 1
                print(f"\n== attack {count} ==\n")
                print(f"name: {attack.get('name')}")
                print(f"required energies: {attack.get('convertedEnergyCost')} / {attack.get('cost')}")
                print(f"damage: {attack.get('damage')}")
                print(f"description: {attack.get('text')}\n")

        else:
            pass
        
        if self.weaknesses:
            print("\n== weaknesses ==\n")
            for weakness in self.weaknesses:
                print(f"{weakness.get('type')} with {weakness.get('value')} multiplier")
        else:
            pass

        if self.retreatCost:
            print("== retreat cost ==")
            for retreat in self.retreatCost:
                print(retreat)
        else:
            pass
        
        if self.convertedRetreatCost != 0:
            print(self.convertedRetreatCost)
        else:
            print("no retreat cost (0)")
        
        print(f"flavour text: {self.flavorText}")