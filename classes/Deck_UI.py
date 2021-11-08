from classes.Deck import *
from classes.config import *
from misc_functions import *
from classes.Game import *

class DeckUI(Deck):
    def __init__(self, user) -> None:
        self.print_decks_frame = tk.Frame(Config.master)
        self.decks = self.get_decks("data/set1.json")
        self.deck_widgets = []
        
        for deck in self.decks:
            card_widget = tk.Button(self.print_decks_frame, text=deck, command=lambda: self.get_active(deck, user))
            self.deck_widgets.append(card_widget)
        widget_count = 0
        
        for widget in self.deck_widgets:
            widget.grid(column = widget_count, row = 1)
            widget_count += 1
        
        self.print_decks_frame.grid(column=0, row=0)
    
    def get_active(self, arg, user):
        user.active_deck = arg
        text = f"{user.username}, {user.matches_won}, {user.matches_lost}, {user.date_joined}, {user.favourite_pokemon}, {user.email_addr}, {user.active_deck}"
        append_to_file("data/player_data.txt", text)
        self.print_decks_frame.destroy()
