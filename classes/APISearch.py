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
        self.search_frame = tk.Frame(Config.master, width = self.search_width, height = self.search_height)
        self.query = tk.StringVar()
        self.entry = tk.Entry(self.search_frame, textvariable=self.query)
        self.submit = tk.Button(self.search_frame, text="search database", command=self.search)
        self.output = tk.Label(self.search_frame)
        Config.master.bind("<Escape>", lambda event: self.destroy(event))
        self.output.place(x=0, y=self.search_height*0.2)
        self.entry.place(x=0, y=0)
        self.submit.place(x=self.search_width*0.3, y=0)
        self.search_frame.place(x=0, y=0)

    def destroy(self, event=None):
        for widget in self.search_frame.winfo_children():
            widget.destroy()
        self.search_frame.destroy()
        Config.master.unbind("<Escape>")

    def search(self):
        name = self.query.get().lower()

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
        self.output.place(x=0, y=self.search_height*0.1)
                    

'''
#THIS CODE GETS A LARGE IMAGE OF A POKEMON CARD FROM THE DATA PROVIDED IN THE BASE1 DATASET, AND USES AN API GET REQUEST TO DOWNLOAD THE DATA AND THEN SUBSEQUENTLY USES PIL TO DISPLAY THE IMAGE TO THE USER
img_url = "https://images.pokemontcg.io/base1/1_hires.png"
#response = requests.get(img_url)
#img = Image.open(BytesIO(response.content))
img = Image.open(requests.get(img_url, stream=True).raw)
img.show()
'''
