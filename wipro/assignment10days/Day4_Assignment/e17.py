'''
17. Write a Python program to sort a string lexicographically. 

'''

def sort_string_lexicographically(s):
    return "".join(sorted(s))

input_string = input("Enter a string: ")
print(sort_string_lexicographically(input_string))
