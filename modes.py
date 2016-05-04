from PIL import Image
from PIL import ImageFilter

img = Image.open("rumi.jpg")
#for CMYK..
#CMYK stands for C=cyan, M=megenta, Y=yellow, K=black
#bw = img.convert('CMYK')

#L stands for Luminent
#bw = img.convert('L')

#bw.show()

#for image blur effect
#blur = img.filter(ImageFilter.BLUR)

#blur.show()
#only edges of an image
edges = img.filter(ImageFilter.FIND_EDGES)

edges.show()

