# Define a Python function called format_price that:
# (a) Has two integer parameters, indicating the cost in dollars
# and cents of an item
# (b) Returns a single string in the format "$D.C".
# (c) Example: if called with arguments 9 and 99, the function
# should return the string $9.99
from scipy.constants import centi


# def format_price(dollar, cent):
#     formatted = "$"+ str(dollar) + "." + str(cent)
#     return formatted
#
# result = format_price(9, 99)
# print(result)



# follow up on types of functions

# with parameters, but no return
# def format_price_v1(dollar, cent):
#     formatted = "$"+ str(dollar) + "." + str(cent)
#     print(formatted)
#
# result = format_price_v1(9, 99)
# print(result)


# no parameter, no return
# def format_price_v2():
#     dollar = input("Enter dollar: ").strip()
#     cent = input("Enter cent: ").strip()
#     formatted = "$"+ dollar + "." + cent
#     print(formatted)
#
# format_price_v2()



def format_price(dollar, cent):
    """
    It takes two numbers as ammout of dollar and cent, and returns a formatted price string
    :param dollar: int, dollar amount
    :param cent: int, cent amount
    :return: string, formatted price string
    """
    formatted = "$"+ str(dollar) + "." + str(cent)
    return formatted
dollar = input("Enter dollar amount:")
cent = int(input("Enter cents:"))
result = format_price(9, 99)
print(result)


# help(format_price)
# print(format_price.__doc__)