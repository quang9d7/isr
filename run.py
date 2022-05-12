import os
import glob
from ISR.models import RDN, RRDN
import numpy as np
from PIL import Image
import tensorflow as tf


gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


input_dir = 'images/input/'
output_dir = 'images/output/'

paths = [path for path in glob.glob(input_dir+'*.png')]
model = RRDN(weights='gans')
for path in paths:
    image = np.array(Image.open(path))
    sr_images = model.predict(image)
    name = os.path.split(path)[-1]
    name = name.split('.')[0]
    Image.fromarray(sr_images).save(os.path.join(output_dir, f'{name}.png'))
