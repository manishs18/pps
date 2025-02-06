'''
Q11

rotate array every kth element
i/p
No of Elememts in the list = 9
Enter the elements

1 2 3 4 5 6 7 8 9

i/p
k= 3

o/p
3 2 1 6 5 4 9 8 7


k=6
6 5 4 3 2 1 9 8 7

k=4
4 3 2 1 8 7 6 5 9


'''


def rotate_array(arr, k):
    rotated = []
    for i in range(0, len(arr), k):
        rotated.extend(arr[i:i + k][::-1])
    return rotated

n = int(input("No of Elements in the list: "))
arr = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter k: "))
print("Rotated Array:", rotate_array(arr, k))
