import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter URL: ')
_count = input('Enter count: ')
_position = input('Enter position: ')
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html').read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print([tag.contents[i] for i in range(len(_count))])


for tag in tags:
    print(tag.contents[0])
