from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())