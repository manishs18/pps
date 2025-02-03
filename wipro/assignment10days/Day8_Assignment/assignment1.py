'''
Problem Statement

Write a Python program to generate tickets for online bus boolong, based on the class diagram given below.

          Ticket

- passenger name
- ticket d
- source
- destinabon 
- counter -> static

__init__(passenger name, source, destination)
+ validate source destination()
+ generate ticket()
+ get ticket id()
+ get passenger_name()
+ get source()
+ get destination()

Method description:

1. Initialize static variable counter to 0
2. validate source destination(): Validate source and destination source must always 
   be Delhi and destination can be either Mumbal, Chennai, Pune or Kolkata. If both are valid, return true. 
   Else return false
3. generate ticket():

   1. Validate source and destination 2.
   2. If valid, generate ticket id and assign it to attribute, ticket id. 
      Ticket id should be generated with the first letter of source followed by first letter of 
      destination and an auto-generated value starting from 01 (Ex: DMOI. DP02, DK10,0C11)
    3. Else, set ticket id as None

Note: Perform case insensitive string comparison

For testing:

Create objects of Ticket class
Invoke generate ticket() method on Ticket object
Display ticket id, passenger name, source, destination
In case of error/invalid data, display appropriate error message
'''

class Ticket:
    counter = 0  

    def __init__(self, passenger_name, source, destination):
        self.passenger_name = passenger_name
        self.source = source
        self.destination = destination
        self.ticket_id = None

    def validate_source_destination(self):
        valid_destinations = ["Mumbai", "Chennai", "Pune", "Kolkata"]
        if self.source.lower() == "delhi" and self.destination.title() in valid_destinations:
            return True
        return False

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1  
            self.ticket_id = f"{self.source[0].upper()}{self.destination[0].upper()}{Ticket.counter:02}"
        else:
            self.ticket_id = None

    def get_ticket_id(self):
        return self.ticket_id

    def get_passenger_name(self):
        return self.passenger_name

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination


def main():
    tickets = [
        Ticket("John Doe", "Delhi", "Mumbai"),
        Ticket("Jane Smith", "Delhi", "Chennai"),
        Ticket("Alan Walker", "Delhi", "Pune"),
        Ticket("Invalid User", "Bangalore", "Mumbai"), 
        Ticket("Another Invalid User", "Delhi", "Paris"),  
    ]

    for ticket in tickets:
        ticket.generate_ticket()
        if ticket.get_ticket_id():
            print(f"Ticket ID: {ticket.get_ticket_id()}, Passenger Name: {ticket.get_passenger_name()}, Source: {ticket.get_source()}, Destination: {ticket.get_destination()}")
        else:
            print(f"Error: Invalid source or destination for Passenger {ticket.get_passenger_name()}")

if __name__ == "__main__":
    main()



