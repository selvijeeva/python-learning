""" Use the while loop to construct a pyramid-shaped wall - it's flat.
    The pyramid is stacked according to one simple principle: 
    each lower layer contains one block more than the layer above.
    Read the number of blocks required.
"""


blocks = int(input("Enter the number of blocks: "))
height = 0
layer = 1

while layer <= blocks:
    height += 1
    blocks -= layer
    layer += 1
print("The height of the 2 dimensional pyramid:", height)
45