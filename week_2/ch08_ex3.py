a = 3
b = 4
c = 5

print(
    (a+b > c) or not (a > c and a > b)
)


# how does python think about this?

def is_called():
    print("this function is called")
    'cmpt'[100]
    return True

print( True or is_called())
