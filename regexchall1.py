# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#imports regex module
import re


user_input=input("Enter the number: ")


#Defined expression for regex
expr=re.compile("^[+-]?[0-9]*\.([0-9]+)$")

#checks the expression with user input
result=expr.search(user_input)
if result:
    print("It is a floating point number.")
else:
    print("Not a floting point")
