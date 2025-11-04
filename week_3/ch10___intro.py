# lists and tuples

# create a list
L = [1, 2, 3]

# indexing and slicing, same as string, or other sequences
print( L[0],
       L[0:2:1],   # slice index 0, 1
       L[:]
)

# methods
# add an item: .append(), .extend(), +
print('-'*20)
L.append(4)   # add 4 to the L list bucket "in-place); it does not create a new list bucket
print(L)

L.extend(['one', 'two', 'three'])   # add the items of a list to L, "in-place", L bucket is still the old L bucket
print(L)

L_new = L + ['apple','orange'] # addition creates a new list, L itself does not change

print(L_new)
print(L)


# remove an item: .remove(), .pop(), del
L.remove('one')   # remove from L, L is changed, but no new list was created
print(L)

what_is_popped = L.pop()   # by default, it removes the last item (index -1) from L, and return it
print(L)
print(what_is_popped)

del L[0]      # remove item (index 0) from L, L is changed
print(L)

# locating an item: index()

print(L.index('two'))   # return the index of an item == 'two


# sorting: .sort()
L_random = [2, 1, 4, 3]
L_random.sort()   # .sort, by deault will change the order of the items in the list, ascending order
L_random.sort(reverse=True) # descending order
print(L_random)
# L.sort() changes L in-place

L_sorted = sorted(L_random)    # creates a sorted new list, L is not changed
print(L_sorted)


print('-'*20)
# let do an attempt to use .sort() without changing the old L
L = [2, 3, 4, 1]
L_new = L   # this = step does not create a new list. this just add another name (L_new) to L
print('before sort L_new')
print('L_new',L_new)
print('L', L)

L_new.sort()
print('after sort L_new')

print('L_new',L_new)
print('L', L)





# list is mutable ! more examples in flowtrace observations





