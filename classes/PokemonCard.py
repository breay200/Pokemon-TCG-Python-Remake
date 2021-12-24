from classes.Card import *
from classes.Colours import *

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
        self.local_img = ""

    def __str__(self):
            return f"name: {self.name}\ntype: {self.supertype}\nstage: {self.subtypes}\nlevel: {self.level}\nhp: {self.hp}\ntype(s): {self.types}\nevolves from: {self.evolvesFrom}\nabilities: {self.abilities}\nattack(s): {self.attacks}\nweaknesses: {self.weaknesses}\nretreat cost: {self.retreatCost} / {self.convertedRetreatCost}\nflavour text: {self.flavorText}\nimage: {self.images}"

    def get_name(self):
        return self.name
    
    def print_card(self):
        for val in self.types:
            colour_obj = Colours()
            colour = getattr(colour_obj, val)

        print(colour)
        print(f"name: {self.name}")
        print(f"\ncard type: {self.supertype}")
        print("\n== stage ==\n")

        for stage in self.subtypes:
            print(stage)
        
        print("")
        print(f"level: {self.level}")
        print(f"\nhp: {self.hp}")
        print("\n== types ==\n")

        for type in self.types:
            print(type)

        if self.evolvesFrom:
            print(f"\nevolves from: {self.evolvesFrom}")
        else:
            pass
        
        if self.abilities:
            print("\n== abilities ==\n")
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
                #print(f"required energies: {attack.get('convertedEnergyCost')} / {attack.get('cost')}")
                
                if attack.get('convertedEnergyCost'):
                    print("\n== required energies ==\n")
                    energy_cost = set(attack.get('cost'))
                    for energy in energy_cost:
                        print(f"{attack.get('cost').count(energy)}x {energy} energies")

                if attack.get('damage'):
                    print(f"\ndamage: {attack.get('damage')}")
                else:
                    print("this attack does not damage the enemy (0)")
                
                if attack.get('text'):
                    print(f"\ndescription: {attack.get('text')}\n")
                else:
                    pass

        else:
            pass
        
        if self.weaknesses:
            print("\n== weaknesses ==\n")
            for weakness in self.weaknesses:
                print(f"{weakness.get('type')} with {weakness.get('value')} multiplier")
        else:
            pass

        if self.retreatCost:
            print("\n== retreat cost ==\n")
            unique_energies = set(self.retreatCost)
            for energies in unique_energies:
                print(f"{self.retreatCost.count(energies)}x {energies} energies")
        else:
            pass
        
        if self.convertedRetreatCost != 0:
            print(f"total required energies: {self.convertedRetreatCost}")
        else:
            print("no retreat cost (0)")
        
        if self.flavorText:
            print(f"\ncard description: {self.flavorText}")
        else:
            pass