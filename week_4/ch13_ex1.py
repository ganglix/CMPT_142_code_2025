# Suppose you have a dictionary of survey responses:
# •keys are student names
# •values are favourite ice cream flavours (one of
# "chocolate", "vanilla", "strawberry", "bubblegum")
# Write a function that takes a dictionary of survey responses
# and returns a new dictionary where:
# •keys are ice cream flavours
# •values are number of students with that favourite flavour

survey = {"Calla": "strawberry",
          "Jassika": "vanilla",
          "Fletcher": "strawberry",
          "Logan": "strawberry",
          "Joshua": "chocolate",
          "Marl": "chocolate",
          "Marc": "chocolate",
          "Kartik": "vanilla",
          "Kale": "chocolate",
          "Barney": "chocolate",
          "Rhett": "strawberry",
          "Gang": "bubblegum"}


def class_flavor(survey):
    """
    Summarize the number of vote for each flavor
    :param survey: dict, people's choice of flavor, {name: flavor}
    :return: dict, vote for each flavor, {flavor: number of votes}
    """
    # initialize a dict  {flavor: number of votes}
    flavor_vote = {}
    # check every vote for flavor and count the name
    for name in survey: # {name: flavor}
        # one by one
        # write down the flavor
        flavor = survey[name]

        # if the flavor is not in flavor_vote, add the flavor write it down first
        if flavor not in flavor_vote:
            flavor_vote[flavor] = 0

        # then add count to that flavor
        flavor_vote[flavor] += 1

    return flavor_vote

print(class_flavor(survey))