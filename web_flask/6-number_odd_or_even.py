#!/usr/bin/python3
"""
A script that starts a Flask web application listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""Displays 'Hello HBNB!'"""
	return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""Dispalys 'HBNB'"""
	return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text():
	"""Route to display 'c' followed by value of the text variable"""
	return "c {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)	
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
	"""displays 'Python', followed by the value of text"""
	return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
	"""Displays 'n is number' only if n is an integer"""
	return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
	"""dispalys html page if n is a number"""
	return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
	"""display a HTML page only if n is an integer"""
	txt = "even" if n % 2 == 0 else "odd"
	return render_template('6-number_odd_or_even.html', number=n, txt=txt)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
