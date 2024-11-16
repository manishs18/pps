#Exercise 13: Print multiplication table from 1 to 10
def mulitplicationTable(t):
    for i in range(1,t+1):
        for j in range(1, 11):
            print(i * j, end= " ")
        print()
    

s = int(input("Enter the number: "))
mulitplicationTable(s)