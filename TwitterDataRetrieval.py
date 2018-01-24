import sys
import json
import time
import logging
import twitter
import urllib.parse
import socket
from os import environ as e
import tweepy
import pandas as pd

CONSUMER_KEY    = 'kovvh2EZtMBTBSs8apZLPKhh0'
CONSUMER_SECRET = 'jpvWljas0GroxIH6q2xKXrxRWAi32xXJY2tsnB31XuNCcGdVSL'

ACCESS_TOKEN  = '842972136910274564-D5APqhxs2xxNcdSdl99k86ofwMcP3g0'
ACCESS_SECRET = '2zIHN65yRwv7IKJGUgTZMNDq3oeuLo0haRtBRV23ikZeC'

def twitterSetup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

t = twitterSetup()

def getTweetUrl(t):
    return "https://twitter.com/%s/status/%s" % (t.user.screen_name, t.id)

def getRepliesUrl(tweet):
    user = tweet.user.screen_name
    tweet_id = tweet.id
    max_id = None
    print("%s" % tweet_url(tweet))


alltweets = [] 
new_tweets = t.user_timeline(screen_name = 'priyankachopra',count=200)
alltweets.extend(new_tweets)
for tweet in alltweets:
    print(tweet)
# oldest = alltweets[-1].id - 1
# while len(new_tweets) > 0:
#     new_tweets = t.user_timeline(screen_name = 'priyankachopra',count=199,max_id=oldest)
#     alltweets.extend(new_tweets)
#     oldest = alltweets[-1].id - 1
#     print("%s -- %s" % (screen_name,len(alltweets)))
#     for reply in get_replies(tweet):
#         print(reply)
