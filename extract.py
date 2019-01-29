import os
try:
    os.system("pip install -r requirements.txt")
    os.system("cls")
except: pass
 
import tweepy
import csv
 
consumer_key="qhB9HRrHRebUOfB0NkRDs3EiB"
consumer_secret="IDmoX01drYYSF85mmP8hqxV5haEb3vOGMfNz0uuUNumrE2WQZm"
access_token="768094106794864641-IpHAvaIAKHozPGgViR2XiFezpvor2gI"
access_token_secret="nYrzsrEmeUetfD2ytWaYyqzPy0pKSXYR1bhYB3Jin6f7d"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('gully.csv', 'a')
 
csvWriter = csv.writer(csvFile)
try:
    for tweet in tweepy.Cursor(api.search,q="gully boy",count=100,lang="en",since="2017-04-03").items():
        print (tweet.text)
        csvWriter.writerow([tweet.text.encode('utf-8')])
except: pass
 
os.system("pip freeze > requirements.txt")