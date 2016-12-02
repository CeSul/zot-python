from PIL import Image
import pyft 

input  ='/home/rcf-proj/ess/csul/image_benchmark/zot_images'
output ='/staging/ess/csul/image_benchmark/output/output_nodb'

def open_image(filename):
    return Image.open(filename)
def process_image(image):
    return pyft.img_fft(image)
def save_image(img_to_save,image_name):
    img_to_save.save(image_name)

for i in range(0,10000):
   image_in  = 'array%04d.png' %i
   image_out = '%s/out_array%04d.png'   %(output, i)
   filename='%s/%s' %(input,image_in)

   im = open_image(filename)
   outfile = process_image(im)
   save_image(im,image_out)
# time python runtask_nodb.py
#
# real	0m51.893s
# user	0m49.982s
# sys	0m1.626s
