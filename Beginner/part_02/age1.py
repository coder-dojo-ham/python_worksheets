# We need to store our users name in a variable.
# to do this we use the input function
name = input('What is your name? ')

# You can concatenate strings together using the + operator
print('Hi ' + name + ' I am Python!')

# Input always assumes what the user writes is a string.
# As a result we have to manually convert it to an integer
# using the int function.
years = int(input('How old are you ' + name + '? '))

months = years * 12

print(name + ' did you know that you are ' + str(months) + ' months old?')
