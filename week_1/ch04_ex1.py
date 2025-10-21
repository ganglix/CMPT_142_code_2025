s = 'fire'
L = [1, 2, 3]
L2 = [ [1 , 2] , [3 , 4] ]

print( L + [4, 5, 6],'\n',
       # L + s, '\n'
       L + L2
       )

print( L * 3)

print("f" in s)   # in checks and return bool True or False
print("fr" in s)
print(1 in L2)
print(1 in L2[0])