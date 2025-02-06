import functools
l1 = []
for i in range(1,5):
    for j in range(2,6,2):
        l1.append(i*j)
print(l1)

l2 = [x*y for x in range(1,5) for y in range(2,6,2) ]

print(l2)

l5 = []
def f(x):
    return x**3

for i in range(1,5):
    l5.append(f(i))

print(l5)


s = lambda x: x**3

l3 = [s(x) for x in range(1,5)]
print(l3)


d1 = {'x':1,'y':2,'z':5}
d2 = {'a':3,'b':4}

d3 = {k:v for d in [d1,d2] for k, v in d.items()}
print(d3)

d4 = {**d1,**d2}
print(d4)