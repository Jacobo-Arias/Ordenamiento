from random import sample
import json

listas = {'100':[],
        '1000':[],
        '100k':[],
        '1M':[]}

listas['100'] = sample(range(0,200),100)
listas['1000'] = sample(range(0,2000),1000)
listas['100k'] = sample(range(0,200000),100000)
listas['1M'] = sample(range(0,2000000),1000000)

with open ('listas.json','w') as file:
    json.dump(listas,file,indent=4)
