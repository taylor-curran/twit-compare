"""Entry point for Twit-Compare"""
from .app import create_app

APP = create_app()

# To Run the App
# We give the command in Terminal

# FLASK_APP=twit_compare flask run

# We are essentially passing FLASK_APP the twit_compare package
# or folder if you will.
# At that point the init statement is run.

# if not working try
# FLASK_APP=twit_compare:APP flask run

# AND Double check that __init__.py is set correctly.