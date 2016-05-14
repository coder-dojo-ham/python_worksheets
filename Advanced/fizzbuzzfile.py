import random
from fizzbuzz import fizzbuzz

with open('fizzbuzztest.txt', 'w') as test_file:
    for _ in range(100):
        test_file.write(str(random.randint(1,1000)) + '\n')

with open('fizzbuzztest.txt', 'r') as test_file:
    for line in test_file:
        print(fizzbuzz(int(line)))
