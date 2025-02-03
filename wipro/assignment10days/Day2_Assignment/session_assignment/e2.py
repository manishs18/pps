# 2. WAP to print the ASCII value of a character. [Hint : ord() function] 


char = input("Enter a character: ")
upper_string = ""
lower_string = ""

for i in char:
    if 'a' <= i <= 'z':  # Check if the character is lowercase
        upper_string += chr(ord(i) - 32)  # Convert to uppercase
    elif 'A' <= i <= 'Z':  # Check if the character is uppercase
        lower_string += chr(ord(i) + 32)  # Convert to lowercase
    else:
        print(f"'{i}' is not an alphabet character.")

if upper_string:
    print(f"Uppercase version: {upper_string}")
if lower_string:
    print(f"Lowercase version: {lower_string}")

