#Exercise 10: Read line number 4 from the following file

with open("C:/Users/mkuma/OneDrive/Desktop/New folder/pps/pps/piaoe/n6.txt", 'r') as fr:
    lines = fr.readlines()


# Check if the file has at least 4 lines
if len(lines) >= 4:
    # Print the fourth line (index 3, since indices start at 0)
    print("Line 4:", lines[3].strip())  # .strip() removes any trailing newline or whitespace
else:
    print("The file does not have 4 lines.")