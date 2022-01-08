import requests
from requests.auth import HTTPBasicAuth
import json
from PIL import Image
from io import BytesIO
import tkinter as tk
from classes.config import *
import re

class APISearch():
    def __init__(self) -> None:
        width, height, _, _ = re.split(r'[x+]', Config.master.winfo_geometry())
        self.search_width = int(width)
        self.search_height = int(height)
        self.search_canvas = tk.Canvas(Config.master, width = self.search_width, height = self.search_height)
        
        #could just do a lamda expression that changes lambda _: self.submit['command'] = self.search_set or self.search_card 
        self.card_search = tk.Button(self.search_canvas, text="Search for one or many cards", command=self.card_search)
        self.set_search = tk.Button(self.search_canvas, text="Search for one or many sets", command=self.set_search)

        self.query = tk.StringVar()
        self.entry = tk.Entry(self.search_canvas, textvariable=self.query)
        
        self.submit = tk.Button(self.search_canvas, text="search database")
        
        self.name_label = tk.Label(self.search_canvas, text="search by name")
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self.search_canvas, textvariable=self.query)
        
        self.output = tk.Label(self.search_canvas,)
        Config.master.bind("<Escape>", lambda event: self.destroy(event))
        self.place()

    def card_search(self):
        self.name_label.place(x=0, y=self.search_height*0.3)
        self.name_entry.place(x=self.search_width*0.25, y=self.search_height*0.3)
        self.submit.place(x=self.search_width*0.6, y=self.search_height*0.3)
        self.submit['command'] = self.search_card
        
    def set_search(self):
        self.name_label.place(x=0, y=self.search_height*0.3)
        self.name_entry.place(x=self.search_width*0.25, y=self.search_height*0.3)
        self.submit.place(x=self.search_width*0.6, y=self.search_height*0.3)
        self.submit['command'] = self.search_set

    def place(self):
        self.card_search.place(x=self.search_width*0.25, y=self.search_height*0.1)
        self.set_search.place(x=self.search_width*0.5,  y=self.search_height*0.1)
        # self.output.place(x=0, y=self.search_height*0.2)
        # self.entry.place(x=0, y=0)
        # 
        self.search_canvas.place(x=0, y=0)

    def destroy(self, event=None):
        for widget in self.search_canvas.winfo_children():
            widget.destroy()
        self.search_canvas.destroy()
        Config.master.unbind("<Escape>")

    def search_card(self):
        name = self.name_var.get().lower()

        headers = { 'User-Agent': 'Mozilla/5.0', 'X-Api-Key': 'a8139628-6932-4c7e-a08c-1c5f2dc52060'}

        url = "https://api.pokemontcg.io/v1/cards?name=" + name

        response = requests.get(url, headers)
        data = json.loads(response.text)
        text = ""
        for key in data:
            if key == 'cards':
                for card in data['cards']:
                    text += f"{card['id']}, {card['name']}\n"
        self.output['text'] = text
        self.output.place(x=0, y=self.search_height*0.4)
    
    def search_set(self):
        name = self.name_var.get().lower()

        headers = { 'User-Agent': 'Mozilla/5.0', 'X-Api-Key': 'a8139628-6932-4c7e-a08c-1c5f2dc52060'}

        url = "https://api.pokemontcg.io/v1/sets?name=" + name

        response = requests.get(url, headers)
        data = json.loads(response.text)
        text = ""
        print(data['sets'])
        for datas in data['sets']:
            print(datas)
            #text += f"{datas}\n" 
            # if key == 'cards':
            #     for card in data['cards']:
            #         text += f"{card['id']}, {card['name']}\n"
        self.output['text'] = text
        self.output.place(x=0, y=self.search_height*0.5)

                    

'''
#THIS CODE GETS A LARGE IMAGE OF A POKEMON CARD FROM THE DATA PROVIDED IN THE BASE1 DATASET, AND USES AN API GET REQUEST TO DOWNLOAD THE DATA AND THEN SUBSEQUENTLY USES PIL TO DISPLAY THE IMAGE TO THE USER
img_url = "https://images.pokemontcg.io/base1/1_hires.png"
#response = requests.get(img_url)
#img = Image.open(BytesIO(response.content))
img = Image.open(requests.get(img_url, stream=True).raw)
img.show()
'''
