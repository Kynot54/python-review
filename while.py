# While Loops + Nested Loops

i = 0
j = 0
while i < 10:
    print(' ' * (10 - i), '*' * i, end="")
    i += 1
    while j < i:
        print('*' * j)
        j += 1
        

while i > 0:
    print(' ' * (10 - i),'*' * i, end="")
    i -= 1
    while j > i:
        print('*' * j)
        j -= 1

