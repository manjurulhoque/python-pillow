from PIL import Image

img = Image.open("rumi.jpg")

square = img.resize((250, 450))

square.show()

#flip = img.transpose(Image.FLIP_LEFT_RIGHT)
rotate = img.transpose(Image.ROTATE_270)

rotate.show()
