import pymongo
client= pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Employee']
print("Done1")
info = mydb.employeeinfo
print("Done2")
record = {
    "firstname":"Digvijay",
    "lastname":"Gaikwad",
    "roll":34
}
info.insert_one(record)
print("done3")
