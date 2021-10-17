from classes.Deck import *
from classes.config import *

class DeckUI(Deck):
    def __init__(self) -> None:
        self.print_decks_frame = tk.Frame(Config.master)
        self.decks = self.get_decks("data/set1.json")
        self.deck_widgets = []
        
        for deck in self.decks:
            card_widget = tk.Button(self.print_decks_frame, text=deck, command=lambda: self.get_active(deck))
            self.deck_widgets.append(card_widget)
        widget_count = 0
        
        for widget in self.deck_widgets:
            widget.grid(column = widget_count, row = 1)
            widget_count += 1
        
        self.print_decks_frame.grid(column=0, row=0)
    
    def get_active(self, arg):
        Config.deck = Deck()
        Config.deck.active_deck = arg
        self.print_decks_frame.destroy()
