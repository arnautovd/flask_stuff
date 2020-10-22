from flask import Flask
app = Flask(__name__)
from modules import *

@app.route('/')
def hello():
    return "Hello, world"

@app.route('/get_sum')
def hello_world():
    return str(getSum(10,20))
