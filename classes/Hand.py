from os import get_terminal_size
from classes.TrainerCard import *
from classes.PokemonCard import *
from classes.EnergyCard import *
from classes.Colours import *
from classes.BenchedPokemon import *

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
            print(f"\nCARD {count}")
            print("======")
            card.print_card()
        print(Colours.Colorless)

    def print_card_names(self, list):
        print(f"\nBASIC CARDS")
        print("===========")
        count = 0
        for card in list:
            count += 1
            print(f"{count}: {card.get_name()}")
    
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
        print("Would you like to add any Basic Pokemon to the Bench?")
        response = input("Enter Y or N: ")
        while response not in ['Y', 'N']:
            response = input("Enter Y or N: ")
        while response == 'Y':
            self.print_card_names(self.basic_cards)
            print("Please enter the name of Basic Pokémon you want to add to the Bench")
            card = self.select_basic()
            benched_pokemon = BenchedPokemon(card, getattr(card, 'hp'), 0)
            bench.add_to_bench(benched_pokemon)
            if len(self.basic_cards)>=1:
                print("Would you like to add any more Basic Pokemon to the Bench?")
                response = input("Enter Y or N: ")
                while response not in ['Y', 'N']:
                    response = input("Enter Y or N: ")
            else:
                break
        else:
            print("You chose not to add any more Pokemon to the Bench")

    def attach_energy(self):
        energy_count = 0
        for card in self.list:
            if card.supertype == 'Energy':
                energy_count += 1
        if energy_count >= 1:
            print("Would you like to attach an energy to a Pokemon?")
            response = input("Enter Y or N: ")
            while response not in ['Y', 'N']:
                response = input("Enter Y or N: ")
            if response == 'Y':
                print("Would you like to attach an energy to the Active Pokemon or a Benched Pokemon?")
        else:
            print("You don't have any energies in your hand")