'''

Q. 
Ways to divide a binary array into sub-arrays such that each sub-array contains exactly one 1

Give an integer array arr[] consisting of elements from the set {0, 1}. The task is to print the number of ways the array can be divided into sub-arrays such that each sub-array contains exactly one 1.

Examples:

    Input: arr[] = {1, 0, 1, 0, 1}
    Output: 4
    Below are the possible ways:

        {1, 0}, {1, 0}, {1}
        {1}, {0, 1, 0}, {1}
        {1, 0}, {1}, {0, 1}
        {1}, {0, 1}, {0, 1}

    Input: arr[] = {0, 0, 0}
    Output: 0 
    
'''


def count_subarrays_with_one_one(arr):
    count_ones = arr.count(1)
    count_zeros = 0
    total_ways = 0
    
    for num in arr:
        if num == 1:
            total_ways += count_zeros
        else:
            count_zeros += 1
    
    return total_ways

arr = [1, 0, 1, 0, 1]

print(count_subarrays_with_one_one(arr))
