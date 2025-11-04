# Up until now, only immutable data types have been passed
# as arguments to functions. What happens when we pass
# mutable data?
# Let us observe the effect on an input variable before,
# during, and after a function call that changes the value.


def appendage(minilist, x):
    minilist.append(42)
    x = x + 5


L = [10, 20, 30]
x = 50
appendage(L, x)
print(L)    # L list bucket is not changed either. however, there is a 42 got added inside
print(x)







# -----------------------------------------
# # does this operation create a new list?
# .copy()
# [i for i in oldlist]

