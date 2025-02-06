def printEle(n):
    if n == 0:
        return 1
    print(n)
    n -= 1
    printEle(n)

    return n

ret = printEle(5)
print("ret=",ret)


def febSer(n):
    if n==0:
        return 1
    n = n * febSer(n-1)
    return n


r = febSer(5)

print(r)