'''
def func1(*args):
    print(type(args), args)
    # print(args[0])
    for i in range(len(args)):
        print(args[i])
    
   # args[0] = 101

    for i in args:
        
        print(i)


func1(1,2,3,4)
func1("manish",'singh', 1)
func1(10)
'''

'''
def func1(**v):
    print(type(v))
    for name,val in v.items():
        print(name,val)


func1(v1=1,v2=23,v3=356,v4='bhima')

'''

'''
def f1(v1,v2=10, *args, **kv):
    print(v1,v2)
    print(args)
    print(kv)

f1(11,33,1,2,3,4,5,v3=10,v4=20)
'''

'''
def f():

    d1 = {1:2,3:4,5:6}
    return d1

ret = f()
print(ret)


'''

#unnamed function => lambda functions
'''
int fun1(int v1, int v2) => stack frame
{
    int a,b;
    return (a+b);
}

fun1 input args call back address
allocate mem v1,v2, a,b
return a+b to call back address


fun1(10,12)

fun()
  return "hello"


sf 


int add(int v1, int v2)
{
  return (v1+v2);
}

int div(int v1, int v2)
{
  if (v2 == 0)
    return 0
  return v1/v2;
}

inline

#define PI 3.142
#define div(x,y) x/y

int main()
{
  int r1,r2,r3;

  r1 = add(1,2);
  r2 = add (2,4);
  r3 = add(5,6);
  r4 = add(6,0);// 6/0

}
'''

def greeting():
    return "Hello"

print(greeting())

greet_me = lambda: "hello"

print(greet_me())

print(type(greet_me), id(greet_me))
greet_me = lambda: 10+20
print(greet_me(), id(greet_me))


s1 = " Manish Kumar Singh "
s2 = s1.strip().upper()
print(s2)


conStr = lambda s: s.upper().strip()
print(conStr(" MANish ")) 

p1 = lambda x, *args, **kv: print(x,args,kv)

p1(10, 1,2,3,4,5,v1=101,v2=102)