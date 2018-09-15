import random

from fizzbuzz import fizzbuzz


def generate_random_numbers():
    with open('numbers.txt', 'w') as file:
        for _ in range(100):
            file.write(str(random.randint(0, 1000)) + '\n')


def fizzbuzz_file(input_name='numbers.txt', output_name='fizzbuzz.txt'):
    with open(input_name) as input_file, open(output_name, 'w') as output_file:
        for num in input_file:
            num = int(num)
            result = str(fizzbuzz(num))
            output_file.write(result + '\n')


if __name__ == '__main__':
    generate_random_numbers()
    fizzbuzz_file()
