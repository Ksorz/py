# 11.1 - Regular Expressions
hand = open('mbox-short.txt')
for line in hand:
    line.strip()
    if line.find('From: ') >= 0: # Variable name.method
        print(line)
import re
hand = open('mbox-short.txt')
for line in hand:
    line.strip()
    if re.search('^X-\S+Type', line): # Library name.function
        print(line)
# 11.2 - Extracting Data
import re
x = 'My 2 favorite numbers are 49 and 114'
y = re.findall('[0-9]+', x)
print(y)
