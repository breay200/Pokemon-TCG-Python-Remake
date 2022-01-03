from os import execl
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
        self.width = Config.master.winfo_width()
        self.height = Config.master.winfo_height()

        self.login_frame = tk.Frame(Config.master, width=self.width, height=self.height)

        self.side_bar_width = int(self.width/3)
        self.side_bar_height = int(self.height)
        self.side_bar_frame = tk.Frame(self.login_frame, width=self.side_bar_width, height=self.side_bar_height, bg="red")
        
        self.login_image = ImageTk.PhotoImage(Image.open("images/login_img.jpg").resize((int(self.width*(2/3)), self.height)))
        self.login_image_label = tk.Label(self.login_frame, image=self.login_image, width=int(self.width*(2/3)), height=self.height, bd=-1)
        self.login_image_label.place(x=int(self.width/3), y=0)
        
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

        self.login_forgot_btn = tk.Button(self.login_frame, text="Forgot Password", command=self.forgot_password, bg="white", fg="red")

        self.login_error_label = tk.Label(self.login_frame, bg="white", fg="red")

        self.login_create_btn = tk.Button(self.login_frame, text="Create an Account", command=self.create_account, bg="white", fg="red")        

        self.txt_label.place(x=0, y=int(self.side_bar_height*0.1))
        
        self.username_label.place(x=0, y=0)
        self.login_username_entry.place(x=0, y=int(input_frame_height*0.1), width=int(self.side_bar_width*0.6), height=int(input_frame_height*0.25))
        
        self.password_label.place(x=0,y=int(input_frame_height*0.4))
        self.login_password_entry.place(x=0, y=int(input_frame_height*0.5), width=int(self.side_bar_width*0.6), height=int(input_frame_height*0.25))
        
        Config.master.bind("<Return>", lambda event:self.check_account(event))

        self.login_submit_btn.place(x=int(self.side_bar_width*0.7), y=int(self.side_bar_height*0.2625))
        self.login_forgot_btn.place(x=0, y=self.height*0.8)
        self.login_create_btn.place(x=0, y=self.height*0.9)

        self.input_frame.place(x=0, y=int(self.side_bar_height*0.2))
        self.side_bar_frame.place(x=0, y=0)
        self.login_frame.place(x=0, y=0)

    def check_account(self, event=None):
        username = self.login_username.get().lower()
        if username:
            if check_in_file("data/passwd.txt", username):
                if self.login(username):
                    Config.master.unbind("<Return>")
                    user = User(username)
                    user.load_user_data()
                    self.login_frame.destroy()
                    mainmenu = MainMenu(user)
                else:
                    self.login_error_label.configure(text="There was an error with the username or password.")
                    self.login_error_label.place(x=0, y=self.side_bar_height*0.7)
            else:
                self.login_error_label.configure(text="This username does not exist")
                self.login_error_label.place(x=0, y=self.side_bar_height*0.7)
        elif not username:
            self.login_error_label.configure(text="You did not enter a username")
            self.login_error_label.place(x=0, y=self.side_bar_height*0.7)

    def create_account(self):
        self.login_frame.destroy()
        account_creator = AccountCreator()
        
    def login(self, username):
            password = self.login_password_entry.get()
            if password and username:
                password_hash = hashlib.md5(str(password).encode('utf-8'))
                password = password_hash.hexdigest()
                if check_password(username, password):
                    return True
                else:
                    return False
            else:
                self.login_error_label.configure(text="You need to enter a username and password")
                self.login_error_label.place(x=0, y=self.side_bar_height*0.7)

    def forgot_password(self):
        """forgot_password: call this method when the user clicks on the forgot password button. Checks to see if the user has entered a username, and continues with the password reset."""
        try:
            username = self.login_username.get()
        except Exception as e:
            print(e)
        
        if username:
            self.forgot_frame_width = int(self.width*(2/3)*(13/20))
            self.forgot_frame_height = int(self.height*(13/20))
            self.forgot_frame = tk.Frame(self.login_frame, width=self.forgot_frame_width, height=self.forgot_frame_height, bg="white")

            self.reset_label = tk.Label(self.forgot_frame, text="To reset your password, we need to submit an authentication token to your E-mail address")
            self.reset_label.place(x=0,y=0)

            self.email_label = tk.Label(self.forgot_frame, text="Enter your E-mail address: ", fg="red")
            self.email_label.place(x=0, y=self.forgot_frame_height*0.1)

            self.email_entry = tk.Entry(self.forgot_frame, fg="black")
            self.email_entry.place(x=0, y=self.forgot_frame_height*0.15)

            self.re_email_label = tk.Label(self.forgot_frame, text="Re-enter your E-mail address: ", fg="red")
            self.re_email_label.place(x=0, y=self.forgot_frame_height*0.2)

            self.re_email_entry = tk.Entry(self.forgot_frame, fg="black")
            self.re_email_entry.place(x=0, y=self.forgot_frame_height*0.25)

            self.forgot_submit_btn = tk.Button(self.forgot_frame, text="Submit", command=self.submit)
            self.forgot_submit_btn.place(x=0, y=self.forgot_frame_height*0.4)

            self.verification_label = tk.Label(self.forgot_frame, text="The authentication token sent to your E-mail address verifies your identity")
            self.verification_label.place(x=0, y=self.forgot_frame_height*0.5)

            self.auth_label = tk.Label(self.forgot_frame, text="Enter the authenticaiton token: ")
            self.auth_label.place(x=0, y=self.forgot_frame_height*0.6)

            self.auth_entry = tk.Entry(self.forgot_frame, fg="black")
            self.auth_entry.place(x=0, y=self.forgot_frame_height*0.65)

            self.forgot_frame.place(x=int(self.width*0.45), y=int(self.height*0.175))

            for widget in self.forgot_frame.winfo_children():
                widget.configure(bg="white")

        # else:
        #     print("no username")

        #     self.login_frame.
        #     account_creator = AccountCreator()
        #     account_creator.create_account(self.master, username)
            
        #     else:
        #         #NEED TO DO THIS - FORGOT PASSWORD METHOD
        #         email = input("Please enter your email address: ")
        #         try:
        #             email = str(email)
        #         except TypeError:
        #             print("You enter an invalid value")
        #         if check_in_file("data/player_data.txt", email):
        #             print("We are sending a password reset token to your email address")
        #             #NEED TO DO: SEND EMAIL RESET CODE - METHODS
        #             pass
        #         else:
        #             print("This email isn't registered to an account")

    def submit(self):
        print("hello")