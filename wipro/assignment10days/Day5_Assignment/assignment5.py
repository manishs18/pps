# Problem statement

# Multiplication of two matrix


def mat1():
    r = int(input("Enter no. of rows: "))
    c = int(input("Enter no. col: "))
    lst1 = []

    for i in range(r):
        lst = []
        for j in range(c):
            lst.append(int(input("Enter the value: ")))
        lst1.append(lst)
    return lst1
def mat2():
    r = int(input("Enter no. of rows: "))
    c = int(input("Enter no. col: "))
    lst2 = []

    for i in range(r):
        lst = []
        for j in range(c):
            lst.append(int(input("Enter the value: ")))
        lst2.append(lst)
    return lst2
obj_mat1 = mat1()
obj_mat2 = mat2()

if len(obj_mat1[0]) != len(obj_mat2):
    print("mat1 & mat2. are not not same.....")

obj_mat3 = [[0 for _ in range(len(obj_mat2[0]))] for _ in range(len(obj_mat1))]

for i in range(len(obj_mat1)):
    for j in range(len(obj_mat2[0])):
        for k in range(len(obj_mat2)):
            obj_mat3[i][j] += obj_mat1[i][k] * obj_mat2[k][j]

print("Resultant Matrix after Multiplication:")
for row in obj_mat3:
    print(row)

