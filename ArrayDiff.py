# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:29:12 2021

@author: Anna Grzyb
"""

def array_diff(a, b):
    
    list = []
    
    for i in a:
        if i not in b:
            list.append(i)
       
    return(list)
    


array_diff([1,2], [1]), [2]
array_diff([1,2,2], [1]), [2,2]
array_diff([1,2,2], [2])
array_diff([1,2,2], []), [1,2,2]
array_diff([], [1,2])






# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.

# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]