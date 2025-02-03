'''
Problem Statement

A vehicle is identified by its mileage (in kms per litre) and fuel left (in litres) in the vehicle. 
From the fuel left, 5 litres will always be considered as reserve fuel. 
At any point of time, the driver of the vehicle may want to know:

- The maximum distance that can be covered without using the reserve fuel 
- how many kms he/she has already travelled based on the initial fuel the vehicle had

Identify the class name and attributes so as to represent a vehicle from the information given.

__init__()
Vehicle
Car
identify_disctance_that_can_be_travelled()
mileage
fuel left
identify_distance_travelled(initial_fuel)

Write a Python program to implement the class chosen with its attributes and methods based on the requirements given below:

identify_distance_that_can_be_travelled(): Return the distance that can be travelled by the vehicle without using the reserve fuel. If the fuel left is less than or equal to reserve fuel, the method should return 0.
identify_distance_travelled(initial_fuel): Return the distance so far travelled by the vehicle based on the initial fuel, fuel left and mileage.

Assume that initial fuel is always greater than fuel left.

Represent a vehicle and test your program by initializing the instance variables and invoking the appropriate methods.
'''


class Vehicle:
    def __init__(self, mileage, fuel_left):
        
        self.mileage = mileage
        self.fuel_left = fuel_left
        self.reserve_fuel = 5  

    def identify_distance_that_can_be_travelled(self):
        
        usable_fuel = self.fuel_left - self.reserve_fuel
        if usable_fuel <= 0:
            return 0
        return usable_fuel * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        
        fuel_used = initial_fuel - self.fuel_left
        return fuel_used * self.mileage

vehicle = Vehicle(mileage=15, fuel_left=10)

max_distance = vehicle.identify_distance_that_can_be_travelled()
print(f"Maximum distance that can be travelled without reserve fuel: {max_distance} kms")

distance_travelled = vehicle.identify_distance_travelled(initial_fuel=20)
print(f"Distance already travelled: {distance_travelled} kms")




























# Practice

# veg_price = 120
# non_veg_price = 150

# user_input = input("Enter your order (veg/non-veg): ")
# quantity = int(input("Enter the quantity: "))
# dist = float(input("Enter the distance in km: "))

# base_price = 0

# if user_input == "veg":
#     base_price = veg_price * quantity
# elif user_input == "non-veg":
#     base_price = non_veg_price * quantity
# else:
#     print("Invalid input. Please enter 'veg' or 'non-veg'.")
#     base_price = None

# delivery_charge = 0
# if dist > 3 and dist <= 6:
#     delivery_charge = (dist - 3) * 3
# elif dist > 6:
#     delivery_charge = (3 * 3) + ((dist - 6) * 6)

# if base_price is not None:
#     total_price = base_price + delivery_charge
#     print(f"The price of your order ({quantity} {user_input} items) is: {base_price}")
#     print(f"The delivery charge is: {delivery_charge}")
#     print(f"The total amount to pay is: {total_price}")




