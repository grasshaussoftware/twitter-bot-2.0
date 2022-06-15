import tweepy
from datetime import datetime
import time
from time import sleep

from cred import *
from config import QUERY, FOLLOW, LIKE, RETWEET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Tweet-Bot v1.0 by deusopus (deusopus@gmail.com)")
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
                    print(tweet.text)

            # check that bot has not already favorited the tweet
            # Favorite the tweet
            if LIKE:
                if not tweet.favorited:
                    tweet.favorite()
                    print('Liked the tweet')

            # Check that bot has not already retweeted the tweet
            # Retweet the tweet
            if RETWEET:
                if not tweet.retweeted:
                    tweet.retweet()
                    print('Retweeted the tweet')

            #timestamp
            time = datetime.now()
            print(time)

            #delay between actions
            print('Sleeping ', end='', flush=True)

            for x in range(250):
                for frame in r'-\|/-\|/':
                # Back up one character then print our next frame in the animation
                    print('\b', frame, sep='', end='', flush=True)
                    sleep(0.2)

                # Back up one character, print a space to erase the spinner, then a newline
                # so that the prompt after the program exits isn't on the same line as our
                # message
            print('\b ')

        except tweepy.errors.TweepyException as e:
            print(e)
