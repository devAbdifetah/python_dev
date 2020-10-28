from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)         
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /



# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if x >= 0 and y >=0:
    print("both x and y positive",x,y)
elif not(x >= 0 and y >=0):
    print("both x and y are negative",x,y)
    if x > 0 or y < 0:
        print("x is positive and y is negative",x,y)
    else:
        print("y is posive and x is negative",x,y)
else:
    print("no other option")
        



