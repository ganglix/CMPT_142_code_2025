# Early feedback


# 1 console input and output

"""
a1q2"
Importantly, your function should do no console input and no console output. It must receive its input
through its parameters and send its output using a return value
"""


# place them outside the function
def fun(p1, p2):
    a = p1 * p2
    return a

p1_input = float(input("type a number"))  # console input
p2_input = float(input("type a number"))  # console input
result = fun(p1_input, p2_input)
print(result) # console output

# place them inside the function
# put print inside the function
def fun(p1, p2):
    a = p1 * p2
    print(a)


# 2 main program
# is the script out side of the function
