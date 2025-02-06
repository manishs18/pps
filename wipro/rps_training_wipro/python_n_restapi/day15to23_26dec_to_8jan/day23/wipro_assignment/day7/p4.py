def xpow():
    for x in range(100):
        yield x**3

g1 = xpow()
print(g1)
try:
    while(True):
        print(next(g1))
except StopIteration as e:
    print("Null")

g1 = xpow()
try:
    while(True):
        print(next(g1))
except StopIteration as e:
    print("Null")