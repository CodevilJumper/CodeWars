# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:22:01 2021

@author: Anna Grzyb
"""

# Split Strings

# INSTRUCTIONS:
    
# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    
    
    if len(s) %2 != 0:
        
        s = s + '_'
    
    return wrap(s, 2)
    

