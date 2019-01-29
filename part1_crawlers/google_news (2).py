##### Google news API
# part1: show users live top and breaking news headlines

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=cbe996c681c848cd91d80a60d699321c')
response = requests.get(url)
print (response.json())



import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=cbe996c681c848cd91d80a60d699321c')
response = requests.get(url)
data_not_cleaned = response.json()

df = data_not_cleaned['articles']
len(df)

import pandas as pd


dataset = []
i = 0
while i <= len(df)-1:
    df1 = df[i]
    def removekey(d, key):
     r = dict(d)
     del r[key]
     return r
    df2 = removekey(d = df1, key = 'source')
    dataset.append(df2)
    data = pd.DataFrame.from_dict(data = dataset, orient = 'columns')
    i = i+1
 

##### Part2: search for news articles that mention a specific topic or keyword
import pandas as pd    
import requests

url = ('https://newsapi.org/v2/everything?'
       'q=datascience&'
       'from=2018-11-16&'
       'sortBy=popularity&'
       'apiKey=cbe996c681c848cd91d80a60d699321c')

response2 = requests.get(url)
data_not_cleaned_2 = response2.json()


df_part2 = data_not_cleaned_2['articles']
len(df_part2)


dataset2 = []
i = 0
while i <= len(df_part2) - 1:
    df1 = df_part2[i]
    def removekey(d, key1,key2):
     r = dict(d)
     source = r[key1][key2]
     del r[key1]
     r.update({'source':source})
     return r
    df2 = removekey(d = df1, key1 = 'source', key2 = 'name')
    dataset2.append(df2)
    data2 = pd.DataFrame.from_dict(data = dataset2, orient = 'columns')
    i = i+1
    
