#!/usr/bin/env python3
""" basic flask"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    """default route"""
    return render_templete("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
