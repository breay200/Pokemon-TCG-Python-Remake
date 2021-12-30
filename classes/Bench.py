from classes.BenchedPokemon import*

class Bench():
    def __init__(self, bench_data=[]):
        self.bench_data = bench_data

    def add_to_bench(self, data):
        self.bench_data.append(data)

    def get_list(self):
        return self.bench_data
    
    # def attach_energy_to_benched(self, index, card):
    #     for pokemon in self.bench_data:
    #         if self.bench_data.index == index:
    #             pokemon.attach_energy
    #     pass