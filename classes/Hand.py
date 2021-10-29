from os import error, get_terminal_size
from classes.TrainerCard import *
from classes.PokemonCard import *
from classes.EnergyCard import *
from classes.Colours import *
from classes.BenchedPokemon import *
from classes.Bench import *
import tkinter as tk

class Hand:
    def __init__(self, list=[], basic_cards=[]):
        #the list of objects is the list of card objects
        self.list = list
        self.basic_cards = basic_cards
        self.completed = False

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

    def ui_card_names(self, list):
        message = "Basic Cards"
        for card in list:
            pass

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
    
    def remove_basic_card(self, basic_card):
        for card in self.basic_cards:
            if (card.name == basic_card.name) and (card.nationalPokedexNumbers == basic_card.nationalPokedexNumbers):
                del self.basic_cards[self.basic_cards.index(card)]
                return
    

    def add_to_bench(self, basic_card, card, bench):
        benched_pokemon = BenchedPokemon(basic_card, getattr(basic_card, 'hp'), 0)
        bench.add_to_bench(benched_pokemon)
        self.remove_basic_card(basic_card)
        card.destroy()
        

    def attach_energy_to_active(self, energy, active_pokemon):
        for card in self.list:
            if card.name == energy.name:
                buffer = card
                del self.list[self.list.index(card)]
                active_pokemon.attach_energy(buffer)


    def attach_energy_to_benched(self, energy, bench, pokemon):
        for card in self.list:
            if card.name == energy.name:
                buffer = card
                del self.list[self.list.index(card)]
                for card in bench.list:
                    if card.card_data.name == pokemon.card_data.name:
                        bench_index = bench.list.index(card)
                        break
                bench.attach_energy_to_benched(bench_index, buffer)