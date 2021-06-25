# Currying functions: multiply all elements in an array
#
# To complete this Kata you need to make a function multiplyAll/multiply_all which takes an array of integers as an argument. This function must return another function, which takes a single integer as an argument and returns a new array.
#
# The returned array should consist of each of the elements from the first array multiplied by the integer.
#
# Example:
#
# multiply_all([1, 2, 3])(2); // => [2, 4, 6]
#
# You must not mutate the original array.

array_list = ([1, 2, 3])(1)

def multiply_all(array_list):
    new_array = []
    for i in array_list:
        print (i)





# print(multiply_all([1, 2, 3])(1))
# print(multiply_all([1, 2, 3])(2))
# print(multiply_all([1, 2, 3])(0))