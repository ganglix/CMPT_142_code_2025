"""
N   F(N)
0   1
1   3
2   5
3   7
4   9
5   11

F(N) = F(N-1) + 2
"""

def F(N):
    # base case
    if N == 0:
        return 1
    else:
        # recusive case: F(N-1)
        # F(N) = F(N-1) + 2
        return F(N-1) + 2


print(F(6))