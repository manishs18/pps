#Exercise 6: Display numbers divisible by 5

def numDivBy(num):
    print("original list of num: ", num)
    for i in num:
        if i % 5 == 0:
            print("This list of num div by 5: ", i)

num = [45, 60, 34, 40]
numDivBy(num)