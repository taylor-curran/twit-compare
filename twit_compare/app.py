"""Main app/routing file for Twit-Compare"""

from flask import Flask, render_template # For Front-End

# function that creates the app
# AKA an App Factory?
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # ... TODO make the app!
    @app.route('/')
    def root():
        return render_template('base.html', tilte='Home')
        return 'Hello, TwitOff'

    return app