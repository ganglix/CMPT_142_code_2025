# Write a Python program that uses a for-loop to print all
# integers between 300 and 600 (inclusive) that are divisible
# by both 3 and 5. Print how many of these numbers were
# found

count = 0
for number in range(300, 601):
    if number % 3 == 0 and number % 5 == 0:
        print(number)
        count += 1   # counter add 1 after each print

print(count, "numbers found")