'''
Q. Find a partition point in array

Given an unsorted array of integers. Find an element such that all the elements to its left are smaller and to its right are greater. Print -1 if no such element exists.

Note that there can be more than one such elements. For example an array which is sorted in increasing order all elements follow the property. We need to find only one such element.

Examples :

Input :  A[] = {4, 3, 2, 5, 8, 6, 7}  
Output : 5 

Input : A[] = {5, 6, 2, 8, 10, 9, 8} 
Output : -1
'''

def find_partition_point(arr):
    left_max = -float('inf')
    right_min = float('inf')
    n = len(arr)
    
    for i in range(n):
        left_max = max(left_max, arr[i])
        right_min = min(right_min, arr[n - i - 1])
        
        if left_max < arr[i] < right_min:
            return arr[i]
    
    return -1

arr1 = [4, 3, 2, 5, 8, 6, 7]
arr2 = [5, 6, 2, 8, 10, 9, 8]

print(find_partition_point(arr1)) 
print(find_partition_point(arr2))  
