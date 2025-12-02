"""
generation  ancestor
n   bees(n)
0   1
1   1
2   2
3   3
4   5
5   8
6   13
------
bees(n) = bees(n-1) + bees(n-2)
"""
def bees(n):
    if n == 0 or n == 1:
        return 1
    else: # bees(n) = bees(n-1) + bees(n-2)
        return bees(n-1) + bees(n-2)

# import time
# start = time.time()
# bees(20)
# end = time.time()
# duration = end - start
# n_calls = 2 ** 20
# time_per_call = duration / n_calls
# print(f"time_per_call:{time_per_call}")
#
# print(f'for bees(60), the time need is '
#       f'{2**60 * time_per_call / 60 / 60 /24 /365 / 100} centuries')

bees_cache = {}  # n : bees(n)
def bees_efficient(n):
    # base case
    if n == 0 or n == 1:
        return 1
    else:
        # recursive case
        # only calculate bees_efficient(n) for the first time
        if n not in bees_cache:
            bees_cache[n] = bees_efficient(n-1) + bees_efficient(n-2)
        return bees_cache[n]

print(bees_efficient(60))


