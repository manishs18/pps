d1 = {10001:101,10002:102}
d2 = dict()
print(type(d1),type(d2))

print(d1)

d1[10003] = 103
print(d1)

d1[10002] = 501
print(d1)

d1[1001] = 45
print(d1)
d1['manish'] = 10001
print(d1)

#print(d1[1002])

emp = {10: ['abc1',25,100001,"M"],
       11: ['abc2',25,100056,"F"],
       12: ['abc3',26,100011,"M"]}

emp1 = {12: {'Name':'Bhima','Age':45,"Sal":100001},
        13: {'Name':'Manish','Age':25,"Sal":10001}}

print(emp[11])

print(emp1[13])

d1 = {10001:101,10002:102}
d2 = {10004:104,10002:105}

d1.update(d2)
print(type(d1),d1)
d1.pop(10002)
print(type(d1),d1)


for k,v in d1.items():
    print(k,v)


for k,v in emp.items():
    print(k,v)
    for i in v:
        if( i == 'M'):
            v[3] = 'X'
            emp[k] = v

print(emp)


emp[13] = ['abc4',22,1001,'M']
print(emp)


for k,v in emp1.items():
    print(k,v)