# Classify the loops in these Python excerpts as terminating
# (reaches an end) or infinite in nature:

# (a) not inf
# for x in range(100, 10, 10):   # this range is empty start stop step does not make sense
#     print(x * 5)               # not inf, not even run once because the empty sequence length is zero

# (b)  infinite loop
# sum = 0
# i = 0
# while i < 10:
#     sum = sum + i



# (c)  inf loop
# x = 5
# goal = 16
# while x != goal:
#     x = x + 2


# (d)   # not inf
# divisor = 2
# dividend = 13
# while dividend % divisor != 0:
#     divisor = divisor + 1

# def prime_check(number):
#     # return true when it is a prime number
#     divisor = 2
#     while number % divisor != 0:
#         divisor = divisor + 1
#     # when while loop is done
#     if divisor == number:  # when number can only divisible by itself
#         print(f'{number}  is a prime number')
#         return True
#     else:
#         return False
#         # print(f'{number} is not a prime number')
#         # print(f'ant least divisible by {divisor} ')
# count = 0
# for n in range(1000,2000):
#     if prime_check(n):
#         count+=1
# print("count", count)

# (e) inf loop
# low = -100
# high = 100
# msg = " Enter int between " + str(low) + " to " + str(high) + ":"
# num = int(input(msg))
# while num >= low or num <= high:   # or -> and
#     num = int(input(msg))
