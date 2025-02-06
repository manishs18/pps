# "Extract Email-Like Patterns from Text Without Using Regular Expressions"


# Sample text containing email addresses
text = "Contact us at manish@wipro.com or support@wipro.o for assistance."

# Simple method to find email-like patterns
words = text.split()
emails = [word.strip('.,') for word in words if '@' in word and '.' in word]

# Print the matched email-like addresses
print(f"Matched email addresses: {emails}")
