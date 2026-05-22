from flask import Flask, render_template, url_for, abort
from modules import get_sum, censor_check, format_message

app = Flask(__name__)

# Maximum allowed input length to prevent DoS
MAX_INPUT_LENGTH = 100


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
    # Validate input length to prevent DoS
    if len(data) > MAX_INPUT_LENGTH:
        abort(400, description="Input too long")
    
    # Validate input contains only safe characters (alphanumeric, spaces, basic punctuation)
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?:;\'\"-()[]{}')
    if not all(char in allowed_chars for char in data):
        abort(400, description="Invalid characters in input")
    
    processed_data = censor_check(data)
    return render_template('index.html', data=processed_data)