# Write a Python function which accepts integer parameter
# grade and prints to the console:
# • "A+" if grade is between 100 and 95
# • "A" if grade is between 94 and 85
# • "B" if grade is between 84 and 75
# • "C" if grade is between 74 and 65
# • "D" if grade is between 64 and 50
# • "F" otherwise

# check my first attempt:
# def letter_grade(grade):
#     """
#     print the letter grade of a number grade
#     :param grade: int, numeric grade
#     :return: None
#     """
#     if grade <= 100 and grade >= 95:
#         print("A+")
#     if grade <= 94 and grade >= 85:
#         print("A")
#     if grade <= 84 and grade >= 75:
#         print("B")
#     if grade <= 74 and grade >= 65:
#         print("C")
#     if grade <= 64 and grade >= 50:
#         print("D")
#     else:
#         print("F")


def letter_grade(grade):
    """
    print the letter grade of a number grade
    :param grade: int, numeric grade
    :return: None
    """
    if grade > 100 or grade < 0:
        print('The grade is out of range of [0, 100]')
    elif grade <= 100 and grade >= 95:
        print("A+")
    elif grade <= 94 and grade >= 85:
        print("A")
    elif grade <= 84 and grade >= 75:
        print("B")
    elif grade <= 74 and grade >= 65:
        print("C")
    elif grade <= 64 and grade >= 50:
        print("D")
    else:
        print("F")

letter_grade(110)

import math as m
def circle_area(radius):
    area =  m.pi*radius**2
    return area

def cost(area, cost_per_unit_area):
    total_cost = area * cost_per_unit_area
    return total_cost

r = 1
unit_cost = 2

total_cost = cost(circle_area(r), unit_cost)

