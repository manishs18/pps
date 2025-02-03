# def add(a,b):
#     return a+b


# assert add(1,2) == 'mk'


def mid(str):
    if len(str) % 2 == 0:
        return ""
    else:
        mid_index = len(str) // 2
        return str[mid_index]

input_str = input("EFDDE")
mid_let = mid(input_str)
print(mid_let)