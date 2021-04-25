# http://www.pythonchallenge.com/pc/return/5808.html
# user: 'huge'
# pass: 'file'

from PIL import Image

# odd event title is the only clue, and we have a image that looks like it is a composition of more than one image

im = Image.open('cave.jpg')
(w, h) = im.size

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i, j))
        if (i + j) % 2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

even.save('even.jpg')
odd.save('odd.jpg')
