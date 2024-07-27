#!/usr/bin/python3
#Script that starts a Flask web application

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell0_world():
	return "Hello HBNB!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
