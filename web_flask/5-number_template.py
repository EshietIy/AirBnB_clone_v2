#!/usr/bin/python3
'''Defines a Flask App'''
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """return string"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """return string"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """return content of variable"""
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """string with default string"""
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ return int"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ render template if n is int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
