'''
Problem Statement

A telecom company wants to generate reports on the call details of the customers.
The data of each call detall include the phone number which made the call, phone number which was called, 
duration of the call and the type of call. Data of such calls are provided as a list of comma separated string.

Problem Statement:

Complete the CallDetail dass with necessary attributes Complete the logic inside the parse customer() method of the Util Class.
This method should accept a list of string of the call detalls and convert it into a list of CallDetall object and assign this list as a value to the attribute of the Util
                
Util                                                  CallDetail

+list_of call_objects                                 -phoneno
__init__(self)                                        -called_no
+ parse customerlist_of_call_string)                  -duration
                                                      -call_type
                                                      __init__(phoneno, called no, duration, call type)

The Util class

'''

class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.phoneno = phoneno
        self.called_no = called_no
        self.duration = duration
        self.call_type = call_type


class Util:
    def __init__(self):
        self.list_of_call_objects = []

    def parse_customer(self, list_of_call_string):
        for call_string in list_of_call_string:
            details = call_string.split(",")
            if len(details) == 4:
                phoneno = details[0].strip()
                called_no = details[1].strip()
                duration = details[2].strip()
                call_type = details[3].strip()
                
                call_detail_obj = CallDetail(phoneno, called_no, duration, call_type)
                self.list_of_call_objects.append(call_detail_obj)


def main():
    call_data = [
        "1234567890, 9876543210, 5, Local",
        "1234567891, 9876543211, 10, International",
        "1234567892, 9876543212, 2, Local",
        "1234567893, 9876543213, 15, ISD",
    ]

    util = Util()
    util.parse_customer(call_data)

    for call in util.list_of_call_objects:
        print(f"Phone No: {call.phoneno}, Called No: {call.called_no}, Duration: {call.duration}, Call Type: {call.call_type}")


if __name__ == "__main__":
    main()
