import lmdb
import StringIO
from PIL import Image

env = lmdb.open('/auto/rcf-proj2/ess/csul/image_benchmark/zot_db', max_dbs=1, map_size=1e9) # max database size set to 1gb
#env = lmdb.open('./zot_db_tostring', max_dbs=1, map_size=1e9) # max database size set to 1gb
data_dir='/auto/rcf-proj2/ess/csul/image_benchmark/zot_images'

txn = env.begin(write=True)
cursor = txn.cursor()

# put in some sample data
for i in range(0,10000):
   key = 'array%04d.png' %i
   print('key = %s' %key)
   filename='%s/%s' %(data_dir,key)
   #data = file(filename,'rb').read()

   im = Image.open(filename)
   string_wrapper = StringIO.StringIO()
   im.save(string_wrapper, format='PNG')
   data = string_wrapper.getvalue()

   cursor.put(key,data)

txn.commit()

# macferd:image_benchmark csul$ time python write_db.py
#
# real	0m1.621s
# user	0m0.740s
# sys	0m0.139s
