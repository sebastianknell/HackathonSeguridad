from flask import Flask, Response
from flask import request
from flask_cors import CORS
import json
import time

app = Flask(__name__)
cors = CORS(app)

id = 1;
db = {}

@app.route("/")
def index():
    return "Hola"

@app.route("/post", methods=["POST"])
def post():
    global id
    data = json.loads(request.data)
    db[id] = data;
    id += 1
    return Response("Creado", 200)

@app.route("/get/<id>")
def get(id):
    res = db[int(id)]
    if res == None:
        res = {"Message": "Invalid id"}
        return Response(json.dumps(res), 400, mimetype='application/json')
    return Response(json.dumps(res), 200, mimetype='application/json')