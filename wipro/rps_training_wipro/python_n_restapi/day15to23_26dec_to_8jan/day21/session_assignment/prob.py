from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def Engine(self):
        pass
    @abstractmethod
    def Wheels(self):
        pass

    @abstractmethod
    def fuel(self):
        pass

class Car(Vehicle):
    def __init__(self):
        print("Car Constr")

    def Engine(self):
        return ("4 cyld")

    def Wheels(self):
        return("4 Wheels")

    def fuel(self):
        return ("Pertol/CNG/Desiel")

    def Drove(self):
        return ("Staring")

    def AirBag(self):
        return ("AirBag")


class Bike(Vehicle):

    def __init__(self):
        print("Bike Constr")

    def Engine(self):
        return "bs 6"

    def Wheels(self):
        return "2 Wheels"

    def fuel(self):
        return ("Petrol/Electric")

    def Drove(self):
        return ("Handle")

    def park(self):
        return "stand"



c = Car()
b = Bike()

strC = (f'Car is made up of {c.Engine()}, it has {c.Wheels()}. '
        f'Car can run on any of these {c.fuel()}. Car has {c.AirBag()} for safety '
        f'Car is controlled by {c.Drove()}')


strB = (f'Bike is made up of {b.Engine()}, it has {b.Wheels()}. '
        f'Bike can run on any of these {b.fuel()}. Bike can be parked by using {b.park()} '
        f'Bike is controlled by {b.Drove()}')


print(strC)
print(strB)
