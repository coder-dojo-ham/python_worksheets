def fizzbuzz(num, fizz=3, buzz=5):
    if num % fizz == 0 and num % buzz == 0:
        return 'FizzBuzz'
    elif num % fizz == 0:
        return 'Fizz'
    elif num % buzz == 0:
        return 'Buzz'
    else:
        return num


if __name__ == '__main__':
    for x in range(50):
        print(fizzbuzz(x))
