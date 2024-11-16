# Exercise 1: Calculate the multiplication and sum of two numbers


def multi_or_sum(n1,n2):
    p=n1*n1
    if p<=1000:
        return p
    else:
        return n1+n2
    
s=multi_or_sum(50,30)
print(s)
