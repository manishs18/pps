'''
Task 1: Write a function in Python that calculates and returns the factorial of a number provided as an argument.
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
