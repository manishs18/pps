'''
Q8. Check whether a given number can be expressed as the sum of two prime number

i/p
Enter a positive integer: 34
Output
34 = 3 + 31
34 = 5 + 29
34 = 11 + 23
34 = 17 + 17
NoofWays = 4

i/p 
Enter a positive integer: 1
o/p
NoofWays=-1
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_two_primes(num):
    if num <= 1:
        return -1
    ways = []
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i) and i <= num - i:
            ways.append((i, num - i))
    if not ways:
        return -1
    for pair in ways:
        print(f"{num} = {pair[0]} + {pair[1]}")
    return len(ways)

number = int(input("Enter a positive integer: "))
result = sum_of_two_primes(number)
print("NoofWays =", result)
