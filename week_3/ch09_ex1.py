# Write Python code which asks a user to input a string from
# the console until it is identical to pre-defined string passcode.
# When this occurs, print the number of attempts made to
# enter the correct string. e.g. "3 attempt(s) made."

passcode = "cmpt142"

# ask user to start inputing a password
user_input = input("Enter your password: ")
count = 1
while user_input != passcode:
    # keep asking user to type in
    user_input = input("Enter your password: ")
    count += 1

# when user input the correct passcode, the while loop is completed
# the condition user_input != passcode becomes false
print(f'{count} attempt(s) made')