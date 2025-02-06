#
#  map(NameFun, args_list)
'''

def doubleValue(v):
    return v*v

l1 = [1,2,3]
for i in l1:
    print(doubleValue(i))

ret = map(doubleValue,l1)
print(ret, type(ret))
l2 = list(ret)
print(l2)

ret = tuple(map(doubleValue,l1))

print(ret)

print(id(l1))
l1 = list(map(doubleValue,l1))
print(l1)
print(id(l1))
l1 = [1,2,3]
l1 = list(map(lambda x: x*x,l1))
print(l1)
'''

''''
def append(ele, to=[]):
    to.append(ele)
    return to


t = append(101)
print(t, id(t))
t = append(102)
print(t, id(t))
t = append(103)
print(t)
t = append(104)
print(t,  id(t))


'''


def even(val):
    return val%2 == 0

l1 = [1,2,3,4,5,6,7,8]
b = filter(even, l1)

print(b, type(b))
print(list(b)) #[2, 4, 6, 8]
c  = list(map(even,l1))
print(c) #[False, True, False, True, False, True, False, True]