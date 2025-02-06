i1=10
i2=20
l1 = []
for i in range(10,110,10):
    print(i)
    l1.append(i)


print(l1,type(l1))

l2 = [i for i in range(10,110,10)]
print(l2)
l2.clear()
for i in range(1,11):
    if i%2 != 0:
        l2.append(i)
print(l2)

l3 = [i for i in range(1,20) if i%2 !=0]+[i for i in range(1,20) if i%2 ==0]
print(l3)

str1 = 'apple'
#o/p 'a***e'

o = 'aeiou'

l4 = [x if x in o else '*' for x in str1]

t1 = (x if x in o else '*' for x in str1)

print(l4)
print(next(t1))
print(next(t1))
print(next(t1))