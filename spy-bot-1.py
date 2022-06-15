import tweepy
from datetime import datetime
import time
from time import sleep

from cred import *
from config import QUERY, FOLLOW, LIKE, RETWEET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Tweet-Bot v2.1 by deusopus (deusopus@gmail.com)")
print("Search criteria :", QUERY) #parses through tweets for the hashtag in config.py
print("Follow user's accounts :", FOLLOW)
print("Like user's tweets :", LIKE)
print("Retweet user's tweets :", RETWEET)

while True:

    for tweet in api.search_tweets(QUERY):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)


            # Check that bot is not already following the user
            # Follow the user who tweeted
            if FOLLOW:
                if not tweet.user.following:
                    tweet.user.follow()
                    print('Followed the user')


            # check that bot has not already favorited the tweet
            # Favorite the tweet
            if LIKE:
                if not tweet.favorited:
                    tweet.favorite()
                    print('Liked the tweet')
                    print(tweet.text)

            # Check that bot has not already retweeted the tweet
            # Retweet the tweet
            if RETWEET:
                if not tweet.retweeted:
                    tweet.retweet()
                    print('Retweeted the tweet')

            #timestamp
            time = datetime.now()
            print(time)
            sleep(10)

        except tweepy.errors.TweepyException as e:
            print(e)
