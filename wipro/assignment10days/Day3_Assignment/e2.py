# 2.   Write a Python program to get the Fibonacci series between 0 to 50

a = 50 
fib = [0,1]
for i in range(a+1):
        next_fib = fib[-1] + fib[-2]
        if next_fib >= 50:
                break
        fib.append(next_fib)
print(fib)