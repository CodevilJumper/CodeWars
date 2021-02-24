# Roman Numerals Encoder
#
# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Example:
#
# solution(1000) # should return 'M'

def solution(n):
    """

    Args:
        n (): float

    Returns:
        string, float converted to roman numerals
    """
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    roman = ""

    for i in range(len(number)):

        while n >= number[i]:
            roman += symbol[i]
            n = n - number[i]

    return roman

print("Check solutions below: ")
print(str(solution(1)) + " expects: 'I'")
print(str(solution(4)) + " expects: 'IV'")
print(str(solution(6)) + " expects: 'VI'")
print(str(solution(14)) + " expects: 'XIV'")
print(str(solution(21)) + " expects: 'XXI'")
print(str(solution(89)) + " expects: 'LXXXIX'")
print(str(solution(91)) + " expects: 'XCI'")
print(str(solution(984)) + " expects: 'CMLXXXIV")
print(str(solution(1000)) + " expects: 'M")
print(str(solution(1889)) + " expects: 'MDCCCLXXXIX")
print(str(solution(1989)) + " expects: 'MCMLXXXIX")