import requests
from requests.auth import HTTPBasicAuth
import json
from PIL import Image
from io import BytesIO


'''
parameters = {
    'X-Api-Key': 'a8139628-6932-4c7e-a08c-1c5f2dc52060'
}
'''

#response = requests.get("https://api.pokemontcg.io/v2/cards", params=parameters)
headers = { 'User-Agent': 'Mozilla/5.0', 'X-Api-Key': 'a8139628-6932-4c7e-a08c-1c5f2dc52060'}

#gets all cards
url = "https://api.pokemontcg.io/v1/cards?name=charizard"


response = requests.get(url, headers)
data = json.loads(response.text)

#name = "Gengar" #input("Enter pokemon name: ")

for key in data:
    print(key)
    if key == 'cards':
        for shit in data['cards']:
            #if shit['name'] == name:
            #    print(shit['id'])
            print(shit['name'])
    elif key == 'page':
        print(data['page'])

'''
#THIS CODE GETS A LARGE IMAGE OF A POKEMON CARD FROM THE DATA PROVIDED IN THE BASE1 DATASET, AND USES AN API GET REQUEST TO DOWNLOAD THE DATA AND THEN SUBSEQUENTLY USES PIL TO DISPLAY THE IMAGE TO THE USER
img_url = "https://images.pokemontcg.io/base1/1_hires.png"
#response = requests.get(img_url)
#img = Image.open(BytesIO(response.content))
img = Image.open(requests.get(img_url, stream=True).raw)
img.show()


#print(response.status_code)

#for key in response:
#    print(key)

#print(response.json())
#name = input("Enter the name of a Pokemon: ")
'''