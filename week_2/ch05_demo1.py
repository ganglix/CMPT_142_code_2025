# In this demonstration we will show how to use the console
# display on console
from week_2.ch05_ex1 import number

# input function to obtain answers to simple questions
# # example 1
number1 = float(input('Please enter a number: '))
number2 = float(input('Please enter another number: '))  # input() will return a str
print(type(number1))
print('The sum of', number1, 'and', number2, 'is', number1 + number2, '.')








# # example 2
#
# # title
# print("If I Were Super Wealthy Simulator")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print()   # prints an empty newline
#
# # prompt user for their name
# name = input("What is your name?: ")
# print("Hello", name, "! We're going to gather some data on you and predict your life")
# print()
#
# # prompt user for some more data about themselves
# animal = input("What is your favourite animal?: ")
# number = int(input("What is your favourite number (please give an integer)?"))
# float_number = float(input("What is another number you like (this time, give a float number)?"))
# print()
#
# # print out the scenario
# print("Hello", name, ". If you were super wealthy, my guess is you would buy", number, animal)
# print("You would make sure that they live in", float_number, "degree celsius weather.")
# print("Should we be concerned? Possibly")
