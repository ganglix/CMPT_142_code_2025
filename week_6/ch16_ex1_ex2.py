# n! = (n-1)! * n
# 3! = 2! * 3
# 2! = 1! *2
# 1! = 0! * 1
# 0! = 1

def factorial_a(N):
    if N == 0:
        return 1
    else:
        return factorial_a(N - 1) * N

# print(factorial_a(5))
# (a) What is the condition for the base case?

# (b) What is the condition for the recursive case?

# (c) What problem is being delegated?

# (d) How is the solution to the delegated problem used?


def factorial_b(N):
    if N < 0:  # safeguard invalid negative number
        return None
    elif N > 0:
        return factorial_b(N - 1) * N
    else:
        return 1



# which one is better?
n = -1
expeted_outputs = None # error or warning
print(
      # f"a: {factorial_a(n)}"  # error # better
      f"b: {factorial_b(n)}"   # returns 1
      )
