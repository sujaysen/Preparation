# import all dependencies
from elasticsearch import helpers
import time
import sys

sys.path.append('../')
from config.conn import es,index
from config.db import testDB

#calculate time 
print('Start Time:', time.ctime(time.time()))
t1=time.time()


fetch_cursor = testDB.cursor(buffered=True , dictionary=True)
count_cursor = testDB.cursor(buffered=True , dictionary=True)

# To calculate total data count
q1 = "SELECT count(1) AS cnt FROM tablename";
count_cursor.execute(q1)
count = count_cursor.fetchone()
count = int(count["cnt"])
count_cursor.close()
print(count)
#quit()
count = 200000
batch_size = 10000

obj = {}
actions = []

#process data to insert
for offset in range(0, count, batch_size):
	actions = []
	fetch_cursor.execute("SELECT data_field,query_field FROM tablename LIMIT %s OFFSET %s",(batch_size, offset))
	for row in fetch_cursor:
		obj = {
		"_index": "testquery",
		"_type": "_doc",
		"_id":row["sphinx_new_id"] ,
		"_source": {
		"data_field" : row["data_field"],
		"query_field" : row["query_field"],
		}
		}
		actions.append(obj)

	#insert data
	helpers.bulk(es, actions)
	print("Total {} data inserted.....".format(offset+batch_size))

# close db connection and fetch cursor
fetch_cursor.close()
testDB.close()

# calculate time
print('End Time:', time.ctime(time.time()))
t2=time.time()
print("Time Taken {} seconds".format(int(t2-t1)))
