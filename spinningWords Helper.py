# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:15:05 2021

@author: Anna Grzyb
"""

sentence = "Hey fellow warriors" 

list_words = []

word = ""

final_sentence = ""

for i in sentence:
    
        if i != ' ' or sentence.index(i) + 1 != len(sentence):
        
            word = word + i
            
                    
        else:
            
            list_words.append(word)
            list_words.append(' ')
            
            word = ""

for i in list_words:
    
    if len(i) >= 5:

        reverse_word = i[::-1]
        final_sentence = final_sentence + reverse_word
        
    
    else:
        
        final_sentence = final_sentence + i

print(final_sentence)
