# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:16:03 2021

@author: Anna Grzyb
"""

def create_phone_number(n):
    #your code here
    string = ""
    for i in n:
        if i in range(0,10):
            string = string + str(i)
            
    number = ("(" + string[0:3] + ") " + string[3:6] + "-" + string[6:len(string)+1])    
    return(number)     

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])