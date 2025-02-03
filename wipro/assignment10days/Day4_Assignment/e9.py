'''
9. Write a Python program to find the first appearance of the substring 'not' and 'poor' 
from a given string, replace the whole 'not'...'poor' substring with 'good'. Return the 
resulting string. 
'''

def replace_not_poor(s):
    not_pos = s.find("not")
    poor_pos = s.find("poor")
    if not_pos != -1 and poor_pos != -1 and poor_pos > not_pos:
        s = s[:not_pos] + "good" + s[poor_pos + 4:]
    return s

input_string = input("Enter a string: ")
print(replace_not_poor(input_string))
