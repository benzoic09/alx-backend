#!/usr/bin/env python3
"""A Basic flask"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ basic html template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
