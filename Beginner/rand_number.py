import random

answer = random.randint(1, 1000)

guess = int(input('Guess a number between 1 and 100: '))


while guess != answer:
    if guess < answer:
        print("That was too low")
    elif guess > answer:
    
        print("That was too high")
    guess = int(input('Guess a number between 1 and 100: '))

print("That was right!")
