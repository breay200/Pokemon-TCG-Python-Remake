from classes.BenchedPokemon import*

class Bench():
    def __init__(self):
        self.on_bench = 0

        self.pokemon_one = BenchedPokemon()
        self.pokemon_two = BenchedPokemon()
        self.pokemon_three = BenchedPokemon()
        self.pokemon_four = BenchedPokemon()
        self.pokemon_five = BenchedPokemon()

    def add_to_bench(self, card):
        if self.on_bench == 0:
            self.pokemon_one.set_card(card, card.hp, [])
            self.on_bench += 1
            return self.pokemon_one
        elif self.on_bench == 1:
            self.pokemon_two.set_card(card, card.hp, [])
            self.on_bench += 1
            return self.pokemon_two
        elif self.on_bench == 2:
            self.pokemon_three.set_card(card, card.hp, [])
            self.on_bench += 1
            return self.pokemon_three
        elif self.on_bench == 3:
            self.pokemon_four.set_card(card, card.hp, [])
            self.on_bench += 1
            return self. pokemon_four
        else:
            self.pokemon_five.set_card(card, card.hp, [])
            self.on_bench += 1
            return self.pokemon_five

    def get_list(self):
        return self.bench_data
    
    # def attach_energy_to_benched(self, index, card):
    #     for pokemon in self.bench_data:
    #         if self.bench_data.index == index:
    #             pokemon.attach_energy
    #     pass