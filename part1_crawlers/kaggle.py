######## kaggle

import requests
import pandas as pd
import json

kaggle1 = 'https://www.kaggle.com/datasets_v2.json?sortBy=hottest&group=public&page='
kaggle2 = '&pageSize=20&size=sizeAll&filetype=fileTypeAll&license=licenseAll'


##### getting web page


kaggle_data = []
for d in range(1,50):
    page = requests.get(kaggle1+str(d)+ kaggle2)
    loaded_json = json.loads(page.content)
    kaggle_data.append(loaded_json)


dataset_list_items = [] 
for i in range(0, len(kaggle_data)):
    dataset_list_items.append(kaggle_data[i]['datasetListItems'])
    

items = []

for j in range(0, len(dataset_list_items)):
    for k in range(0,20):
        items.append(dataset_list_items[j][k])
        

list_of_features = ['categories','creatorName','datasetUrl','dateUpdated','downloadCount',
                    'overview','ownerUrl','title']


for m in range(0, len(items)):
    items[m] = { your_key: items[m][your_key] for your_key in list_of_features }
    
for m in range(0, len(items)):
    items[m]['categories'] = { your_key: items[m][your_key] for your_key in list_of_features }
 
    
    
for m in range(0, len(items)):
    items[m]['categories'] = { your_key: items[m]['categories'][your_key] for your_key in ['categories'] }


for m in range(0, len(items)):
    items[m]['categories'] = { your_key: items[m]['categories']['categories'][your_key] for your_key in ['categories'] }


for m in range(0, len(items)):
    items[m]['categories'] = items[m]['categories']['categories']
    
    


for m in range(0, len(items)):
    for n in range(0, len(items[m]['categories'])):
        items[m]['categories'] = [items[m]['categories'][n][your_key] for your_key in ['name']]


item_new2={}
item_new4 = {}
item_new = [None]*len(items)

for d in range(len(items))   :
    
    item_new3 = [None]*len(items[d]['categories'])
    
    for c in range(len(items[d]['categories'])):
        print(c)
        item_new2['name'] =    items[d]['categories'][c]['name']
        item_new3[c]=item_new2.copy()
    
    item_new4['categories'] = item_new3
    item_new[d] = item_new4.copy()
        
    


    