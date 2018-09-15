class Animal:
    alive = True

    def die(self):
        self.alive = False


class Mammal(Animal):
    legs = 4
    eyes = 2

    def speak(self):
        print('squeak')


class Dog(Mammal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('My name is {}'.format(self.name))
