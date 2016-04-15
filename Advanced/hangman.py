"""
A refresh lesson to go over most of the control flow in Python and a few of the data types.
"""

import random

words = []

word = random.choice(words)

revealed = ['_' if char != ' ' else char for char in word]

guesses = []

tries = 0

while ''.join(revealed) != word and tries < 15:
    print(''.join(revealed))
    guess = input('Which letter do you want to try?')

    if guess not in guesses:
        guesses.append(guess)
        if guess in word:
            positions = [i for i, chr in enumerate(word) if chr == guess]
            for pos in positions:
                revealed[pos] = guess
            print('Yes that was in the word!')
        else:
            print('Sorry that was not in the word.')

    else:
        print('You guessed that already!')
    tries += 1

    print('You have had {} tr{}'.format(tries, 'ies' if tries > 1 else 'y'))

if guess == word:
    print('Congrats! You won!')
else:
    print('Sorry you lost :-(')