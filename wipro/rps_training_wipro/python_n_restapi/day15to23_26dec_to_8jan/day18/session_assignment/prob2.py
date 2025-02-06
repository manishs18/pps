'''

Q2.
Description
Problem Statement

A god number is a positive integer whose prime factors are limited to 2,3 and 5.

Given an integer n, return the n-th God number.

Input Format

First-line contains an integer n.
Constraints

1<=n<=1000
Output Format

Return the integer as asked in the problem.
Evaluation Parameters

Sample Input
10
Sample Output
12
Explanation
[1,2,3,4,5,6,8,9,10,12] is the sequence of the first 10 god numbers.


The number **7** is **not** considered a God number because its only prime factor is **7**, which is **greater than 5**. 

### Definition of a God Number:
A **God number** (also called an **ugly number** in some contexts) is a positive integer whose **prime factors** are limited to the set `{2, 3, 5}`. In other words:
- The number must be divisible **only** by 2, 3, or 5 (or a combination of them).
- Any number that has a prime factor other than 2, 3, or 5 **cannot** be a God number.

### Why 7 is not a God Number:
- The prime factorization of 7 is simply **7**.
- Since **7** is a prime number and does not belong to the set `{2, 3, 5}`, it does not meet the criteria to be a God number.

### Examples:
| Number | Prime Factors 	| God Number? |
|--------|---------------	|-------------|
| 1      | None (1 is special) 	| Yes         |
| 2      | 2             	| Yes         |
| 3      | 3             	| Yes         |
| 4      | 2 × 2         	| Yes         |
| 5      | 5             	| Yes         |
| 6      | 2 × 3         	| Yes         |
| 7      | 7             	| **No**      |
| 8      | 2 × 2 × 2     	| Yes         |
| 9      | 3 × 3         	| Yes         |
| 10     | 2 × 5         	| Yes         |
| 12     | 2 × 2 × 3     	| Yes         |
| 14     | 2 × 7         	| **No**      |

### Key Points:
1. **7** is not divisible by 2, 3, or 5.
2. It introduces a prime factor outside the allowed set, making it ineligible to be a God number.

### Contrast with God Numbers:
A valid God number might look like:
- **6** (2 × 3): Both factors are in the set {2, 3, 5}.
- **10** (2 × 5): Both factors are in the set {2, 3, 5}.

However, a number like **7** or **14** (which is 2 × 7) is disqualified because **7** is not allowed.

### Conclusion:
**7** is not a God number because its only prime factor is **7**, which is not in the allowed set of prime factors `{2, 3, 5}`.


'''


def find_god_number(n):
    i2, i3, i5 = 0, 0, 0
    god_numbers = [1] * n
    next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 = 2, 3, 5
    next_god_number = 1
    
    for count in range(1, n):
        next_god_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        god_numbers[count] = next_god_number
        
        if next_god_number == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = god_numbers[i2] * 2
        if next_god_number == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = god_numbers[i3] * 3
        if next_god_number == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = god_numbers[i5] * 5
    
    return god_numbers[-1]

n = 10
print(find_god_number(n))  
