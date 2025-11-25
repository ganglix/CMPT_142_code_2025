# Read in the file data to create dictionary extensions that
# maps extension numbers to employees

# workflow

# find the directory
# absolute directory
# file_path = r"C:\Users\gal894.STPETERS\Desktop\CMPT_142_code_2025\week_5\ext_directory_data.txt"

# relative directory
# . means current folder
# .. means parent folder
# file_path = "./ext_directory_data.txt"   # . means week_5 folder
# file_path = "../week_5/ext_directory_data.txt" # .. means CMPT_142_code_2025 folder

file_path = "ext_directory_data.txt"
# by default python will find this file in the current folder which contains your py file
# open file
f = open(file_path, "r")  # r means read mode, f is the handle

# initialize a dict
extensions = {}   # ext number: name

# read line by line
for line in f:
    line = line.rstrip() # to remove the hidden "new line \n" at the end of each line
    # parse the line
    line = line.split(',') # to parse the long string into a list of substrings using,
    print(line)
    # add records into the dict
    extensions[int(line[0])] = line[1]

print(extensions)

# close the file  Dont forget to close the file
f.close()