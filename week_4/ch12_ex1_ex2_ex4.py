def is_valid_username(username):
    """
    determines if username meets these constraints:
    - 1-18 characters long
    - can be letters and/or numbers
    - underscore is allowed if it’s not the first character
    username: string to check validity of
    return: True if username satisfies constraints
    """

# Testing - black box
# black box reason: To test if the function does what it has promised in the docstring
# coverage: cover every single functionality of the function

# test cases

    # length- 1-18 characters long
    """
    input: 'a'
    expected_output: True  # we determine this by reading the docstring, and use our brain to figure out
    reason: 'a' length is 1, only letters, no underscore
    
    input: 'a'*18
    expected_output: True  # we determine this by reading the docstring, and use our brain to figure out
    reason: input length is 18, only letters, no underscore
    
    input: 'a'*19
    expected_output: False  # we determine this by reading the docstring, and use our brain to figure out
    reason: input length is 19, violates the length constraint
    
    input: ''
    expected_output: False  # we determine this by reading the docstring, and use our brain to figure out
    reason: input length is zero, violates the length constraint
    """

    # - can be letters and/or numbers
    """
    input: 'abc'
    expected_output: True  # we determine this by reading the docstring, and use our brain to figure out
    reason: 'abc' has only letters, satisfies constraints
    
    input: '12'
    expected_output: True  # we determine this by reading the docstring, and use our brain to figure out
    reason: '12' has only numbers, satisfies constraints
   
    input: 'abc12'
    expected_output: True  # we determine this by reading the docstring, and use our brain to figure out
    reason: 'abc12' has numbers and letters, satisfies constraints
    
    input: 'abc12@gmail.com'
    expected_output: False  # we determine this by reading the docstring, and use our brain to figure out
    reason: input has special characters, which violates constraints
    """
    # - underscore is allowed if it’s not the first character
    """
    input: '_'
    expected_output: False  # we determine this by reading the docstring, and use our brain to figure out
    reason: input has _ as the first character, which violates _ constraints
    
    input: 'a_'
    expected_output: True  # we determine this by reading the docstring, and use our brain to figure out
    reason: input has _ not as the first character, which satisfies _ constraints
    
    input: 'a_b'
    expected_output: False  # we determine this by reading the docstring, and use our brain to figure out
    reason: input has _ in the middle, which satisfies _ constraints

    

    """



# test driver example
# test driver is a program that runs the test cases

# for example:
    """
    input: 'abc12@gmail.com'
    expected_output: False  # we determine this by reading the docstring, and use our brain to figure out
    reason: input has special characters, which violates constraints
    """
inputs = 'abc12@gmail.com'
expected_output = False  # we determine this by reading the docstring, and use our brain to figure out
reason = "input has special characters, which violates constraints"

output = is_valid_username(inputs)
# if output == expected_output:      # do not report passed test cases
#     print("test case passed!!!")

if output != expected_output:    # only report when fault is found
    print("fault found!",
          'inputs:', inputs,
          'output got from the function:', output,
          'expected_output:', expected_output,
          'test reason', reason)





# # ~~~~~~~~~~~~~~~~after dictionary~~~~~~~~~~~~~~~~~~~~
#
# # dictionary of test case suite to feed into test driver loop
test_suite = [
    # call for length -zero username (empty string)
    {"inputs": [""],
     "outputs": False,
     "reason": "length must be be 1-18 characters"},

    # call for length -one username of invalid character
    {"inputs": ["+"],
     "outputs": False,
     "reason": "username can only contain letters , numbers , underscores"},

    # call for length -one username of a letter
    {"inputs": ["a"],
     "outputs": True,
     "reason": "username is allowed to have letters"},

    # call for length -18 username of numbers only with trailing underscore
    {"inputs": ["0" * 17 + "_"],
     "outputs": True,
     "reason": "username is allowed to have numbers and trailing underscore"},

    # call for length -three username with letter , number , underscore
    {"inputs": ["a_0"],
     "outputs": True,
     "reason": "username is allowed to have letters , numbers , underscore"},

    # call for length -three username with letter , number , starting underscore
    {"inputs": ["_a0"],
     "outputs": False,
     "reason": "can’t start with underscore"},

    # call for length -18+ username of letters and numbers
    {"inputs": ["a0" * 18],
     "outputs": False,
     "reason": "can’t have more than 18 characters"}
]

# a generic loop for test drivers
# the inputs are in a list , so it has to be modified
for test in test_suite:
    inputs = test["inputs"]
    result = is_valid_username(inputs[0])

    if result != test["outputs"]:
        print(f"Testing fault: is_valid_username () returned {result} on inputs {inputs}"
              f"\ntest reason: {test['reason']})\n")
