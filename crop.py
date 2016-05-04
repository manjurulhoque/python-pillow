from PIL import Image

img = Image.open("rumi.jpg")

area = (200, 10, 450, 400)
cropped_img = img.crop(area)

cropped_img.show()
