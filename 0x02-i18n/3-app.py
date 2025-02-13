#!/usr/bin/env python3
"""Flask app with i18n support"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import List

app = Flask(__name__)


class Config:
    """A basic configuring class"""
    LANGUAGES: List[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render index page with translations"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
