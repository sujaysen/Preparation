# pip install pymongo
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Check if Database Exists
def is_exist_database(db):
    dblist = myclient.list_database_names()
    if db in dblist:
        mydb = myclient[db]
        print("Selected db is ",db)
    else:
        print("The database does not exist.")
        quit()
    return mydb


# Check if Collection Exists
def is_exist_collection(mydb,col):
    collist = mydb.list_collection_names()
    if col in collist:
        mycol = mydb[col]
        print("Selected collection is ",col)
    else:
        print("The collection does not exist.")
        quit()
    return mycol

# Return batch result 
def _as_batch(cursor, batch_size=50):
    # iterate over something (pymongo cursor, generator, ...) by batch.
    # Note: the last batch may contain less than batch_size elements.
    batch = []
    try:
        while True:
            for _ in range(batch_size):
                batch.append(next(cursor))
            yield batch
            batch = []
    except StopIteration as e:
        if len(batch):
            yield batch

db = input("Enter the database: ") or "test"
mydb = is_exist_database(db)
col = input("Enter the collection: ") or "sujay"
mycol = is_exist_collection(mydb,col)
batch_size = int(input("Enter the batch_size: ")) or 10
cursor = mycol.find()
for data in _as_batch(cursor,batch_size):
    print(data)
    print("\n\n")
