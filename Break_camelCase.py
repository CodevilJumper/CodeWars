def solution(s):
    new_word = ""
    for letter in s:
        if letter.isupper():
            new_word += ' ' + letter
        else:
            new_word += letter
    return new_word

print(solution('camelCase'))