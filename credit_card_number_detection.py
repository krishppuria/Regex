#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:41:40 2018

@author: krishna
"""

card_list=["4123456789123456","5123-4567-8912-3456","61234-567-8912-3456","4123356789123456","5133-3367 -8912-3456","5123 - 3567 - 8912 - 3456"]
expr=re.compile("^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}")
for cards in card_list:
    result=expr.findall(cards)
    if len(result)>0 and not re.search(r'(\d)\1{3}',re.sub('-','',cards)):
        print("Valid")
    else:
        print("Invalid")