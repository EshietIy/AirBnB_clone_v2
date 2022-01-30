#!/usr/bin/python3
'''Defines a Flask App'''
from flask import Flask


app = Flask('__name__')
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """returns a string"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """returns a string"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ returns c and the variable text"""
    return 'C {:s}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
