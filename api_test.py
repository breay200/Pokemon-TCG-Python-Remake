import requests
from requests.auth import HTTPBasicAuth
import json
from PIL import Image
from io import BytesIO

headers = { 'User-Agent': 'Mozilla/5.0', 'X-Api-Key': 'a8139628-6932-4c7e-a08c-1c5f2dc52060'}

url = "https://api.pokemontcg.io/v1/cards?name=charizard"

response = requests.get(url, headers)
data = json.loads(response.text)

for key in data:
    if key == 'cards':
        for card in data['cards']:
            print(card['name'])

'''
#THIS CODE GETS A LARGE IMAGE OF A POKEMON CARD FROM THE DATA PROVIDED IN THE BASE1 DATASET, AND USES AN API GET REQUEST TO DOWNLOAD THE DATA AND THEN SUBSEQUENTLY USES PIL TO DISPLAY THE IMAGE TO THE USER
img_url = "https://images.pokemontcg.io/base1/1_hires.png"
#response = requests.get(img_url)
#img = Image.open(BytesIO(response.content))
img = Image.open(requests.get(img_url, stream=True).raw)
img.show()
'''
