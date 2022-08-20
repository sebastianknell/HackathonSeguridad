import json
from flask import Flask, Response
from flask import request
from flask_cors import CORS
from model import *

app = Flask(__name__)
cors = CORS(app)

# CRUD PRODUCTO
@app.route("products/getall")
def getAllProducts():
    products = Product.select()
    print(products)
    return json.dumps(products)

@app.route("/products/update", methods=["POST"])
def updateProduct():
    data = json.loads(request.data)
    id = data['id']

@app.route("product/delete", methods=['POST'])
def deleteProduct():
    data = json.loads(request.data)
    id = data['id']
    prod = Product.get(Product.id = id)
    prod.delete_instance()
    return Response(200)