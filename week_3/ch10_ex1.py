# A given list called pkg_weights contains weights of parcels
# (in lbs) queued for shipping. Write Python code that:
# (a) Creates list light_pkgs of parcels that weigh less than 5
# lbs from pkg_weights
# (b) Removes parcels from pkg_weights that exceed 15 lbs
# (c) Print the:
# • contents of light_pkgs in ascending order
# • number of parcels in light_pkgs
# • number of parcels removed from pkg_weights

pkg_weights = [2, 6, 8, 34, 56, 67, 4, 2, 33]

# (a) Creates list light_pkgs of parcels that weigh less than 5
light_pkgs = []
for p in pkg_weights:
    if p < 5:
        light_pkgs.append(p)
print(light_pkgs)

# (b) Removes parcels from pkg_weights that exceed 15 lbs

# for p in pkg_weights:    # pkg_weights is changing during the for loop
#     if p > 15:           # DO NOT iterate over a size-changing list
#         pkg_weights.remove(p)
# print(pkg_weights)

# pkg_weights_clone = pkg_weights.copy()
# for p in pkg_weights_clone:    # .copy() creates a (new)clone of the list
#     if p > 15:           # so the cloned list does not change during iteration
#         pkg_weights.remove(p)
# print(pkg_weights)


heavy_pkgs = []
for p in pkg_weights:
    if p > 15:
        heavy_pkgs.append(p)

for p in heavy_pkgs:  # heavy_pkgs does not change during iteration
    pkg_weights.remove(p)

print(pkg_weights)



# (c) Print the:
# • contents of light_pkgs in ascending order
# light_pkgs.sort()
# print(light_pkgs)

print(sorted(pkg_weights))


# • number of parcels in light_pkgs
print(len(light_pkgs))

# • number of parcels removed from pkg_weights
print(len(heavy_pkgs))













# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention
# Modifying list while iterating DO NOT DO IT
# don't change list if possible
# use a clone



# create a clone, new list
# L_new = L.copy() # use .copy()
# L_new = L[:] # use slicing
