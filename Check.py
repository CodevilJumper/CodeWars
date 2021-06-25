from collections import Counter

def first_non_repeating_letter(string):
    freq = Counter(string)

    for i in string:
        if len(string) == 0:
            return ''
        elif (freq[i] == 1):
            return (i)
            break
        else:
            return ''
    

print(first_non_repeating_letter("stress"))