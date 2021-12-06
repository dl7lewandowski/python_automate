import re, pyperclip


url = re.compile(r'''

https:\/\/\.?[a-zA-Z-+_]+ \.[a-zA-Z0-9\.]{0,24} |

http:\/\/? [a-zA-Z-+_]+ \.[a-zA-Z0-9\.]{0,24} |

www?\.?[a-zA-Z0-9-+_#]+ \.[a-zA-Z0-9\.]{0,24} 




''', re.VERBOSE)

# text = '''http://www.foufos.gr
# https://www.foufos.gr
# http://foufos.gr
# http://www.foufos.gr/kino
# http://werer.gr
# www.foufos.gr
# www.mp3.com
# www.t.co
# http://t.co
# http://www.t.co
# https://www.t.co
# www.aa.com
# http://aa.com
# http://www.aa.com
# https://www.aa.com
# www.foufos
# www.foufos-.gr
# www.-foufos.gr
# foufos.gr
# http://www.foufos
# http://foufos
# www.mp3#.com'''

text = str(pyperclip.paste())

match_object = url.findall(text)
print(match_object)
print(len(match_object))
matches = []
for groups in url.findall(text):
    url = ''.join([groups])
    matches.append(url)



if len(matches) > 0:

    pyperclip.copy('\n'.join(matches))
    print('Copy to clipboard')
    print('\n'.join(matches))
else:
    print('No address urls found')