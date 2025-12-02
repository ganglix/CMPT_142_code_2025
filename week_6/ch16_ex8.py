"""
N   F(N)
0   1
1   2
2   4
3   7
4   11
5   16

F(N) = F(N-1) + N
"""

def F(N):
    # base case
    if N == 0:
        return 1
    else:
        # recusive case: F(N-1)
        # F(N) = F(N-1) + N
        return F(N-1) + N


print(F(6))


