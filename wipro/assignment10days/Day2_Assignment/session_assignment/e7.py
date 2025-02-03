# 7. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn 


n = input("Enter an integer (n): ")
nn = n * 2
nnn = n * 3
result = int(n) + int(nn) + int(nnn)
print(f"The result of n + nn + nnn is: {result}")
