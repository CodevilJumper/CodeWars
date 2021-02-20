# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:27:43 2021

@author: Anna Grzyb
"""

def is_isogram(string):
    #your code here
    list = ""
    for char in string:
        lower = char.lower()
        if lower in list:
            
            break
        else:
            list = list + char
            
    if len(string) == len(list):
         return(True)
         
    else: 
         return(False)
            


    
    
    
is_isogram("Dermatoglyphics")
is_isogram("isogram")
is_isogram("aba")
is_isogram("moOse")
is_isogram("isIsogram")
is_isogram("")