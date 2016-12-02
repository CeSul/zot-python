from PIL import Image
import numpy as np
import PIL_test as pt


data = np.array(Image.open('./zot_images/array000.png'))

output = pt.img_fft(data)
output.save('output.png')
