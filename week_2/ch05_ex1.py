blanket_cost = 8
pillow_cost = 12
cash = 50

# For each print function call:
# 1) how many arguments do you see?
# 2) How many expression operators do you see?
# 3) Why use str() in b)?
# 4) What will be "wrong" about c)?

# (a)
print("A blanket is", blanket_cost, "dollars")


# (b)
print("Four pillows will cost " + str(pillow_cost * 4) + ".")


# (c)
print("One blanket and two pillows will cost $",
      blanket_cost + pillow_cost * 2, ". If I pay with $", cash,
      ", I will have $", (cash - (blanket_cost + pillow_cost * 2)),
      "left.") # print adds space to displayed args by default

print("One blanket and two pillows will cost $"+
      str(blanket_cost + pillow_cost * 2)+ ". If I pay with $"+ str(cash)+
      ", I will have $"+ str(cash - (blanket_cost + pillow_cost * 2))+
      " left.") # concat the string args into one arg

print("One blanket and two pillows will cost $",
      blanket_cost + pillow_cost * 2, ". If I pay with $", cash,
      ", I will have $", (cash - (blanket_cost + pillow_cost * 2)),
      " left.", sep='') # print adds empty string (nothing) to displayed args by changing sep=

# f-string since python 3.5, not covered in this course
number = 10
print('The number is', number)
print('The number is ' + str(number))
print(f'The number is {number}')  # formatted string

