import urllib.request, urllib.parse, urllib.error
import re
_adress = input('enter:')
fhand = urllib.request.urlopen(_adress)# Parse the URL. what server to talk to, what document to retrieve, HTTP version, GET request, all that stuff. (Almost the same as open(file))
_count = 0
for line in fhand:
    line = line.decode().strip()
    _urls = re.findall('href="(\S+mail?\S+)"', line)
    if len(_urls) > 0:
        for i in _urls:
            _count += 1
            print(i + '\n')
print(_count)


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

_adress = input('enter:')
fhand = urllib.request.urlopen(_adress).read()

sp = BeautifulSoup(fhand, 'html.parser')
tags = sp('a')
for tag in tags:
    print(tag.get('href', tag))
