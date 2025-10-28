# creating functions: parameter, arguments, return, (scope)
def addition(number1, number2):
    total = number1 + number2
    return total

a = 3
b = 4
result = addition(a, b)
print(result)

"""Flowtrace
a = 3
b = 4
result = addition(3, 4)

    ------another piece of paper, underhood of the function, not accessible from outside-----
    number1 = 3
    number2 = 4
    total = 3 + 4
    return 7
    ------this is the end of this paper------------------------------------------------------

result = 7
print(7)

"""