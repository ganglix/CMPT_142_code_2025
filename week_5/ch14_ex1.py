# Topic(s): Reading Files
# read file and create a list of dictionaries to store data
# looks like this:
# scientists = [{"name": "Isaac Newton",
#                "birth_year": 1643,
#                "death_year": 1727},
#               {"name": "Albert Einstein",
#                "birth_year": 1879,
#                "death_year": 1955}]

file_path = "./subfolder/scientists_data.txt"

# open the file
f = open(file_path, "r")
scientists = []   # a list to store all dicts
for line in f:
    # read
    line = line.rstrip()
    # parse the line
    line = line.split(",")
    record_dict = {'name': line[0],
                   'birth_year': int(line[1]),
                   'death_year': int(line[2]),}
    scientists.append(record_dict)

print(scientists)

f.close()  # do not forget to close the file

#pretty print
from pprint import pprint   # importing pprint function from a module which happens to be called "pprint"
pprint(scientists)

