#Q6.Sum of Even and odd values
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_sum = sum(x for x in list if x % 2 == 0)
odd_sum = sum(x for x in list if x % 2 != 0)
print("Sum of Even Values:", even_sum)
print("Sum of Odd Values:", odd_sum)
