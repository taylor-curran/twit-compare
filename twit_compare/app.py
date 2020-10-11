"""Main app/routing file for Twit-Compare"""

from flask import Flask, render_template # For Front-End
from .models import DB, User, insert_example_users

# function that creates the app
# AKA an App Factory?
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    # config ? - Where to save the DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # What does this line do?
    DB.init_app(app)

    # ... TODO make the app!
    @app.route('/')
    def root():

        return render_template('base.html', tilte='Home',
                                # Select * Rendered in Template
                                users=User.query.all())

    @app.route('/update')
    def update():
        # Reset the DB
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        return render_template('base.html')

    return app
