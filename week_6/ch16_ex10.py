"""
S       F(S)
''       ''
’a’     ’a’
’ab’    ’ba’
’abc’   ’cba’
’abcd’  ’dcba’
--------------------------------------------
F(S) = F(S[1:]) + S[0]
"""
def reverse(S):
    """
    return a reversed string
    :param S: string, input string
    :return: string, reversed string
    """
    # base case when len is 0
    if len(S) == 0:
        return ''
    else:
        # recursive case: put the first ch to the last, and
        # use reverse(S[1:]) to reverse the rest
        return reverse(S[1:]) + S[0]

print(reverse('abcd'))
