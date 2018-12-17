#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:40:25 2018

@author: krishna
"""
import re
large_cities=open('largest_cities_germany.txt','r')
cities_data=open('post_codes_germany.txt','r')
post_data=cities_data.read()
cities_list=large_cities.readlines()
expr1=re.compile('\s[\w\s]+\s+')
final_dict={}
#q=pd.read_csv('zuordnung_plz_ort.csv')
for city in cities_list:
    zip_list=[]
    z=expr1.findall(city)
    #print(z,city)
    x=z[0].strip()
    a='\s'+x+'\s[\d]+\s'
    z2=re.findall(a,post_data)
    for counter in range(3):
        fin=z2[counter].replace(x,'').strip()
        zip_list.append(fin)
    final_dict[x]=zip_list
    
    