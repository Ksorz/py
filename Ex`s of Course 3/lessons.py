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

x = 'From: using the: char'
print( re.findall('^F.+:', x) ) # ['From: using the:'] Greedy
print( re.findall('^F.+?:', x) ) # ['From:'] Not greedy

x = open('mbox-short.txt')
for line in x:
    line.strip()
    if len(re.findall('^From (\S+@\S+)', line)) > 0:
        print( re.findall('^From (\S+@\S+)', line) )  # print something non-blank'@'non-blank after 'From' but not including 'From'
        print( re.findall('@([^ ]*)', line) ) # after '@' match non-blank [^ ] match any of them *
        print( re.findall('From .*@([^ ]*)', line) )
