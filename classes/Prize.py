from classes.Deck import *

class Prize():
    def __init__(self, prize_list=[]):
        self.prize_list = prize_list
    
    def append_prize_list(self, card):
        self.prize_list.append(card)
    
    def take_prize_card(self):
        card = self.prize_list.pop()
        return card
    
    def get_remaining_prize_cards(self):
        return len(self.prize_list)
    
    def set_prize_cards(self, deck):
        self.prize_list = deck.draw_number_of_cards(6)