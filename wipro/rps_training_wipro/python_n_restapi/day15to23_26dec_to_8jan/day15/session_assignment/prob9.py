'''

Q9. write a program to get the patter printed in the following 

Sample Input:

5

Sample Output:

12345
21234
32123
43212
54321

'''

n = int(input("Enter the number of rows: "))

i = 1

while i <= n:
    j = i
    while j > 0:
        print(j, end="")
        j -= 1
    j = 2
    while j <= n - i + 1:
        print(j, end="")
        j += 1
    print()
    i += 1
