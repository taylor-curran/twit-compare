"""Main app/routing file for Twit-Compare"""

from flask import Flask, render_template # For Front-End
from .models import DB, User
from .twitter import insert_example_users

# . means THIS directory or current directory

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
        insert_example_users()
        return render_template('base.html', title='Users updated!',
                                users=User.query.all())


    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')

    return app
