# http://www.pythonchallenge.com/pc/def/oxygen.html

from urllib.request import urlopen
from PIL import Image

image = Image.open(urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png"))
print(image)
size = width, height = 629, 95
#image.show()
print(size)

for x in range (0, size[0]):
    for y in range (0, size[1]):
        print(image.getpixel((x,y)))

print("--------")
y = 48

# for x in range (0, size[0]-22):
#     print(image.getpixel((x, y)))

message = ""
for x in range(0, size[0]-22, 7):
    message = message + chr(image.getpixel((x, y))[0])

print(message)
# --------
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

final_message = [105, 110, 116, 101, 103, 114, 105, 116, 121]
the_message = ""
for x in final_message:
    the_message = the_message + chr(x)
print(the_message)
