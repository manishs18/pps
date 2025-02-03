'''
12.  Write a Python program to remove the characters which have odd index values of a 
given string.
'''

def remove_odd_index_chars(s):
    return s[::2]

input_string = input("Enter a string: ")
print(remove_odd_index_chars(input_string))
