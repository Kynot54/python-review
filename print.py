# Printing in Python

# To print out a statement in python the "print()"
# statement is used.

print("Hello World!")

# To print with special characters use 'r' at the beginning
# such as a path in UNIX
print(r"/usr/bin/name")

# To make your print statements span multiple lines; use triple quotes...
print(''' \
      Hello,
            My name is Paul
      ''')

# Strings can be concatenated using the '+' operator and repeated with the '*' operator
sentence = 3 * "I'm..." + "having a seizure"
print(sentence)

# Two or more string literals, next to each other are automatically concatenated
"Fuck" " this, shit! I'm out."

# This is more useful when breaking long strings across lines
print("Basketball is Kyle's Favorite Sport,"
      "Tom's favorite sport is Baseball.")

# Note: This only works with string literals, not variables or expressions

# String Concatenation with Variables
# To concatnate a string with a variable, do the following:
prefix = "I have a..."
print(prefix + "\nboner")

# String Indexing; strings can be indexed (subscripted) using '[]'
word = "elephant"

word[3] # word[3] is equal to 'p'

# Note: Python specifically supports negative indexing
word[-1] # word[-1] is equal to 't'

# String Slicing: To get a particular part of a string use '[x:y]'
word[0:3] # Note: 'x' the first indicy is included, but 'y's indicy is excluded

# Python strings are __immutable__ and can not be changed
'''
    The following would be invalid:
        >>> word[0] = 'j'
        >>> word[2:] = 'py'
'''

# Getting the length of a string...
# len() can be used to get the length of a string
print(len(word))
