# 4.   Write a Python program to check whether an alphabet is a vowel or consonant

ch = input("Enter the alphabetic Word: ")
v = 'aeiouAEIOU'
if ch in v:
    print(F"{ch} is Vowel ")
else:
    print(f"{ch} is Consonent ")

