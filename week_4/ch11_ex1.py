"""
Exercise 1:
Apply the algorithm-pseudocode-code workflow:
Given a list of numbers, compute how many
numbers are above the average

"""
# algorithm
"""
compute the sum of all numbers
compute the average
count the number of numbers that are greater than the average
"""

# pseudocode
"""
function:
input: list
output: number of numbers above the list's average
total = 0
for every number in the list:
    add number to total
average = total / number of numbers
count = 0
for every number in the list:
    if that number > average
    count += 1
return count
"""

# if you find it challanging to code it up, do not change the pseudocode; try to figure it out
# code
def above_average(L):
    """
    compute the number of numbers that are greater than the average
    :param L: list, A list of numbers
    :return: int, number of numbers above the list's average
    """
    # compute the sum of all numbers
    total = 0
    for number in L:
        total += number

    # computer the average
    average = total / len(L)

    # count the number of numbers that are greater than the average
    count = 0
    for number in L:
        if number > average:
            count += 1

    return count
