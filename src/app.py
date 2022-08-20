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

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = User.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            #redirect page
    #render login

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']
        phon = reques.form['phon']
        addressaux = request.form['addressaux']
        rol = request.form['rol']
        register = user(username = uname, email = mail, password = passw, phone = phon, address = addressaux, rol_id = rol)
        db.session.add(register)
        db.session.commit()
        #redirect login
    #render register