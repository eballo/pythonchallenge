#
#  http://www.pythonchallenge.com/pc/def/equality.html
#
#  One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import requests
import string
import re

alphabet_string = string.ascii_lowercase

r = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
# print(r.text)

pattern = '<!--\\D(.*?)\\D-->'
extract_text = re.compile(pattern, re.DOTALL)
filtered_text = re.findall(extract_text, r.text)[0]
print(filtered_text)

pattern = '[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'
extract_text = re.compile(pattern, re.DOTALL)
filtered_text = re.findall(extract_text, filtered_text)

print(filtered_text)
