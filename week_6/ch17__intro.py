# Search algorithm

# search for a number from a list of numbers


# linear search
def linear_membership_search(c, target_key):
    """
    a linear membership search for the target key

    c:          a sequence of numbers or strings
    target_key: the target key for the search
    return: True if target key is in the collection
    """
    # base case
    if len(c) == 0: # empty list
        return False
    # elif len(c) == 1:      # this base case merges into recursive case
    #     if c[0] == target_key:
    #         return True
    else:
        # recursive case, remove c[0], and search c[1:]
        if c[0] == target_key:
            return True
        else:
            return linear_membership_search(c[1:], target_key)



# binary search

def binary_membership_search(c, target_key):
    """
    A binary membership search function
    :param c: list, collection of data, sorted by its search keys
    :param target_key: target key to search for
    :return: True if target key is in the collection
    """
    # base case
    if len(c) == 0:
        return False
    else:
        # recursive case: split c into halves
        mid_index = len(c) // 2   # round up index  0 1 2
        if c[mid_index] == target_key:
            return True
        # search the half lists
        elif c[mid_index] < target_key:
            # check the right
            return binary_membership_search(c[mid_index+1 :], target_key)
        else:
            # check the left
            return binary_membership_search(c[:mid_index], target_key)


# generate an array to work with
import numpy as np
c = np.random.uniform(0,9, size=5).astype(int)
c.sort()
print(f"is 1 in {c}? {binary_membership_search(c, 1)}")

