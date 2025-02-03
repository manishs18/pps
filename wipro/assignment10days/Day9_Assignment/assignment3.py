'''
Problem Statement

An apparel shop wants to manage the items which it sells.
Write a python program to implement the class diagram given below.

Apparel

- item_id
- price
- item_type
- counter -> static

__init__(price,item_type)
+ calculate_price()
+ get_item_id()
+ get_price()
+ get_item_type()
+ set_price(price)

Cotton                                        Silk
- discount                                  - points

__init__(price, discount)                   __init__(price)
+ calculate_price()                         + calculate_price()
+ get_discount()                            + get_points()

Class Description:
Apparel class:

1. Initialize static variable counter to 100
2. In the constructor, auto-generate item id starting from 101 prefixed by "C" for cotton apparels and "S" for silk apparels. Example C101, S102, 5103, C104 etc.
3. calculate price(): Add 5% service tax on the price of the apparel and update attribute, price with the new value

Cotton class:

1. While invoking parent constructor from child constructor, pass "Cotton" as item_type
2. Calculate price(): Update attribute, price of Apparel class based on rules given below
   a. Add service tax on price by invoking appropriate method of Apparel class
   b. Apply discount on price
   c. Add 5% VAT on final price

Silk class:

1. While Invoking parent constructor from child constructor, pass "Silk" as item type 2. calculate_price(): Update attribute, price of Apparel class based on rules given below
   a. Add service tax on price by invoking appropriate method of Apparel class
   b. Identify points earned based on rules given below:
      - Silk apparels with price more than Rs. 10000, earn 10 points and anything less than or equal to that earn 3 points
   c. Initialize attribute, points with the identified points
   d. Add 10% VAT on price

Note: Perform case sensitive string comparison

For testing:
Create objects of Cotton class and Silk class
Invoke calculate_price() on Cotton objects and Silk objects
Display their details
'''


class Apparel:
    __counter = 100

    def __init__(self, price, item_type):
        Apparel.__counter += 1
        self.__item_id = f"{item_type[0]}{Apparel.__counter}"  # "C" for Cotton, "S" for Silk
        self.__price = price
        self.__item_type = item_type

    def calculate_price(self):
        self.__price += self.__price * 0.05

    def get_item_id(self):
        return self.__item_id

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def set_price(self, price):
        self.__price = price


class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "Cotton")
        self.__discount = discount

    def calculate_price(self):
        super().calculate_price()
        discounted_price = self.get_price() - self.get_price() * (self.__discount / 100)
        self.set_price(discounted_price)
        self.set_price(self.get_price() + self.get_price() * 0.05)

    def get_discount(self):
        return self.__discount


class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, "Silk")
        self.__points = 0

    def calculate_price(self):
        super().calculate_price()
        if self.get_price() > 10000:
            self.__points = 10
        else:
            self.__points = 3
        self.set_price(self.get_price() + self.get_price() * 0.10)

    def get_points(self):
        return self.__points


def main():
    cotton1 = Cotton(1000, 10)

    cotton1.calculate_price()

    print(f"Item ID: {cotton1.get_item_id()}, Type: {cotton1.get_item_type()}, Price: {cotton1.get_price()}, Discount: {cotton1.get_discount()}%")


if __name__ == "__main__":
    main()
