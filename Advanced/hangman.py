"""
A refresh lesson to go over most of the control flow in Python and a few of the data types.
"""

import random  # We need to randomly choose a word so need to import random.

words = ['coder dojo', 'kingston', 'richmond', 'raspberry pi', 'python', 'ruby', 'computer', 'jurassic world',
         'turtle', 'hangman']

word = random.choice(words).lower()  # pick a random word.

revealed = ['_' if char != ' ' else char for char in word]  # create the revealed list, for letters we have guessed.

guesses = []

tries = 0

# We want them to be guessing until they get it right or run out of tries.
while ''.join(revealed) != word and tries < 15:
    print(''.join(revealed))  # Show the revealed word.

    # Ask for input, and show what has been guessed so far.
    guess = input('\nYou have tried these letters: {}\nWhich letter do you want to try? '.format(guesses)).lower()

    if guess == word:  # They guessed the word, we need to break the loop!
        break

    elif len(guess) == 1: # We need to make sure the guess was only 1 character long now.

        if guess not in guesses:  # We haven't tried this letter before.
            guesses.append(guess)  # Add it to the list of things we have guessed.

            if guess in word:  # if it is in the word it is a good guess.

                # This makes a list telling us where the letters are in the word.
                positions = [i for i, char in enumerate(word) if char == guess]

                for pos in positions:  # So replace the '_' in revealed at those positions with the letter.
                    revealed[pos] = guess

                print('\nYes that was in the word!')

            else:  # This else means the guess was not in the word.
                print('\nSorry that was not in the word.')

        else:  # This else means that we have already guessed that letter.
            print('\nYou guessed that already!')

    else:  # This else means they guessed a word and it wasn't right (len > 1).
        print('\nSorry that was not the word')

    tries += 1  # We have had a try so + 1.

    print('\nYou have had {} tr{} out of 15'.format(tries, 'ies' if tries > 1 else 'y'))

if word in (guess, ''.join(revealed)):
    print('\nCongrats! You won! It was {}!'.format(word))
else:
    print('\nSorry you lost :-(. The answer was {}.'.format(word))
