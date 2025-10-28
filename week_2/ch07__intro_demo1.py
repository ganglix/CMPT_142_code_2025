# How to import a module
import math
print(
    math.pi,
    math.radians(90),
    math.sin(math.radians(90)),
    math.sqrt(2),
    math.pow(2, 6),
    math.log(1),   # natural log, log10
    math.log(math.e),
    sep='\n'
)

# alias
import math as m
m.exp(2)


# real world engineering (my experience)
# scientific computing, matrix, array
import numpy as np
arr = np.linspace(1, 8, 100)  # 100 points between 1 and 8, inclusive
arr1 = np.arange(1, 8, 1)

arr * 2

# visualization
import matplotlib.pyplot as plt

plt.plot(arr, np.sin(arr), linetype = '--', marker = 'o', color = 'red')
# plt.savefig('plot.tiff', dpi=1200)
plt.show()



# Things I want to mention
# import one or *all

# from math import cos
# cos(2)
#
# from math import *   # import all functions from math, which will take up a lot of name space, do not use
