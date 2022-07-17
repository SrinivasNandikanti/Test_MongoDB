import pymongo
client = pymongo.MongoClient("mongodb+srv://srinivas:admin123@cluster0.cea5rsa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name":"srinivas",
     "surname":"nandikanti",
     "age": 28}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )