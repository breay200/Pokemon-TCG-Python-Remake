from classes.DiscardPile import *

class ActivePokemon():
    def __init__(self, card_data=object, health=0, energies=[], isAsleep=False, isBurned=False, isConfused=False, isParalyzed=False, isPoisoned=False, isProtectedFromAttackNextTurn=False):
        self.card_data = card_data
        self.health = health
        self.energies = energies
        self.isAsleep = isAsleep
        self.isBurned = isBurned
        self.isConfused = isConfused
        self.isParalyzed = isParalyzed
        self.isPoisoned = isPoisoned
        self.isProtectedFromAttackNextTurn = isProtectedFromAttackNextTurn

    def get_name(self):
        return self.card_data.name

    def evolve(self):
        pass

    def attach_energy(self, energy):
        self.energies.append(energy)

    def use_ability(self):
        pass

    def retreat(self):
        pass

    def remove_energy(self, name, number, discard):
        removed_cards = []
        count = 0
        for energy in self.energies:
            if energy.name == name:
                count += 1
                if count <= number:
                    print(f"Energies attached to {self.card_data.name}: {len(self.energies)}")
                    removed_cards.append(self.energies.remove(energy))
                    print(f"Energies attached to {self.card_data.name}: {len(self.energies)}")
                    discard.append(removed_cards)
                elif count > number:
                    break
        
    
