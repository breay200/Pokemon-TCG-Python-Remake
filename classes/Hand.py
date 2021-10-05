from classes.TrainerCard import *
from classes.PokemonCard import *
from classes.EnergyCard import *
from termcolor import colored

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
        print(len(list))
        count = 0
        for card in list:
            count += 1
            print(colored(f"\nCARD {count}","red"))
            print("======")
            card.print_card()
    
    def find_basics(self):
        for card in self.list:
            if card.supertype == 'Pokémon':
                if 'Basic' in card.subtypes:
                    self.basic_cards.append(card)
                else:
                    continue
            else:
                continue
        
    def select_basic_active(self):
        print("\nPlease enter the name of Basic Pokémon you want to make the Active Pokemon")
        chosen_pokemon = input("Enter Pokémon's name: ")
        try:
            chosen_pokemon = str(chosen_pokemon)
        except ValueError:
            print("Invalid data type.")
        basic_card_names = []
        for card in self.basic_cards:
            basic_card_names.append(card.name)
        while chosen_pokemon not in basic_card_names:
            chosen_pokemon = input("Enter Pokémon's name: ")
        for card in self.basic_cards:
            if card.name == chosen_pokemon:
                del self.basic_cards[card]
                return chosen_pokemon
            else:
                pass
            