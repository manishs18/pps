n = int(input("N: "))
i = 1
while(i<=n*n):
    if(i%n==0):
        print(i)
    else:
        print(str(i)+"*",end="")
    i+=1



# n=5

# 1*2*3*4*5
# 6*7*8*9*10
