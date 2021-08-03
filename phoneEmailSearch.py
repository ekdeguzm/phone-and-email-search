#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?     # area code (optional)
(\s|-)             # first reparator
\d\d\d             # first 3 digits
-                  # separator
\d\d\d\d           # last 4 digits
(((ext(\.)?\s)|x)   # extension (optional)
(\d{2,5}))?        # extention number part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# something.+?_@something.com/edu/net/gov

[a-zA-Z0-9_.+]+          # name part
@                       # @ symbol
[a-zA-Z0-9_.+]+          # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    

print(allPhoneNumbers)
print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)


