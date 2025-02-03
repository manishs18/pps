'''
Problem Statement

Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.
Sample Input  Expected Output

23,34,55      553423

'''


def create_largest_number(number_list):
    number_list = list(map(str, number_list))
    number_list.sort(key=lambda x: x*2, reverse=True)
    largest_number = ''.join(number_list)
    
    return int(largest_number)

number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)