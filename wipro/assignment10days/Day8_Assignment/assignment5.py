'''
Problem Statement

Animal Welfare Trust is on a visit to the circus camp to have a look at the four talking parrots added to the camp. 
A parrot is identified by its name and color. Apart from this, the trust has asked to assign a unique number for each parrot. 
The unique number should begin with 7001 and should be auto-incremented by 1 for every new parrot added to the camp.

Identify the class name and attributes so as to represent parrots from the list given.

- beak color
- __init__(name,color)
- name
- Parrot
- counter->static
- color
- Parrots
- unique_number

Write a Python program to implement the class chosen with its attributes and methods. Represent few parrots, display their names, color and unique number.

Note: Consider all the attributes to be private and methods to be public. Include getter methods for all the instance variables.
'''

class Parrot:
    __counter = 7001

    def __init__(self, name, color, beak_color):
        self.__name = name
        self.__color = color
        self.__beak_color = beak_color
        self.__unique_number = Parrot.__counter
        Parrot.__counter += 1  

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_beak_color(self):
        return self.__beak_color

    def get_unique_number(self):
        return self.__unique_number


def main():
    parrot1 = Parrot("Polly", "Green", "Yellow")
    parrot2 = Parrot("Kiwi", "Blue", "Orange")
    parrot3 = Parrot("Sunny", "Yellow", "Red")
    parrot4 = Parrot("Chirpy", "Red", "Black")

    parrots = [parrot1, parrot2, parrot3, parrot4]

    for parrot in parrots:
        print(f"Name: {parrot.get_name()}, Color: {parrot.get_color()}, Beak Color: {parrot.get_beak_color()}, Unique Number: {parrot.get_unique_number()}")


if __name__ == "__main__":
    main()
