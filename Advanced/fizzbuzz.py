"""
A simple recap on functions which kids may be expected to do themselves.
"""


def fizzbuzz(num, fizz=3, buzz=5):
    """
    A function which takes a number and tries to divide it by fizz and buzz.

    Fizz and buzz are by default numbers 3 and 5 but can be changed in the arguments.

    If it divides by fizz, we return 'fizz'.

    If it divides by buzz we return 'buzz'.

    If it divides by both we return 'fizzbuzz'.

    Otherwise we return the number.

    :param num: int, the number we are trying to divide.
    :param fizz: int, the number we use for fizz.
    :param buzz: int, the number we use for buzz.
    :return: int/str, the result.
    """
    if num % fizz == 0 and num % buzz == 0:
        return 'fizzbuzz'
    elif num % fizz == 0:
        return 'fizz'
    elif num % buzz == 0:
        return 'buzz'
    else:
        return num

for x in range(50):  # The main loop to run the function.
    print(fizzbuzz(x))
