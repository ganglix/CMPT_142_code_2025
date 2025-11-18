# demo1
# Tower Name Location
# Tokyo Skytree Japan
# Canton Tower China
# CN Tower Canada

tower = {
    "Tokyo Skytree": "Japan",
    "CN Tower": "Canada",
    "Canton Tower": "China",
}


# Let’s modify the dictionary:
# (a) Remove the entry whose location is "Canada"
# for this_tower in tower:      # tower {tower name: country) # DO NOT iterate a size-changing dict
#     # check country; look for canada
#     if tower[this_tower] == "Canada":
#         # remove the entry
#         tower.pop(this_tower)

for this_tower in tower.copy():      # tower {tower name: country) iterate the copy, which does not change during iteration
    # check country; look for canada
    if tower[this_tower] == "Canada":
        # remove the entry
        tower.pop(this_tower)
print(tower)

# (b) Add a new entry with tower name "Eiffel Tower" and
# location "Paris"
tower['Eiffel Tower'] = 'Paris'


# (c) Oops! Update the tower entry "Eiffel Tower" to have
# location "France"
tower['Eiffel Tower'] = 'France'

print(tower)


