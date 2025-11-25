import numpy as np

# Create a signed 8-bit integer array
# with the single data item 10.
x = np.array([10]).astype('int8')

# x[0] starts at 10 and gets larger with each loop iteration.
# Is this In infinite loop?

while x[0] > 0:
    x[0] = x[0] + 1
    print(x[0])


L = [2 ** n for n in range(16-1)] # 16 bit signed, 0...14
print(sum(L))  # max value for 16 bit signed number
