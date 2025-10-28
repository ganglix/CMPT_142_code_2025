a = False
b = False
c = True

print(
    not b,
    c and b,
    a or b,
    not b and c,  # True
    b or not c,   # False
    b and c or a, # False
    c or b and a  # bonus False   # N A O
)

