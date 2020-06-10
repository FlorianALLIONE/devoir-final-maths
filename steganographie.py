from PIL import Image


im = Image.open("python_img.png")

width, height = im.size

r, g, b, a = im.split()

redList = list(r.getdata())
greenList = list(g.getdata())
blueList = list(b.getdata())

print(redList)
print(greenList)
print(blueList)

#im.show()