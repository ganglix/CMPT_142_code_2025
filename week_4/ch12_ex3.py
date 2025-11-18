def is_valid_password(password):
    """
    determines if password meets these constraints:
    - 9-18 characters long
    - no Underscores or minus _,-
    password: string to check validity of
    return: True if password satisfies constraints
    """
    is_valid = True

    if len(password) < 9 or len(password) > 18:
        is_valid = False
        return is_valid
    if "_" in password:
        is_valid = False
        return is_valid
    if "-" in password:
        is_valid = True #False
        return is_valid
    return is_valid


# Testing - white box
# reasoning: Strategically pick test inputs that will trigger all lines of code; each line of code should run at least once
# comment: trigger every if, every loop (while, for)

"""
inputs: ''
expected_outputs: False  # DO NOT read the code, as we do not trust it (that is why we are testing it), we figure it out by reading the docstring, same as the blackbox testing
reason: inputs' length is zero, which triggers line 11 if statement to be true, covering code line 11-13

inputs: 'a_'
expected_outputs: False  # DO NOT read the code, as we do not trust it (that is why we are testing it), we figure it out by reading the docstring, same as the blackbox testing
reason: inputs has an _, which triggers line 14 if statement to be true, covering code line 14-16

inputs: 'a-'   # bad test case to trigger line 17 if, because line 11 if was triggered and function returned early
expected_outputs: False  # DO NOT read the code, as we do not trust it (that is why we are testing it), we figure it out by reading the docstring, same as the blackbox testing
reason: [bad one] inputs contains - , which triggers line 17 if statement to be true, covering code line 17-19

inputs: 'a' * 9 + '-'  
expected_outputs: False  # DO NOT read the code, as we do not trust it (that is why we are testing it), we figure it out by reading the docstring, same as the blackbox testing
reason: [good one] inputs contains -, proper length, no _, which triggers line 17 if statement to be true, covering code line 17-19

"""

# test drive
"""
inputs: 'a-'
expected_outputs: False  # DO NOT read the code, as we do not trust it (that is why we are testing it), we figure it out by reading the docstring, same as the blackbox testing
reason: inputs contains - , which triggers line 17 if statement to be true, covering code line 17-19
"""

inputs = 'a'*9 +'-'
expected_outputs = False  # DO NOT read the code, as we do not trust it (that is why we are testing it), we figure it out by reading the docstring, same as the blackbox testing
reason = "inputs contains -, proper length, no _, which triggers line 17 if statement to be true, covering code line 17-19"
outputs = is_valid_password(inputs)
if outputs != expected_outputs:
    print(f"fault found!, "
          f"input: {inputs} "
          f"output: {outputs} "
          f"expected ouput: {expected_outputs} "
          f"test reason: {reason}"
        )
print(outputs)
