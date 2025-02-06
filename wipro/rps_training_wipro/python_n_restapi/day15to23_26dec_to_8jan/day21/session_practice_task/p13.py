class A:

    def dA(self):
        return "A"


class B(A):

    def dB(self):
        return "B"


class C(B):

    def dC(self):
        return "C"

class D:

    def dD(self):
        return "D"

class E(A,D):

    def dE(self):
        return "E"

class F(A):

    def dF(self):
        return "F"


class G(B,F): #hybrid inh

    def dG(self):
        return "G"

b = B()
print(b.dB())
print(b.dA())

c = C() # multilevel
print(c.dC())
print(c.dB())
print(c.dA())

e = E() #multiple inheritence

print(e.dE())
print(e.dA())
print(e.dD())
# print(e.dB())

print("===============")
g = G()

print(g.dG())
print(g.dB())
print(g.dF())
print(g.dA())

