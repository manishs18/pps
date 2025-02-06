#Q7.Sum of Even and odd pos values
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_pos_sum = sum(list[i] for i in range(len(list)) if i % 2 == 0)
odd_pos_sum = sum(list[i] for i in range(len(list)) if i % 2 != 0)
print("Sum of Even Positioned Values:", even_pos_sum)
print("Sum of Odd Positioned Values:", odd_pos_sum)
