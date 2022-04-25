# Import library
import csv
import pymongo

# create connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["stock"]
mycol = mydb["justdialLog"]

# Collect Data
date = input("Inter date(dd-mm-yyyy) : ")
open_price = 
today_low = 
today_high = 
prev_close = 

# craete doc
idd = date
doc = {"_id":date,"date":date}

# Insert doc
mycol.update_one({"_id": idd},{"$set": doc},upsert=True)

