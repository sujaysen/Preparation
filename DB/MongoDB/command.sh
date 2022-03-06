# Create Database
use DATABASE_NAME;

# Show all dbs
show dbs;

# Switch db
use DATABASE_NAME;

# Drop Database
db.dropDatabase();
This will delete the selected database. If you have not selected any database, then it will delete default 'test' database.

# Create Collection
db.createCollection(name);

db.createCollection("mycol", { capped : true, autoIndexId : true, size : 6142800, max : 10000 } );

capped -->> If you specify true, you need to specify size parameter also
autoIndexId -->> if true, automatically create index on _id fields. Default value is false.
size -->> If capped is true, then you need to specify this field also
max -->> Specifies the maximum number of documents allowed in the capped collection

# Drop Collection
db.COLLECTION_NAME.drop();

# Show all collection 
show collections;

# Insert document
db.COLLECTION_NAME.insert(document);

You can also pass an array of documents into the insert() method
db.COLLECTION_NAME.insert([{},{},{} ..... {}]);	
To insert the document you can use db.post.save(document) also

# Insert one method
db.COLLECTION_NAME.insertOne(document);

# Insert many method
db.COLLECTION_NAME.insertMany([{},{},{} ..... {}]);

You can insert multiple documents using the insertMany() method. To this method you need to pass an array of documents.

# Query Document
db.COLLECTION_NAME.find();

# To display the results in a formatted way, you can use pretty() method.
db.COLLECTION_NAME.find().pretty();

# The findOne() method
db.COLLECTIONNAME.findOne();

# Equality
db.COLLECTIONNAME.find({"name":"value"});

# Less Than
db.COLLECTIONNAME.find({"key":{$lt:value}})

# Less Than Equals
db.COLLECTIONNAME.find({"key":{$lte:value}})

# Greater Than
db.COLLECTIONNAME.find({"key":{$gt:value}})

# Greater Than Equals
db.COLLECTIONNAME.find({"key":{$gte:value}})

# Not Equal
db.COLLECTIONNAME.find({"key":{$ne:value}})

# Values in an array	
db.COLLECTIONNAME.find({"key":{$in:[array]}})

# Values not in an array	
db.COLLECTIONNAME.find({"key":{$nin:[array]}})

# AND in MongoDB
db.COLLECTIONNAME.find({$and:[{"key":"value"},{"key":"value"}]})

# OR in MongoDB
db.COLLECTIONNAME.find({$or:[{"key":"value"},{"key":"value"}]})

# Using AND and OR Together
db.sujay.find({"key":{$gte:value},$or:[{"key":"value"},{"key":"value"}]})

# NOR in MongoDB
db.COLLECTIONNAME.find({$nor:[{"key":"value"},{"key":"value"}]})

# Update Document 
db.COLLECTION_NAME.update({"key":"value"},{$set:{"key":"updated value",...., "key":"updated value"}});

# Update multiple document
db.COLLECTION_NAME.update({"key":"value"},{$set:{"key":"updated value",...., "key":"updated value"}},{multi:true});

# replaces the existing document
For save, If the document contains _id, it will upsert querying the collection on the _id field, If not, it will insert.
db.COLLECTIONNAME.save({"key":"value",.....,"key":"value"})  --->>>> just insert
db.COLLECTIONNAME.save({"_id" : ObjectId("55551809132c1f084b005cd0"),"key":"value", ..... ,"key":"value"})  -->>> upsert

# findOneAndUpdate() method
db.COLLECTION_NAME.findOneAndUpdate({"key":"value"},{$set:{"key":"updated value",...., "key":"updated value"}});

# updateOne() method
db.COLLECTION_NAME.updateOne({"key":"value"},{$set:{"key":"updated value",...., "key":"updated value"}});

# updateMany() method
db.COLLECTION_NAME.updateMany({"key":"value"},{$set:{"key":"updated value",...., "key":"updated value"}});

# Delete Document
db.COLLECTION_NAME.remove({"key":"value"});

# Delete only one match document
db.COLLECTION_NAME.remove({"key":"value"},1);

# Delete all document
db.COLLECTION_NAME.remove({});

# Projection
db.COLLECTION_NAME.find({},{"key":1 ... "key":0});
ex . db.COLLECTION_NAME.find({},{"name":1,_id:0})

# Count
db.COLLECTION_NAME.count();

# Limit method
db.COLLECTION_NAME.find().limit(limit_value);

# Skip Method
db.COLLECTION_NAME.find().limit(limit_value).skip(skip_value);

# Sort method
db.COLLECTION_NAME.find().sort({"key":1,... ,"key":-1});   -->>> 1 for ascending order and -1 for descending order.

# Indexing
db.COLLECTION_NAME.createIndex({"key":1,... ,"key":-1});   -->>> 1 for ascending order and -1 for descending order.

# Drop particular 
db.COLLECTION_NAME.dropIndex({"key":1,... ,"key":-1});   -->>> 1 for ascending order and -1 for descending order.

# Drop all
db.COLLECTION_NAME.dropIndexes()

# Get indexes
db.COLLECTION_NAME.getIndexes()

# Aggregation
db.mycol.aggregate([{$group : {_id : "$key", field_name : {$sum : "$key"}}}])
db.mycol.aggregate([{$group : {_id : "$key", field_name : {$avg : "$key"}}}])
db.mycol.aggregate([{$group : {_id : "$key", field_name : {$min : "$key"}}}])
db.mycol.aggregate([{$group : {_id : "$key", field_name : {$max : "$key"}}}])
db.mycol.aggregate([{$group : {_id : "$key", field_name : {$sum : "$key"}}}])

# Backup data
mongodump
mongodump --host HOST_NAME --port PORT_NUMBER
mongodump --dbpath DB_PATH --out BACKUP_PATH
mongodump --collection COLLECTION_NAME --db DB_NAME

# Restore data
mongorestore
