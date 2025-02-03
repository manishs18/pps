# 8. Take a 5 digit number as input and reverse it without using loop

num = (input("Enter a 5-digit number: "))
reversed_num = int(num[::-1]) # Use slicing to reverse the string
print(f"The reversed number is: {reversed_num}")



# def findProduct(num1,num2,num3):
#     product = 0
    
#     if (num1,num2,num3) is not 7:
#         print(num1*num2*num3)
#     elif (num1) is 7:
#         print(num2*num3)
#     elif (num2) is 7:
#         print(num1*num3)
    

#     return product


# product = findProduct(7,6,2)
# print(product)