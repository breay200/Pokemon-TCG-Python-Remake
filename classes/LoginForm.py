from os import execl
from tkinter.font import Font
from typing import Text
from classes.AccountCreator import *
from classes.Form import *
from classes.MainMenu import MainMenu
from misc_functions import check_in_file, check_password
from tkinter import font
import tkinter as tk
import getpass
import hashlib
from classes.config import *
from PIL import Image, ImageTk

class LoginForm(Form):
    def __init__(self):
        width = Config.master.winfo_width()
        height = Config.master.winfo_height()
        self.width = width
        self.height = height

        self.login_frame = tk.Frame(Config.master, width=self.width, height=self.height)

        self.side_bar_width = int(width/3)
        self.side_bar_height = int(height)
        self.side_bar_frame = tk.Frame(self.login_frame, width=self.side_bar_width, height=self.side_bar_height, bg="red")
        

        self.failed_logins = 0
        
        font_height = 0 - int(self.side_bar_height*0.04)
        txt_label_font = font.Font(family="Courier", size=font_height, weight="bold", underline=1)
        self.txt_label = tk.Label(self.side_bar_frame, text="Sign into your account", fg="white", bg="red", font=txt_label_font)


        input_frame_height = int(self.side_bar_height*0.3)
        self.input_frame = tk.Frame(self.login_frame, width=self.side_bar_width, height=input_frame_height, bg="red")
        
        input_font = font.Font(family="Courier", size=(0 - int(self.side_bar_height*0.02)), weight="bold")
        
        self.username_label = tk.Label(self.input_frame, text="USERNAME:", font=input_font, fg="white", bg="red")
        self.password_label = tk.Label(self.input_frame, text="PASSWORD:", font=input_font, fg="white", bg="red")

        self.login_username = tk.StringVar()
        self.login_password = tk.StringVar()
        
        self.login_username_entry = tk.Entry(self.input_frame, textvariable=self.login_username, bg="white", fg="black")
        self.login_password_entry = tk.Entry(self.input_frame, textvariable=self.login_password, show="*")

        
        self.arrow_img = Image.open("images/arrow.png").resize((int(self.side_bar_width*0.2), int(input_frame_height*0.4)))
        self.arrow_img = ImageTk.PhotoImage(self.arrow_img)

        self.login_submit_btn = tk.Button(self.login_frame, bg="red" , image=self.arrow_img, command=self.check_account, width=int(self.side_bar_width*0.2), height=int(input_frame_height*0.4))

        self.login_forgot_btn = tk.Button(self.login_frame, text="Forgot Password", command=self.forgot_password)

        self.login_error_label = tk.Label(self.login_frame)

        self.login_create_btn = tk.Button(self.login_frame, text="Create Account", command=self.create_account)

        self.login_fail_label = tk.Label(self.login_frame)

        self.txt_label.place(x=0, y=int(self.side_bar_height*0.1))
        
        self.username_label.place(x=0, y=0)
        self.login_username_entry.place(x=0, y=int(input_frame_height*0.1), width=int(self.side_bar_width*0.6), height=int(input_frame_height*0.25))
        
        self.password_label.place(x=0,y=int(input_frame_height*0.4))
        self.login_password_entry.place(x=0, y=int(input_frame_height*0.5), width=int(self.side_bar_width*0.6), height=int(input_frame_height*0.25))
        
        self.login_submit_btn.place(x=int((self.side_bar_width*0.5)-(self.side_bar_width*0.1)), y=int(self.side_bar_height*0.5))

        self.input_frame.place(x=0, y=int(self.side_bar_height*0.2))
        self.side_bar_frame.place(x=0, y=0)
        self.login_frame.place(x=0, y=0)

    def check_account(self):
        username = self.login_username.get()
        if username:
            if check_in_file("data/passwd.txt", username):
                if self.login(username):
                    user = User(username)
                    user.load_user_data()
                    self.login_frame.destroy()
                    mainmenu = MainMenu(user)
                else:
                    self.login_error_label.configure(text="You did not login successfully.")
                    self.login_error_label.grid(column=3, row=5)
            else:
                self.login_error_label.configure(text="User does not exist")
                self.login_error_label.grid(column=3, row=5)
        elif not username:
            self.login_error_label.configure(text="You did not enter a username")
            self.login_error_label.grid(column=3, row=5)

    def create_account(self):
        self.login_frame.destroy()
        account_creator = AccountCreator()
        
    def login(self, username):
            password = self.login_password_entry.get()
            if password and username:
                password_hash = hashlib.md5(str(password).encode('utf-8'))
                password = password_hash.hexdigest()
                if check_password(username, password):
                    self.login_error_label.configure(text="You have logged in successfully!")
                    self.login_error_label.grid(column=3, row=6)
                    #return a True value if login success
                    return True
                else:
                    self.failed_logins += 1
                    self.login_error_label.configure(text="You have failed to login.")
                    self.login_error_label.grid(column=3, row=6)
                    self.login_fail_label.configure(text=f"There are {3-self.failed_logins} attempts remaining")
                    self.login_fail_label.grid(column=4, row=6)
                    if self.failed_logins >= 3:
                        print(self.failed_logins)
                        self.login_error_label.configure("You have failed too many times. Account has been locked.")
                        self.login_error_label.grid(column=3, row=6)
                        self.login_submit_btn.grid_remove()
                        #need to create account lock method
                        #return a False value if login failed
                        return False
            else:
                self.login_error_label.configure(text="You need to enter a username and password")
                self.login_error_label.grid(column=3, row=5)

    def forgot_password(self):
        """forgot_password: call this method when the user clicks on the forgot password button. Checks to see if the user has entered a username, and continues with the password reset."""
        try:
            username = self.login_username.get()
        except Exception as e:
            print(e)
        
        if len(username)>1:
            print("username greater than 1")
        else:
            print("no username")

'''
            self.login_frame.
            account_creator = AccountCreator()
            account_creator.create_account(self.master, username)
            
            else:
                #NEED TO DO THIS - FORGOT PASSWORD METHOD
                email = input("Please enter your email address: ")
                try:
                    email = str(email)
                except TypeError:
                    print("You enter an invalid value")
                if check_in_file("data/player_data.txt", email):
                    print("We are sending a password reset token to your email address")
                    #NEED TO DO: SEND EMAIL RESET CODE - METHODS
                    pass
                else:
                    print("This email isn't registered to an account")
'''