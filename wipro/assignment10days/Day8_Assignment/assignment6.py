'''
Problem Statement

A telecom company wants to generate reports on the call details of the customers. Each customer can make multiple phone calls.

Problem Statement: The parse_customer method takes a list of Customer objects and a list of CallDetail objects.
For every customer, identify all the corresponding Call Detail objects (the customer phone number and the phone number of Call detail object have to match), 
add them to the list_of_calls of corresponding customer object and add the updated customer object to list_of_customer_calldetail_objects of Util class.

Util                                                                Customer                                    CallDetail

+ list_of_customer_calldetail_objects
+ phone_no                                                         + phone_no                                   + called_no
__init__(self)
+ parse_customer(list_of_customers,list_of_calls)                  + name                                       + duration
                                                                   + age
                                                                   + list_of_calls
                                                                   __init__(phone_no, name, age)                __init__(phoneno, called_no, duration, call_type
'''

class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.phoneno = phoneno
        self.called_no = called_no
        self.duration = duration
        self.call_type = call_type


class Customer:
    def __init__(self, phone_no, name, age):
        self.phone_no = phone_no
        self.name = name
        self.age = age
        self.list_of_calls = []  

    def add_call_detail(self, call_detail):
        self.list_of_calls.append(call_detail)


class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects = []

    def parse_customer(self, list_of_customers, list_of_calls):
        for customer in list_of_customers:
            for call in list_of_calls:
                if customer.phone_no == call.phoneno:
                    customer.add_call_detail(call)
            self.list_of_customer_calldetail_objects.append(customer)


def main():
    call1 = CallDetail("1234567890", "9876543210", 5, "Local")
    call2 = CallDetail("1234567890", "9876543211", 10, "International")
    call3 = CallDetail("9876543212", "1234567890", 3, "Local")
    call4 = CallDetail("5678901234", "4567890123", 15, "ISD")

    customer1 = Customer("1234567890", "John Doe", 30)
    customer2 = Customer("9876543212", "Jane Smith", 25)

    list_of_customers = [customer1, customer2]
    list_of_calls = [call1, call2, call3, call4]

    util = Util()
    util.parse_customer(list_of_customers, list_of_calls)

    for customer in util.list_of_customer_calldetail_objects:
        print(f"Customer: {customer.name}, Phone No: {customer.phone_no}, Age: {customer.age}")
        print("Call Details:")
        for call in customer.list_of_calls:
            print(f"  Called No: {call.called_no}, Duration: {call.duration}, Call Type: {call.call_type}")
        print()


if __name__ == "__main__":
    main()
