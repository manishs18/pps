# Task 2: Write a pytest test case to check if an exception is raised for a function that divides two numbers.


# division_function.py
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
