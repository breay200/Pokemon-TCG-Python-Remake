import json

def get_set_names(filename):
    file = open(filename,encoding='utf-8')
    data = json.load(file)
    for i in data:
        #print(i['name]) gets the names of the sets in this file
        #if i['name] == 'setname':
        
        print(i['name'])
    file.close()