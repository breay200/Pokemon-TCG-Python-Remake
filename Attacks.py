import random

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
        print(f"{active_pokemon.card_data.name} dealt {DMG} to {defending_pokemon.card_data.health}")
        return active_pokemon, defending_pokemon
    
    def bubblebeam(self, active_pokemon, defending_pokemon):
        DMG = 40
        COIN = random.choice([True, False])
        defending_pokemon = defending_pokemon - DMG
        if COIN:
            defending_pokemon.isParalyzed = True
            print(f"{active_pokemon.card_data.name} paralyzed and dealt {DMG} to {defending_pokemon.card_data.name}!")
        else:
            print(f"failed to paralyze {defending_pokemon.card_data.name}")
            print(f"{active_pokemon.card_data.name} dealt {DMG} to {defending_pokemon.card_data.name}!")
        return active_pokemon, defending_pokemon

