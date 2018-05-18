class Animal:
    alive = True

    def die(self):
        self.alive = False


class Mammal(Animal):
    legs = 4
    eyes = 2

    def speak(self):
        print('squeak')

class Cat(Mammal):
    def speak(self):
        print('Meow')

class Dog(Mammal):
    def speak(self):
        print('Woof')

class Puppy(Dog):
    young = True

class Human(Mammal):
    legs = 2
    arms = 2
    def speak(self):
        print('Hello')