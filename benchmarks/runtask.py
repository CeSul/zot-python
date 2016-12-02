from PIL import Image
import numpy as np
import pyft as pt


data = np.array(Image.open('../zot_images/array0000.png'))

output = pt.img_fft(data)
output.save('output.png')
