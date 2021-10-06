class ActivePokemon():
    def __init__(self, card_data=object, health=0, energies=[], isAsleep=False, isBurned=False, isConfused=False, isParalyzed=False, isPoisoned=False):
        self.card_data = card_data
        self.health = health
        self.energies = energies
        self.isAsleep = isAsleep
        self.isBurned = isBurned
        self.isConfused = isConfused
        self.isParalyzed = isParalyzed
        self.isPoisoned = isPoisoned

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
    
