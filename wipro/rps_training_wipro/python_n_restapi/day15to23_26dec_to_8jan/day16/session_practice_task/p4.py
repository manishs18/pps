t1 = (range(5,8),101,102,103)
t2 = tuple(range(1,10))

print(t1,t2)
print(type(t1),type(t2))

for i in t2:
    print(i)

print(type(range(1)))

for i in t1:
    if (type(range(1))== type(i)):
        for j in i:
            print(j)
    else:
        print(i)

t3 = (1,2,3,4,5)
print(id(t3))

t3 = list(t3)
t3[3] = 101
t3 = tuple(t3)
print(t3,id(t3))

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)

print(l1)

print(t3)
# del t3[1]
print(t3)
