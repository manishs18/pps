#3. WAP to find difference of two small integers (not greater than 10) without using minus (-) operator. [Hint : Use ^ operator] 

a = int(input("Enter the first integer (<=10): "))
b = int(input("Enter the second integer (<=10): "))
difference = a + (~b + 1)  # Used bitwise NOT (~) and add 1 to get negative equivalent
print(f"The difference is: {difference}")
