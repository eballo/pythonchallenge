# Decrypted message:
# i hope you didnt translate it by hand. thats what computers are for. doing it
# in by hand is inefficient and thats why this text is so long. using
# string.maketrans() is recommended. now apply on the url.
#
# http://www.pythonchallenge.com/pc/def/maketrans.html
# http://www.pythonchallenge.com/pc/def/ocr.html
import requests
import string
import re

alphabet_string = string.ascii_lowercase

r = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
# print(r.text)

pattern = '<!--\\D(.*?)\\D-->'
extract_text = re.compile(pattern, re.DOTALL)
filtered_text = re.findall(extract_text, r.text)[1]
print(filtered_text)
secret_message = ""
for character in filtered_text:
    if character.lower() in alphabet_string:
        secret_message = secret_message + character

print("-------------------------------")
print(secret_message)
