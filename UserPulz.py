# Libraries
import tweepy
import sys
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import datetime, time
import json
import sqlite3
from db import Db

# Files
from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret
from twitter_credentials import last_tweet_ID 

class TwitterAuthenticator():

    def twitter_auth(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

twitter_authenticator = TwitterAuthenticator()
api = API(twitter_authenticator.twitter_auth())

class GetTwitter():

    def get_tweets(self, api, username):
        page = 1
        deadend = False
        get_tweets.tweet_list = []

        while True:
            tweets = api.user_timeline(username, page = page)

            for tweet in tweets:
                if (datetime.datetime.now() - tweet.created_at).days < 20:
                    tweet_list.append(tweet.text.encode("utf-8"))
                    print("hello words!!!")
            else:
                return (tweet_list)
                deadend = True
                return

            if not deadend:
                page+1
                time.sleep(500)

get_twitter = GetTwitter()
get_twitter.get_tweets(api, "oculus")

db = Db()
