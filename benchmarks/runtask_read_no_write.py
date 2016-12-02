from PIL import Image
import numpy as np
import pyft
from StringIO import StringIO
import lmdb

input  ='/home/rcf-proj/ess/csul/image_benchmark/zot_images'
output ='/staging/ess/csul/image_benchmark/output/output_read_db'
env = lmdb.open(input, max_dbs=1,map_size=1e3)


txn = env.begin(write=False)
cursor = txn.cursor()
#read out the DB values
for key,value in cursor:
    image_in=key
    image_out='%s/out_%s' %(output, key)

    im = Image.open(StringIO(value))

    outfile = pyft.img_fft(im)

    #outfile.save(image_out)
    #print (key,value)

# time python runtask_read_no_write.py
#
# real	0m51.719s
# user	0m50.470s
# sys	0m0.868s
