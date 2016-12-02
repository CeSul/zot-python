import lmdb
import sys

db_name = sys.argv[1]

env = lmdb.open(db_name, max_dbs=1,map_size=1e3)


txn = env.begin(write=True)
cursor = txn.cursor()
#read out the DB values
for key,value in cursor:
	#print (key)
	print (key,value)
