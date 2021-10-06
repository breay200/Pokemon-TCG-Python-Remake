from classes.BenchedPokemon import*

class Bench():
    def __init__(self, list=[]):
        self.list = list

    def add_to_bench(self, benched_pokemon):
        self.list.append(benched_pokemon)

    def get_list(self):
        return self.list
    
    def attach_energy_to_benched(self, index, card):
        for pokemon in self.list:
            if self.list.index == index:
                pokemon.attach_energy
        pass