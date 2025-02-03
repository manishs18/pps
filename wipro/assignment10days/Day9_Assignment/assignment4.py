'''
Problem Statement

Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India. 
They want to keep track of customers who buy fruits from them and also the billing process.
Write a python program to implement the class diagram given below.

FruitInfo                                     Purchase                                         Customer

- fruit_name_list -> static                   - purchase_id                                   - customer_name
- fruit_price_list -> static                  - customer                                      - cust_type
                                              - fruit_name
                                              - quantity                                      + __init__(customer_name, cust_type)
                                              - counter -> static                             + get_customer_name()
                                                                                              + get_cust_type()
+ get_fruit_price(fruit_name) -> static       __init__(customer, fruit_name, quantity)                                               
+ get_fruit_name_list() -> static             + get_purchase_id()
+ get fruit price list() ->static             + get_customer()
                                              + get_quantity()
                                              + calculate_price()

Class Description:

Fruit Info class:

1. fruit name list: Static list which contains the list of fruits available 
2. fruit price list: Static list which contains the price/kg of fruits
3. The above two lists have one-to-one correspondence, initialize it with the data given in the table 
4. get fruit price(fruit_name): Accept a fruit name and return its price/kg. If fruit is not available, return -1

Fruit Name            Apple  Guava  Orange  Grape  Sweet Lime

Price per Kg          200    00     70      110    60

Purchase class:

1. Initialize static variable counter to 101
2. calculate price(): Calculate and return total fruit price based on rules given below
   a. For valid fruit name (hint: invoke get fruit price(fruit_name)),
      - Calculate price based on price/kg and quantity of the fruit purchased by the customer
      - If price/kg of the fruit is maximum among the fruits in fruit lists and quantity purchased is more than 1kg, apply 2% discount on calculated price 
      - If price/kg of the fruit is minimum among the fruits in fruit lists and quantity purchased is 5kg or more, apply 5% discount on calculated price
      - If the customer is a "wholesale" customer, provide an additional 10% discount. Apply this discount on already discounted price, if any one of the above two points are applicable. Else apply it oncalculated price 
      - Auto-generate purchase id starting from 101 prefixed by "P". Example -P101, P102 P103 etc.
      - Return final fruit price

    b. Else, return -1.


Note:

Perform case sensitive string comparison
There will be only one fruit with maximum price and one with minimum price

For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details
'''

class FruitInfo:
    __fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    __fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            index = FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo.__fruit_price_list[index]
        return -1

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list


class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type


class Purchase:
    __counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__purchase_id = f"P{Purchase.__counter}"
        Purchase.__counter += 1

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        fruit_price = FruitInfo.get_fruit_price(self.__fruit_name)
        if fruit_price == -1: 
            return -1

        total_price = fruit_price * self.__quantity
        max_price = max(FruitInfo.get_fruit_price_list())
        min_price = min(FruitInfo.get_fruit_price_list())

        if fruit_price == max_price and self.__quantity > 1:
            total_price *= 0.98

        if fruit_price == min_price and self.__quantity >= 5:
            total_price *= 0.95

        if self.__customer.get_cust_type() == "wholesale":
            total_price *= 0.90

        return total_price


def main():
    customer1 = Customer("Alice", "retail")


    purchase1 = Purchase(customer1, "Apple", 2)


    print(f"Purchase ID: {purchase1.get_purchase_id()}, Customer: {purchase1.get_customer().get_customer_name()}, "
          f"Fruit: {purchase1._Purchase__fruit_name}, Quantity: {purchase1.get_quantity()}, "
          f"Total Price: {purchase1.calculate_price()}")



if __name__ == "__main__":
    main()
