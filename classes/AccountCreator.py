from classes.AccountManger import *
from classes.User import *
from misc_functions import check_in_file
import tkinter as tk
from classes.config import *
from classes.Game import *

class AccountCreator(AccountManager):
    def __init__(self):
        self.create_account_frame = tk.Frame(Config.master)
        
        self.title_label = tk.Label(self.create_account_frame, text="Enter information below to create an account")
        self.title_label.grid(column=1,row=0)

        self.username_label = tk.Label(self.create_account_frame, text="Enter a username: ")
        self.username_label.grid(column=1, row=1)
        
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self.create_account_frame, textvariable=self.username)
        self.username_entry.grid(column=1,row=2)
        
        self.password_label = tk.Label(self.create_account_frame, text="Enter a password: ")
        self.password_label.grid(column=1, row=3)
        
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self.create_account_frame, textvariable=self.password)
        self.password_entry.grid(column=1,row=4)

        self.password_label_2 = tk.Label(self.create_account_frame, text="Repeat password: ")
        self.password_label_2.grid(column=1, row=5)

        self.password2 = tk.StringVar()
        self.password_entry2 = tk.Entry(self.create_account_frame, textvariable=self.password2, show="*")
        self.password_entry2.grid(column=1,row=6)

        self.email_label = tk.Label(self.create_account_frame, text="Enter your email address: ")
        self.email_label.grid(column=1, row=7)

        self.email = tk.StringVar()
        self.email_entry = tk.Entry(self.create_account_frame, textvariable=self.email)
        self.email_entry.grid(column=1,row=8)
        
        self.fav_label = tk.Label(self.create_account_frame, text="Enter the name of your favourite Pokemon: ")
        self.fav_label.grid(column=1, row=9)

        self.fav_poke = tk.StringVar()
        self.fav_entry = tk.Entry(self.create_account_frame, textvariable=self.fav_poke)
        self.fav_entry.grid(column=1,row=10)

        self.submit_btn = tk.Button(self.create_account_frame, text="Submit", command=self.create_account)
        self.submit_btn.grid(column=1, row=11)

        self.error_msg = tk.Label(self.create_account_frame)
        
        self.create_account_frame.grid(column=0, row=0)

    def create_account(self):
        username = self.username.get()
        password = self.password.get()
        if not check_in_file("data/passwd.txt", username):
            if (self.password.get()) == (self.password2.get()):
                hash_and_store(username, password)
                self.create_account_frame.destroy()
                user = User(username)
                user.create_user_data(self.fav_poke.get(), self.email.get())
                deck_ui = DeckUI(user)

            else:
                self.error_msg.configure(text="Passwords must match")
                self.error_msg.grid(column=1, row=12)
        else:
            self.error_msg.configure(text="Username already in use")
            self.error_msg.grid(column=1, row=12)