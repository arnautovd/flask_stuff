from flask import Flask, render_template

app = Flask(__name__)
from modules import *

@app.route('/')
def hello():
    return "Hello, world"

@app.route('/get_sum')
def hello_world():
    return str(getSum(10,20))

@app.route('/hello/<string:data>')
def get_results(data):
    
    data = mutateData(data)
    return render_template('index.html', data=data)