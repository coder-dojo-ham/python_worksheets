import random

target = random.randint(1, 1000)

guess = int(input('Guess a number between 1 and 100: '))

while guess != target:
    if guess < target:
        guess = int(input('That is too low! Try again: '))
    elif guess > target:
        guess = int(input('That is too high! Try again: '))

print('Yes! That is the number!')
