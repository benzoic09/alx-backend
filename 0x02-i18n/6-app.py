#!/usr/bin/env python3
"""A Basic Flask app with Babel integration"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
from typing import Optional, Dict


app = Flask(__name__)


class Config:
    """Configuration for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    user = getattr(g, 'user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # Locale from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Returns a user dictionary or None if ID cannot
    be found or not provided."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Executed before all other functions."""
    g.user = get_user()


@app.route('/')
def index():
    """Basic HTML template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
