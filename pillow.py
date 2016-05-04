from PIL import Image

img = Image.open("rumi.jpg")

print(img.size)
print(img.format)

img.show()
