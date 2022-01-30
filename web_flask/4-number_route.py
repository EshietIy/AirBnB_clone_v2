#!/usr/bin/python3
'''Defines a Flask App'''
from flask import Flask


app = Flask('__name__')
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
    """return with variable"""
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """return varaible with default text"""
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """return variable if its a number"""
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
