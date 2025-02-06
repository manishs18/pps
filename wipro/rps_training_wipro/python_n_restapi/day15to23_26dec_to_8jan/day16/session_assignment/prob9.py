'''
Q9.Program to find nth number made of given four digits 1, 4,6 and 9 as the only digits..

Input Format:

The First Line Of Input Contains T no of test cases
The Second Line Of Input Contains N as input taken.

Output Format:
Print the number of digits in the nth number .

Constraints:

1<=T<=100
1<=N<=100

Examples:

Input : 6
Output : 14
'''


from itertools import product

def nth_number(t, n_list):
    digits = [1, 4, 6, 9]
    max_n = max(n_list)
    numbers = []
    for length in range(1, 10): 
        numbers.extend(int("".join(map(str, p))) for p in product(digits, repeat=length))
        if len(numbers) >= max_n:
            break
    numbers.sort()
    return [len(str(numbers[n - 1])) for n in n_list]

t = int(input("Enter number of test cases: "))
n_list = [int(input("Enter N: ")) for _ in range(t)]
result = nth_number(t, n_list)
print("Output:", *result)
