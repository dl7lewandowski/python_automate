import pyperclip, re

# regex for phone numbers
phone_regex = re.compile(r'''
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # seprator
(\d{3}) # first 3 digit 
(\s|-|\.) # separator
(\d{4}) # last 4 digits 
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
''', re.VERBOSE)

# regex for email

email_regex = re.compile((r'''
[a-zA-Z0-9.%_+-]+   # username
@ # symbole
[a-zA-Z0-9.-]+ # domain name
\.[a-zA-Z0-9.-]{2,4} # dot something
'''), re.VERBOSE)

# FInd matches in clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[0], groups[2], groups[4]])

    if groups[5] != '':
        phone_num += ' x' + groups[5]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups)

match_object = email_regex.findall(text)

if len(matches) > 0:

    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found')
