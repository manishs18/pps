str1 = "hello World"

print(str1+" Welcome")
print(str1*2)
print(str1[3])
print(str1[1:4])
print(str1[-1])

print('f' in str1)

str2 = r"hello \n world"
print(str2)

print(len(str1))


print(str1.upper())
str1 = str1.lower()
print(str1.islower())

print("2002".isdigit())

str2 = "Java is OOPS based language. Java required JVM to run. To run java programs needs javac"

str3 = str2.replace("Java","Python")
print(str3)

str4 = str2.split(sep="Java")
print(str4,type(str4))

str2 = "Python is OOPS based language"

print(str2.find("OOPS"))
print(str2.index("OOPS"))

if(str2.find("OOPS",11) == -1):
    print("String not found")
#print(str2.index("OOPS",11)) #valueError

l1 = ['Python', 'is', "OOPS","language"]
print(l1)
str1 = " ".join(l1).upper()
print(str1)

str1 =" Python "
print(str1)
print(str1.strip())
str1 = str1.strip()

print(str1[::-1])

