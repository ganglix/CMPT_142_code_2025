# Exercise 2

# Suppose we have dictionary availability:
# keys: friend’s name
# values: list of days they are available to play a game
# (a) Write a function that accepts an availability dictionary and returns a new dictionary mapping days to
# friends who can play that day.
# (b) Using the function from a):
# Find the day most friends can attend to play the game
# List who can and can not attend the session that day

availability = {"Neo":      ["Monday"],
                "Morpheus": ["Sunday"],
                "Smith":    ["Monday", "Tuesday"]}

def scheduler(availability):
    """
    Convert a dictionary of availability to a dictionary of schedule
    :param availability: dict, name: list of available days
    :return: dict, day: list of available names
    """
    # initialize dict
    schedule = {}   #  day: list of names
    # iterate over the availability dict
    for name in availability:    # availability {name: list of days}
        days_list = availability[name]
        # check each day; write down the day
        # add available name to the list for that day
        for day in days_list:
            if day not in schedule:
                schedule[day] = []    # if day was not previously added to the dict during the iteration history
            schedule[day].append(name)

    return schedule

schedule = scheduler(availability)   # day: name list


# find the day that most friends can attend

# routine to find the "max"
max_n_ppl = 0
day_of_max_ppl = ''

for day in schedule:
    if len(schedule[day]) > max_n_ppl:
        max_n_ppl = len(schedule[day])  # update the max number
        day_of_max_ppl = day  # update the day

print(f"The day that most people can attend: {day_of_max_ppl}")

# List who can and can not attend the session that day

ppl_attend = schedule[day_of_max_ppl]

ppl_not_attend = []
for day in schedule:
    namelist = schedule[day]
    for name in namelist:
        if name not in ppl_attend:
            ppl_not_attend.append(name)

print(f"people who attend {ppl_attend}")
print(f"people who do not attend {ppl_not_attend}")

