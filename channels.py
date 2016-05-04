from PIL import Image

img = Image.open("rumi.jpg")
# split into RGB
r, g, b = img.split()

r.show()
g.show()
b.show()
