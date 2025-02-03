'''
15.  Write a Python function to get a string made of 4 copies of the last two characters of a 
specified string (length must be at least 2). 
'''

def last_2_chars_repeated(s):
    return s[-2:] * 4 if len(s) >= 2 else ""

input_string = input("Enter a string: ")
print(last_2_chars_repeated(input_string))
