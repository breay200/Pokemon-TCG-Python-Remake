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
from classes.User import *

class Game():
    def __init__(self, user):
        self.user = user

    def main_game_loop(self):
        deck = Deck()
        if self.user.active_deck != "":
            print(f"Your current deck is:{self.user.active_deck}. Would you like to change your deck?")
            response = ""
            while response not in ["y", "n"]:
                response = input("Enter y or n: ").lower()
                try:
                    response = str(response)
                except ValueError:
                    print("You entered an invalid value!")
                if response == "y":
                    deck.set_active_deck()
                    deck.load_deck("data/set1.json")
                    break
                elif response == "n":
                    deck.active_deck = str(self.user.active_deck).replace(" ", "")
                    deck.load_deck("data/set1.json")
                    break
        else:
            print("You don't have an active deck selected, please choose one for your battle: ")
            deck.set_active_deck()
            print("Would you like to make this Deck your go-to? ")
            response = ""
            while response not in ["y", "n"]:
                print("Enter y or n: ")
            if response == "y":
                #implement save to deck functionality 
                pass
            else:
                pass
            deck.load_deck("data/set1.json")

        #GAME STARTS
        deck.shuffle_deck()
        hand = deck.draw_number_of_cards(7)
        obj_list = self.load_card_data(hand)
        hand_obj = Hand(obj_list)
        hand_obj.find_basics()

        while not hand_obj.basic_cards:
            print("There were no Basic Pokemon in your hand\nRe-shuffling...")
            deck.return_to_deck(hand)
            deck.shuffle_deck()
            hand = []
            hand = deck.draw_number_of_cards(7)
            obj_list = []
            obj_list = self.load_card_data(hand)
            hand_obj.list = obj_list
            hand_obj.find_basics()

        hand_obj.print_cards(hand_obj.list)
        print("\nPLEASE SELECT A BASIC CARD FROM YOUR HAND")
        hand_obj.print_card_names(hand_obj.basic_cards)
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
        

        
