'''
13. Write a Python script that takes input from the user and displays that input back in 
upper and lower cases. 
'''


def display_upper_lower(input_str):
    print("Uppercase:", input_str.upper())
    print("Lowercase:", input_str.lower())

user_input = input("Enter a string: ")
display_upper_lower(user_input)
