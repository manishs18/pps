l1 = [range(5,10), range(1,5)]
l2 = list(range(1,11,2))
a = 10
l3 = [a]
print(l3,type(l3))

print(l1,type(l1))
print(l2,type(l2))


print(l1[0])
for i in l1:
    for j in i:
        print(j)


l1 = [1,2,3,4]
l2 = [7,8,9]

l3 = l1+l2
print(l3)

l4 = l2*3
print(l4)

a=10
del a
#print(a)  #NameError: name 'a' is not defined

l1 = [1,2,4]
del l1
#print(l1[1]) #NameError: name 'l1' is not defined


l1 = [3,2,1,4,6,5]
l2 = sorted(l1)
print(l2)
print(l1)

l1.sort()
print(l1)


# def b():
#     print("b")

# class test:
#     def a(self):
#         print("a")
# t1 = test()
# t1.a()
# b()


l1 = [10,20,30]

l1.append(40)
print(l1)
l1.insert(1, 101)
print(l1)

l1.clear()
print(l1)
del l1
print(l1)