#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:20:24 2018

@author: krishna
"""

email_list=["lara@hackerrank.com","brian-23@hackerrank.com","britts_54@hackerrank.com"]
new_list=[]
#defines the expression

expr=re.compile("^([a-z0-9-_]+)@([a-z0-9]+)\.[a-z]{2,4}$")

#checks for valid email and append it to new list and sorts the new list
for addr in email_list:
    result=expr.search(addr)
    if result:
        new_list.append(addr)
new_list.sort()
print(new_list)