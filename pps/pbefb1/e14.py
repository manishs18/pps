#Exercise 14: Print a downward half-pyramid pattern of stars
def downwardPyramid(n):
    for i in range(n+1, 0, -1):
        for j in range(i):
            print( "*", end= " ")
        print()

s = int(input("Enter the Value: "))
downwardPyramid(s)