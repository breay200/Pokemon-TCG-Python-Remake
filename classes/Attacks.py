import random
from classes.Bench import *

class Attacks():
    def __init__(self) -> None:
        pass

    def confuse_ray(self, defending_pokemon):
        COIN = random.choice([True, False])
        if COIN:
            defending_pokemon.isConfused = True
            print(f"{defending_pokemon.card_data.name} is now Confused")
        else:
            print("Confuse Ray failed")
        return defending_pokemon
    
    def hydro_pump(self, active_pokemon, defending_pokemon):
        DMG = 40
        water_energy_count = 0
        for energy in active_pokemon.energies:
            if energy.name == "Water Energy":
                water_energy_count += 1
        if water_energy_count > 3:
            DMG = 50
        defending_pokemon.health = defending_pokemon.health - DMG
        print(f"{active_pokemon.card_data.name} dealt {DMG} damage to {defending_pokemon.card_data.name}!")
        return active_pokemon, defending_pokemon
    
    def scrunch(self, active_pokemon):
        COIN = random.choice([True, False])
        if COIN:
            active_pokemon.isProtectedFromAttackNextTurn = True
            print(f"{active_pokemon.card_data.name} is invulnerable to all damage done during your opponent's next turn (Any other effects of attacks still happen)")
        else:
            print("Scrunch failed")
        return active_pokemon

    def double_edge(self, active_pokemon):
        DMG = 80
        active_pokemon.health = active_pokemon.health = DMG
        print(f"{active_pokemon.name} dealth {DMG} to itself")
        return active_pokemon

    def fire_spin(self, active_pokemon, defending_pokemon):
        DMG = 100
        active_pokemon.remove_energy("Fire Energy", 2)
        defending_pokemon.health = defending_pokemon.health - DMG
        print(f"{active_pokemon.card_data.name} dealth {DMG} to {defending_pokemon.card_data.name}")
        return active_pokemon, defending_pokemon

    def sing(self, defending_pokemon):
        COIN = random.choice([True, False])
        if COIN:
            defending_pokemon.isAsleep = True
            print(f"{defending_pokemon.card_data.name} is now Asleep")
        else:
            print("Sing failed")
        return defending_pokemon
    
    #TO DO: METRONOME

    def dragon_rage(self, active_pokemon, defending_pokemon):
        DMG = 50
        defending_pokemon.health = defending_pokemon.health - DMG
        print(f"{active_pokemon.card_data.name} dealt {DMG} to {defending_pokemon.card_data.name}")
        return active_pokemon, defending_pokemon
    
    def paralyze_hit(self, DMG, active_pokemon, defending_pokemon):
        COIN = random.choice([True, False])
        defending_pokemon = defending_pokemon - DMG
        if COIN:
            defending_pokemon.isParalyzed = True
            print(f"{active_pokemon.card_data.name} paralyzed and dealt {DMG} to {defending_pokemon.card_data.name}!")
        else:
            print(f"failed to paralyze {defending_pokemon.card_data.name}")
            print(f"{active_pokemon.card_data.name} dealt {DMG} to {defending_pokemon.card_data.name}!")
        return active_pokemon, defending_pokemon

    def bubblebeam(self, active_pokemon, defending_pokemon):
        self.paralyze_hit(40, active_pokemon, defending_pokemon)

    def thunder_wave(self, active_pokemon, defending_pokemon):
        self.paralyze_hit(30, active_pokemon, defending_pokemon)

    #should we use decorators or something for attacks that do not have any special conditions
    def basic_attack(self, DMG, active_pokemon, defending_pokemon):
        defending_pokemon.health -= DMG
        print(f"{active_pokemon.card_data.name} dealt {DMG} to {defending_pokemon.card_data.name}")

    def jab(self, active_pokemon, defending_pokemon):
        DMG = 20
        self.basic_attack(DMG, active_pokemon, defending_pokemon)
        return active_pokemon, defending_pokemon

    def special_punch(self, active_pokemon, defending_pokemon):
        DMG = 40
        self.basic_attack(DMG, active_pokemon, defending_pokemon)
        return active_pokemon, defending_pokemon
    
    def seismic_toss(self, active_pokemon, defending_pokemon):
        DMG = 60
        self.basic_attack(DMG, active_pokemon, defending_pokemon)
        return active_pokemon, defending_pokemon
    
    def selfdestruct(self, bench, active_pokemon, opponents_bench):
        DMG = 20
        for benched_pokemon in bench:
            benched_pokemon.hp -= DMG
        
        for benched_pokemon in opponents_bench:
            benched_pokemon.hp -= DMG
        
        active_pokemon.health -= 80

        print(f"{active_pokemon.card_data.name} dealt {DMG} damage to each Pokémon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pokémon.) {active_pokemon.card_data.name} did 80 damage to itself!")

        return active_pokemon, bench, opponents_bench

    def psychic(self, active_pokemon, defending_pokemon):
        energy_count = len(defending_pokemon.energies)
        DMG = 10 + (energy_count*10)
        defending_pokemon.health -= DMG
        print(f"{active_pokemon.card_data.name} dealt {DMG} to {defending_pokemon.card_data.name}")
        return active_pokemon, defending_pokemon

    def barrier(self, active_pokemon, defending_pokemon):   
        active_pokemon.energies.remove('')
        index = 0
        print(f"Number of attached energies: {len(active_pokemon.energies)}")
        for energy in active_pokemon.energies:
            if energy.name == 'Psychic Energy':
                index = active_pokemon.energies.index(energy)
                del active_pokemon.energies[index]
                break
        print(f"Number of attached energies: {len(active_pokemon.energies)}")
        active_pokemon.isProtectedFromAttackNextTurn = True
        print(f"{active_pokemon.card_data.name} is invulnerable to all damage done during your opponent's next turn (Any other effects of attacks still happen)")
        return active_pokemon, defending_pokemon

    def thrash(self, active_pokemon, defending_pokemon):
        DMG = 30
        COIN = random.choice([True, False])
        if COIN:
            DMG += 10
        else:
            active_pokemon.health -= 10
            defending_pokemon.health -= DMG
            print(f"{active_pokemon.card_data.name} dealt 10 damage to itself and {DMG} to {defending_pokemon.card_data.name}")
        return active_pokemon, defending_pokemon