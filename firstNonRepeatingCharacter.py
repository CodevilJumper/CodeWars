# First non-repeating character

# Instructions
#
# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.


def first_non_repeating_letter(string):

    dict_letters = {}
    order_letters = []

    if len(string) == 0:
        return ''

    elif len(string) == 1:
        return string

    else:
        word = string.lower()

        for i in string.lower():
            if i in dict_letters:
                dict_letters[i] += 1
            else:
                dict_letters[i] = 1
            order_letters.append(i)

        for item in order_letters:
            if dict_letters[item] == 1:
                position = order_letters.index(item)
                return string[position]


        return ''

#TESTS

print(str(first_non_repeating_letter('a')) + ": should return a")
print(str(first_non_repeating_letter('stress'))+ ": should return 't'")
print(str(first_non_repeating_letter('moonmen')) + ": should return 'e'")
print(str(first_non_repeating_letter(' ')) + ": should return empty string")
print(str(first_non_repeating_letter('abba')) + ": should return empty string")
print(str(first_non_repeating_letter('aa')) + ": should return empty string")
print(str(first_non_repeating_letter('~><#~><')) + ": should return '#'")
print(str(first_non_repeating_letter('hello world, eh?')) + ": should return 'w'")
print(str(first_non_repeating_letter('sTreSS')) + ": should return 'T'")
print(str(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')) + ": should return ','")