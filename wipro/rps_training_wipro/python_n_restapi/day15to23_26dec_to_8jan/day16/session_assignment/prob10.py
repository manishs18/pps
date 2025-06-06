'''
Q10.
Problem Statement:
Given an unsorted array a of size N of non-negative integers, 
find a continuous sub-array which adds to a given number sum.

Input Format:
The first line contains an integer, denoting the size of the array. 
The second line contains integers denoting the elements 
of the array.
The last line contains an integer, denoting the sum. 

Constraints
1<= n<=100
1<=arr<= 1000, where arr is the ith element of the array.
1<= n<=100000

Output Format:
The output line contains integers denoting the indexes.

TESTCASE 1:
Input:
7
[1, 4, 0, 0, 3, 10, 5]

sum = 7
Output: 
Sum found between indexes 1 and 4

TESTCASE 2:
Input:
2
[1, 4]
sum = 0
Output: 
No subarray found
'''


def find_subarray_with_sum(arr, target_sum):
    start, curr_sum = 0, 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target_sum and start <= end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target_sum:
            return f"Sum found between indexes {start} and {end}"
    return "No subarray found"

n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
target_sum = int(input("Enter target sum: "))
print(find_subarray_with_sum(arr, target_sum))
