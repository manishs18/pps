#Exercise 5: Accept a list of 5 float numbers as an input from the user


# class AcceptListFiveFloatNummber:
#     def __init__(self, a):
#         print(a)

# n = int(input("Enter the Number: "))
# while True:
#     if n<0:
#         print("pls enter greater than 0: ")
#     else:
#         s = list(input("Enter the List Value: "))
# o = AcceptListFiveFloatNummber(s)


numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)
