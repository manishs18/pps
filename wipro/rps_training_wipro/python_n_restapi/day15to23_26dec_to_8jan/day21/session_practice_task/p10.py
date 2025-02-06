class Animal:

    def __init__(self):
        print("Constr Animal")

    def speak(self):
        return "Make a sound"

class Dog(Animal):

    def __init__(self):
        print("Constr Dog")

    def speak(self):
        return "Woof!"

class Cat(Animal):

    def __init__(self):
        print("Constr Cat")

    def speak(self):
        return "Meow!"

class Cow(Animal):

    def __init__(self):
        print("Constr Cow")

    def speak(self):
        return "Mow!"



def commonFunc(obj):
    print(obj.speak())

# d = Dog()
# print(d.speak())
#
# commonFunc(d)

animals = [Dog(),Cat(),Cow()]

for animal in animals:
    print(type(animal))
    commonFunc(animal)