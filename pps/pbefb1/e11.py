#Exercise 11: Get each digit from a number in the reverse order.



def reverseOrder(n):
    print("Orginal Number: ", n)
    print("Reverse Order Number: ", end="")
    while n > 0:
        digit =  n % 10
        n = n // 10
        print(digit, end = " ")
    print()


s = int(input("Enter the value: "))
r = reverseOrder(s)
