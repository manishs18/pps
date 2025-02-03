'''
Problem Statement

Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors. 
Handle the possible errors in the code written inside the function.

Sample Input           Expected Output

16                     120

'''


def find_smallest_number(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    def count_divisors(number):
        count = 0
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                if i * i == number:
                    count += 1
                else:
                    count += 2 
        return count

    smallest = 1
    while True:
        if count_divisors(smallest) == n:
            return smallest
        smallest += 1

num = 16
try:
    print("The number of divisors:", num)
    result = find_smallest_number(num)
    print(f"The smallest number having {num} divisors is: {result}")
except ValueError as e:
    print(e)