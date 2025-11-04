# flowtrace



# flowtrace

L = [1, 2, 3, 4, 5, 6]
for value in L:
    L.remove(value)
print(L)

"""
L = [1, 2, 3, 4, 5, 6]
for value in [1, 2, 3, 4, 5, 6]:
    value = 1  # first item
    [1, 2, 3, 4, 5, 6].remove(1)
    
for value in [2, 3, 4, 5, 6]:
    value = 3   # second item
    [2, 3, 4, 5, 6].remove(3)
    
for value in [2, 4, 5, 6]:
    value = 5 # third item   
    [2, 4, 5, 6].remove(5)
    
for value in [2,4,6]:
    value = # forth item, there is no forth item, the for loop is done
    
print([2,4,6])
"""







# L = []
# for i in range(3):
#     L.append([])
# for char in "abc":
#     L[0].append(char)
# print(L)


