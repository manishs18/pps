#Exercise 8: Print the following pattern

def patternTriangle(a):
    for i in range(1, a+1):
        for r in range(i):
            print(i, end=" ")
        print("\n")


num = int(input("enter the num: "))
num2 = patternTriangle(num)