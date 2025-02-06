# Q3. Find  the  sum  of  series  1+4-9+16-25+36

n = 1+4-9+16-25+36
# int(input("Enter the number of terms: "))

i = 1
sum_series = 0
while i <= n:
    term = i * i 
    if i % 2 == 0:
        sum_series += term  
    else:
        sum_series -= term 
    i += 1  
print("Sum of the series:", sum_series)
