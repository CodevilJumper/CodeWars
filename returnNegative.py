# Return Negative
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
#
# Example:
#
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
#
# Notes:
#
#     The number can be negative already, in which case no change is required.
#     Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative(number):
    """

    Args:
        number (): INTEGER

    Returns:
        INTEGER, Returns negative of the number.
    """
    return abs(number)*(-1)


print("Returns: " + str(make_negative(42)) + " *** Should return -42")
print("Returns: " + str(make_negative(-9)) + " *** Should return -9")
print("Returns: " + str(make_negative(0)) + " *** Should return 0")