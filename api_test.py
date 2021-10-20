import requests
from requests.auth import HTTPBasicAuth
import json

parameters = {
    'X-Api-Key': 'a8139628-6932-4c7e-a08c-1c5f2dc52060'
}

#response = requests.get("https://api.pokemontcg.io/v2/cards", params=parameters)

url = "https://api.pokemontcg.io/v2/cards"

response = requests.get(url, parameters)
data = json.loads(response.text)

name = input("Enter pokemon name: ")

for key in data:
    if key == 'data':
        for shit in data['data']:
            if shit['name'] == name:
                print(shit['id'])

#print(response.status_code)

#for key in response:
#    print(key)

#print(response.json())
#name = input("Enter the name of a Pokemon: ")
