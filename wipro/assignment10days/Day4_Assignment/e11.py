'''
11.  Write a Python program to change a given string to a new string where the first and 
last chars have been exchanged. 
'''

def swap_first_and_last_char(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]

input_string = input("Enter a string: ")
print(swap_first_and_last_char(input_string))
