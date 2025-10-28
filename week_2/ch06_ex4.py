# Flowtrace with function

# status = "Healthy"
# def set_status(s):
#     status = s
#
# set_status("Poisoned")
# print(status)


""" Flowtrace
status = "Healthy"
set_status("Poisoned")

    ------execute the function---another piece of paper, can not be touched from outside--------
    s = "Poisoned"
    status = "Poisoned"
    -----------------------------------------------------------------------------

print("Healthy")
"""

# status = "Healthy"
# def set_status(s):
#     return s
#
# status = set_status("Poisoned")
# print(status)

# Takeaway: the function can not assign a new value to a global variable internally


#~~(things I want to mention: scope, return, dangerous thing to do)







# optional: global var can be accessed from inside the func but can not be assigned
