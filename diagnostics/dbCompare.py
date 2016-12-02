import lmdb
import sys

db1_path = sys.argv[1]
db2_path = sys.argv[2]

db1 = lmdb.open(db1_path, max_dbs=1)
db2 = lmdb.open(db2_path, max_dbs=1)

txn_db1 = db1.begin(write=False)
txn_db2 = db2.begin(write=False)

cursor = txn_db1.cursor()

for key,value1 in cursor:
    value2 = txn_db2.get(key)
    if value1 != value2:
        print("%s is not the same for %s and %s" %(key,db1_path,db2_path))
    
