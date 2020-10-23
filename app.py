from flask import Flask, render_template, url_for
from modules import *

app = Flask(__name__)


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