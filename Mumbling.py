# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:05:09 2021

@author: Anna Grzyb
"""

def accum(s):
    
    output = []
    
    for char in s:
        
        output.append(char.upper() + char.lower()*s.find(char))
    print('-'.join(output))

# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"






accum("ZpglnRxqenU")
accum("NyffsGeyylB")
accum("MjtkuBovqrU")
accum("EvidjUnokmM")
accum("HbideVbxncC")