"""
Choose one:

Write a program that asks the user to enter a POSITIVE number.
The program should keep using CONSOLE INPUT to get the user's answer AS MANY TIMES AS NEEDED
until they enter a positive number.
"""

# user_input = float(input('type in a positive number: '))
#
# while user_input <= 0:
#     user_input = float(input('type in a positive number: '))


"""
Define a FUNCITON that accepts a list of integers. The function should RETURN True 
if the list CONTAINS at least one NEGATIVE NUMBER, and False otherwise.
"""

def check_negative(L):
    # check each number
    for n in L:
        if n < 0:
            return True
        # else:
            # do nothing
    # when the loop checking is done, no early return True due to any negative number being found
    return False


print(check_negative([1,-1]))