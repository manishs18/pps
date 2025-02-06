s1 = {1,2,4,5,3,2}

print(s1, type(s1))

s1.add(10)
print(s1)
s1.add(5)
print(s1)

s2 = {11,12,3,4,7}
s1.update(s2)
print(s1)
s2.update(s1)
print(s2)

l1 = [1,2,3,4,5,2,4]
s3 = set(l1)
print(s3)