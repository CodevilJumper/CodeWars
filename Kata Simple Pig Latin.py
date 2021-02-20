# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:44:28 2021

@author: Anna Grzyb
"""

# INSTRUCTIONS

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# SOLUTION:
    
def pig_it(text):
    """
    

    Parameters
    ----------
    text : STRING

    Returns
    -------
    STRING, returns original sentence with first letter of every word added at the end and then added "ay". Exept of punctuation marks which stay unchanged.

    """
    
    text_split = text.split()
    
    pigged_words = []

    for i in text_split:
        
        if i == '!' or i == '?' or i == '.' or i == ',':
            
            pigged_words.append(i)
        

            
        else:
            
            word = i[1:] + i[0]
            word = word+ 'ay'
            pigged_words.append(word)           

    return " ".join(pigged_words)

#TEST

# pig_it('Pig latin is cool')
# # EXPECTED 'igPay atinlay siay oolcay'

# pig_it('This is my string')
# #EXPECTED 'hisTay siay ymay tringsay'

# pig_it('Quis custodiet ipsos custodes ?')
# EXPECTED 'uisQay ustodietcay psosiay ustodescay ?'
