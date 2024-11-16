# Exercise 2: Print the Sum of a Current Number and a Previous number

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(11):
    x_sum = previous_num + i
    print(f"Current Number: {i} Previous Number: {previous_num} Sum: {x_sum}")
    previous_num = i
