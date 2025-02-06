'''
Q1.
Description
Problem Description
Write a program that takes two comma-separated lists of integers as input. For each integer N in the first list, the program needs to find the count of its occurrence called C in the second list. The program should print the N-C for each integer (one per line of output).

Sample Input 1
7,8,29
29,8,8,8,7,7,8,7
Sample Output 1
7-3
8-4
29-1
Sample Input 2
1,2,3
4,5,6,5,5,3
Sample Output 2
1-0
2-0
3-1
Note: 
The input and the output test cases should be an exact match as shown in the above example, otherwise the test cases will fail and you will be awarded No marks.
========================================================

'''

def count_occurrences(elements, target_list):
    counts = {}
    for element in elements:
        count = target_list.count(element)
        counts[element] = count
    return counts

def main():
    input1 = "7,8,29"
    input2 = "29,8,8,8,7,7,8,7"
    
    list1 = list(map(int, input1.split(',')))
    list2 = list(map(int, input2.split(',')))
    
    counts = count_occurrences(list1, list2)
    
    for number, count in counts.items():
        print(f"{number}-{count}")

if __name__ == "__main__":
    main()
