'''
Problem Statement

ABC DTH (Direct to Home) firm wants to calculate monthly rent for its consumers.
A consumer can register for one Base Package. Write a python program to implement the below given class diagram.

DirectToHomeService

- consumer_number
- consumer_name
- counter -> static

__init__(consumer_name)
+ get_consumer_number()
+ get_consumer_name()
+ calculate_monthly_rent()-> abstract


BasePackage

- base_pack_name
- subscription_period

__init__(consumer_name,base_pack_name,subscription_period)
+ get_base_pack_name()
+ get_subscnption_period() 
+ validate_base_pack_name()
+ calculate_monthly_rent()

Class Description:

DirectToHomeService class:
1. Initialize static variable counter to 101
2. Inside constructor, auto-generate consumer_number starting from 101

Class Description:
DirectToHomeService class:
1. Initialize static variable counter to 101
2. Inside constructor, auto-generate consumer_number starting from 101

BasePackage class:
1. validate_base_pack_name():
   a. Validate base pack name. Valid values are "Silver", "Gold" and "Platinum".
   b. If invalid, set attribute, base_pack_name as "Silver" and display "Base package name is incorrect, set to Silver"

2. calculate_monthly_rent():
   a. Check if subscription period is between 1 and 24 (both inclusive). If so, Validate base pack name
      - Identify monthly rent based on base pack. Refer table given.
      - Consumers are eligible for discount of one month's rent, if subscription period is more than 12 months
      - Calculate final monthly rent as per the formula given below:
      - final monthly rent = ((monthly rent subscription period) - discount amount)/subscription period
      - Return the calculated final monthly rent

    b. If not, return -1

Base Pack Name                   Monthly Rent

Silver                           350.00
Gold                             440.00
Platinum                         560.00

Note: Perform case sensitive string comparison

For testing:

- Create objects of BasePackage class
- Invoke calculate_monthly_rent() on BasePackage object
- Display the details
'''

from abc import ABC, abstractmethod


class DirectToHomeService(ABC):
    __counter = 101

    def __init__(self, consumer_name):
        self.__consumer_name = consumer_name
        self.__consumer_number = DirectToHomeService.__counter
        DirectToHomeService.__counter += 1 

    def get_consumer_number(self):
        return self.__consumer_number

    def get_consumer_name(self):
        return self.__consumer_name

    @abstractmethod
    def calculate_monthly_rent(self):
        pass


class BasePackage(DirectToHomeService):
    def __init__(self, consumer_name, base_pack_name, subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name

    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        valid_packages = {"Silver": 350.0, "Gold": 440.0, "Platinum": 560.0}
        if self.__base_pack_name not in valid_packages:
            print("Base package name is incorrect, set to Silver")
            self.__base_pack_name = "Silver"
        return valid_packages[self.__base_pack_name]

    def calculate_monthly_rent(self):
        if 1 <= self.__subscription_period <= 24:
            monthly_rent = self.validate_base_pack_name()
            if self.__subscription_period > 12:
                discount = monthly_rent  
            else:
                discount = 0.0
            final_monthly_rent = ((monthly_rent * self.__subscription_period) - discount) / self.__subscription_period
            return round(final_monthly_rent, 2)
        else:
            return -1


def main():
    consumer1 = BasePackage("Alice", "Gold", 15)
    consumer2 = BasePackage("Bob", "Diamond", 10)
    consumer3 = BasePackage("Charlie", "Silver", 25)

    consumers = [consumer1, consumer2, consumer3]
    for consumer in consumers:
        rent = consumer.calculate_monthly_rent()
        print(f"Consumer Number: {consumer.get_consumer_number()}, Name: {consumer.get_consumer_name()}")
        print(f"Base Pack: {consumer.get_base_pack_name()}, Subscription Period: {consumer.get_subscription_period()} months")
        if rent != -1:
            print(f"Final Monthly Rent: {rent}")
        else:
            print("Invalid subscription period!")
        print()


if __name__ == "__main__":
    main()
