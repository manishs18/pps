'''
super()-Invoke Overridden Method - Try out

Problem Statement

Even though the child class may override the methods of the parent class, 
it might still decide to use the parent class overridden method. 
To invoke anything belonging to the parent class, the child class needs to use the super() function, 
as shown below:
'''

class Phone:
    def _init_(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    def _init_(self, price, brand, camera):
        super()._init_(price, brand, camera)
        print("Inside SmartPhone constructor")

    def buy(self):
        print("Buying a smartphone")
        super().buy()  


s = SmartPhone(2000, "Apple", 11)

s.buy()