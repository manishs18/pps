'''
18.  Write a Python program to remove a newline in Python. 
'''

def remove_newline(s):
    return s.replace("\n", "")

input_string = input("Enter a string with a newline: ")
print(remove_newline(input_string))
