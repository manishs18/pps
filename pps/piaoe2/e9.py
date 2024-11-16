#Exercise 9: Check file is empty or not

import os

file_size = os.stat("C:/Users/mkuma/OneDrive/Desktop/New folder/pps/pps/piaoe/n6.txt").st_size

if file_size == 0:
    print("Empty file.")
else:
    print("File has some data.")