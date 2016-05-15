"""
This is a template for hangman.

Use the hints here to write your own program.
"""

import random # import a module which does random things here

# put your own words in here.
list_of_words = ['put', 'some', 'words', 'here']

# choose a random word from your list, use the import above.
word = some random word

# You might need to make some variables here
# to say how many tries has had, and their guesses.

tries = 0

guesses = []

hidden_word = ['_' for char in word]

# Now you need to loop around asking them to guess
# until they get it right or run out of tries.
while some conditions:
    # you need a hidden version of the word to show how
    # big it is and what they've guessed so far.
    print the hidden word
    # Ask them to guess a letter or word here.
    guess = a users guess

    # check here if they got the right letter or word.
    if some guess is good:
        # tell the user is good
        tell the user it is good.
    else:
        # make sure to tell them if it is wrong.
        tell the user it is wrong

    # outside of the if now.
    add the guess to the list of guesses

# outside the loop now.

if they won:
    # tell them they won.
else:
    # tell them they lost.
