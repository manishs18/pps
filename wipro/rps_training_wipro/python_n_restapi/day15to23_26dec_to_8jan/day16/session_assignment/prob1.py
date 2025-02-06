'''

Insert Substring
subject Codinggraphic_eq Mediumlabel Data Structures
solvesolve
Description
Problem Statement
You are given a substring sss and main string ss Your task is to insert a substring at a given position p in the main string.

Input Format
The First line contains the main string ss.
The second line contains substring sss.
The third line contains integer position p at which the substring will be inserted.
Constraints

1<=ss.length<=1000
1<=sss.length<=1000
1<=p<=100
Output Format

Print the resulting string after inserting the substring at the specified position.
Sample Input 1
 Velocity
 loc
 3
Sample Output 1
 Vellococity 
Explanation

the main string is "Velocity", the substring is "loc", and the position is 3. Inserting "loc" at position 3 in "Velocity" results in "Vellococity".

Sample Input 2
 Hello world!
 Java-
 6
Sample Output 2
 Hello Java-world!
Explanation

the main string is "Hello world!", the substring is "Java-", and the position is 6. Inserting "Java-" at position 6 in "Hello world!" results in "Hello Java-world!".

'''

main_string = input().strip()
substring = input().strip()
position = int(input().strip())


result = main_string[:position - 1] + substring + main_string[position - 1:]

print(result)
