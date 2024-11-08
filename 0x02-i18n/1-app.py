#!/usr/bin/env python3
# File: 1-app.py
# Author: Oluwatobiloba Light
"""Basic Babel setup"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def index():
    """Index route"""
    return render_template("/1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
