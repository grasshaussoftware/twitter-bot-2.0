# import the module
import tweepy
from cred import *
import time
from time import sleep

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth, wait_on_rate_limit=True)
# dm = "Join us on Discord... https://discord.gg/btMwEseSDw"

while True:
# printing the latest 20 followers of the user
    for user in api.get_followers(screen_name="CannaCoin"):
        try:
            if True:
                if not user.following:
                    user.follow()
                    print (user.screen_name)
                    print ("Followed")

        except tweepy.errors.TweepyException as e:
            print(e)
