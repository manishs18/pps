'''
Problem Statement

A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are: 3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input        Expected Output

'3523014'           ['5230', '23014', '523', '352']

'''
def find_ten_substring(num_str):
    try:

        if not isinstance(num_str, str) or not num_str.isdigit():
            raise ValueError("Input must be a string containing only digits.")

        ten_substrings = []
        length = len(num_str)

 
        for i in range(length):
            current_sum = 0
            substring = ""
            

            for j in range(i, length):
                current_sum += int(num_str[j])
                substring += num_str[j]
                
                if current_sum == 10:
                    ten_substrings.append((substring, i)) 
                elif current_sum > 10:
                    break  

        ten_substrings.sort(key=lambda x: (-len(x[0]), x[1]))

        return [x[0] for x in ten_substrings]

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


num_str = "3523014"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print("10-substrings are:", result_list)




