import json

class Deck:
    def __init__(self):
        pass
    
    def add_card():
        pass

    def remove_card():
        pass

    def get_cards():
        #for card object in list print card details
        pass
    
    def get_decks(self, filename):
        print("Available Decks: ")
        file = open(filename,encoding='utf-8')
        data = json.load(file)
        for i in data:
            print(i['name'])
        file.close()
    


    '''
    f = open('set1.json',encoding='utf-8')
    data = json.load(f)
    for i in data:
        #print(i['name]) gets the names of the sets in this file
        #if i['name] == 'setname':
            #get info
        print(i['cards'])
    f.close()
    '''