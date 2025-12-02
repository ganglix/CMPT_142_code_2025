# recursion
# "the family chain of new phones"


# problem solving - delegation metaphor

# 1: find the base case (simplest version of the problem) (easy)
# 2: find a way to reduce the problem: reduce steps of procedure, reduce the number, reduce the length of a list (difficult)
# 3: find the relationship between the solution of the reduced problem and the original problem (medium)

def is_even(n):
    """
    Determine if a number is an even number.
    :param n: int, number to check
    :return: bool, True if number is even, False otherwise
    """
    # base case
    if n == 0: # even case
        return True
    elif n == 1: # non even case
        return False
    else:
        # recursive case: reduce the problem by n - 2
        # find if n-2 is even
        is_n_minus_2_even = is_even(n-2)
        # whether n is even or not is the same as n - 2
        return is_n_minus_2_even

print(is_even(5))


"""
print(is_even(5))
is_even(5)
    n = 5
    if 5 == 0
    elif 5 == 1
    is_n_minus_2_even = is_even(5-2)
                        n = 3
                        if 3 == 0
                        elif 3 == 1
                        is_n_minus_2_even = is_even(3-2)
                                            n = 1
                                            if 1 == 0
                                            elif 1 == 1
                                            return False
                        return False
    return False

print(False)
"""


def is_even_v2(n):
    """
    Determine if a number is an even number.
    :param n: int, number to check
    :return: bool, True if number is even, False otherwise
    """
    # base case
    if n == 0: # even case
        return True
    # elif n == 1: # non even case    # this base case merges into recursive cases
    #     return False
    else:
        # recursive case: reduce the problem by n - 1
        # find if n-1 is even  # whether n is even or not is the opposite as n - 1
        return not is_even_v2(n-1)

print(is_even_v2(4))