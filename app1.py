# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json

# initial object
app = Flask(__name__)

# initiate objeck flask restful
api = Api(app)

# initiate object flask_cors
CORS(app)

# initiate identitas
#identitas = {}
#complete_name = "output_text/7.json"
#identitas = json.load(open(complete_name)) # variabel global, dictionary = json

# make Resources Class
class ContohResource(Resource):
    # method get and post
    def get(self):
        #response = {"msg" : "Hello world"}
        return identitas

    def post(self):
        
        return identitas
    
# setup resources
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
    complete_name = "output_text/7.json"
    identitas = json.load(open(complete_name))
    
    
