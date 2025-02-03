'''
7. Write a Python program to get a string from a given string where all occurrences of its 
first char have been changed to '$', except the first char itself. 
'''
def change_char_to_dollar(s):
    first_char = s[0]
    return first_char + s[1:].replace(first_char, '$')

input_string = input("Enter a string: ")
print(change_char_to_dollar(input_string))
