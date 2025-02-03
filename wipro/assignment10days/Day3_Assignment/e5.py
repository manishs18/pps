# 5.   Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

def calculate_sum_and_average():
    total = 0
    count = 0

    while True:
        try:
            number = int(input("Enter a number (0 to finish): "))
            if number == 0:
                break
            total += number
            count += 1
        except ValueError:
            print("Please enter a valid integer.")

    if count > 0:
        average = total / count
        print(f"Sum of numbers: {total}")
        print(f"Average of numbers: {average:.2f}")
    else:
        print("No numbers entered.")

calculate_sum_and_average()



            

# import keyword

# a = keyword.kwlist
# b = keyword.softkwlist

# print(a, b)
        

