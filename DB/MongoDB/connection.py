# pip install pymongo
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]

# Check if Database Exists
dblist = myclient.list_database_names()
if "test" in dblist:
  print("The database exists.")

mycol = mydb["sujay"]

# Check if Collection Exists

collist = mydb.list_collection_names()
if "sujay" in collist:
  print("The collection exists.")


doc = { "name": "John", "address": "Highway 37" }
mycol.insert_one(doc)

doc = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

mycol.insert_many(doc)

for x in mycol.find():
  print(x)
