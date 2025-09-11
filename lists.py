# Python has what's known as 'compund' data types
# They're used to group together multiple values

# The most versatile is the list (i.e. vector)
# Lists in Python can contain different data types; however,
# it is more common for them to all have the same data types

cubes = [1, 8, 27, 125]

# Lists also being sequence types like strings can be accesed with
# the index operator

print(cubes[3]) # prints '125'

# Lists unlike strings are mutable meaning the data within them
# can be changed.

# The append() methods adds the element to the end of the list
cubes.append(216)
cubes.append(7 ** 3) # Note operations can be performed before appending

# The assignment operator __never__ copies data when creating a new varible
# and assigning it another variable it is always referencing the same value
rgb = [255, 45, 135]
rgba = rgb

#Note: Use id() to check the memeory address of a varible
print(id(rgb))
print(id(rgb) == id(rgba))
rgba.append(0.69)

print(rgb)

# To get the amount of data in a list, you can also use the len() function
print(len(rgb))

# Nested Lists
x = ['a', 'b', 'c']
y = [1 , 2, 3]
z = [x, y]

print(z[0][2])
