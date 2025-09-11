# Control - Flow Statements

# if, else-if (elif), and else statementes

x = int(input("Input Integer: "))
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

birds = ["blue jay", "red-tailed hawk", "bald eagle"]

for b in birds:
    print(b, len(b))

'''
    Code that modifies a collection while iterating over that same 
    collection can be tricky to get right. 
    Instead, it is usually more straight-forward to loop over a copy 
    of the collection or to create a new collection:
'''

'''*****Example:*********************************************************'''

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

'''******END_OF_EXAMPLE***************************************************'''


# If needing to iterate over a sequenece of numbers use the range()
# when running a for-loop

for i in range(5): #Numbers is exlusive: i.e. 0 - 4
    print(i + 1)

# The range() function can have it's start, stop, and 
# step modified range(start,stop,step).

print(list(range(1,11,1)))

# If needing to iterate over the indicies of
# a sequence use range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# Bookmark: https://docs.python.org/3/tutorial/controlflow.html

# Range Returns a what at first appears to be a list "range(0, x)"
# ,but it really is in fact an iterable

# Break and Continue Statements

# When using the 'break' statement it breaks out of the innermost 'for' or
# 'while' loop

# Note: The 'else' clause may be used on the loop

for n in range(2,10):
    for o in range(2, n):
        if n % o == 0:
            print(f"{n} equals {o} * {n//o}")
            break
    else:
        # Loop fell through without finding a factor
        print(f"{n} is a prime number")

# Using a 'continue' statement, continues with the next iteration of the loop
for num in range(2, 20):
    if num % 2 == 0:
        print(f"{num} is even")
        continue
    print(f"{num} is odd")

# The keyword "pass" does nothing, but is useful as a place-holder when developing
# a function

def testFunc(*args):
    pass # Or '...'


# match-case statements

'''

    A match statement takes an expression and compares its value to sucessive
    patterns given as one or more case blocks, similar to switch in C++, but more
    similar to pattern matching in Rust or Haskell

'''

def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        # Note: can be piped together using the bitwise-OR
        case 500 | 505 | 504:
            return "Internal Server Error"
        # Note: '_' is a wildcard and can take place of anything
        case _:
            return "Something went wrong"

print(http_error(418))

# Function Defintions and Special Arguements

# Default Argument Values
def ask_ok(prompt, retries=3, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yee', 'yes', 'yeah'}:
            return True
        elif reply in {'n', 'neigh', 'nein', 'no', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("invalid response")
        if retries < 1:
            print(reminder)
        else:
            print(reminder + ", you imbecile!")
        

prompt = "Do you really want to quit?"
ask_ok(prompt, 2, reminder="Try again")

'''
    Note: Default values are carried over by default in subsequent calls,
          in order to avoid that, special checking must be done.
'''

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(5))
print(f2(3))
print(f2(7))

# Refer back to section 4 of functions, for positional vs. keyword arguements,
# and labmda expressions
