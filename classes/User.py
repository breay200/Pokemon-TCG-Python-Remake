from datetime import date
from misc_functions import append_to_file

class User():
    def __init__(self, username="", matches_won=0, matches_lost=0, date_joined=00-00-00, favourite_pokemon="", email_addr=""):
        self.username = username
        self.matches_won = matches_won
        self.matches_lost = matches_lost
        self.date_joined = date_joined
        self.favourite_pokemon = favourite_pokemon
        self.email_addr = email_addr
    
    def __str__(self):
        return f"username: {self.username}\nmatches won: {self.matches_won}\nmatches lost: {self.matches_lost}\ndate joined: {self.date_joined}\nfavourite pokemon: {self.favourite_pokemon}\nemail address: {self.email_addr}"

    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username

    def update_wins(self):
        self.matches_won += 1

    def update_losses(self):
        self.matches_lost += 1 
    
    def update(self):
        #TO DO
        pass

    def load_user_data(self):
            file = open("player_data.txt", "r")
            lines = file.readlines()
            for line in lines:
                username, matches_won, matches_lost, date_joined, favourite_pokemon, email_addr = line.strip().split(",")
                if (self.username in username):
                    self.matches_won = matches_won
                    self.matches_lost = matches_lost
                    self.date_joined = date_joined
                    self.favourite_pokemon = favourite_pokemon
                    self.email_addr = email_addr
                    break
                else:
                    print("username not found")
            file.close()


    def create_user_data(self):
        while True:
            print("Setting up your account for the first time...")
            print("Please enter the name of your favourite Pokemon")
            favourite_pokemon = input("input: ")
            try:
                favourite_pokemon = str(favourite_pokemon)
            except ValueError:
                print("Please enter a string value!")
            print("Please enter your email address.")
            email_addr = input("input: ")
            try:
                email_addr = str(email_addr)
            except ValueError:
                print("Please enter a string value!")
            if type(favourite_pokemon) == str and type(email_addr) == str:
                break
            else:
                pass
        today = date.today()
        self.date_joined = today.strftime("%d-%m-%Y")
        self.favourite_pokemon = favourite_pokemon
        self.email_addr = email_addr
        text = f"{self.username}, {self.matches_won}, {self.matches_lost}, {self.date_joined}, {self.favourite_pokemon}, {self.email_addr}"
        append_to_file("player_data.txt", text)
    
    def update_to_file(self):
        file = open("player_data.txt", "wr")
        lines = file.readlines()
        for line in lines:
            username, matches_won, matches_lost, date_joined, favourite_pokemon, email_addr = line.strip().split(",")
            if (self.username in username):
                username = self.username
                matches_won = self.matches_won
                matches_lost = self.matches_lost
                date_joined = self.date_joined
                favourite_pokemon = self.favourite_pokemon
                email_addr = self.email_addr
                file.write(f"{username},{matches_won},{matches_lost},{date_joined},{favourite_pokemon},{email_addr}")
            else:
                print("username not found")
            file.close()
        
        
            
        

