import re, pyperclip
#TODO

date = re.compile(r'''
# case: dzien, miesiac, rok
([012][1-9])[\/\-\.]([0123][0-9])[\/\-\.]([012]\d\d\d) |
([012]\d\d\d)[\/\-\.] ([0123][0-9])[\/\-\.]([012][1-9])  # case: rok, miesiac, dzien
''', re.VERBOSE)

text = '12-23-2020  21.31-2012 13-31-2020 12-23-2012 01-03-2024 13-13-2020 2020-31-20 2022-12-12'

mo = date.findall(text)
print(mo)
matches = []

for i in date.findall(text):
    if i[0] != '':
        if int(i[0]) > 0 and int(i[0]) < 12:
            data_format = '-'.join([i[1], i[0], i[2]])
            matches.append(data_format)
    elif i[4] != '':
        if int(i[4]) > 0 and int(i[4]) < 12:
            data_format = '-'.join([i[5], i[4], i[3]])
            matches.append(data_format)





print(matches)
# (dzien - miesiac - rok)