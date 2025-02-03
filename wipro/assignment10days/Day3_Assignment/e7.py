# 7.   Write a program to sum seven terms of given series.
#    [Hint: use Math. Factorial(x) by import math]

import math

def sum_of_series(terms):
    total_sum = 0
    for x in range(1, terms + 1):
        total_sum += x / math.factorial(x)
    return total_sum

terms = int(input("Enter the Number to find sum seven terms: "))

result = sum_of_series(terms)
print(f"The sum of the first {terms} terms of the series is: {result:.5f}")
