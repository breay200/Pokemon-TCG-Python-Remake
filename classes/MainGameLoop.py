from os import error
from tkinter.constants import W
from classes.Bench import Bench
from classes.GameBoard import Gameboard
from classes.Player import *
from classes.Deck import *
from classes.EnergyCard import *
from classes.Prize import Prize
from classes.TrainerCard import *
from classes.PokemonCard import *
from classes.Hand import *
from classes.ActivePokemon import *
from classes.Colours import *
from classes.Bench import *
from classes.config import *
from classes.Deck_UI import *
from classes.GameLogic import *
from classes.User import *
from misc_functions import *

class MainGameLoop:
    def __init__(self, user, networking):
        self.user = user
        self.networking = networking
        self.opponent = networking.opponent

        self.play_order = ""
        self.completed = False
        self.added_to_bench = False
        self.attached_energy = False
        self.changed_deck = False

        # self.hand_obj = object
        # self.bench = object
        # self.active_pokemon = object
        # self.obj_list = object
        # self.prize = object

        self.game_logic = GameLogic(self.user, self.networking)
        self.deck = Deck()
        self.gameboard = Gameboard()

        self.mgl_frame = tk.Frame(Config.master)
        self.mgl_frame.place(x=0,y=0)

        if user.active_deck != "":
            answer = tk.messagebox.askyesno("Deck Selection", f"The currently selected deck is {self.user.active_deck}.\nWould you like to change it?")
            if answer:
                chosen_deck = self.deck.change_deck(self.mgl_frame)
                self.user.active_deck = str(chosen_deck).replace(" ", "")
        else:
            tk.messagebox.showinfo("Deck Selection", "You don't have a deck selected.\nPlease choose one for your battle!")
            chosen_deck = self.deck.change_deck(self.mgl_frame)
            self.user.active_deck = str(chosen_deck).replace(" ", "")

        self.deck.active_deck = str(self.user.active_deck).replace(" ", "")
        self.deck.load_deck("data/set1.json")
        self.initiate_game()
        
        

    

    # #should make a card frame to put cards into
    #     if not self.completed:
    #         self.game_logic.rock_paper_scissors(self.mgl_frame)
    #         self.deck.shuffle_deck()
    #         self.hand = self.deck.draw_number_of_cards(7)
    #         self.obj_list = self.load_card_data(self.hand)
    #         self.hand_obj = Hand(self.obj_list)
    #         self.hand_obj.find_basics()

    #         while not self.hand_obj.basic_cards:
    #             message = "Re-shuffling deck..."
    #             self.block_inner_label.configure(text=message)
    #             self.block_inner_label.grid(column=0, row=0)
    #             self.deck.return_to_deck(self.hand)
    #             self.deck.shuffle_deck()
    #             self.hand = []
    #             self.hand = self.deck.draw_number_of_cards(7)
    #             obj_list = []
    #             obj_list = self.load_card_data(self.hand)
    #             self.hand_obj.list = obj_list
    #             self.hand_obj.find_basics()
            
    #         self.active_pokemon = ActivePokemon()
    #         self.bench = Bench()
    #         buttons = []
    #         for basic_card in self.hand_obj.basic_cards: 
    #             card = tk.Button(self.mgl_frame, text=basic_card.name, width=20, height=70, command= lambda: set_active_pokemon(basic_card))
    #             buttons.append(card)
                
    #         count=0
    #         for value in buttons:
    #             value.grid(column=count, row=3)
    #             count += 1

    #         message = "Please click on the Pokemon you would like to make the Active!"
    #         self.block_inner_label.configure(text=message)
    #         self.block_inner_label.grid(column=0, row=0)
    #     elif not self.added_to_bench:
    #         add_to_bench()
    #     elif not self.attached_energy:
    #         attach_energy()
    #     else:
    #         self.prize = Prize()
    #         self.prize.set_prize_cards(self.deck)
    #         print("working on it...")
    #         self.choose_player_order()

    def initiate_game(self):
        open('data/received_data.txt', 'w').close()
        winner = ""
        turn = 1
        while True:
            winner = self.game_logic.rock_paper_scissors(self.mgl_frame, turn)
            turn += 1
            if winner:
                break
        #self.play_order = self.game_logic.first_or_second(self.mgl_frame, turn, winner)
        #print(self.play_order)
        for widget in self.mgl_frame.winfo_children():
            widget.destroy()

        self.mgl_frame.destroy()

        self.deck.shuffle_deck()

        self.hand = self.deck.draw_number_of_cards(7)
        self.obj_list = self.load_card_data(self.hand)
        self.hand_obj = Hand(self.obj_list)
        self.hand_obj.find_basics()

        while not self.hand_obj.basic_cards:
            print("Re-shuffling deck...")
            self.deck.return_to_deck(self.hand)
            self.deck.shuffle_deck()
            self.hand = []
            self.hand = self.deck.draw_number_of_cards(7)
            obj_list = []
            obj_list = self.load_card_data(self.hand)
            self.hand_obj.list = obj_list
            self.hand_obj.find_basics()

        for x in self.hand_obj.list:
            print(x.name)
            print(x.images)
            
        self.gameboard.place()
        

            # def set_active_pokemon(basic_card):
            #     self.hand_obj.remove_basic_card(basic_card)
            #     self.active_pokemon.set_card_data(basic_card)
            #     for widget in buttons:
            #         widget.destroy()
            #     print(f"active pokemon: {self.active_pokemon.get_name()}")
            #     self.completed = True
            #     self.initiate_game()

            # def add_to_bench():
            #     def call_hand_methods(basic_card, card):
            #         self.hand_obj.add_to_bench(basic_card, card, self.bench)
            #         if self.hand_obj.basic_cards:
            #             add_to_bench()
            #         else:
            #             self.added_to_bench = True
            #             self.initiate_game()
                
            #     def no():
            #         try:
            #             self.yes_btn.destroy()
            #             self.no_btn.destroy()
            #         except error:
            #             print("error trying to delete btn")
            #         message = "You chose not to add any cards to the Bench."
            #         self.block_inner_label.configure(text=message)
            #         self.block_inner_label.grid(column=0, row=0)
            #         self.added_to_bench = True
            #         self.initiate_game()


            #     def yes():
            #         try:
            #             self.yes_btn.destroy()
            #             self.no_btn.destroy()
            #         except error:
            #             print("error trying to delete btn")
            #         for basic_card in self.hand_obj.basic_cards:
            #             buttons=[] 
            #             card = tk.Button(self.mgl_frame, text=basic_card.name, width=20, height=70, command= lambda: call_hand_methods(basic_card, card))
            #             buttons.append(card)
            #         count=0
            #         for widget in buttons:
            #             widget.grid(column=count, row=3)
            #             count += 1

            #     if self.hand_obj.basic_cards:  
            #         if (len(self.bench.list)<6):
            #             message = "Would you like to add any Pokemon to the Bench"
            #             self.block_inner_label.configure(text=message)
            #             self.block_inner_label.grid(column=0, row=0)

            #             self.yes_btn = tk.Button(self.block_label, text="Yes", command=yes)
            #             self.yes_btn.grid(column=0, row=1)

            #             self.no_btn = tk.Button(self.block_label, text="No", command=no)
            #             self.no_btn.grid(column=1, row=1)
            #         else:
            #             message = "You have the maximum number of Pokemon on the bench"
            #             self.block_inner_label.configure(text=message)
            #             self.block_inner_label.grid(column=0, row=0)
            #     else:
            #         message = "There are no basic cards in your hand."
            #         self.block_inner_label.configure(text=message)
            #         self.block_inner_label.grid(column=0, row=0)  
            #         self.added_to_bench = True
            #         self.initiate_game() 
        
            # def attach_energy():
            #     """attach_energy: called by the main game loop - it lets the user decide whether they want to attach an energy to their pokemon"""
            #     def no():
            #         """no: called by no_btn when user does not want to add an energy to one of their pokemon"""
            #         message = "You chose not to add any energies to your Pokemon."
            #         self.block_inner_label.configure(text=message)
            #         self.block_inner_label.grid(column=0, row=0)
                
            #     def yes():
            #         """yes: called by yes_btn when the user chooses to add an energy to either an active or benched pokemon"""
            #         def attach_to_active():
            #             """attach_to_active: called when user chooses to add an energy to their active pokemon"""
            #             def attach_energy(energy):
            #                 """attach_energy: calls the functionality in hand object to attach the energy to the active pokemon object"""
            #                 self.hand_obj.attach_energy_to_active(energy, self.active_pokemon)
            #                 for widget in buttons:
            #                     widget.destroy()
            #                 message = f"Attached a {energy.name} to {self.active_pokemon.card_data.name}."
            #                 self.block_inner_label.configure(text=message)
            #                 self.block_inner_label.grid(column=0, row=0)
            #                 self.attached_energy = True
            #                 self.initiate_game()
                        
            #             buttons=[] 
                        
            #             for energy in energy_list:
            #                 card = tk.Button(self.mgl_frame, text=energy.name, width=20, height=70, command= lambda: attach_energy(energy))
            #                 buttons.append(card)
                
            #             count=0

            #             for value in buttons:
            #                 value.grid(column=count, row=3)
            #                 count += 1
            
            #             message = "Select the Energy Card you would like to attach to the Active Pokemon."
            #             self.block_inner_label.configure(text=message)
            #             self.block_inner_label.grid(column=0, row=0)

            #         def attach_to_benched():
            #             """attach_to_benched: called when the user chooses to attach an energy to a Benched Pokemon"""
            #             def select_pokemon(pokemon, buttons):
            #                 """select_pokemon: responsible for making the user choose what Benched Pokemon to add the energy to"""
            #                 def attach_energy(energy, pokemon):
            #                     """attach_energy: the method that actually attaches the energy to the Benched Pokemon"""
            #                     self.hand_obj.attach_energy_to_benched(energy, self.bench, pokemon)
            #                     for widget in buttons:
            #                         widget.destroy()
            #                     message = f"Attached a {energy.name} to {pokemon.card_data.name}."
            #                     self.block_inner_label.configure(text=message)
            #                     self.block_inner_label.grid(column=0, row=0)
            #                     self.attached_energy = True
            #                     self.initiate_game()

            #                 for widget in buttons:
            #                     widget.destroy()
                            
            #                 try:
            #                     self.active_btn.destroy()
            #                     self.benched_btn.destroy()
            #                 except error:
            #                     print("error trying to destroy btn")
                            
            #                 buttons=[] 
                            
            #                 for energy in energy_list:
            #                     card = tk.Button(self.mgl_frame, text=energy.name, width=20, height=70, command= lambda: attach_energy(energy, pokemon))
            #                     buttons.append(card)
                    
            #                 count=0
            #                 for widget in buttons:
            #                     widget.grid(column=count, row=3)
            #                     count += 1

            #                 message = f"Select the Energy Card you would like to attach to the {pokemon.card_data.name}."
            #                 self.block_inner_label.configure(text=message)
            #                 self.block_inner_label.grid(column=0, row=0)


            #             message = "Select the the Pokemon on the Bench that you want to attach an Energy to."
            #             self.block_inner_label.configure(text=message)
            #             self.block_inner_label.grid(column=0, row=0)

            #             buttons = []

            #             for pokemon in self.bench.list:
            #                 card = tk.Button(self.mgl_frame, text=pokemon.card_data.name, width=20, height=70, command= lambda: select_pokemon(pokemon, buttons))
            #                 buttons.append(card)
                
            #             count=0
            #             for card in buttons:
            #                 card.grid(column=count, row=3)
            #                 count += 1

            #         if not (self.bench.list):
            #             attach_to_active()
            #         else:
            #             message = "Would you like to attach an energy to the Active Pokemon or a Benched Pokemon?"
            #             self.block_inner_label.configure(text=message)
            #             self.block_inner_label.grid(column=0, row=0)
                        
            #             self.yes_btn.destroy()
            #             self.no_btn.destroy()

            #             self.active_btn = tk.Button(self.block_label, text="Attach to the Active Pokemon", command=attach_to_active)
            #             self.active_btn.grid(column=0, row=1)

            #             self.benched_btn = tk.Button(self.block_label, text="Attach to a Pokemon on the Bench.", command=attach_to_benched)
            #             self.benched_btn.grid(column=1, row=1)
                
            #     energy_list = []
            #     for card in self.hand_obj.list:
            #         if card.supertype == 'Energy':
            #             energy_list.append(card)
            #     if len(energy_list) >= 1:
            #         message = "Would you like to attach an energy to a Pokemon?"
            #         self.block_inner_label.configure(text=message)
            #         self.block_inner_label.grid(column=0, row=0)

            #         self.yes_btn = tk.Button(self.block_label, text="Yes", command=yes)
            #         self.yes_btn.grid(column=0, row=1)

            #         self.no_btn = tk.Button(self.block_label, text="No", command=no)
            #         self.no_btn.grid(column=1, row=1)
            #     else:
            #         message = "There are no energies in your hand."
            #         self.block_inner_label.configure(text=message)
            #         self.block_inner_label.grid(column=0, row=0)
            #         self.attached_energy = True
            #         self.initiate_game()

    # def choose_player_order(self):
    #     """choose_player_order: this method decides which player goes first. If flip coin returns true, then the player decides. Else, we wait for the opponent to decide."""
    #     if self.flip_coin:
    #         """let the user decide"""
    #     else:
    #         """wait for user to decide"""
            

    # def flip_coin(self):
    #     """flip_coin: call this method when you need to flip a coin and return the result. Returns True if 0, and 1 if false"""
    #     self.coin_result = random.randint(0, 1)
    #     if self.coin_result == 0:
    #         return True
    #     else:
    #         return False

    def load_card_data(self, hand):
        obj_list = []
        file = open("data/base1.json",encoding='utf-8')
        data = json.load(file)
        for card in hand:
            count = 0
            for x in data:
                if card == x['id']:
                    count += 1
                    if x['supertype'] == 'Pokémon':
                        if (x.get('weaknesses')!=None) and (x.get('retreatCost')!=None) and (x.get('evolvesFrom')!=None) and (x.get('abilities')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['evolvesFrom'], x['abilities'], x['attacks'], x['weaknesses'], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('weaknesses')!=None) and (x.get('retreatCost')!=None) and (x.get('evolvesFrom')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['evolvesFrom'], [], x['attacks'], x['weaknesses'], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('weaknesses')!=None) and (x.get('retreatCost')!=None) and (x.get('abilities')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", x['abilities'], x['attacks'], x['weaknesses'], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('weaknesses')!=None) and (x.get('retreatCost')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", [], x['attacks'], x['weaknesses'], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('weaknesses')!=None) and (x.get('evovlesFrom')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['evolvesFrom'], [], x['attacks'], x['weaknesses'], [], 0, x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('weaknesses')!=None) and (x.get('abilities')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", x['abilities'], x['attacks'], x['weaknesses'], [], 0, x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('weaknesses')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", [], x['attacks'], x['weaknesses'], [], 0, x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('retreatCost')!=None) and (x.get('evolvesFrom')!=None) and (x.get('abilities')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['evolvesFrom'], x['abilities'], x['attacks'], [], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif  (x.get('retreatCost')!=None) and (x.get('abilities')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", x['abilities'], x['attacks'], [], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('retreatCost')!=None) and (x.get('evolvesFrom')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['evolvesFrom'], [], x['attacks'], [], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('retreatCost')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", [], x['attacks'], [], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('evolvesFrom')!=None) and (x.get('abilties')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['evolvesFrom'], x['abilities'], x['attacks'], [], [], 0, x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('evovlesFrom')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['evolvesFrom'], [], x['attacks'], [], [], 0, x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        elif (x.get('abilities')!=None):
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", x['abilities'], x['attacks'], [], [], 0, x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        else:
                            new_card = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], "", [], x['attacks'], [], [], 0, x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                    elif x['supertype'] == 'Trainer':
                        new_card = TrainerCard(x['name'], x['supertype'], x['rules'], x['number'], x['artist'], x['rarity'], x['images'])
                    elif x['supertype'] == 'Energy':
                        if (x.get('rules')!=None):
                            new_card = EnergyCard(x['name'], x['supertype'], x['subtypes'], x['rules'],x['number'], x['artist'], x['rarity'], x['images'])
                        else:
                            new_card = EnergyCard(x['name'], x['supertype'], x['subtypes'], x['number'], x['artist'], x['rarity'], x['images'])
                    obj_list.append(new_card)
        file.close()
        return obj_list
        
    def player_turn_loop(self, hand, deck, bench):
        hand.append_to_hand(deck.pop_card())
        hand.add_to_bench(bench)