# while vs. for
# In this demonstration, we’ll see a situation where using a
# while-loop is preferable to using a for-loop.

# password example
passcode = "cmpt142"

# ask user to start inputing a password
user_input = input("Enter your password: ")
count = 1
n_max_attempt = 3

# keep asking user to type when the user's input is wrong AND the use did not exceed the max trial
while user_input != passcode and count < n_max_attempt:
    # keep asking user to type in
    user_input = input("Enter your password: ")
    count += 1

# while is done when (user_input != passcode and count <= n_max_attempt) is False
# there are ONLY two outcomes
if user_input == passcode:         # either 1 the user got the correct passcode
    print(f'{count} attempts made')
else:                              # or 2 the user exceed the max number of attempt
    print(f'wrong trials reaching maximum {n_max_attempt} attempts')
