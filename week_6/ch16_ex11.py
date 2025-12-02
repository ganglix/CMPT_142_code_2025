# Write a recursive function to find the smallest value in a list of
# numbers.


# 1 base case
# 2 recursive case (reduced problem, how to reduce)
# 3 relationship between the problem and the reduced problem

def smallest(L):
    """
    returns the smallest number of a list of numbers
    :param L: list, a list of numbers
    :return: int or float, the smallest number in the list L
    """
    # base case
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    else:
        # recursive case, reduce len by 1, remove the first number
        # find the smallest of L[1:]
        smallest_in_short_list = smallest(L[1:])
        # return the smaller one between L[0] and the smallest(L[1:])
        if L[0] < smallest_in_short_list:
            return L[0]
        else:
            return smallest_in_short_list

L = [3, 3,1,0]
print(smallest(L))


def smallest_v2(L):
    # base case
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    # recursive case
    mid_index = len(L)//2
    left_smallest = smallest_v2(L[:mid_index]) # left
    right_smallest = smallest_v2(L[mid_index:])  # right

    # return the smaller one between the two smallest
    if left_smallest > right_smallest:
        return right_smallest
    else:
        return left_smallest

L = [3, 3,1,0]
print(smallest_v2(L))
