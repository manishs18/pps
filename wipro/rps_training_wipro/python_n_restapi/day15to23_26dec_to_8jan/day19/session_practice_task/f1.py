'''
handling file operations

'''

f1 = open("file1.txt", "r")

#print(f1, type(f1))
content = f1.read()
print(content)

f1.close()