"""
Learn how to open, write and read files.

We'll incorporate fizzbuzz from earlier to force us to learn about newlines and requiring strings to write to files.

Also teaches about local imports.
"""
import random
from fizzbuzz import fizzbuzz  # Import fizzbuzz which we should have made earlier.

with open('fizzbuzztest.txt', 'w') as test_file:  # Open the file for writing.
    for _ in range(100):
        test_file.write(str(random.randint(1, 1000)) + '\n')  # Don't forget str conversion to write your random number

with open('fizzbuzztest.txt', 'r') as test_file:  # open the file for reading.
    for line in test_file:
        print(fizzbuzz(int(line)))  # don't forget that fizzbuzz requires an integer (could we change this?)
