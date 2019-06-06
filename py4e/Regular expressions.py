import re
re.search('^From: ', line) # ^ caret caracter means is 'F' in the BEGINING of the line? --T/F--
x = re.findall('[0-9]+', line) # Extracting more than one + things that matches [0-9] from variable line. Returns    --LIST-- with zero or more matches as --STRING-- type.
^ # Starts with; ^X- means starts with 'X' followed by '-'...
. # is ANY caracter
* # 0 or more times >= 2 (asterisk)
+ # 1 or more times >= 1
? # Dont be greedy (shortest with, longest without)
[0-9]
\S # any non whitespace caracter
^X.*: # 'X' at the begining, followed by ANY NUMBER * of ANY . caracters, followed by ':' a colon (^.* are special caracters) T/F
^X-\S+: # 'X-' at the begining, followed by \S ANY NON-BLANK caracter, followed by a ':' T/F
