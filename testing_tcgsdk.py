from pokemontcgsdk import Card
from pokemontcgsdk import RestClient
from pokemontcgsdk import Set

RestClient.configure('a8139628-6932-4c7e-a08c-1c5f2dc52060')
RestClient.get('https://api.pokemontcg.io/v2/cards', {})

name = "Charizard"

#cards = Card.all()
#cards = Card

cards = Card.where(q=f'name = {name}')

print(cards)
