# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

def check_even(s):
    """
    accepts a string and print message to show if the string has even or odd  number of chars
    :param s: string, string to be checked
    :return: None
    """
    if len(s) % 2 == 0:
        print('"' + s + '" has an even number of characters.')
    else:
        print('"' + s + '" has an odd number of characters.')

check_even('Dog')