import pandas as pd
import os
import re

def readWordList():
    cwd = os.getcwd()
    data = open(cwd + "/BadWordsList.txt", "rb").read()
    data = "".join(map(chr, data))
    return data

def cleanData(data) :
   return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data).split())

def offensive(tweet):
    #msg = "Tweet stuff here"
    data = cleanData(readWordList())
    data = data.split(" ")
    for i in data:
        if tweet.find(i) == -1:
            continue
        else :
            print("Offensive")
            break
            
def sentiment(tweet):
    analysis = TextBlob(cleanData(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return offensive(tweet)
