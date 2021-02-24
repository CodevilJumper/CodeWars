# Your order, please
#
# INSTRUCTIONS
#
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
# Examples
#
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence):
    """
    Args:
        sentence (): string, original string . Each word containing a single digit.

    Returns: Ordered string with words in ascending order based on a digit in every word.
    """

    dict_words = {}
    list_words = sentence.split()
    final_sentence = []

    for i in list_words:
        for char in i:
            if char.isdigit():
                dict_words[char] = i
    dict_words = sorted(dict_words.items())

    for i in dict_words:
        final_sentence.append(i[-1])
    return " ".join(final_sentence)

# TEST

sentence = "4of Fo1r pe6ople g3ood th5e the2"
print(order(sentence))
