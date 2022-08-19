from flask import Flask, Response
from flask import request
from flask_cors import CORS
import json
import time

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def index():
    return "Hola"