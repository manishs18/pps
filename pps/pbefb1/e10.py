#Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.

def mergeTwoList(a,b):
    print("Original list1: ", a)
    print("Original list2: ", b)
    odd_l1 = [i for i in a if i % 2 != 0]
    even_l2 = [j for j in b if j % 2 == 0]
    l1l2= odd_l1 + even_l2
    return l1l2

l1 = list(map(int, input("Enter List1 value: ").split()))
l2 = list(map(int, input("Enter List2 value: ").split()))
l3 = mergeTwoList(l1,l2)
print(l3)