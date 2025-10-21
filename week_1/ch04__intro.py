# Indexing and Slicing of !Sequences!
# str

# list

# tuple




# •What is indexing used for?
# •What does a positive index mean?
# •What does a negative index mean?

#         --------
#         87654321
#         01234567
course = 'CMPT 142'
print(len(course))
print(course[3])
# print(course[8])  # Error: string index out of range
print('last char: ', course[-1])
print('last char:', course[ len(course)-1 ] )
print('second last char: ', course[-2])







# --------- take a break -----------

# •What is slicing used for?
# •What are the meanings of the First, second, and third
# numbers in a slicing operation?
#       ----------------
#       GFEDCBA987654321
#       0123456789ABCDEF
text = 'computer science'
# 'computer' [0,1,2...7]
print(text[0:7+1:1]) # first: start, second: stop(not included), third:step
print(text[0:8]) # third when omitted, by default 1
print(text[:8]) # first when  omitted, by default 0
print(text[:]) # start from left boundary, to right boundary, step 1

# science
print(text[-1: -8: -1])
print(text[-7: : 1])  # stop at (right) boundary
print(text[ : : -1])  # from right to left boundary, reverse

# out of range slice, does not give you error
print(text[9:1000])
#                [................]
#       0123456789ABCDEF
text = 'computer science'









# I want to mention omitted value, index out of range, and range of slice
