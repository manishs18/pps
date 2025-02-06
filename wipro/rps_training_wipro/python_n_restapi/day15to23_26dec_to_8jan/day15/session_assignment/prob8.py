'''
Q8. write a program to get the patter printed in the following 

Sample Input:

5

Sample Output:

*
**
***
****
*****
****
***
**
*

'''


n = int(input("Enter the number of rows: "))

i = 1

while i <= n:
    print("*" * i)
    i += 1

i = n - 1

while i > 0:
    print("*" * i)
    i -= 1
