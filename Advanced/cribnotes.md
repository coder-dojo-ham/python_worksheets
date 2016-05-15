# Notes on Python

## types
    list = ['a', 'b', 1, 2, 3]  # You can store lists of items in a list.
    string = 'hello'  # a string is just some text.
    int = 1  # an int is a number

## if statements

If statements check if something is true or not, and do a thing based on that.

    x = 1

    if x == 1:  # If the first thing is true we do the stuff after that.  
        print('x is 1')
    elif x == 2:  # Otherwise we check the elif.
        print('x is 2')
    else:  # If everything fails we do what is after the else.
        print('x is neither 1 nor 2')
    
## for loops

For loops cycle through a list of things so we can do stuff to it.

    for number in [1,2,3,4,5,6,7,8,9]:
        print(number)  # this will print all the number in the list one by one.
    
## while loops

While loops let us do the same thing over and over (sometimes infinitely) as long as a condition is true.

    x = 1
    while x < 10:
        x += 1
        print(x)
