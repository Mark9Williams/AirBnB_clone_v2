#!/usr/bin/python3
"""
Script that starts a Flask web application
The application listens on 0.0.0.0, port 5000.
It has two routes:
- /: Displays "Hello HBNB!"
-/hbnb: Displays "HBNB"
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes = False)
def hell0_world():
    """
        displays 'Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
