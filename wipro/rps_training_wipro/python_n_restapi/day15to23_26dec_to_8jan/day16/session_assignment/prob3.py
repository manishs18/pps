'''

Description
Problem Statement
You are given 3 strings A, B, and C. Your task is to find whether you can write both A and B using the characters of C. Not only that, after writing A and B from C, there should be no letter left in C.

Input Format
The first line contains A.
The second line contains B.
﻿The third line contains C.
Constraints
1 <= |A|, |B|, |C| <= 100
A, B, and C contain only uppercase English letters.
Output Format
If it is possible to write A and B from the letters of C, and there are no letters in C left after doing so, print "YES", otherwise print "NO".
Evaluation Parameters
Sample Input
ANNMMC
LLDKKD
ANNLLDKKCMMD
Sample Output

YES
Explanation

We can use all the letters of ANNLLDKKCMMD to write ANNMMC and LLDKKD. Also, C is empty after the transformation.


'''

from collections import Counter

def can_write_strings(A, B, C):
    count_A = Counter(A)
    count_B = Counter(B)
    count_C = Counter(C)
    
    combined_count = count_A + count_B

    if combined_count == count_C:
        return "YES"
    else:
        return "NO"

A = input().strip()
B = input().strip()
C = input().strip()

print(can_write_strings(A, B, C))
