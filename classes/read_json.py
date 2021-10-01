import json

'''
f = open('base1.json',encoding='utf-8')
data = json.load(f)
for i in data:
    print(i['id'])
f.close()
'''
f = open('set1.json',encoding='utf-8')
data = json.load(f)
for i in data:
    #print(i['name]) gets the names of the sets in this file
    #if i['name] == 'setname':
        #get info
    print(i['cards'])
f.close()
