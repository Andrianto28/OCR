# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json

# initial object
app = Flask(__name__)

complete_name = "output_text/7.json"
identitas = json.load(open(complete_name))

@app.route("/", methods=['GET', 'POST'])
def output_score():
    if request.method == 'GET':
        A = {"A":"6"}
        return A
    elif request.method == 'POST':
        A["A"] = "7"
        return A

if __name__ == "__main__":
    app.run(debug=True, port=5005)
    complete_name = "output_text/7.json"
    identitas = json.load(open(complete_name))
