import re # Regular expression library
re.search('^From: ', line) # Is 'From:' in the begining ^ of the line? --T/F--
x = re.findall('[0-9]+', line) # Extracting more than one + things that matches [0-9] from variable line. Returns    --LIST-- with zero or more matches as --STRING-- type.

^           # Matches the beginning of a line
$           # Matches the end of the line
.           # Matches any character
\s          # Matches whitespace
\S          # Matches any non-whitespace character
*           # Repeats a character zero or more times
*?          # Repeats a character zero or more times (non-greedy)
+           # Repeats a character one or more times
+?          # Repeats a character one or more times (non-greedy)
[aeiou]     # Matches a single character in the listed set
[^XYZ]      # Matches a single character not in the listed set
[a-z0-9]    # The set of characters can include a range
(           # Indicates where string extraction is to start
)           # Indicates where string extraction is to end
# https://docs.python.org/3/howto/regex.html   (more information)

'^X.*:' # 'X' at the begining, followed by ANY NUMBER * of ANY . caracters, followed by ':' a colon (^.* are special caracters) T/F
'^X-\S+:' # 'X-' at the begining, followed by \S ANY NON-BLANK caracter, followed by a ':' T/F

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) ) # 'data.pr4e.org' - host; 80 - port (tuple)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # encode coverts Unicode to bytes (UTF-8 by default). When we send it we --encode-- it
mysock.send(cmd) # Sending bytes (cmd)
while True:
    data = mysock.recv(512) # variable data is bytes
    if (len(data) < 1):
        break
    encdata = data.decode() # decode converts UTF-8 or ASCII (by default ()) to Unicode (encdata). When we receive it we --decode-- it
    print(encdata)
mysock.close()
