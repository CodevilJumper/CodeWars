# -*- coding: utf-8 -*-.
"""
Created on Thu Feb 18 17:21:26 2021

@author: Anna Grzyb
"""

# Kata: Stop gninnipS My sdroW!

# Instructions:
    
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"

# spinWords( "This is a test") => returns "This is a test"

# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    

    split_sentence = sentence.split()
    spinned_list = []
       
    for i in split_sentence:
        
        if len(i) >= 5:
            
             spinned_list.append(i[::-1])
        
        else:
            
            spinned_list.append(i)
        
    return " ".join(spinned_list)



# TEST:
    
print(spin_words( "Hey fellow warriors" ))

# RESULT EXPECTED:
    
# "emocleW"