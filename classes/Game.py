from classes.Player import *
from classes.Deck import *
from classes.EnergyCard import *
from classes.TrainerCard import *
from classes.PokemonCard import *

class Game():
    def __init__(self, user):
        self.user = user

    def main_game_loop(self):
        deck = Deck()
        #player = Player(self.user.username)
        print("Your current deck is: {}. Would you like to change your deck?")
        response = ""
        while response not in ["Y", "N"]:
            response = input("Enter Y or N: ")
            try:
                response = str(response)
            except ValueError:
                print("You entered an invalid value!")
            if response == "Y":
                decks = deck.get_decks("set1.json")
                deck.set_active_deck(decks)
                deck.load_deck("set1.json")
                break
            else:
                print("Need to implement this functionality. Save active deck to file and load in.")
        deck.shuffle_deck()
        hand = deck.draw_number_of_cards(7)
        
        obj_list = []
        file = open("base1.json",encoding='utf-8')
        data = json.load(file)
        for card in hand:
            count = 0
            for x in data:
                if card == x['id']:
                    count += 1
                    if x['supertype'] == 'Pokémon':
                        count = PokemonCard(x['name'], x['supertype'], x['subtypes'], x['level'], x['hp'], x['types'], x['attacks'], x['weaknesses'], x['retreatCost'], x['convertedRetreatCost'], x['number'], x['artist'], x['rarity'], x['flavorText'],x['nationalPokedexNumbers'], x['images'])
                        obj_list.append(count)
                    elif x['supertype'] == 'Trainer':
                        count = TrainerCard(x['name'], x['supertype'], x['rules'], x['number'], x['artist'], x['rarity'], x['images'])
                        obj_list.append(count)
                    elif x['supertype'] == 'Energy':
                        count = EnergyCard(x['name'],x['supertype'],x['subtypes'], x['number'], x['artist'], x['rarity'], x['images'])
                        obj_list.append(count)
                continue
        file.close()
        print(obj_list)
        
