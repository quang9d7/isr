import glob
import os
from PIL import Image


paths = glob.glob('images/samples/og/*.jpg')


for path in paths:
    image = Image.open(path)
    image.thumbnail((512, 512), Image.BICUBIC)
    name = os.path.split(path)[-1]
    name = name.split('.')[0]
    image.save(os.path.join('images/samples/ds', f'{name}.png'))
