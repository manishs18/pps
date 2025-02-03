'''
Assignment

WeCare insurance company wants to calculate premium of vehicles.
Vehicles are of two types - "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two wheelers and 5% of the vehicle cost for four wheelers. 
Calculate the premium amount and display the vehicle details

Identify the class name and attributes to represent vehicles. Drag and drop the chosen class name, 
attributes and methods into the appropriate section of the box shown below.
'''

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, cost):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.cost = cost
        self.premium_amount = 0 

    def calculate_premium(self):
        if self.vehicle_type == "Two Wheeler":
            self.premium_amount = 0.02 * self.cost
        elif self.vehicle_type == "Four Wheeler":
            self.premium_amount = 0.05 * self.cost

    def display_details(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Vehicle Cost: {self.cost}")
        print(f"Premium Amount: {self.premium_amount}")


vehicle1 = Vehicle("V001", "Two Wheeler", 50000)
vehicle2 = Vehicle("V002", "Four Wheeler", 600000)

vehicle1.calculate_premium()
vehicle2.calculate_premium()

vehicle1.display_details()
vehicle2.display_details()

