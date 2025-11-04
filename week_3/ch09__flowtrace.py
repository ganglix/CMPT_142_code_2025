# flowtrace

i = 1
while i < 10:
    i = i * 2
print(i)

"""
i = 1
while 1 < 10:
    i = 1 * 2
while 2 < 10:
    i = 2 * 2
while 4 < 10:
    i = 4 * 2
while 8 < 10:
    i = 8 * 2 
while 16 < 10:

print(16)
"""





for c in 'pika':
    print(c)
print('Hoorah!')

"""flowtrace
for c in 'pika':
    c = 'p'
    print('p')
    c = 'i'
    print('i')
    c = 'k'
    print('k')
    c = 'a'
    print('a')
print('Hoorah!')
"""



total = 0
for i in range(2):
    for j in range(2):
        total = total + 1
print(total)

"""
total = 0
for i in range(2):   # 0, 1
    i = 0
    for j in range(2):  # 0, 1
        j = 0
        total = 0 + 1
        j = 1
        total = 1 + 1
        
    i = 1
    for j in range(2): # 0, 1
        j = 0
        total = 2 + 1
        j = 1
        total = 3 + 1
print(4)
"""
