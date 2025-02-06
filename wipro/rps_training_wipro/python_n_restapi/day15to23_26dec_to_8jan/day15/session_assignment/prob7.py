'''
Q7. write a program to get the patter printed in the following 
Sample Input1:
5
Sample Output1:
      *
     * *
    * * *
   * * * *
  * * * * *
   * * * *
    * * *
     * *
      *
          
'''

n=5
i=1
while i<=n:
    print(" " * (n-i) + "*" * (2 * i -1))
    i +=1
i = n - 1
while i>0:
    print(" " * (n-i) + "*" * (2*i-1))
    i -=1
