from os import get_terminal_size
from classes.TrainerCard import *
from classes.PokemonCard import *
from classes.EnergyCard import *
from classes.Colours import *
from classes.BenchedPokemon import *
from classes.Bench import *

class Hand:
    def __init__(self, list=[], basic_cards=[]):
        #the list of objects is the list of card objects
        self.list = list
        self.basic_cards = basic_cards

    def send_to_graveyard(self):
        pass

    def append_to_hand(self, card_obj):
        self.list.append(card_obj)

    def send_to_deck(self):
        pass
    
    def print_cards(self, list):
        count = 0
        for card in list:
            count += 1
            print(Colours.Colorless)
            print(f"\nCARD {count}")
            print("======")
            card.print_card()
        print(Colours.Colorless)

    def print_card_names(self, list):
        print(f"\nBASIC CARDS")
        print("===========")
        count = 0
        for card in list:
            colour = ""
            for val in card.types:
                colour_obj = Colours()
                colour = getattr(colour_obj, val)
            count += 1
            print(f"{count}: {colour}{card.get_name()}")
            print(Colours.Colorless)
        print(Colours.Colorless)
    
    def find_basics(self):
        for card in self.list:
            if card.supertype == 'Pokémon':
                if 'Basic' in card.subtypes:
                    self.basic_cards.append(card)
                else:
                    continue
            else:
                continue
        
    def select_basic(self):
        chosen_pokemon = input("Enter Pokémon's name: ")       
        basic_card_names = []
        
        for card in self.basic_cards:
            basic_card_names.append(card.name)
        
        while chosen_pokemon not in basic_card_names:
            chosen_pokemon = input("Enter Pokémon's name: ")
        
        for card in self.basic_cards:
            if card.name == chosen_pokemon:
                buffer = card
                del self.basic_cards[self.basic_cards.index(card)]
                return buffer
            else:
                pass
        
    def add_to_bench(self, bench):
        if (len(bench.list)<=5):
            print("Would you like to add any Basic Pokemon to the Bench?")
            response = input("Enter y or n: ").lower()
            while response not in ['y', 'n']:
                response = input("Enter y or n: ").lower()
            while response == 'y':
                self.print_card_names(self.basic_cards)
                print("Please enter the name of Basic Pokémon you want to add to the Bench")
                card = self.select_basic()
                benched_pokemon = BenchedPokemon(card, getattr(card, 'hp'), 0)
                bench.add_to_bench(benched_pokemon)
                if len(self.basic_cards)>=1 and (len(bench.list<=5)):
                    print("Would you like to add any more Basic Pokemon to the Bench?")
                    response = input("Enter y or n: ")
                    while response not in ['y', 'n']:
                        response = input("Enter y or n: ").lower()
                else:
                    break
            else:
                print("You chose not to add any more Pokemon to the Bench")
        else:
            print("Your bench is already full")

    def attach_energy(self, active_pokemon, bench):
        energy_list = []
        for card in self.list:
            if card.supertype == 'Energy':
                energy_list.append(card)
        if len(energy_list) >= 1:
            print("Would you like to attach an energy to a Pokemon?")
            response = input("Enter y or n: ").lower()
            while response not in ['y', 'n']:
                response = input("Enter y or n: ").lower()
            if response == 'y':
                print("Would you like to attach an energy to the Active Pokemon or a Benched Pokemon?")
                choice = input("Enter a (Active) or b (Benched): ").lower()
                while choice not in ['a', 'b']:
                    choice = input("Enter a (Active) or b (Benched): ").lower()
                if choice == 'a':
                    energy_list_names = []
                    for energy in energy_list:
                        energy_list_names.append(energy.name)
                    energy_list_names = set(energy_list_names)
                    print("Enter the energy type you would like to attach to the active pokemon")
                    for energy in energy_list_names:
                        print(energy)
                    energy_choice = input("Enter type: ")
                    while energy_choice not in energy_list_names:
                        energy_choice = input("Enter an energy type in your hand: ")
                    for card in self.list:
                        if self.list.name == energy_choice:
                            buffer = card
                            del self.list[self.list.index(card)]
                            active_pokemon.attach_energy(buffer)
                            return "you added an energy to the active pokemon"
                else:
                    print("Enter the name of the pokemon you would like to attach an energy to")
                    pokemon_names = []
                    bench_index = 0 
                    for pokemon in bench.list:
                        pokemon_names.append(pokemon.card_data.name)
                        print(pokemon.card_data.name)
                    ##PROBLEM STARTS HERE 
                    name_count = 0
                    name_indices = []
                    for name in pokemon_names:
                        if (pokemon_names.count(name))>1:
                            name_indices.append(pokemon_names.index(name))
                    for name in pokemon_names:
                        for index in name_indices:
                            print(index)
                            print(pokemon_names.index(name))
                            if pokemon_names.index(name) == index:
                                name_count += 1
                                #BROKEN BLOCK
                                print(f"{name} {name_count}")
                    pokemon_choice = input("Enter a pokemon's name: ")
                    while pokemon_choice not in pokemon_names:
                        pokemon_choice = input("Enter a pokemon's name that is on the bench: ")
                    for pokemon in bench.list:
                        if pokemon.card_data.name == pokemon_choice:
                            bench_index = bench.list.index(pokemon)
                    energy_list_names = []
                    for energy in energy_list:
                        energy_list_names.append(energy.name)
                    energy_list_names = set(energy_list_names)
                    print(f"Enter the energy type you would like to attach to {pokemon_choice}")
                    for energy in energy_list_names:
                        print(energy)
                    energy_choice = input("Enter type: ")
                    while energy_choice not in energy_list_names:
                        energy_choice = input("Enter an energy type in your hand: ")
                    for card in self.list:
                        #PROBLEM HERE AND BELOW AttributeError: 'list' object has no attribute 'name'
                        if card.name == energy_choice:
                            buffer = card
                            del self.list[self.list.index(card)]
                            #active_pokemon.attach_energy(buffer)
                            bench.attach_energy_to_benched(bench_index, buffer)
                            return f"you added a {energy_choice} to {pokemon_choice}"
            else:
                print("You don't have any energies in your hand")