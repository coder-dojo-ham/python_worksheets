# In this program we need to choose a random number.
# Python has an in built way of choosing random things.
# To use this we import a module called "random"
import random

# Using the randint function inside the random module
# we can choose a random number in a given range.
target = random.randint(1, 1000)

guess = int(input('Guess a number between 1 and 100: '))

# The while loop allows us to constantly do the same thing
# until a condition is no longer True.
while guess != target:
    if guess < target:
        guess = int(input('That is too low! Try again: '))
    elif guess > target:
        guess = int(input('That is too high! Try again: '))

print('Yes! That is the number!')
