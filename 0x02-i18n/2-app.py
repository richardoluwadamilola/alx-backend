#!/usr/bin/env python3
"""A Basic flask app with internationalized support."""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTF"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    return request.accept_languages.best_match(App.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
