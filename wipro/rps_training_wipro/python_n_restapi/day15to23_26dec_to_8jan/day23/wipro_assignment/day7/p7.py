def deco(f):
    return f

def f1():
    print("Hello")

f1()

s = lambda : "Hello"
print(s())

ret = deco(f1)

print(ret, type(ret))

ret()