#6.   Write a Python program to create the multiplication table (from 1 to 10) of a number.

user_input = int(input("Enter the Number: "))
for i in range(1,11):
        print(f"{user_input} x {i} = {user_input*i} ")
