"""
4. Write a Python program to check if a string contains all letters of the alphabet.  
"""
user_input = input("Enter the value as own: ").lower() 
alphabet = "abcdefghijklmnopqrstuvwxyz" 

contains_all_letters = True

for letter in alphabet:
    if letter not in user_input: 
        contains_all_letters = False
        break

if contains_all_letters:
    print("Yes, all letters of the alphabet are present in the input!")
else:
    print("No, the input does not contain all letters of the alphabet.")
