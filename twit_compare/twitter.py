"""Retrieve Tweets, embeddings, and persist in the DB."""

from os import getenv
import tweepy
from .models import DB, Tweet, User


# TWITTER_USERS = ['elonmusk', 'rrherr']

TWITTER_API_KEY = getenv('TWITTER_API_KEY')
TWITTER_API_KEY_SECRET = getenv('TWITTER_API_KEY_SECRET')

TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY,
                                    TWITTER_API_KEY_SECRET)

TWITTER = tweepy.API(TWITTER_AUTH)

def add_or_update_user(username):
    try:
        """Add or update a user and their Tweets, error if not a Twitter user."""
        twitter_user = TWITTER.get_user(username)
        # Get a User, if they don't exist, make a user.
        # I don't totally understand querying with models.
        db_user = (User.query.get(twitter_user.id) or 
                    User(id=twitter_user.id, name=username))
        DB.session.add(db_user)
        # Let's get the tweets - focusing on primary (not retweet/reply)
        tweets = twitter_user.timeline(
            count=200, exclude_replies=True, include_rts=False,
            tweet_mode='extended', since_id=db_user.newest_tweet_id
        )
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        for tweet in tweets:
            # embedding = BASILICA.embed_sentence(tweet.full_text,
            #                                   model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300])
                                # , embedding=embedding)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e
    else:
        DB.session.commit()


def insert_example_users():
    add_or_update_user('austen')
    add_or_update_user('elonmusk')