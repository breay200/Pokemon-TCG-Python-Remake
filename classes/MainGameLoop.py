from classes.Bench import Bench
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
from classes.config import Config
import time

class MainGameLoop:
    def __init__(self, user) -> None:
        self.user = user

        self.mgl_frame = tk.Frame(Config.master)
        
        self.block_label = tk.Label(self.mgl_frame, width=400, height=200, background='#4A7A8C')
        self.block_label.grid(column=0, row=0)

        self.block_inner_label = tk.Label(self.block_label)

        self.deck = Deck()

        if user.active_deck != "":
            message = f"Your current deck is: {self.user.active_deck}.\nWould you like to change your deck?"
            self.block_inner_label.configure(text=message)
            self.block_inner_label.grid(column=0, row=0)

            self.yes_btn = tk.Button(self.block_label, text="Yes")
            self.yes_btn.grid(column=0, row=1)

            self.no_btn = tk.Button(self.block_label, text="No", command=self.load_current_deck)
            self.no_btn.grid(column=1, row=1)

        else:
            #call method to choose deck
            message = "You don't have an active deck selected, please choose one for your battle: "
            self.block_inner_label.configure(text=message)
            self.block_inner_label.grid(column=0, row=0)
        
        self.mgl_frame.grid(column=0, row=0)

    def change_deck(self):
        self.deck.set_active_deck()
        self.deck.load_deck("data/set1.json")
                    
    def load_current_deck(self):
        self.deck.active_deck = str(self.user.active_deck).replace(" ", "")
        self.deck.load_deck("data/set1.json")
        self.initiate_game()

    def initiate_game(self):
        if self.yes_btn:
            self.yes_btn.destroy()
            self.no_btn.destroy()
        
        message = "STARTING GAME!"
        self.block_inner_label.configure(text=message)
        self.block_inner_label.grid(column=0, row=0)
        
        time.sleep(1)

        self.deck.shuffle_deck()
        hand = self.deck.draw_number_of_cards(7)
        obj_list = self.load_card_data(hand)
        hand_obj = Hand(obj_list)
        hand_obj.find_basics()

        while not hand_obj.basic_cards:
            message = "There were no Basic Pokemon in your hand\nRe-shuffling..."
            time.sleep(1)
            self.block_inner_label.configure(text=message)
            self.block_inner_label.grid(column=0, row=0)
            self.deck.return_to_deck(hand)
            self.deck.shuffle_deck()
            hand = []
            hand = self.deck.draw_number_of_cards(7)
            obj_list = []
            obj_list = self.load_card_data(hand)
            hand_obj.list = obj_list
            hand_obj.find_basics()
        
        ## I AM UP TO HERE
        #hand_obj.print_cards(hand_obj.list)
        #print("\nPLEASE SELECT A BASIC CARD FROM YOUR HAND")
        #hand_obj.print_card_names(hand_obj.basic_cards)
        
        for card in hand_obj.basic_cards:
            
        
        print("\nplease enter the name of Basic Pokémon you want to make the Active Pokemon")
        chosen_pokemon = hand_obj.select_basic()
        active_pokemon = ActivePokemon(chosen_pokemon)
        print(f"active pokemon: {active_pokemon.get_name()}")
        bench = Bench()
        hand_obj.add_to_bench(bench)
        print(hand_obj.attach_energy(active_pokemon, bench))
        prize = Prize()
        print(f"deck size: {deck.get_deck_size()}")
        prize.set_prize_cards(deck)
        print(f"deck size: {deck.get_deck_size()}")

        print("working on it...")
    
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
