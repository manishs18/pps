'''
Problem Statement

Write a python program to find and display the product of three positive integer values based on the rule mentioned below:
It should display the product of the three values except when one of the integer value is 7. 
In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1.
Note: Assume that if 7 is one of the positive integer values, then it will occur only once. Refer the sample I/O given below.

Sample Input
Input          Expected Output

1, 5, 3  ->    15
3, 7, 8  ->    8
7, 4, 3  ->    12
1, 5, 7  ->    -1

'''

def find_product(num1, num2, num3):
    product = 0
    nums = [num1, num2, num3]
    
    if 7 in nums:
        index = nums.index(7)
        nums = nums[index + 1:]
    
    if not nums:
        return -1
    
    product = 1
    for num in nums:
        product *= num
    
    return product

product = find_product(7, 6, 2)
print(product)  

product = find_product(3, 7, 8)
print(product)  

product = find_product(1, 5, 3)
print(product)  

product = find_product(1, 5, 7)
print(product) 