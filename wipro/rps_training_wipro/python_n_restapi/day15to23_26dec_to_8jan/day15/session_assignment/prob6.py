'''
Q6. Write a program to Count number of ways to divide a given number in 4 parts.

Input:  

  5
Output: 1

Input:  
6
Output: 2

Input:  
  8
Output: 5
'''
'''
def count_ways_to_divide(n):
    count = 0
    a = 1
    while a <= n:
        if n % a == 0:
            count += 1
        a += 1
    
    return count
        
n = int(input("Enter the number: "))
result = count_ways_to_divide(n)
print(f"Number of ways to divide {n} into 4 parts: {result}")

'''



def countWays(n):

    counter = 0 


    for i in range(1, n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    if (i + j + k + l == n):
                        counter += 1
    return counter


n =int(input("enter n:"))
print (countWays(n))

