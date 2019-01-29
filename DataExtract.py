import os
try:
	os.system("pip install -r requirements.txt")
	os.system("cls")
except: pass

import tweepy
import csv
Access_token = "768094106794864641-DUwAChsZ8fr9ZQfgy5dnJ7cDICc2lhr"
Access_secret = "KaqsTV2t11AgmHtKBK61dlLFMNC7qmGfLFgOywQaEPpCE"
consumer_token = "S5pk1IbFQlnm6mASeaoXyPSIA"
consumer_secret = "yMaWE5xgA5K9SqjdDhA680HSQVrhO8gtHx3rf2Yy7ZLVjSSnax"
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)


auth.set_access_token(Access_token,Access_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)

csvFile=open('cricket.csv','a')
csvWriter = csv.writer(csvFile)
try:
	for tweet in tweepy.Cursor(api.search,q="IndvsNz", count=100,lang="en",since="2019-01-01").items():
		print(tweet.text)
		csvWriter.writerow([tweet.text.encode('utf-8')])
	
except: pass
os.system ("pip freeze > requirements.txt")
