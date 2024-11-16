#Exercise 5: Check if the first and last numbers of a list are the same


def firstLastNumSame(num):
    print("Original Number: " , num)
    first_num = num[0]
    last_num = num[-1]
    if first_num == last_num:
        print(f"Yes first {first_num} & last value {last_num} same ")
    else:
        print(f"No first {first_num} & last value {last_num} not same")

num = list(input("Enter Number: "))
firstLastNumSame(num)