'''
Task 2: Create a list comprehension in Python to generate squares of even numbers between 1 to 10.
'''
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Squares of even numbers:", squares)
