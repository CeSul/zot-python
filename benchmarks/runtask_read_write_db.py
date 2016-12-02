from PIL import Image
import pyft
from StringIO import StringIO
import lmdb

input  ='/home/rcf-proj/ess/csul/image_benchmark/zot_db'
output ='/staging/ess/csul/image_benchmark/output/output_read_write_db'

read_db = lmdb.open(input, max_dbs=1,map_size=50e9)
write_db = lmdb.open(output, max_dbs=1,map_size=50e8)


txn_read  = read_db.begin(write=False)
txn_write = write_db.begin(write=True)

#cursor_read = txn_read.cursor()
#cursor_write = txn_write.cursor()

def open_image(img_name):
    img_string=txn_read.get(img_name)
    return Image.open(StringIO(img_string))

def process_image(image):
    return pyft.img_fft(image)

def save_image(img_to_save,image_name):
    string_wrapper = StringIO()
    img_to_save.save(string_wrapper, format='PNG')
    out_str = string_wrapper.getvalue()
    txn_write.put(image_name,out_str)


#read out the DB values
for i in range(0,10000):
    image_in  = 'array%04d.png' %i
    image_out='%s/out_%s' %(output, image_in)

    # im = Image.open(StringIO(value))
    #
    # outfile = pt.img_fft(im)
    #
    # string_wrapper = StringIO()
    # outfile.save(string_wrapper, format='PNG')
    # out_str = string_wrapper.getvalue()
    # cursor_write.put(image_out,out_str)

    im = open_image(image_in)
    outfile = process_image(im)
    save_image(outfile,image_out)

txn_write.commit()

# time python runtask_read_write_db.py
#
# real	0m47.186s
# user	0m46.697s
# sys	0m0.321s
