from PIL import Image

img = Image.open("rumi.jpg")
img1 = Image.open("rumi.jpg")

area = (200, 10, 450, 400)

img.paste(img1, area)

img.show()
