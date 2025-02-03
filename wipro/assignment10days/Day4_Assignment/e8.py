'''
8. Write a Python program to get a single string from two given strings, separated by a 
space and swap the first two characters of each string. 
'''

def swap_first_2_chars(s1, s2):
    return s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(swap_first_2_chars(string1, string2))
