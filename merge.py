from PIL import Image

img = Image.open("rumi.jpg")

r, g, b = img.split()

#new_img = Image.merge("RGB", (b, r, g))
new_img = Image.merge("RGB",(b,g, r))

new_img.show()
