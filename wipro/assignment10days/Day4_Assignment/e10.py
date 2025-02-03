'''
10. Write a Python program to remove the nth index character from a nonempty string. 
'''


def remove_nth_char(s, n):
    return s[:n] + s[n+1:]

input_string = input("Enter a string: ")
n = int(input("Enter the index to remove: "))
print(remove_nth_char(input_string, n))
