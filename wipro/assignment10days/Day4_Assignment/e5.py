'''
5.  Write a Python program to count the number of characters (character frequency) in a 
string. 
'''

def count_char_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

input_string = input("Enter a string: ")
print(count_char_frequency(input_string))
