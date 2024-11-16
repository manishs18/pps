#Exercise 7: Accept any three string from one input() call

class S:
    def v(a):
        print(a)


str1 = int(input("Enter the value of string to enter: "))
str2 = []
for i in range(str1):
    str0 = str(input("Enter the string {i + 1}: "))
    str2.append(str0)
results = " ".join(str2)
v = S.v(str2)