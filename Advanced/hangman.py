"""
A refresh lesson to go over most of the control flow in Python and a few of the data types.
"""

import random

words = ['coder dojo', 'kingston', 'richmond', 'raspberry pi', 'python', 'ruby', 'computer', 'jurassic world',
         'turtle', 'hangman']

word = random.choice(words).lower()

revealed = ['_' if char != ' ' else char for char in word]

guesses = []

tries = 0

while ''.join(revealed) != word and tries < 15:
    print(''.join(revealed))
    guess = input('\nWhich letter do you want to try? ').lower()

    if guess == word:
        break

    if guess not in guesses:
        guesses.append(guess)
        if guess in word:
            positions = [i for i, char in enumerate(word) if char == guess]
            for pos in positions:
                revealed[pos] = guess
            print('Yes that was in the word!')
        else:
            print('Sorry that was not in the word.')

    else:
        print('You guessed that already!')
    tries += 1

    print('You have had {} tr{} out of 15'.format(tries, 'ies' if tries > 1 else 'y'))

if word in (guess, ''.join(revealed)):
    print('Congrats! You won!')
else:
    print('Sorry you lost :-(')