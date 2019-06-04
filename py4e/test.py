hand = open('mbox-short.txt')
for line in hand:
    line.strip()
    if line.find('From: ') >= 0:
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line.strip()
    if re.search('From: ', line):
        print(line)
