import re

'''
text = "An apple a day keeps the doctor away"

pat = r'apple'

m1 = re.match(pat,text)
m2 = re.search(pat,text)
m3 = re.findall(pat, text)

print(m1, type(m1))
print(m2, type(m2))
print(m3, type(m3))


pattern = r'\d'
replacement = 'X'
text = 'Today is 2022-01-15'

# Replace all digits with 'X'
new_text = re.sub(pattern, replacement, text)
print("Replaced text:", new_text)


t1 = "This is a Python Programming class"

p1 = r'class'

l1 = re.split(p1,t1)

print(l1)
print(t1.split('class'))
'''

'''
pattern = r'(\w+), (\w+), (\W+)'
text = 'Doe, John'
text1 = '2005, 45, #$%'

# Extract first and last name using groups
match_result = re.match(pattern, text1)
print(match_result)
print(len(match_result.group(0)))
if match_result:
    last_name = match_result.group(1)
    first_name = match_result.group(2)
    print("Last name:", last_name)
    print("First name:", first_name)
else:
    print("No Match Found")
    
'''


# Sample text containing email addresses
text = "Contact us at info@example.com or support@example.o for assistance."

# Regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all email addresses in the text
matched_emails = re.findall(email_pattern, text)

print(matched_emails)
