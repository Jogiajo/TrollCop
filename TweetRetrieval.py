import sys
import json
import time
import logging
import urllib#.parse
import socket
from os import environ as e
import tweepy
import pandas as pd
import jsonpickle
import DBConnection as db
import TextAnalysis as txtAnlyze


CONSUMER_KEY    = 'Y5jkXs4qLEKxGLPuDtt6WcxEJ'
CONSUMER_SECRET = 'EpDaF38AemfxyMPIwPt2JEcgd3ZVcdWF0Y9d03CXE0zD0EBBFY'

ACCESS_TOKEN  = '3259667124-98F3247LTeTTcpDlgmAogxMhjAHD3YcIcTpsnIq'
ACCESS_SECRET = 'qQeZBV1YavQ58fGwS33zMnPyGihXX0eL0A1sZDBeWt2B1'

def twitterSetup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

t = twitterSetup()


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def analyzeData(hashtag):
    count = 50
    for tweet in tweepy.Cursor(t.search, q=hashtag).items():
        if isEnglish(tweet.text):
            try:
               isTroll = txtAnlyze.sentiment(tweet.text)
               print(isTroll)
               if db.isExistingUser(tweet.user.screen_name) and isTroll :
                    db.updateUser(tweet.user.screen_name)
               elif (not db.isExistingUser(tweet.user.screen_name)) and isTroll :
                    db.insertUser(tweet.user.screen_name,1)
               else :
                    print("Insert")
                    db.insertUser(tweet.user.screen_name)
              
               db.insertTweet(tweet.id, tweet.user.screen_name, tweet.text[:50],tweet.created_at, isTroll)

               count -= 1
               if count == 0:
                return

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                return


analyzeData(sys.argv[0])
