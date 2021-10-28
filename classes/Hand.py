from os import get_terminal_size
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
    
    def ui_add_to_bench(self, mgl, bench):
        def add_to_bench(basic_card, card):
            benched_pokemon = BenchedPokemon(basic_card, getattr(basic_card, 'hp'), 0)
            bench.add_to_bench(benched_pokemon)
            self.remove_basic_card(basic_card)
            card.destroy()
            self.ui_add_to_bench(mgl, bench)
        
        def no():
            message = "You chose not to add any cards to the Bench."
            mgl.block_inner_label.configure(text=message)
            mgl.block_inner_label.grid(column=0, row=0)

        def yes():
            mgl.yes_btn.destroy()
            mgl.no_btn.destroy()
            for basic_card in self.basic_cards:
                buttons=[] 
                card = tk.Button(mgl.mgl_frame, text=basic_card.name, width=20, height=70, command= lambda: add_to_bench(basic_card, card))
                buttons.append(card)
        
            count=0
            for value in buttons:
                value.grid(column=count, row=3)
                count += 1

        if self.basic_cards:  
            if (len(self.basic_cards)>=1) and (len(bench.list)<=5):
                message = "Would you like to add any Pokemon to the Bench"
                mgl.block_inner_label.configure(text=message)
                mgl.block_inner_label.grid(column=0, row=0)

                mgl.yes_btn = tk.Button(mgl.block_label, text="Yes", command=yes)
                mgl.yes_btn.grid(column=0, row=1)

                mgl.no_btn = tk.Button(mgl.block_label, text="No", command=no)
                mgl.no_btn.grid(column=1, row=1)
            else:
                message = "You have the maximum number of Pokemon on the bench"
                mgl.block_inner_label.configure(text=message)
                mgl.block_inner_label.grid(column=0, row=0)
        else:
            message = "There are no basic cards in your hand."
            mgl.block_inner_label.configure(text=message)
            mgl.block_inner_label.grid(column=0, row=0)
            return

    def attach_energy(self, mgl, active_pokemon, bench):
        def yes():
            def active():
                def attach_energy(energy):
                    for card in self.list:
                        if card.name == energy.name:
                            buffer = card
                            del self.list[self.list.index(card)]
                            active_pokemon.attach_energy(buffer)
                            for widget in buttons:
                                widget.destroy()
                            message = f"Attached a {energy.name} to {active_pokemon.card_data.name}."
                            mgl.block_inner_label.configure(text=message)
                            mgl.block_inner_label.grid(column=0, row=0)
                            self.completed = True 

                if self.completed:
                    pass
                else:
                    mgl.active_btn.destroy()
                    mgl.benched_btn.destroy()
                    
                    buttons=[] 
                    
                    for energy in energy_list:
                        card = tk.Button(mgl.mgl_frame, text=energy.name, width=20, height=70, command= lambda: attach_energy(energy))
                        buttons.append(card)
            
                    count=0
                    for value in buttons:
                        value.grid(column=count, row=3)
                        count += 1

                    message = "Select the Energy Card you would like to attach to the Active Pokemon."
                    mgl.block_inner_label.configure(text=message)
                    mgl.block_inner_label.grid(column=0, row=0)

            def benched():
                def select_pokemon(pokemon, buttons):
                    def attach_energy(energy, pokemon):
                        for card in self.list:
                            if card.name == energy.name:
                                buffer = card
                                del self.list[self.list.index(card)]
                                for card in bench.list:
                                    if card.card_data.name == pokemon.card_data.name:
                                        bench_index = bench.list.index(card)
                                bench.attach_energy_to_benched(bench_index, buffer)
                                for widget in buttons:
                                    widget.destroy()
                                message = f"Attached a {energy.name} to {pokemon.card_data.name}."
                                mgl.block_inner_label.configure(text=message)
                                mgl.block_inner_label.grid(column=0, row=0)


                    for widget in buttons:
                        widget.destroy()
                    
                    buttons=[] 
                    
                    for energy in energy_list:
                        card = tk.Button(mgl.mgl_frame, text=energy.name, width=20, height=70, command= lambda: attach_energy(energy, pokemon))
                        buttons.append(card)
            
                    count=0
                    for widget in buttons:
                        widget.grid(column=count, row=3)
                        count += 1

                    message = "Select the Energy Card you would like to attach to the Active Pokemon."
                    mgl.block_inner_label.configure(text=message)
                    mgl.block_inner_label.grid(column=0, row=0)
                        

                message = "Select the the Pokemon on the Bench that you want to attach an Energy to."
                mgl.block_inner_label.configure(text=message)
                mgl.block_inner_label.grid(column=0, row=0)

                buttons = []

                for pokemon in bench.list:
                    card = tk.Button(mgl.mgl_frame, text=pokemon.card_data.name, width=20, height=70, command= lambda: select_pokemon(pokemon, buttons))
                    buttons.append(card)
        
                count=0
                for card in buttons:
                    card.grid(column=count, row=3)
                    count += 1

            
            if self.completed:
                pass
            else:
                message = "Would you like to attach an energy to the Active Pokemon or a Benched Pokemon?"
                mgl.block_inner_label.configure(text=message)
                mgl.block_inner_label.grid(column=0, row=0)
                
                mgl.yes_btn.destroy()
                mgl.no_btn.destroy()

                mgl.active_btn = tk.Button(mgl.block_label, text="Attach to the Active Pokemon", command=active)
                mgl.active_btn.grid(column=0, row=1)

                mgl.benched_btn = tk.Button(mgl.block_label, text="Attach to a Pokemon on the Bench.", command=benched)
                mgl.benched_btn.grid(column=1, row=1)
                

        
        def no():
            message = "You chose not to add any energies to your Pokemon."
            mgl.block_inner_label.configure(text=message)
            mgl.block_inner_label.grid(column=0, row=0)
            return

        energy_list = []
        for card in self.list:
            if card.supertype == 'Energy':
                energy_list.append(card)
        if len(energy_list) >= 1:
            message = "Would you like to attach an energy to a Pokemon?"
            mgl.block_inner_label.configure(text=message)
            mgl.block_inner_label.grid(column=0, row=0)

            mgl.yes_btn = tk.Button(mgl.block_label, text="Yes", command=yes)
            mgl.yes_btn.grid(column=0, row=1)

            mgl.no_btn = tk.Button(mgl.block_label, text="No", command=no)
            mgl.no_btn.grid(column=1, row=1)
        else:
            message = "There are no energies in your hand."
            mgl.block_inner_label.configure(text=message)
            mgl.block_inner_label.grid(column=0, row=0)
            return