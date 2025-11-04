# Control Flow: Repetition
# what is a computer good at?
# repeat till what? when?


# while loop starts and stops according to a condition
## things I want to mention: condition boolean, if/while

# counting example : 1~5
count = 0
while count < 5:
    count += 1  # same  as count = count + 1
    print('count inside while loop, count=', count)

print('when while loop is done, count =', count)



# for : repeat over a sequence
# mention types of sequence: string, range, list, dict

s = 'cmpt142'
for i in range(len(s)): # 0, 1, 2, 3, 4, 5 6
    print(i, s[i])  # print index and char

# directly iterate over the sequence
for char in s:
    print(char)
