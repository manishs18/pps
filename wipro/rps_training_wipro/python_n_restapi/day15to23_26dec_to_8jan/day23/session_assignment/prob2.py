# "Extract Email-Like Patterns from Text With Using Regular Expressions"


import re

# Sample text containing email addresses
text = "Contact us at manish@rps.com or support@rps.o for assistance."

# Regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all email addresses in the text
matched_emails = re.findall(email_pattern, text)

print(matched_emails)