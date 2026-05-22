from flask import Flask, render_template, url_for
from modules import get_sum, censor_check, format_message

app = Flask(__name__)


@app.route('/')
def index():
    """Render the home page with a greeting."""
    return "Hello, world"


@app.route('/get_sum')
def sum_endpoint():
    """Return the sum of two predefined numbers."""
    return str(get_sum(10, 20))


@app.route('/hello/<string:data>')
def show_greeting(data: str):
    """Display processed data on the index page."""
    processed_data = censor_check(data)
    return render_template('index.html', data=processed_data)