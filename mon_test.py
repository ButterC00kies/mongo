import pymongo

client = pymongo.MongoClient("mongodb+srv://Butter:ajaymongodb@butter.ra2a9.mongodb.net/?retryWrites=true&w=majority")  # to establish the communication
db = client.test
print(db)


# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

d = {
    "name" : "parth",
    "email" : "parth@gmail.com",
    "surname" : "mehta"
}

db1 = client['mon_test']
coll = db1['test']
coll.insert_one(d )
