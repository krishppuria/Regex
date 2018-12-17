import pandas as pd
import re
large_cities=open('largest_cities_germany.txt','r')
cities_list=large_cities.readlines()
expr=re.compile('\s[\w\s]+\s+')
zip_list=[]
q=pd.read_csv('zuordnung_plz_ort.csv')
for city in cities_list:
    z=expr.findall(city)
    #print(z,city)
    x=z[0].strip()
    print(z)
    a =list( q['plz'][q['ort']==x])
    #print(x,'{',a)
    zip_list.append(list(a))