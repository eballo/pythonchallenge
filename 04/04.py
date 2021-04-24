# http://www.pythonchallenge.com/pc/def/linkedlist.html
#
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

import urllib.request
import re

nothing = 66831
pattern = "[^and the next nothing is]([0-9]+)"
while True:
    response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(nothing))
    html = response.read().decode()
    match = re.search(pattern, html)
    if match:
        print(match.group(0))
        nothing = match.group(0)
    else:
        break

print(html)
