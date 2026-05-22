# Flask Web Application

A simple Flask web application with basic routing, template rendering, and static file serving.

## Project Structure

```
├── app.py              # Main Flask application
├── modules.py          # Utility functions
├── templates/          # HTML templates
│   └── index.html      # Main template
└── static/             # Static files
    ├── css/
    │   └── main.css    # Stylesheet
    └── js/
        └── main.js     # JavaScript file
```

## Features

- **Flask Framework**: Lightweight Python web framework
- **Template Rendering**: Jinja2 templates for dynamic HTML
- **Static File Serving**: CSS and JavaScript support
- **Custom Routes**: Multiple endpoints with different functionalities
- **Content Filtering**: Basic content moderation in text processing

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Returns "Hello, world" |
| `/get_sum` | GET | Returns the sum of 10 and 20 |
| `/hello/<string:data>` | GET | Renders template with processed data |

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install dependencies:
```bash
pip install flask
```

## Usage

Run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000` (default Flask development server).

## API Endpoints

### GET `/`
Returns a simple greeting message.

**Response:**
```
Hello, world
```

### GET `/get_sum`
Returns the sum of two numbers (10 + 20).

**Response:**
```
30
```

### GET `/hello/<string:data>`
Processes input data and renders it in an HTML template.

**Features:**
- Filters inappropriate words (returns "CENSORED" for filtered terms)
- Returns string length information for other inputs

**Example Requests:**
- `/hello/test` → "The length of test is 4"
- `/hello/fuck` → "CENSORED"

## Modules

### `modules.py`

Contains utility functions:

- **`getSum(a, b)`**: Returns the sum of two numbers
- **`mutateData(data)`**: Processes string input with content filtering

## Technologies Used

- **Python 3**
- **Flask** - Web framework
- **Jinja2** - Template engine
- **HTML/CSS/JavaScript** - Frontend

## License

This project is open source.
