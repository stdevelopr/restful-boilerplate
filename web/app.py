from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# Stablishes a connection with the server
client = MongoClient("mongodb://db:27017")

# connects to the database or create a new one if not exists
db = client.aNewDB

# creates a new collection
UserNum = db["UserNum"]

# insert a document in the collection
UserNum.insert({
    "num_of_visits":0
})

# here we can validate the posted data and return a status code
def checkPostedData(postedData, functionName):
    if (functionName == "method"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

#Here we create resources for the api, with get, post, put or delete methods
####################################################
class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_visits']
        new_num = prev_num + 1
        UserNum.update({}, {"$set": {"num_of_visits": new_num}})
        return str("Hello visitor number: "+ str(new_num))

class Read(Resource):
    def get(self):
        # "If here, then the resource Read was requested using the method GET"
        
        retMAP = {
            'msg': "OK",
            'Status Code': 200
        }

        return jsonify(retMAP)

    def post(self):
        # "If here, then the resource Read was requested using the method POST"
        
        postedData = request.get_json()

        # verify the posted data
        status_code = checkPostedData(postedData, "method")
        if (status_code != 200):
            retJson={
                "Message": "An error happened",
                "Status Code": status_code
            }
        
            return jsonify(retJson)

        else:
            # continue the code....
            pass



# create endpoints for the api resources
#####################################################
api.add_resource(Read, "/")
api.add_resource(Visit, "/visit")



#Run the application
############################################
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
