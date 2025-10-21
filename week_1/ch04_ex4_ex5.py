
#    _______
#    7654321
#    0123456
# s = "Fiction"
#
# print(s[1:3]) # ic
#
# print(s[-4:10])  # tion
# # wrong: [-4, -3, -2, -1, 0, 1, 2...9]
# # when we have a mixture of positive and negative indices
# # we focus on position, not the index number value
#
# print(s[0: len(s): 2]) # start from 0, end at 7 (out of range, not included), step is 2
#
# print("result:", s[0: len(s) :-1])  #start from 0, end at 7, step is -1 (left to right), does not make sense
# what_is_this = s[0: len(s) :-1]
# print(type(what_is_this))
#
# print(s[len(s):-8:-1])
# print(s[::-1])



#    ___________
#    BA987654321
#    0123456789A        note: A is 10    B is 11
s = "Green Arrow"

# (a) the first five characters of s, i.e. "Green"
print("(a)")
print(s[0:5])
print(s[:5])

# (b) the fourth to eighth characters of s inclusive, i.e. "en Ar"
print(s[3:7+1])

# (c) the last five characters of s, i.e. "Arrow"
print(s[6:10+1])
print(s[6:])   # from 5 to right boundary, step 1
print(s[-5:])  # from position -5 to right boundary, step 1

# (d) every third character of s from the second character
# onwards, i.e. "rnrw"
print(s[1::3])

# (e) the last five characters of s in reverse, i.e. "worrA".

print(s[-1:-6:-1])
print(s[:-6:-1])  # start from right boundary, to -6 (not included) wit step -1