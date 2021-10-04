from classes.TrainerCard import *
from classes.PokemonCard import *
from classes.EnergyCard import *

class Hand:
    def __init__(self, list=[]):
        #the list of objects is the list of card objects
        self.list = list

    def send_to_graveyard(self):
        pass

    def append_to_hand(self, card_obj):
        self.list.append(card_obj)

    def send_to_deck(self):
        pass
    
    def see_hand(self):
        print(len(self.list))
        count = 0
        for card in self.list:
            count += 1
            print(f"\ncard {count}")
            print("======")
            print(card.print_card())