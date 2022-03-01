from email import message
import json
from bson.objectid import ObjectId
from flask import Flask, Response,request
import pymongo
app = Flask(__name__)

################################
try:
    mongo = pymongo.MongoClient(host="localhost", port=27017,serverSelectionTimeoutMS=1000)
    db = mongo.company
    mongo.server_info()#trigger exception if cannot connect to db
except:
    print("Error-cannot connect to db")
##########################################
@app.route("/user",methods=["GET"])
def get_user():
    try:
        data =list(db.company.find())
        for user in data:
            user["_id"]= str(user["_id"])
        return Response(response=json.dumps(data),status=500,mimetype="application/json")
    except Exception as ex:
        print(ex)       
        return Response(response=json.dumps({"message":"cannot read user"}),status=500,mimetype="application/json")
@app.route("/user",methods = ["POST"])
def create_user():
    try:
        #user = {"name": "ZZ","lname":"RR"}
        user = {"name":request.form["Firstname"],"lname":request.form["Lastname"]}
        dbResponse = db.company.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(response=json.dumps({"message":"user created","id":f"{dbResponse.inserted_id}"}),status=200,mimetype="application/json")
    except Exception as ex:
        print("***----***")
        print(ex)
        
@app.route("/user/<id>",methods = ["PATCH"])
def update_user(id):
    try:
        dbResponse =db.company.update_one(
            {"_id":ObjectId(id)},
            #{"$set":{"name":"DD"}}
            {"$set":{"name":request.form["name"]}}
        )
        print("done")
        for attr in dir(dbResponse):
            print(f"-------{attr}-------")
        return Response(response=json.dumps({"message":"user updated"}),status=200,mimetype="application/json")
        
    except Exception as ex:
        print("************------------------**************")
        print(ex)
        print("************------------------**************")
        return Response(response=json.dumps({"message":"cannot update"}),status=500,mimetype="application/json")
@app.route("/user/<id>",methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse=db.company.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(response=json.dumps({"message":"user deleted","id":f"{id}"}),status=200,mimetype="application/json")
        else:
            return Response(response=json.dumps({"message":"sorry  user not found","id":f"{id}"}),status=500,mimetype="application/json")
            
        #for attr in dir(dbResponse):
        #    print(f"---{attr}----")
        
        
        #return Response(response=json.dumps({"message":"user deleted","id":f"{id}"}),status=200,mimetype="application/json")
        
    except Exception as ex:
        print("********-----------------************")
        print(ex)
        print("********-----------------************")
        return Response(response=json.dumps({"message":"sorry  cannot delete"}),status=500,mimetype="application/json")
    


if __name__=="__main__":
    app.run(port=5005,debug=True)