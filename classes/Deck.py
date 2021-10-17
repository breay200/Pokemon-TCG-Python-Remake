import json
import random
import tkinter as tk

class Deck:
    def __init__(self, active_deck="", id_list=[]):
        self.active_deck = active_deck
        self.id_list = id_list
    
    def __str__(self):
        return f"active deck: {self.active_deck}\n{self.id_list}"

    def add_card():
        pass

    def remove_card():
        pass

    def get_cards():
        #for card object in list print card details
        pass
    
    def get_decks(self, filename):
        print("Available Decks: \n")
        file = open(filename,encoding='utf-8')
        data = json.load(file)
        decks = []
        for i in data:
            decks.append(i['name'])
        file.close()
        return decks

    def get_active_deck(self):
        return self.active_deck

    def set_active_deck(self):
        self.active_deck = self.print_decks()

    def load_deck(self, filename):
        file = open(filename,encoding='utf-8')
        data = json.load(file)
        for set in data:
            if set['name'] == self.active_deck:
                for x in set['cards']:
                    count = int(x['count'])
                    for n in range(count):
                        self.id_list.append(x['id'])
        file.close()

    def check_deck(self):
        
        pass

    def shuffle_deck(self):
        random.shuffle(self.id_list)

    def pop_card(self):
        return self.id_list.pop(0)

    def append_to_deck(self, card):
        self.id_list.append(card)

    def draw_number_of_cards(self, number):
        cards = []
        for x in range(number):
            cards.append(self.id_list.pop(0))
        return cards
    
    def return_to_deck(self, cards):
        for card in cards:
            self.id_list.append(card)

    def get_deck_size(self):
        return len(self.id_list)