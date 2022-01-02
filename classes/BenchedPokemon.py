class BenchedPokemon():
    def __init__(self, card_data="", hp=0, energies=[]):
        self.card_data = card_data
        self.hp = hp
        self.energies = energies

    def set_card(self, card_data, hp, energies):
        self.card_data = card_data
        self.hp = hp
        self.energies = energies
    
    def add_energy(self, energy):
        self.energies.append(energy)

    def remove_energy(self, energy):
        self.energies.remove(energy)

    def set_hp(self, hp):
        self.hp = hp
    
    def get_hp(self):
        return self.hp