from flask_pymongo import PyMongo
import upload as s
import urllib

s.app.config['MONGO_DBNAME'] = 'mydb'
s.app.config['MONGO_URI'] = 'mongodb+srv://Sumit111:Sumit@mydb.hm5qe.mongodb.net/mydb?retryWrites=true&w=majority'
mongo = PyMongo(s.app)

# user name : Sumit111
# pass : Sumit
