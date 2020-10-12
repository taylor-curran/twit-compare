"""SQLAlchemy models and utility functions for Twit-Compare."""

# Connects Us to Our Database

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# To most of development world, model refers to like a 
# data model or data structure.



class User(DB.Model):
    """Twitter users corresponding to Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    # Tweet IDs are ordinal ints, so can be used to fetch only more recent
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(DB.Model):
    """Tweet, text, and data"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300)) # Allows for Text + Links
    # We need the DB to somehow store the embedding.
    # embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '-Tweet {}-'.format(self.text)


