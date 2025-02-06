'''
def func(args):
    block of sts related to functions
'''
'''
34

31 + 3 = 34
17 + 17 = 34
29 + 5 = 34
11 + 23 = 34

'''



def isPrime(val):
    if val <= 1:
        return 1 
    flag = 0

    for i in range(2,int(val/2)+1):
        if val % i == 0:
            flag = 1
            break
    
    if(flag == 1):
        return 1
    else:
        return 0





num = int(input("Enter the number: "))
count = 0

l1 = []
for i in range(2,num+1):
    if(not(isPrime(i))):
        l1.append(i)

print(l1)

for i in range(len(l1)):
    for j in range(i,len(l1)):
        if(num == (l1[i]+l1[j])):
            count += 1
            print(l1[i],l1[j])

if count>0:
    print(count)
else:
    print(-1)