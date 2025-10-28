# Given variables:
nation = "Canada !!!"
nation_motto = "From sea to Sea"

# Write expressions to:
# (a) Determine if nation has only alphabetic letters and digits
print(nation.isalnum())  # no arg passed to this method

# (b) Remove "!" characters and whitespace from nation
print(nation.replace("!", "").replace(" ", "") )

# (c) Find the location of the first word "Sea" substring in nation_motto
print(nation_motto.lower().find('sea'))
print(nation_motto.title().find('Sea'))


print(nation.lower())

