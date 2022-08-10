from pymongo import MongoClient

client = MongoClient("mongodb+srv://nirjon:mongocomp590136@cluster0.cdfli6d.mongodb.net/?retryWrites=true&w=majority")
db = client["mydb"]

all = db.mycollection.find({})
for r in all:
    print(r)

row = db.mycollection.find_one({"name" : "samarjit"})
print(row["hobby"])
