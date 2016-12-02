from PIL import Image
import pyft
from StringIO import StringIO
import lmdb

input  ='/home/rcf-proj/ess/csul/image_benchmark/zot_db'
output ='/staging/ess/csul/image_benchmark/output/output_read_db'
env = lmdb.open(input, max_dbs=1,map_size=1e3)


txn = env.begin(write=False)
cursor = txn.cursor()
#read out the DB values

def open_image(img_name):
    img_string=txn.get(img_name)
    return Image.open(StringIO(img_string))

def process_image(image):
    return pyft.img_fft(image)

def save_image(img_to_save,image_name):
    img_to_save.save(image_name)

for i in range(0,10000):
    image_in  = 'array%04d.png' %i
    image_out='%s/out_%s' %(output, image_in)

    #im = Image.open(StringIO(value))
    #outfile = pt.img_fft(im)
    #outfile.save(image_out)

    im = open_image(image_in)
    outfile = process_image(im)
    save_image(im,image_out)

# time python runtask_read_db.py
#
# real	0m51.986s
# user	0m49.706s
# sys	0m1.750s
