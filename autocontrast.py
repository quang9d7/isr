from PIL import Image, ImageOps


im = Image.open('images/input/00042.png')
im.show()
ImageOps.autocontrast(im).show()