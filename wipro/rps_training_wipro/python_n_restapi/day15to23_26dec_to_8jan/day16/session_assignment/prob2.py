'''

Description
Problem Statement

Given a string str, Your task here is to re-order the string using the following algorithm:

Pick the smallest character from str and append it to the result.
Pick the smallest character from str which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from str and append it to the result.
Pick the largest character from str which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from str.
Input Format

Single line containing a string S
Constraints

1 <= S.length <= 500
S contains only lower case English letters
Output Format

Single line containing re-ordered string
Evaluation Parameters

Sample Input
sat
Sample Output
ast
Explanation
The word "sat" becomes "ast" after re-ordering it with the mentioned algorithm.

'''

def reorder_string(s):
    s = sorted(s)
    result = []

    while s:
        if s:
            result.append(s.pop(0))
        
        while s and s[0] > result[-1]:
            result.append(s.pop(0))

        if s:
            result.append(s.pop(-1))
        
        while s and s[-1] < result[-1]:
            result.append(s.pop(-1))

    return ''.join(result)

input_str = input().strip()

print(reorder_string(input_str))
