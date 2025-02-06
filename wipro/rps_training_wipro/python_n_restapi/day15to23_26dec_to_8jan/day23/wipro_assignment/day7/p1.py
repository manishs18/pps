import re

text = "cat, bat, rat, mat, cute, pattern"

l1 = text.split(',')
print(l1)
text1 = "bhima, shankar"
pattern = r'.at'
l2 = []
for i in l1:
    m = re.findall(pattern,i)
    if len(m)>0:
       l2.append(i)

print(l2)
# matches = re.findall(pattern, text1)

# print(matches)